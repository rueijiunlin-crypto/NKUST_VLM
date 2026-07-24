"""ROS2 latest-frame camera → real VLM adapter → validated semantic JSON topic."""
from __future__ import annotations

import json
import threading
import time

import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String

from vlm_adapter import AdapterConfig, RealVLMAdapter


class SemanticNode(Node):
    def __init__(self):
        super().__init__("realtime_vlm_semantic")
        for name, default in (
            ("image_topic", "/camera/image_raw"),
            ("result_topic", "/vlm/semantic"),
            ("max_age_ms", 500.0),
            ("model_id", "Qwen/Qwen2.5-VL-3B-Instruct"),
            ("model_revision", "main"),
            ("device", "auto"),
            ("dtype", "auto"),
            ("max_new_tokens", 160),
            ("prompt", AdapterConfig.prompt),
        ):
            self.declare_parameter(name, default)

        config = AdapterConfig(
            model_id=self.get_parameter("model_id").value,
            revision=self.get_parameter("model_revision").value,
            device=self.get_parameter("device").value,
            dtype=self.get_parameter("dtype").value,
            max_new_tokens=int(self.get_parameter("max_new_tokens").value),
            prompt=self.get_parameter("prompt").value,
        )
        self.bridge = CvBridge()
        self.adapter = RealVLMAdapter(config)
        self.publisher = self.create_publisher(String, self.get_parameter("result_topic").value, 10)
        self._latest = None
        self._replaced = 0
        self._lock = threading.Lock()
        self._wake = threading.Event()
        self._stop = threading.Event()
        self._worker = threading.Thread(target=self._worker_loop, daemon=True)
        self._worker.start()
        self.create_subscription(Image, self.get_parameter("image_topic").value, self.on_image, 1)
        self.get_logger().info(
            f"Loaded real adapter model={config.model_id} revision={config.revision}; "
            "publishing semantic observations only"
        )

    def on_image(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")
        source_ns = msg.header.stamp.sec * 1_000_000_000 + msg.header.stamp.nanosec
        with self._lock:
            if self._latest is not None:
                self._replaced += 1
            self._latest = (frame, source_ns)
        self._wake.set()  # capacity-one latest-frame policy

    def _take_latest(self):
        with self._lock:
            item, self._latest = self._latest, None
        return item

    def _worker_loop(self):
        while not self._stop.is_set():
            self._wake.wait(timeout=0.1)
            self._wake.clear()
            item = self._take_latest()
            if item is None:
                continue
            frame, source_ns = item
            now_ns = self.get_clock().now().nanoseconds
            age_ms = (now_ns - source_ns) / 1e6
            result = {
                "source_timestamp_ns": source_ns,
                "result_timestamp_ns": now_ns,
                "model_id": self.adapter.config.model_id,
                "model_revision": self.adapter.config.revision,
                "objects": [],
                "relations": [],
                "uncertain": [],
                "valid": False,
                "age_ms": age_ms,
                "inference_ms": 0.0,
                "queue_replacements": self._replaced,
            }
            if age_ms > float(self.get_parameter("max_age_ms").value):
                result["uncertain"] = ["stale frame rejected before inference"]
            else:
                try:
                    semantic, evidence = self.adapter.infer(frame)
                    result.update(semantic)
                    result["inference_ms"] = evidence["inference_ms"]
                    result["result_timestamp_ns"] = self.get_clock().now().nanoseconds
                    result["publish_latency_ms"] = (
                        result["result_timestamp_ns"] - source_ns
                    ) / 1e6
                    result["valid"] = all(isinstance(result[key], list) for key in ("objects", "relations", "uncertain"))
                    result["runtime_evidence"] = evidence
                except Exception as error:
                    result["uncertain"] = [f"{type(error).__name__}: {error}"]
            output = String()
            output.data = json.dumps(result, ensure_ascii=False)
            self.publisher.publish(output)

    def destroy_node(self):
        self._stop.set()
        self._wake.set()
        self._worker.join(timeout=2.0)
        super().destroy_node()


def main():
    rclpy.init()
    node = SemanticNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
