"""引導式程式閱讀：觀察兩層 Projector 的 shape 與中間值。"""

from __future__ import annotations

import argparse
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)
    features = np.arange(12, dtype=np.float32).reshape(1, 3, 4) / 10
    w1 = rng.normal(0, 0.2, (4, 5))
    w2 = rng.normal(0, 0.2, (5, 6))
    hidden = np.maximum(features @ w1, 0)
    projected = hidden @ w2
    print(f"vision features : {features.shape}")
    print(f"first weight    : {w1.shape}")
    print(f"hidden          : {hidden.shape}")
    print(f"second weight   : {w2.shape}")
    print(f"projected       : {projected.shape}")
    print("first projected token:", np.round(projected[0, 0], 4).tolist())
    print("\nBatch 與 token axes 保留，最後一維轉成語言模型介面。")


if __name__ == "__main__":
    main()
