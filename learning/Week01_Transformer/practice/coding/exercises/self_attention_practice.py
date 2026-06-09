"""Practice: simple self-attention."""

import numpy as np


def softmax(x, axis=-1):
    """Compute softmax along the requested axis."""
    # TODO: Implement a numerically stable softmax.
    raise NotImplementedError


def self_attention(x, w_q, w_k, w_v):
    """Compute self-attention output for x."""
    # TODO: Build q, k, v from x.
    q = None
    k = None
    v = None

    # TODO: Compute attention weights and output.
    weights = None
    output = None
    return output, weights


def main():
    x = np.array(
        [
            [1.0, 0.0, 0.5],
            [0.0, 1.0, 0.5],
            [1.0, 1.0, 0.0],
        ]
    )
    w_q = np.eye(3)
    w_k = np.eye(3)
    w_v = np.eye(3)

    output, weights = self_attention(x, w_q, w_k, w_v)
    print("weights:\n", weights)
    print("output:\n", output)


if __name__ == "__main__":
    main()
