"""Publish a VLM result as JSON in std_msgs/String, with a ROS-free dry-run."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from uuid import uuid4

TOPIC_NAME = "/vlm/semantic_description"


def build_payload() -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task": "caption",
        "status": "ok",
        "source_image": "outputs/camera.jpg",
        "question": None,
        "answer": "a desk with a laptop",
        "model_id": "Salesforce/blip-image-captioning-base",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--interval", type=float, default=2.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.interval <= 0:
        raise ValueError("--interval must be positive")
    if args.dry_run:
        print(json.dumps(build_payload(), ensure_ascii=False, indent=2))
        return

    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class SemanticPublisher(Node):
        def __init__(self) -> None:
            super().__init__("vlm_semantic_publisher")
            self.publisher = self.create_publisher(String, TOPIC_NAME, 10)
            self.timer = self.create_timer(args.interval, self.publish_result)

        def publish_result(self) -> None:
            message = String()
            message.data = json.dumps(build_payload(), ensure_ascii=False)
            self.publisher.publish(message)
            self.get_logger().info(f"published observation: {message.data}")

    rclpy.init()
    node = SemanticPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
