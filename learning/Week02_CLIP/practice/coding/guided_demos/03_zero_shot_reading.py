"""逐步閱讀零樣本分類中的分數、Softmax 軸與 top-1。"""

import numpy as np


def softmax(values: np.ndarray, axis: int) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def main() -> None:
    labels = ["robot", "dog", "red apple", "laboratory", "chair"]

    # Step 1: 假設這是一張圖片與五個文字 prompt 的 cosine scores。
    cosine_scores = np.array([[0.96, 0.22, 0.38, 0.55, 0.31]])
    print("Step 1 - cosine scores")
    print("shape:", cosine_scores.shape)
    print(cosine_scores)

    # Step 2: 溫度尺度放大分數差距，真實 CLIP 會學習相似作用的尺度。
    logits = cosine_scores * 10.0
    print("\nStep 2 - scaled logits")
    print("shape:", logits.shape)
    print(logits)

    # Step 3: axis=1 表示每張圖片在所有 label 之間形成分布。
    probabilities = softmax(logits, axis=1)
    print("\nStep 3 - probabilities")
    print("shape:", probabilities.shape)
    print(np.round(probabilities, 4))
    print("row sums:", probabilities.sum(axis=1))

    # Step 4: top-1 是目前候選集合內機率最高的 label。
    top_index = int(np.argmax(probabilities[0]))
    print("\nStep 4 - prediction")
    for label, score, probability in zip(labels, cosine_scores[0], probabilities[0]):
        print(f"{label:10s} score={score:.2f}, probability={probability:.4f}")
    print("top-1:", labels[top_index])

    print("\n觀察問題：加入一個分數很高的新 label 後，原本機率會如何改變？")


if __name__ == "__main__":
    main()
