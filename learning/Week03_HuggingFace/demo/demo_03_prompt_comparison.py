"""Compare how different prompt sets affect CLIP zero-shot predictions."""

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
    parser.add_argument("--image", type=Path, required=True, help="Path to a local image.")
    return parser.parse_args()


def run_prompt_set(processor, model, image, prompt_set_name: str, labels: list[str]) -> None:
    import torch

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    with torch.inference_mode():
        outputs = model(**inputs)
        probabilities = outputs.logits_per_image.softmax(dim=1)[0]

    top_index = int(probabilities.argmax())
    print(f"\nPrompt set: {prompt_set_name}")
    for label, probability in zip(labels, probabilities.tolist()):
        print(f"- {label}: {probability:.4f}")
    print(f"Top-1: {labels[top_index]} ({probabilities[top_index].item():.4f})")


def main() -> int:
    try:
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

    print(f"Model: {MODEL_NAME}")
    print(f"Image path: {args.image}")

    for prompt_set_name, labels in PROMPT_SETS.items():
        run_prompt_set(processor, model, image, prompt_set_name, labels)

    print("\nInterpretation:")
    print("- CLIP compares the image against the exact prompts you provide.")
    print("- Different prompt wording can change text embeddings and prediction scores.")
    print("- For multi-object images, scene-aware prompts may better describe the whole image.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
