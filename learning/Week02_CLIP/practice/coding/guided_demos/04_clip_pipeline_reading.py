"""逐步串接簡化 CLIP Encoder、投影、正規化與對比配對。"""

import numpy as np


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


def softmax(values: np.ndarray, axis: int) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def main() -> None:
    pairs = [("robot image", "robot text"), ("laboratory image", "laboratory text")]

    # Step 1: 兩個 Encoder 可輸出不同 feature 維度。
    image_features = np.array([[1.0, 0.1, 0.2, 0.0], [0.1, 0.3, 0.9, 0.8]])
    text_features = np.array([[0.9, 0.1, 0.1], [0.1, 0.4, 0.9]])
    print("Step 1 - encoder features")
    print("image_features shape:", image_features.shape)
    print("text_features shape:", text_features.shape)

    # Step 2: 各自 projection 到共同的 3 維 embedding space。
    image_projection = np.array(
        [[1.0, 0.0, 0.0], [0.0, 0.8, 0.0], [0.0, 0.0, 0.7], [0.0, 0.1, 0.6]]
    )
    text_projection = np.eye(3)
    image_embeddings = image_features @ image_projection
    text_embeddings = text_features @ text_projection
    print("\nStep 2 - projected embeddings")
    print("image_embeddings shape:", image_embeddings.shape)
    print("text_embeddings shape:", text_embeddings.shape)
    print("image_embeddings:\n", np.round(image_embeddings, 4))
    print("text_embeddings:\n", np.round(text_embeddings, 4))

    # Step 3: 正規化後，矩陣乘法得到所有圖文配對分數。
    normalized_images = normalize(image_embeddings)
    normalized_texts = normalize(text_embeddings)
    logits_per_image = normalized_images @ normalized_texts.T * 10.0
    logits_per_text = logits_per_image.T
    print("\nStep 3 - pair logits")
    print("logits_per_image shape:", logits_per_image.shape)
    print(np.round(logits_per_image, 4))
    print("logits_per_text shape:", logits_per_text.shape)

    # Step 4: 圖找文與文找圖分別沿各自候選軸做 Softmax。
    image_to_text = softmax(logits_per_image, axis=1)
    text_to_image = softmax(logits_per_text, axis=1)
    print("\nStep 4 - probabilities")
    print("image-to-text:\n", np.round(image_to_text, 4))
    print("text-to-image:\n", np.round(text_to_image, 4))

    # Step 5: 此 batch 按正配對排列，因此對角線是學習目標。
    print("\nStep 5 - positive pairs")
    for index, pair in enumerate(pairs):
        print(f"{pair[0]} <-> {pair[1]}: logit={logits_per_image[index, index]:.4f}")

    print("\n觀察問題：若交換兩段文字的列順序，正配對還會位於對角線嗎？")


if __name__ == "__main__":
    main()
