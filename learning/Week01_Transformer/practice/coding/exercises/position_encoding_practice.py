"""Practice: add simple position encoding."""

import numpy as np


def make_position_encoding(seq_len, dim):
    """Create a simple deterministic position encoding."""
    # TODO: Return an array with shape (seq_len, dim).
    return None


def add_position_encoding(embeddings):
    """Add position information to embeddings."""
    # TODO: Create position encoding with the same shape as embeddings.
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
