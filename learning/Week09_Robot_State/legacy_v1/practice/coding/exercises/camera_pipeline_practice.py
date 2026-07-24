"""Week09 implementation practice: complete every TODO."""

import argparse
from pathlib import Path
from typing import Any


def open_source(camera_index: int, synthetic: bool) -> Any:
    """Return a source suitable for read_frame."""
    # TODO 1: create a synthetic marker or an opened cv2.VideoCapture.
    raise NotImplementedError


def read_frame(source: Any, synthetic: bool) -> Any:
    """Return one valid BGR uint8 frame."""
    # TODO 2: generate or read a frame and validate the result.
    raise NotImplementedError


def save_snapshot(frame: Any, output: Path) -> None:
    """Save a frame and reject write failures."""
    # TODO 3: create the parent directory and check cv2.imwrite's return value.
    raise NotImplementedError


def build_handoff(frame: Any, output: Path, task: str, question: str | None) -> dict[str, Any]:
    """Build the request passed to the Week08 VLM pipeline."""
    # TODO 4: validate task/question and include frame metadata and trace fields.
    raise NotImplementedError


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
        print(build_handoff(frame, args.output, args.task, args.question))
    finally:
        if not args.synthetic and source is not None:
            source.release()


if __name__ == "__main__":
    main()
