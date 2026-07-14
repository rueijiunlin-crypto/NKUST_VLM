"""Trace a tiny two-layer MLP projector with visible shapes and values."""

from __future__ import annotations

import argparse

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    return parser.parse_args()


def gelu(x: np.ndarray) -> np.ndarray:
    """Approximate GELU activation used by many transformer MLPs."""
    coefficient = np.sqrt(2.0 / np.pi)
    return 0.5 * x * (1.0 + np.tanh(coefficient * (x + 0.044715 * x**3)))


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    batch, image_tokens = 1, 3
    vision_hidden, projector_hidden, language_hidden = 4, 5, 6
    vision_features = np.arange(
        batch * image_tokens * vision_hidden, dtype=np.float32
    ).reshape(batch, image_tokens, vision_hidden) / 10.0

    # Step 1: first linear layer maps the vision dimension to an MLP dimension.
    weight_1 = rng.normal(0.0, 0.2, (vision_hidden, projector_hidden))
    hidden_pre_activation = vision_features @ weight_1
    hidden = gelu(hidden_pre_activation)

    # Step 2: second linear layer maps into the LLM embedding dimension.
    weight_2 = rng.normal(0.0, 0.2, (projector_hidden, language_hidden))
    projected = hidden @ weight_2

    print(f"vision_features shape : {vision_features.shape}")
    print(f"weight_1 shape        : {weight_1.shape}")
    print(f"hidden shape          : {hidden.shape}")
    print(f"weight_2 shape        : {weight_2.shape}")
    print(f"projected shape       : {projected.shape}")
    print()
    print(f"first vision token    : {np.round(vision_features[0, 0], 3)}")
    print(f"first hidden token    : {np.round(hidden[0, 0], 3)}")
    print(f"first projected token : {np.round(projected[0, 0], 3)}")
    print()
    print("Observation: batch and image-token axes stay; the last dimension changes.")
    print("This toy projector aligns dimensions, but it does not generate text.")


if __name__ == "__main__":
    main()
