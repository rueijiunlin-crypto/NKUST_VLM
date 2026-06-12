"""整合展示簡化 CLIP 的編碼、相似度矩陣與預測流程。"""

import numpy as np


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def main() -> None:
    images = ["robot_scene.jpg", "laboratory_scene.jpg"]
    labels = ["a photo of a robot", "a photo of a laboratory", "a photo of a chair"]

    # 這些固定向量代表 Encoder 的簡化輸出，不是手工影像特徵。
    image_embeddings = np.array(
        [[0.90, 0.10, 0.20], [0.20, 0.30, 0.90]], dtype=float
    )
    text_embeddings = np.array(
        [[0.88, 0.12, 0.20], [0.18, 0.28, 0.92], [0.25, 0.75, 0.20]],
        dtype=float,
    )

    similarity_matrix = normalize(image_embeddings) @ normalize(text_embeddings).T

    print("Image -> Image Encoder -> Image Embedding")
    print("image_embeddings shape:", image_embeddings.shape)
    print("\nText Labels -> Text Encoder -> Text Embeddings")
    print("text_embeddings shape:", text_embeddings.shape)
    print("\nSimilarity Matrix")
    print("shape:", similarity_matrix.shape)
    print(np.round(similarity_matrix, 4))
    print("\nPrediction")
    for image_index, image_name in enumerate(images):
        label_index = int(np.argmax(similarity_matrix[image_index]))
        print(f"- {image_name} -> {labels[label_index]}")


if __name__ == "__main__":
    main()
