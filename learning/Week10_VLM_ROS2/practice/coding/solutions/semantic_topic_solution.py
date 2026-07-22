"""Reference solution for the Week10 semantic topic practice."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

TOPIC_NAME = "/vlm/semantic_description"
REQUIRED_FIELDS = {
    "schema_version",
    "observation_id",
    "timestamp_utc",
    "task",
    "status",
    "source_image",
    "question",
    "answer",
    "model_id",
}


def build_payload(answer: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task": "caption",
        "status": "ok",
        "source_image": "outputs/camera.jpg",
        "question": None,
        "answer": answer,
        "model_id": "Salesforce/blip-image-captioning-base",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_FIELDS - payload.keys())
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    if payload["task"] not in {"caption", "vqa"}:
        raise ValueError("task must be caption or vqa")
    if payload["status"] not in {"ok", "unknown", "error"}:
        raise ValueError("status must be ok, unknown, or error")
    if payload["task"] == "vqa" and not payload["question"]:
        raise ValueError("VQA requires question")
    if payload["status"] == "ok" and not payload["answer"]:
        raise ValueError("ok result requires answer")


def run_publisher(interval: float) -> None:
    if interval <= 0:
        raise ValueError("interval must be positive")
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class SemanticPublisher(Node):
        def __init__(self) -> None:
            super().__init__("practice_semantic_publisher")
            self.publisher = self.create_publisher(String, TOPIC_NAME, 10)
            self.timer = self.create_timer(interval, self.publish_result)

        def publish_result(self) -> None:
            payload = build_payload("a desk with a laptop")
            validate_payload(payload)
            message = String()
            message.data = json.dumps(payload, ensure_ascii=False)
            self.publisher.publish(message)
            self.get_logger().info(f"published {payload['observation_id']}")

    rclpy.init()
    node = SemanticPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


def run_subscriber() -> None:
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class SemanticSubscriber(Node):
        def __init__(self) -> None:
            super().__init__("practice_semantic_subscriber")
            self.subscription = self.create_subscription(String, TOPIC_NAME, self.on_message, 10)

        def on_message(self, message: String) -> None:
            try:
                payload = json.loads(message.data)
                if not isinstance(payload, dict):
                    raise ValueError("Payload must be a JSON object")
                validate_payload(payload)
                self.get_logger().info(f"received {payload['observation_id']}: {payload['answer']}")
            except (json.JSONDecodeError, ValueError) as error:
                self.get_logger().error(f"invalid message: {error}")

    rclpy.init()
    node = SemanticSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("publisher", "subscriber"), required=True)
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.dry_run:
        payload = build_payload("dry-run semantic result")
        validate_payload(payload)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif args.mode == "publisher":
        run_publisher(args.interval)
    else:
        run_subscriber()


if __name__ == "__main__":
    main()
