"""Solution: embedding lookup with NumPy."""

import numpy as np


def lookup_embeddings(token_ids, embedding_table):
    return embedding_table[token_ids]


def main():
    token_ids = np.array([0, 2, 1, 2])
    embedding_table = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )

    embeddings = lookup_embeddings(token_ids, embedding_table)
    print("token_ids shape:", token_ids.shape)
    print("embeddings shape:", embeddings.shape)
    print(embeddings)


if __name__ == "__main__":
    main()
