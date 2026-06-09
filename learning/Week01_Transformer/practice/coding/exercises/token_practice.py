"""Practice: token to token id mapping."""


def build_vocab(tokens):
    """Return a dict that maps each token to an integer id."""
    # TODO: Replace None with a token-to-id dictionary.
    return None


def encode(tokens, vocab):
    """Convert tokens to token ids."""
    # TODO: Return a list of ids by looking up each token in vocab.
    raise NotImplementedError


def decode(token_ids, id_to_token):
    """Convert token ids back to tokens."""
    # TODO: Return a list of tokens by looking up each id.
    raise NotImplementedError


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
