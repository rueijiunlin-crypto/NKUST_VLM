"""Practice: scaled dot-product attention weights."""

import numpy as np


def softmax(x, axis=-1):
    """Compute softmax along the requested axis."""
    # TODO: Subtract max for stability, exponentiate, and normalize.
    raise NotImplementedError


def attention_weights(q, k):
    """Return the attention matrix from q and k."""
    d_k = q.shape[-1]
    # TODO: Compute scaled scores with q @ k.T / sqrt(d_k).
    scores = None
    # TODO: Apply softmax over the key axis.
    return None


def main():
    q = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    k = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])

    weights = attention_weights(q, k)
    print("weights shape:", weights.shape)
    print(weights)
    print("row sums:", weights.sum(axis=-1))


if __name__ == "__main__":
    main()
