"""Inspect Hugging Face CLIPProcessor outputs for image-text inputs."""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to a local image.")
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"Missing package: {error.name}")
        print("Install dependencies with: python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image path does not exist: {args.image}")
        return 1

    image = Image.open(args.image).convert("RGB")

    print("Loading processor. The first run may download files.")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    inputs = processor(
        text=DEFAULT_LABELS,
        images=image,
        return_tensors="pt",
        padding=True,
    )

    print(f"Model: {MODEL_NAME}")
    print(f"Image path: {args.image}")
    print("Labels:")
    for label in DEFAULT_LABELS:
        print(f"- {label}")

    print("\nProcessor output keys and shapes:")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\nInterpretation:")
    print("- input_ids / attention_mask come from text prompts.")
    print("- pixel_values comes from the image after resize and normalization.")
    print("- These tensors are the actual inputs sent to CLIPModel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
