"""Solution: split and combine attention heads."""

import numpy as np


def split_heads(x, num_heads):
    seq_len, d_model = x.shape
    if d_model % num_heads != 0:
        raise ValueError("d_model must be divisible by num_heads")
    head_dim = d_model // num_heads
    return x.reshape(seq_len, num_heads, head_dim).transpose(1, 0, 2)


def combine_heads(x):
    num_heads, seq_len, head_dim = x.shape
    return x.transpose(1, 0, 2).reshape(seq_len, num_heads * head_dim)


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
