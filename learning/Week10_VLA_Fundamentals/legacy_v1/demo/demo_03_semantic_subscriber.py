"""Subscribe to and validate JSON VLM results, with a ROS-free dry-run."""

from __future__ import annotations

import argparse
import json
from typing import Any

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
DEFAULT_MESSAGE = json.dumps(
    {
        "schema_version": "1.0",
        "observation_id": "dry-run-observation",
        "timestamp_utc": "2026-01-01T00:00:00+00:00",
        "task": "caption",
        "status": "ok",
        "source_image": "outputs/camera.jpg",
        "question": None,
        "answer": "a desk with a laptop",
        "model_id": "Salesforce/blip-image-captioning-base",
    }
)


def validate_message(raw: str) -> dict[str, Any]:
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError("Payload must be a JSON object")
    missing = sorted(REQUIRED_FIELDS - payload.keys())
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    if payload["task"] not in {"caption", "vqa"}:
        raise ValueError("task must be caption or vqa")
    if payload["status"] not in {"ok", "unknown", "error"}:
        raise ValueError("status must be ok, unknown, or error")
    if payload["task"] == "vqa" and not payload["question"]:
        raise ValueError("VQA result requires question")
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--message-json", default=DEFAULT_MESSAGE)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.dry_run:
        print(json.dumps(validate_message(args.message_json), ensure_ascii=False, indent=2))
        return

    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class SemanticSubscriber(Node):
        def __init__(self) -> None:
            super().__init__("vlm_semantic_subscriber")
            self.subscription = self.create_subscription(String, TOPIC_NAME, self.on_message, 10)

        def on_message(self, message: String) -> None:
            try:
                payload = validate_message(message.data)
                self.get_logger().info(
                    f"valid observation={payload['observation_id']} answer={payload['answer']}"
                )
            except (json.JSONDecodeError, ValueError) as error:
                self.get_logger().error(f"invalid semantic message: {error}")

    rclpy.init()
    node = SemanticSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
