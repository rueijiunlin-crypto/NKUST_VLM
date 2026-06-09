"""Practice: split and combine attention heads."""

import numpy as np


def split_heads(x, num_heads):
    """Split x from (seq_len, d_model) to (num_heads, seq_len, head_dim)."""
    seq_len, d_model = x.shape
    # TODO: Check that d_model can be split evenly.
    # TODO: Reshape and transpose to put num_heads first.
    return None


def combine_heads(x):
    """Combine x from (num_heads, seq_len, head_dim) to (seq_len, d_model)."""
    # TODO: Transpose and reshape back to one matrix.
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
