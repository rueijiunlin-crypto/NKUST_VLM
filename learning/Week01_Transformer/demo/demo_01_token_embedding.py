"""快速展示文字如何變成 Token、Token ID 與向量。"""


def main() -> None:
    sentence = "take me to the laboratory"
    tokens = sentence.split()
    vocabulary = {token: index for index, token in enumerate(dict.fromkeys(tokens))}
    token_ids = [vocabulary[token] for token in tokens]

    # 使用小型固定向量建立直覺；真實模型的 Embedding 會由訓練學得。
    embeddings = {
        token: [round(token_id / 10, 1), round((token_id + 1) / 10, 1)]
        for token, token_id in vocabulary.items()
    }

    print("Text:", sentence)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)
    print("Embedding examples:", [embeddings[token] for token in tokens])
    print("\n觀察：文字先變成 Token 與索引，再查表取得模型可計算的向量。")


if __name__ == "__main__":
    main()
