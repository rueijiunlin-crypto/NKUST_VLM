"""追蹤文字如何變成 Token ID，再查表取得 Embedding。"""

import numpy as np


SENTENCE = "a small robot sees a cup"
EMBEDDING_DIM = 3


def main() -> None:
    # 先切成 Token。這裡使用空白切分，只為了看清楚資料流。
    tokens = SENTENCE.lower().split()

    # 依首次出現順序建立詞彙表，讓重複 Token 共用同一個 ID。
    vocabulary: dict[str, int] = {}
    for token in tokens:
        if token not in vocabulary:
            vocabulary[token] = len(vocabulary)

    token_ids = np.array([vocabulary[token] for token in tokens])

    # 每一列對應一個 Token ID；真實模型會在訓練中學習這些數值。
    embedding_table = np.arange(
        len(vocabulary) * EMBEDDING_DIM, dtype=float
    ).reshape(len(vocabulary), EMBEDDING_DIM)
    embedding_table /= 10.0

    # NumPy 使用 Token ID 當列索引，一次取出整段序列的向量。
    embeddings = embedding_table[token_ids]

    print("輸入文字:", SENTENCE)
    print("Tokens:", tokens)
    print("Vocabulary:", vocabulary)
    print("Token IDs:", token_ids)
    print("token_ids shape:", token_ids.shape)
    print("\nEmbedding table:")
    print(embedding_table)
    print("embedding_table shape:", embedding_table.shape)
    print("\nLookup result:")
    print(embeddings)
    print("embeddings shape:", embeddings.shape)
    print("\n為什麼這樣寫：Token ID 只負責查表，Embedding 才是後續矩陣運算使用的向量。")


if __name__ == "__main__":
    main()
