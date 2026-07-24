"""Capture and save one camera or synthetic frame."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera-index", type=int, default=0)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--synthetic", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    import cv2
    import numpy as np

    if args.synthetic:
        x = np.linspace(0, 255, 640, dtype=np.uint8)
        frame = np.tile(x, (480, 1))
        frame = cv2.merge((frame, np.flip(frame, axis=1), np.full_like(frame, 80)))
        cv2.putText(frame, "synthetic", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        capture = cv2.VideoCapture(args.camera_index)
        try:
            if not capture.isOpened():
                raise RuntimeError(f"Cannot open camera index {args.camera_index}")
            ok, frame = capture.read()
            if not ok or frame is None:
                raise RuntimeError("Camera opened but returned no frame")
        finally:
            capture.release()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(args.output), frame):
        raise RuntimeError(f"Failed to write {args.output}")
    print(f"saved: {args.output.resolve()}")
    print("frame shape:", frame.shape)


if __name__ == "__main__":
    main()
