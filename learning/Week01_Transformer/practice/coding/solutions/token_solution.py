"""Solution: token to token id mapping."""


def build_vocab(tokens):
    vocab = {}
    for token in tokens:
        if token not in vocab:
            vocab[token] = len(vocab)
    return vocab


def encode(tokens, vocab):
    return [vocab[token] for token in tokens]


def decode(token_ids, id_to_token):
    return [id_to_token[token_id] for token_id in token_ids]


def main():
    tokens = ["a", "small", "robot", "sees", "a", "cup"]
    vocab = build_vocab(tokens)
    ids = encode(tokens, vocab)
    id_to_token = {idx: token for token, idx in vocab.items()}
    restored = decode(ids, id_to_token)

    print("vocab:", vocab)
    print("ids:", ids)
    print("restored:", restored)


if __name__ == "__main__":
    main()
