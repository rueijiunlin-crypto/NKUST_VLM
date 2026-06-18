"""Run Hugging Face CLIP zero-shot image classification on a local image."""

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
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="Candidate labels or prompts. CLIP compares the image against these texts.",
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of highest-scoring labels to print.")
    return parser.parse_args()


def main() -> int:
    try:
        import torch
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
    labels = args.labels

    print("Loading CLIPProcessor and CLIPModel...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()

    print(f"Model: {MODEL_NAME}")
    print(f"Image: {args.image}")
    print("\nTensor shapes:")
    print(f"- input_ids: {tuple(inputs['input_ids'].shape)}")
    print(f"- attention_mask: {tuple(inputs['attention_mask'].shape)}")
    print(f"- pixel_values: {tuple(inputs['pixel_values'].shape)}")
    print(f"- logits_per_image: {tuple(logits.shape)}")
    print(f"- probabilities for image 0: {tuple(probabilities.shape)}")

    print("\nLabels and probabilities:")
    for index, (label, probability) in enumerate(zip(labels, probabilities.tolist())):
        print(f"{index}: {label} -> {probability:.4f}")

    print(f"\nTop-{top_k} predictions:")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. label[{index}] {labels[index]} ({probabilities[index].item():.4f})")

    print("\nNotes:")
    print("- logits_per_image has shape [num_images, num_texts].")
    print("- softmax(dim=1) normalizes across the candidate text labels for each image.")
    print("- topk().indices returns label indices, so we use labels[index] for the text.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
