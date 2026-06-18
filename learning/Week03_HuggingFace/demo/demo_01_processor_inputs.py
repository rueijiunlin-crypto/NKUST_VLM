"""Inspect Hugging Face CLIPProcessor inputs for one image and several labels."""

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
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="Candidate text labels or prompts passed to CLIPProcessor.",
    )
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"Missing dependency: {error.name}")
        print("Install with: python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image file not found: {args.image}")
        print("Try the Week02 demo image or pass another local image with --image.")
        return 1

    image = Image.open(args.image).convert("RGB")
    labels = args.labels

    print("Loading CLIPProcessor...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    print(f"Model: {MODEL_NAME}")
    print(f"Image: {args.image}")
    print("\nLabels / prompts:")
    for index, label in enumerate(labels):
        print(f"{index}: {label}")

    print("\nProcessor output tensors:")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\nHow to read the shapes:")
    print("- input_ids: [num_texts, sequence_length]")
    print("- attention_mask: [num_texts, sequence_length]")
    print("- pixel_values: [num_images, channels, height, width]")
    print("- num_texts should match the number of labels above.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
