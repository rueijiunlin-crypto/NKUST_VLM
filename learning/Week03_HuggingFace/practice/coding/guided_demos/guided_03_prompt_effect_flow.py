"""Guided reading: compare CLIP predictions across prompt sets."""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
PROMPT_SETS = {
    "object_only": ["cat", "dog", "sofa", "robot", "laboratory"],
    "photo_template": [
        "a photo of a cat",
        "a photo of a dog",
        "a photo of a sofa",
        "a photo of a robot",
        "a photo of a laboratory",
    ],
    "scene_aware": [
        "a photo of two cats on a pink sofa",
        "a photo of a dog on a sofa",
        "a photo of an empty sofa",
        "a photo of a robot in a laboratory",
        "a photo of a laboratory room",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument("--top-k", type=int, default=3, help="Number of top predictions to inspect.")
    return parser.parse_args()


def run_prompt_set(processor, model, image, name: str, labels: list[str], top_k: int) -> None:
    import torch

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    safe_top_k = min(top_k, len(labels))
    top_indices = probabilities.topk(safe_top_k).indices.tolist()

    print(f"\n[Prompt set] {name}")
    print(f"labels count: {len(labels)}")
    print(f"logits_per_image shape: {tuple(logits.shape)}")
    for index, (label, probability) in enumerate(zip(labels, probabilities.tolist())):
        print(f"{index}: {label} -> {probability:.4f}")
    print(f"Top-{safe_top_k}:")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. labels[{index}] = {labels[index]} ({probabilities[index].item():.4f})")


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"Missing dependency: {error.name}")
        print("Install with: python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image file not found: {args.image}")
        return 1
    if args.top_k < 1:
        print("--top-k must be at least 1.")
        return 1

    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    for name, labels in PROMPT_SETS.items():
        run_prompt_set(processor, model, image, name, labels, args.top_k)

    print("\nObservation prompts:")
    print("- Did top-1 change across prompt sets?")
    print("- Which prompt set produced the sharpest probability distribution?")
    print("- Which prompt set seems most stable, and why?")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
