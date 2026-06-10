"""Practice: split and combine attention heads."""

import numpy as np


def split_heads(x, num_heads):
    """Split x from (seq_len, d_model) to (num_heads, seq_len, head_dim)."""
    seq_len, d_model = x.shape
    # TODO: 檢查 d_model 是否可以被平均分成多個 head。
    # TODO: 重新 reshape 並 transpose，讓 num_heads 放在第一個維度。
    return None


def combine_heads(x):
    """Combine x from (num_heads, seq_len, head_dim) to (seq_len, d_model)."""
    # TODO: transpose 後再 reshape 回單一矩陣。
    return None


def main():
    x = np.arange(24, dtype=float).reshape(3, 8)
    heads = split_heads(x, num_heads=2)
    restored = combine_heads(heads)

    print("x shape:", x.shape)
    print("heads shape:", heads.shape)
    print("restored shape:", restored.shape)
    print("restored equals x:", np.allclose(restored, x))


if __name__ == "__main__":
    main()
