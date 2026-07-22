"""Reference solution for the Week09 camera pipeline practice."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


def open_source(camera_index: int, synthetic: bool) -> Any:
    if synthetic:
        return "synthetic"
    import cv2

    source = cv2.VideoCapture(camera_index)
    if not source.isOpened():
        source.release()
        raise RuntimeError(f"Cannot open camera index {camera_index}")
    return source


def read_frame(source: Any, synthetic: bool) -> Any:
    import cv2
    import numpy as np

    if synthetic:
        x = np.linspace(0, 255, 640, dtype=np.uint8)
        gray = np.tile(x, (480, 1))
        frame = cv2.merge((gray, np.flip(gray, axis=1), np.full_like(gray, 80)))
        cv2.putText(frame, "synthetic", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame
    ok, frame = source.read()
    if not ok or frame is None:
        raise RuntimeError("Camera opened but returned no frame")
    if frame.dtype != np.uint8 or frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError(f"Unexpected frame contract: shape={frame.shape}, dtype={frame.dtype}")
    return frame


def save_snapshot(frame: Any, output: Path) -> None:
    import cv2

    output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output), frame):
        raise RuntimeError(f"Failed to write {output}")


def build_handoff(frame: Any, output: Path, task: str, question: str | None) -> dict[str, Any]:
    if task == "vqa" and not (question and question.strip()):
        raise ValueError("VQA requires a non-empty question")
    height, width, channels = frame.shape
    return {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_image": str(output.resolve()),
        "frame": {"width": width, "height": height, "channels": channels, "color_space": "BGR"},
        "task": task,
        "question": question.strip() if task == "vqa" else None,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera-index", type=int, default=0)
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--task", choices=("caption", "vqa"), default="caption")
    parser.add_argument("--question")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = open_source(args.camera_index, args.synthetic)
    try:
        frame = read_frame(source, args.synthetic)
        save_snapshot(frame, args.output)
        print(json.dumps(build_handoff(frame, args.output, args.task, args.question), ensure_ascii=False, indent=2))
    finally:
        if not args.synthetic:
            source.release()


if __name__ == "__main__":
    main()
