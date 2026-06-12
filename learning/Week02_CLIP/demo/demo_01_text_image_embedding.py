"""快速展示影像與文字如何以相同維度向量表示。"""

import numpy as np


def main() -> None:
    labels = ["robot", "dog", "red apple", "laboratory", "chair"]
    image_embedding = np.array([0.90, 0.10, 0.30, 0.20], dtype=float)
    text_embeddings = np.array(
        [
            [0.88, 0.12, 0.28, 0.22],
            [0.10, 0.90, 0.20, 0.10],
            [0.20, 0.15, 0.90, 0.10],
            [0.45, 0.20, 0.30, 0.80],
            [0.20, 0.30, 0.10, 0.85],
        ],
        dtype=float,
    )

    print("Image embedding shape:", image_embedding.shape)
    print("Text embeddings shape:", text_embeddings.shape)
    print("\nImage embedding:", image_embedding)
    print("\nLabel -> text embedding")
    for label, embedding in zip(labels, text_embeddings):
        print(f"- {label:12s} -> {embedding}")

    print("\n觀察：兩種 embedding 的最後一維都是 4，因此可以做內積或餘弦相似度。")
    print("真實 CLIP 的向量由 Encoder 學得；這裡使用固定小向量建立資料流直覺。")


if __name__ == "__main__":
    main()
