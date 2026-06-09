"""Solution: simplified encoder-decoder flow."""

import numpy as np


def encoder_step(source_embeddings):
    return source_embeddings.mean(axis=0)


def decoder_step(target_embeddings, encoder_memory):
    return target_embeddings + encoder_memory


def main():
    source_embeddings = np.array([[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]])
    target_embeddings = np.array([[1.0, 1.0], [0.0, 1.0]])

    memory = encoder_step(source_embeddings)
    output = decoder_step(target_embeddings, memory)

    print("encoder memory:", memory)
    print("decoder output:\n", output)


if __name__ == "__main__":
    main()
