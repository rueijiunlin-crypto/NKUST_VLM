"""使用固定假向量展示零樣本分類的分數、機率與 top-1。"""

import numpy as np


LABELS = [
    "a photo of a robot",
    "a photo of a dog",
    "a photo of a red apple",
    "a photo of a laboratory",
    "a photo of a chair",
]


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def softmax(values: np.ndarray) -> np.ndarray:
    shifted = values - np.max(values)
    exponentials = np.exp(shifted)
    return exponentials / exponentials.sum()


def main() -> None:
    image_embedding = np.array([[0.90, 0.10, 0.30, 0.20]])
    text_embeddings = np.array(
        [
            [0.88, 0.12, 0.28, 0.22],
            [0.10, 0.90, 0.20, 0.10],
            [0.20, 0.15, 0.90, 0.10],
            [0.45, 0.20, 0.30, 0.80],
            [0.20, 0.30, 0.10, 0.85],
        ]
    )

    similarities = (normalize(image_embedding) @ normalize(text_embeddings).T)[0]
    probabilities = softmax(similarities * 10.0)

    print("Zero-shot classification")
    for label, score, probability in zip(LABELS, similarities, probabilities):
        print(f"- {label}")
        print(f"  similarity score: {score:.4f}")
        print(f"  probability: {probability:.4f}")

    best_index = int(np.argmax(probabilities))
    print("\nTop-1 prediction:", LABELS[best_index])


if __name__ == "__main__":
    main()
