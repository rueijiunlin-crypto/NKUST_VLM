"""Practice: scaled dot-product attention weights."""

import numpy as np


def softmax(x, axis=-1):
    """Compute softmax along the requested axis."""
    # TODO: 為了數值穩定先減去最大值，再取指數並正規化。
    raise NotImplementedError


def attention_weights(q, k):
    """Return the attention matrix from q and k."""
    d_k = q.shape[-1]
    # TODO: 使用 q @ k.T / sqrt(d_k) 計算縮放後的分數。
    scores = None
    # TODO: 沿著 key 軸套用 softmax。
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
