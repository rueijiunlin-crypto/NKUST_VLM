"""Guided reading: trace CLIP logits, softmax probabilities, and top-k indices."""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
    "a photo of a laboratory",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_LABELS, help="Candidate labels or prompts.")
    parser.add_argument("--top-k", type=int, default=3, help="Number of top predictions to inspect.")
    return parser.parse_args()


def main() -> int:
    try:
        import torch
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

    print("[Step 1] Load image, processor, and model")
    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    print("\n[Step 2] Build model inputs")
    labels = args.labels
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    print(f"labels count: {len(labels)}")
    print(f"input_ids shape: {tuple(inputs['input_ids'].shape)}")
    print(f"attention_mask shape: {tuple(inputs['attention_mask'].shape)}")
    print(f"pixel_values shape: {tuple(inputs['pixel_values'].shape)}")

    print("\n[Step 3] Run inference without gradients")
    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    print(f"logits_per_image shape: {tuple(logits.shape)}")
    print(f"probabilities shape after [0]: {tuple(probabilities.shape)}")

    print("\n[Step 4] Compare logits and probabilities")
    for index, (label, logit, probability) in enumerate(zip(labels, logits[0].tolist(), probabilities.tolist())):
        print(f"{index}: {label} | logit={logit:.4f} | probability={probability:.4f}")

    print("\n[Step 5] Inspect top-k indices")
    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()
    print(f"requested top_k={args.top_k}, safe top_k={top_k}")
    print(f"top indices: {top_indices}")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. labels[{index}] = {labels[index]} ({probabilities[index].item():.4f})")

    print("\nObservation prompts:")
    print("- Why does logits_per_image use [num_images, num_texts]?")
    print("- Why is softmax applied with dim=1?")
    print("- Why do top-k results need indices to recover label text?")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
