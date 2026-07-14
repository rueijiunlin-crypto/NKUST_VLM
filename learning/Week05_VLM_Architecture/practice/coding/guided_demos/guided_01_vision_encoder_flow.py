"""引導式程式閱讀：追蹤小型 RGB 圖片如何形成 patch vectors。"""

from __future__ import annotations

import argparse
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image-size", type=int, default=4)
    parser.add_argument("--patch-size", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.image_size <= 0 or args.patch_size <= 0 or args.image_size % args.patch_size:
        print("image size 與 patch size 必須為可整除的正整數。")
        return 1
    image = np.arange(3 * args.image_size**2, dtype=np.float32).reshape(
        1, 3, args.image_size, args.image_size
    )
    grid = args.image_size // args.patch_size
    patches = image.reshape(1, 3, grid, args.patch_size, grid, args.patch_size)
    patches = patches.transpose(0, 2, 4, 1, 3, 5)
    patch_vectors = patches.reshape(1, grid * grid, 3 * args.patch_size**2)
    print(f"[步驟 1] image shape        : {image.shape}")
    print(f"[步驟 2] patch grid         : {grid} x {grid}")
    print(f"[步驟 3] patch vector shape : {patch_vectors.shape}")
    print(f"[步驟 4] first patch values : {patch_vectors[0, 0].tolist()}")
    print("\nPatch vector 還不是 contextualized vision feature。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
