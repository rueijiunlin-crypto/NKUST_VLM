"""Practice: token to token id mapping."""


def build_vocab(tokens):
    """Return a dict that maps each token to an integer id."""
    # TODO: 將 None 替換成 token 到 id 的字典。
    vocab = {}
    for token in tokens:
        if token not in vocab:
            vocab[token] = len(vocab)
    return vocab


def encode(tokens, vocab):
    """Convert tokens to token ids."""
    # TODO: 透過 vocab 查詢每個 token，回傳 id 清單。
    return [vocab[token] for token in tokens]


def decode(token_ids, id_to_token):
    """Convert token ids back to tokens."""
    # TODO: 透過每個 id 查詢對應 token，回傳 token 清單。
    return [id_to_token[token_id] for token_id in token_ids]


def main():
    tokens = ["a", "small", "robot", "sees", "a", "cup"]
    vocab = build_vocab(tokens)
    print("vocab:", vocab)

    ids = encode(tokens, vocab)
    print("ids:", ids)

    id_to_token = {idx: token for token, idx in vocab.items()}
    restored = decode(ids, id_to_token)
    print("restored:", restored)


if __name__ == "__main__":
    main()
