"""逐步追蹤圖文 embedding 與相似度矩陣的 shape。"""

import numpy as np


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


def main() -> None:
    images = ["robot image", "laboratory image"]
    texts = ["robot text", "laboratory text", "chair text"]

    # Step 1: 每一列是一個樣本，每一欄是一個 embedding 維度。
    image_embeddings = np.array([[0.9, 0.1, 0.2], [0.2, 0.3, 0.9]])
    text_embeddings = np.array(
        [[0.88, 0.12, 0.2], [0.18, 0.28, 0.92], [0.2, 0.9, 0.1]]
    )
    print("Step 1 - encoder outputs")
    print("image_embeddings shape:", image_embeddings.shape)
    print("text_embeddings shape:", text_embeddings.shape)

    # Step 2: 對每列做 L2 normalization。
    normalized_images = normalize(image_embeddings)
    normalized_texts = normalize(text_embeddings)
    print("\nStep 2 - row norms")
    print("image row norms:", np.round(np.linalg.norm(normalized_images, axis=1), 4))
    print("text row norms:", np.round(np.linalg.norm(normalized_texts, axis=1), 4))

    # Step 3: 文字矩陣轉置後，所有圖片可一次和所有文字比較。
    similarity_matrix = normalized_images @ normalized_texts.T
    print("\nStep 3 - similarity matrix")
    print("shape:", similarity_matrix.shape)
    print(np.round(similarity_matrix, 4))

    # Step 4: 逐列讀取每張圖片最相近的文字。
    print("\nStep 4 - best text per image")
    for row, image in enumerate(images):
        column = int(np.argmax(similarity_matrix[row]))
        print(f"{image} -> {texts[column]}")

    print("\n觀察問題：矩陣 row、column 各代表哪一種模態？")


if __name__ == "__main__":
    main()
