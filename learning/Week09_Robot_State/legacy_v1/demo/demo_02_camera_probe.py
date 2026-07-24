"""Probe one camera frame or use a deterministic synthetic source."""

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera-index", type=int, default=0)
    parser.add_argument("--synthetic", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    import cv2
    import numpy as np

    if args.synthetic:
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(frame, "synthetic frame", (120, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("source: synthetic")
        print("frame shape:", frame.shape)
        return

    capture = cv2.VideoCapture(args.camera_index)
    try:
        if not capture.isOpened():
            raise RuntimeError(f"Cannot open camera index {args.camera_index}")
        ok, frame = capture.read()
        if not ok or frame is None:
            raise RuntimeError("Camera opened but returned no frame")
        print("source: camera", args.camera_index)
        print("backend:", capture.getBackendName())
        print("frame shape:", frame.shape)
        print("dtype:", frame.dtype)
    finally:
        capture.release()


if __name__ == "__main__":
    main()
