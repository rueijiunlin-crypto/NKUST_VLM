"""Run Hugging Face CLIP zero-shot classification on a local image."""

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
    parser.add_argument("--image", type=Path, required=True, help="Path to a local image.")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="Candidate text labels or prompts. Provide one or more quoted labels.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of top predictions to print.",
    )
    return parser.parse_args()


def main() -> int:
    try:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"Missing package: {error.name}")
        print("Install dependencies with: python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"Image path does not exist: {args.image}")
        return 1

    image = Image.open(args.image).convert("RGB")

    print("Loading processor and model. The first run may download pretrained weights.")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    labels = args.labels
    inputs = processor(
        text=labels,
        images=image,
        return_tensors="pt",
        padding=True,
    )

    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()

    print(f"Model: {MODEL_NAME}")
    print(f"Image path: {args.image}")
    print(f"logits_per_image shape: {tuple(logits.shape)}")
    print("\nLabels and probabilities:")
    for label, probability in zip(labels, probabilities.tolist()):
        print(f"- {label}: {probability:.4f}")

    print(f"\nTop-{top_k} predictions:")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {labels[index]} ({probabilities[index].item():.4f})")

    print("\nInterpretation:")
    print("- logits_per_image is the raw score for each image-label pair.")
    print("- softmax converts scores into a relative distribution over the provided labels.")
    print("- The result depends on the candidate labels you provide.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
