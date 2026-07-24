"""ROS2 camera-to-semantic-topic node; model adapter is intentionally read-only."""
import json
import time

import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String


class SemanticNode(Node):
    def __init__(self):
        super().__init__("realtime_vlm_semantic")
        self.declare_parameter("image_topic", "/camera/image_raw")
        self.declare_parameter("result_topic", "/vlm/semantic")
        self.declare_parameter("max_age_ms", 500.0)
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(String, self.get_parameter("result_topic").value, 10)
        self.create_subscription(Image, self.get_parameter("image_topic").value, self.on_image, 1)

    def on_image(self, msg):
        started = time.perf_counter()
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")
        source_ns = msg.header.stamp.sec * 1_000_000_000 + msg.header.stamp.nanosec
        now_ns = self.get_clock().now().nanoseconds
        age_ms = (now_ns - source_ns) / 1e6
        # Replace only this read-only adapter with the Week06 model call.
        result = {
            "source_timestamp_ns": source_ns,
            "result_timestamp_ns": now_ns,
            "image_shape": list(frame.shape),
            "model_id": "adapter-not-configured",
            "objects": [],
            "unknown": True,
            "valid": age_ms <= float(self.get_parameter("max_age_ms").value),
            "age_ms": age_ms,
            "inference_ms": (time.perf_counter() - started) * 1000,
        }
        out = String()
        out.data = json.dumps(result, ensure_ascii=False)
        self.publisher.publish(out)


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
