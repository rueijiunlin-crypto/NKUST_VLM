"""Practice: simple self-attention."""

import numpy as np


def softmax(x, axis=-1):
    """Compute softmax along the requested axis."""
    # TODO: 實作數值穩定的 softmax。
    raise NotImplementedError


def self_attention(x, w_q, w_k, w_v):
    """Compute self-attention output for x."""
    # TODO: 從 x 建立 q、k、v。
    q = None
    k = None
    v = None

    # TODO: 計算 attention weights（注意力權重）與輸出。
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
