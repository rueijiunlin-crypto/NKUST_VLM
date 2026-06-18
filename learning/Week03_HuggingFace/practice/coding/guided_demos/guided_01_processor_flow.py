"""Guided reading: inspect CLIPProcessor text and image tensors."""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "cat",
    "a photo of a cat",
    "a photo of two cats on a pink sofa",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_LABELS, help="Prompts to inspect.")
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"Missing dependency: {error.name}")
        print("Install with: python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image file not found: {args.image}")
        return 1

    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    print("[Step 1] Input labels")
    for index, label in enumerate(args.labels):
        print(f"{index}: {label}")

    print("\n[Step 2] Run CLIPProcessor")
    inputs = processor(text=args.labels, images=image, return_tensors="pt", padding=True)

    print("\n[Step 3] Tensor keys and shapes")
    for key, value in inputs.items():
        print(f"{key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n[Step 4] Token ids and attention mask")
    print("input_ids[0]:", inputs["input_ids"][0].tolist())
    print("attention_mask[0]:", inputs["attention_mask"][0].tolist())

    print("\nObservation prompts:")
    print("- Which dimension changes when you add more labels?")
    print("- Why do input_ids and attention_mask have the same shape?")
    print("- What does pixel_values tell you about image batch, channels, height, and width?")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
