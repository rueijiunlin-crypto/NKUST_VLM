"""Solution: scaled dot-product attention weights."""

import numpy as np


def softmax(x, axis=-1):
    shifted = x - np.max(x, axis=axis, keepdims=True)
    exp = np.exp(shifted)
    return exp / np.sum(exp, axis=axis, keepdims=True)


def attention_weights(q, k):
    d_k = q.shape[-1]
    scores = q @ k.T / np.sqrt(d_k)
    return softmax(scores, axis=-1)


def main():
    q = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    k = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])

    weights = attention_weights(q, k)
    print("weights shape:", weights.shape)
    print(weights)
    print("row sums:", weights.sum(axis=-1))


if __name__ == "__main__":
    main()
