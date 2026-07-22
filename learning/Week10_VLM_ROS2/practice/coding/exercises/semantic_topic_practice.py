"""Week10 implementation practice: complete every TODO."""

import argparse
from typing import Any

TOPIC_NAME = "/vlm/semantic_description"


def build_payload(answer: str) -> dict[str, Any]:
    """Build a Week08-compatible semantic result."""
    # TODO 1: include schema, trace, task, status, source, answer, and model fields.
    raise NotImplementedError


def validate_payload(payload: dict[str, Any]) -> None:
    """Validate required fields and cross-field rules."""
    # TODO 2: reject missing fields, invalid enum values, and VQA without a question.
    raise NotImplementedError


def run_publisher(interval: float) -> None:
    """Create and spin a ROS2 publisher node."""
    # TODO 3: import ROS2 packages here, publish JSON String, and clean up safely.
    raise NotImplementedError


def run_subscriber() -> None:
    """Create and spin a ROS2 subscriber that validates each message."""
    # TODO 4: parse JSON, validate it, log the result, and clean up safely.
    raise NotImplementedError


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
        print(payload)
    elif args.mode == "publisher":
        run_publisher(args.interval)
    else:
        run_subscriber()


if __name__ == "__main__":
    main()
