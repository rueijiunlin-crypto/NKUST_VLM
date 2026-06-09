"""Solution: add simple position encoding."""

import numpy as np


def make_position_encoding(seq_len, dim):
    positions = np.arange(seq_len, dtype=float).reshape(seq_len, 1)
    scales = np.arange(1, dim + 1, dtype=float).reshape(1, dim)
    return positions / scales


def add_position_encoding(embeddings):
    seq_len, dim = embeddings.shape
    position = make_position_encoding(seq_len, dim)
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
