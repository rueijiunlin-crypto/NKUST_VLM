"""觀察 Token Embedding 如何加入位置資訊。"""

import numpy as np


SEQUENCE_LENGTH = 3
EMBEDDING_DIM = 4


def sinusoidal_position_encoding(sequence_length: int, embedding_dim: int) -> np.ndarray:
    positions = np.arange(sequence_length)[:, np.newaxis]
    dimensions = np.arange(embedding_dim)[np.newaxis, :]
    angle_rates = 1.0 / np.power(10000.0, 2 * (dimensions // 2) / embedding_dim)
    angles = positions * angle_rates

    encoding = np.zeros((sequence_length, embedding_dim))
    encoding[:, 0::2] = np.sin(angles[:, 0::2])
    encoding[:, 1::2] = np.cos(angles[:, 1::2])
    return encoding


def main() -> None:
    # 使用相同內容向量，刻意凸顯「位置」造成的差異。
    token_embeddings = np.tile(
        np.array([[0.5, 0.5, 0.5, 0.5]]), (SEQUENCE_LENGTH, 1)
    )
    position_encoding = sinusoidal_position_encoding(
        SEQUENCE_LENGTH, EMBEDDING_DIM
    )

    # 兩者 shape 相同，因此可以逐元素相加且不改變輸出 shape。
    position_aware_embeddings = token_embeddings + position_encoding

    print("Token embeddings:")
    print(token_embeddings)
    print("token_embeddings shape:", token_embeddings.shape)
    print("\nPosition encoding:")
    print(np.round(position_encoding, 4))
    print("position_encoding shape:", position_encoding.shape)
    print("\nPosition-aware embeddings:")
    print(np.round(position_aware_embeddings, 4))
    print("output shape:", position_aware_embeddings.shape)
    print("\n為什麼這樣寫：Self-Attention 沒有天然順序感，相加的位置訊號讓相同內容可被區分。")


if __name__ == "__main__":
    main()
