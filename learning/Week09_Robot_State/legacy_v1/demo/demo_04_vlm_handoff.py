"""Create a Week08-compatible VLM request from a saved camera frame."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--task", choices=("caption", "vqa"), default="caption")
    parser.add_argument("--question")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    import cv2

    if args.task == "vqa" and not (args.question and args.question.strip()):
        raise ValueError("VQA requires --question")
    frame = cv2.imread(str(args.image))
    if frame is None:
        raise FileNotFoundError(f"Cannot decode image: {args.image}")

    height, width, channels = frame.shape
    payload = {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_image": str(args.image.resolve()),
        "frame": {"width": width, "height": height, "channels": channels, "color_space": "BGR"},
        "task": args.task,
        "question": args.question.strip() if args.task == "vqa" else None,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
