"""展示內積、向量長度與餘弦相似度的計算。"""

import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> tuple[float, float, float, float]:
    dot_product = float(np.dot(a, b))
    norm_a = float(np.linalg.norm(a))
    norm_b = float(np.linalg.norm(b))
    similarity = dot_product / (norm_a * norm_b)
    return dot_product, norm_a, norm_b, similarity


def main() -> None:
    image_embedding = np.array([0.9, 0.1, 0.3, 0.2])
    text_embeddings = {
        "a photo of a robot": np.array([0.88, 0.12, 0.28, 0.22]),
        "a photo of a dog": np.array([0.10, 0.90, 0.20, 0.10]),
        "a photo of a laboratory": np.array([0.45, 0.20, 0.30, 0.80]),
    }

    results = []
    for label, text_embedding in text_embeddings.items():
        dot_product, image_norm, text_norm, similarity = cosine_similarity(
            image_embedding, text_embedding
        )
        results.append((label, similarity))
        print(f"\nLabel: {label}")
        print(f"dot product: {dot_product:.4f}")
        print(f"image norm: {image_norm:.4f}")
        print(f"text norm: {text_norm:.4f}")
        print(f"cosine similarity: {similarity:.4f}")

    print("\nSimilarity ranking")
    for rank, (label, similarity) in enumerate(
        sorted(results, key=lambda item: item[1], reverse=True), start=1
    ):
        print(f"{rank}. {label}: {similarity:.4f}")


if __name__ == "__main__":
    main()
