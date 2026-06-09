"""Practice: simplified encoder-decoder flow."""

import numpy as np


def encoder_step(source_embeddings):
    """Create a simple encoder memory from source embeddings."""
    # TODO: Return a representation that summarizes or transforms source_embeddings.
    return None


def decoder_step(target_embeddings, encoder_memory):
    """Use target embeddings and encoder memory to produce a simple decoder output."""
    # TODO: Combine target information with encoder memory.
    raise NotImplementedError


def main():
    source_embeddings = np.array([[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]])
    target_embeddings = np.array([[1.0, 1.0], [0.0, 1.0]])

    memory = encoder_step(source_embeddings)
    output = decoder_step(target_embeddings, memory)

    print("encoder memory:", memory)
    print("decoder output:\n", output)


if __name__ == "__main__":
    main()
