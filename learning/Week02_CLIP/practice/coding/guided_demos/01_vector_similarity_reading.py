"""逐步閱讀向量正規化與餘弦相似度的計算流程。"""

import numpy as np


def main() -> None:
    image_vector = np.array([3.0, 1.0, 2.0])
    text_vector = np.array([2.8, 1.2, 2.1])

    # Step 1: 確認兩個向量維度一致，才能做內積。
    print("Step 1 - shapes")
    print("image_vector shape:", image_vector.shape)
    print("text_vector shape:", text_vector.shape)

    # Step 2: 計算內積與各自長度。
    dot_product = float(image_vector @ text_vector)
    image_norm = float(np.linalg.norm(image_vector))
    text_norm = float(np.linalg.norm(text_vector))
    print("\nStep 2 - intermediate values")
    print("dot product:", round(dot_product, 4))
    print("image norm:", round(image_norm, 4))
    print("text norm:", round(text_norm, 4))

    # Step 3: 用長度正規化，將比較重點放在方向。
    normalized_image = image_vector / image_norm
    normalized_text = text_vector / text_norm
    cosine = float(normalized_image @ normalized_text)
    print("\nStep 3 - normalized vectors")
    print("normalized image:", np.round(normalized_image, 4))
    print("normalized text:", np.round(normalized_text, 4))
    print("normalized image norm:", round(float(np.linalg.norm(normalized_image)), 4))
    print("normalized text norm:", round(float(np.linalg.norm(normalized_text)), 4))
    print("cosine similarity:", round(cosine, 4))

    print("\n觀察問題：把 text_vector 乘以 10，內積與 cosine similarity 各如何變化？")


if __name__ == "__main__":
    main()
