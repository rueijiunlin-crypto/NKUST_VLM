"""追蹤輸入 X 經過三組權重後如何形成 Q、K、V。"""

import numpy as np


def main() -> None:
    # 三個 Token，每個 Token 使用四維表示。
    x = np.array(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
            [1.0, 1.0, 0.0, 0.0],
        ]
    )

    # 投影到二維，讓中間數值容易閱讀。
    w_q = np.array([[1.0, 0.0], [0.0, 1.0], [0.5, 0.0], [0.0, 0.5]])
    w_k = np.array([[0.5, 0.0], [0.0, 0.5], [1.0, 0.0], [0.0, 1.0]])
    w_v = np.array([[0.5, 0.0], [0.0, 0.5], [0.5, 0.0], [0.0, 0.5]])

    # 相同輸入搭配不同權重，會得到用途不同的三組表示。
    q = x @ w_q
    k = x @ w_k
    v = x @ w_v

    print("X:")
    print(x)
    print("X shape:", x.shape)
    print("\nW_Q / W_K / W_V shape:", w_q.shape, w_k.shape, w_v.shape)
    print("\nQ:")
    print(q)
    print("Q shape:", q.shape)
    print("\nK:")
    print(k)
    print("K shape:", k.shape)
    print("\nV:")
    print(v)
    print("V shape:", v.shape)
    print("\n為什麼這樣寫：Q 與 K 用來決定關注關係，V 保存最後要被加權取用的內容。")


if __name__ == "__main__":
    main()
