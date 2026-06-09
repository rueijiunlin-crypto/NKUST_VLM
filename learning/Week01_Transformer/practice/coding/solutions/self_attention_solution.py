"""Solution: simple self-attention."""

import numpy as np


def softmax(x, axis=-1):
    shifted = x - np.max(x, axis=axis, keepdims=True)
    exp = np.exp(shifted)
    return exp / np.sum(exp, axis=axis, keepdims=True)


def self_attention(x, w_q, w_k, w_v):
    q = x @ w_q
    k = x @ w_k
    v = x @ w_v
    scores = q @ k.T / np.sqrt(q.shape[-1])
    weights = softmax(scores, axis=-1)
    output = weights @ v
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
