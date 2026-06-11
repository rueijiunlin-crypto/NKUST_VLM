"""逐步顯示 Self-Attention 的分數、權重與輸出。"""

import numpy as np


def softmax(values: np.ndarray, axis: int = -1) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def main() -> None:
    tokens = ["red", "door", "ahead"]
    x = np.array(
        [
            [1.0, 0.0, 0.5],
            [0.8, 0.2, 0.5],
            [0.0, 1.0, 0.5],
        ]
    )

    # 使用單位矩陣讓 Q、K、V 等於 X，方便聚焦 Attention 資料流。
    q = x.copy()
    k = x.copy()
    v = x.copy()

    raw_scores = q @ k.T
    scaled_scores = raw_scores / np.sqrt(q.shape[-1])
    weights = softmax(scaled_scores, axis=-1)
    context = weights @ v

    print("Tokens:", tokens)
    print("X / Q / K / V shape:", x.shape)
    print("\nRaw scores = Q @ K.T:")
    print(np.round(raw_scores, 4))
    print("raw_scores shape:", raw_scores.shape)
    print("\nScaled scores:")
    print(np.round(scaled_scores, 4))
    print("\nAttention weights:")
    print(np.round(weights, 4))
    print("weights shape:", weights.shape)
    print("row sums:", np.round(weights.sum(axis=-1), 4))
    print("\nContext = weights @ V:")
    print(np.round(context, 4))
    print("context shape:", context.shape)

    for index, token in enumerate(tokens):
        focus_index = int(np.argmax(weights[index]))
        print(f"Query '{token}' 最關注 Key '{tokens[focus_index]}'")

    print("\n為什麼這樣寫：權重先描述每個 Query 如何分配注意力，再用相同權重混合 Value。")


if __name__ == "__main__":
    main()
