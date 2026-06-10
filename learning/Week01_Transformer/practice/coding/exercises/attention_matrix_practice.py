"""Practice: scaled dot-product attention weights."""

import numpy as np


def softmax(x, axis=-1):#softmax(x_i) = exp(x_i) / sum(exp(x))
    """Compute softmax along the requested axis."""
    # TODO: 為了數值穩定先減去最大值，再取指數並正規化。
    shifted = x - np.max(x, axis=axis, keepdims=True)  #每一組分數先減掉最大值，避免 exp() 數值爆掉。
    exp = np.exp(shifted)                              #把每個分數取指數，讓大分數變得更突出，小分數變得更小。
    return exp / np.sum(exp, axis=axis, keepdims=True) #把每個指數值除以該列的總和，讓輸出總和為 1。


def attention_weights(q, k):
    """Return the attention matrix from q and k."""
    d_k = q.shape[-1]
    scores = q @ k.T / np.sqrt(d_k)
    # TODO: 沿著 key 軸套用 softmax。
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
