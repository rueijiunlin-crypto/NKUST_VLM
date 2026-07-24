"""Show the OpenCV frame contract and BGR-to-RGB conversion."""

import cv2
import numpy as np


def main() -> None:
    frame_bgr = np.zeros((3, 4, 3), dtype=np.uint8)
    frame_bgr[:, :, 0] = 255
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

    print("BGR shape:", frame_bgr.shape)
    print("dtype:", frame_bgr.dtype)
    print("contiguous:", frame_bgr.flags.c_contiguous)
    print("first BGR pixel:", frame_bgr[0, 0].tolist())
    print("first RGB pixel:", frame_rgb[0, 0].tolist())


if __name__ == "__main__":
    main()
