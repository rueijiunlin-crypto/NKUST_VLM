"""Compare how different prompt sets change CLIP zero-shot predictions."""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
PROMPT_SETS = {
    "object_only": [
        "cat",
        "dog",
        "sofa",
        "robot",
        "laboratory",
    ],
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
        "a photo of a pink sofa without animals",
        "a photo of a robot in a laboratory",
        "a photo of a laboratory room",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument("--top-k", type=int, default=3, help="Number of predictions per prompt set.")
    return parser.parse_args()


def run_prompt_set(processor, model, image, prompt_set_name: str, labels: list[str], top_k: int) -> None:
    import torch

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    safe_top_k = min(top_k, len(labels))
    top_indices = probabilities.topk(safe_top_k).indices.tolist()

    print(f"\nPrompt set: {prompt_set_name}")
    print(f"logits_per_image shape: {tuple(logits.shape)}")
    for index, (label, probability) in enumerate(zip(labels, probabilities.tolist())):
        print(f"{index}: {label} -> {probability:.4f}")

    print(f"Top-{safe_top_k}:")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. label[{index}] {labels[index]} ({probabilities[index].item():.4f})")


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"Missing dependency: {error.name}")
        print("Install with: python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image file not found: {args.image}")
        print("Try the Week02 demo image or pass another local image with --image.")
        return 1
    if args.top_k < 1:
        print("--top-k must be at least 1.")
        return 1

    image = Image.open(args.image).convert("RGB")

    print("Loading CLIPProcessor and CLIPModel...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    print(f"Model: {MODEL_NAME}")
    print(f"Image: {args.image}")

    for prompt_set_name, labels in PROMPT_SETS.items():
        run_prompt_set(processor, model, image, prompt_set_name, labels, args.top_k)

    print("\nNotes:")
    print("- Each prompt set creates a different candidate-label space.")
    print("- Softmax probabilities are relative within that prompt set.")
    print("- Compare whether top-1 changes and whether the distribution becomes sharper or flatter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
