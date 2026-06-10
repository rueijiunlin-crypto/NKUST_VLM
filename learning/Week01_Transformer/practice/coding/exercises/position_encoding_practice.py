"""Practice: add simple position encoding."""

import numpy as np


def make_position_encoding(seq_len, dim):
    """Create a simple deterministic position encoding."""
    # TODO: 回傳 shape（形狀）為 (seq_len, dim) 的陣列。
    return None


def add_position_encoding(embeddings):
    """Add position information to embeddings."""
    # TODO: 建立與 embeddings 相同 shape（形狀）的 position encoding（位置編碼）。
    position = None
    return embeddings + position


def main():
    embeddings = np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
        ]
    )
    encoded = add_position_encoding(embeddings)
    print("encoded shape:", encoded.shape)
    print(encoded)


if __name__ == "__main__":
    main()
