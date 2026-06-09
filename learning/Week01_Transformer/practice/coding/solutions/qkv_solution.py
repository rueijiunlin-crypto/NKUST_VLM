"""Solution: create Q, K, V projections."""

import numpy as np


def project_qkv(x, w_q, w_k, w_v):
    q = x @ w_q
    k = x @ w_k
    v = x @ w_v
    return q, k, v


def main():
    x = np.array(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
            [1.0, 1.0, 0.0, 0.0],
        ]
    )
    w_q = np.eye(4, 2)
    w_k = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
    w_v = np.array([[0.5, 0.0], [0.0, 0.5], [0.5, 0.0], [0.0, 0.5]])

    q, k, v = project_qkv(x, w_q, w_k, w_v)
    print("Q shape:", q.shape)
    print("K shape:", k.shape)
    print("V shape:", v.shape)
    print("Q:\n", q)
    print("K:\n", k)
    print("V:\n", v)


if __name__ == "__main__":
    main()
