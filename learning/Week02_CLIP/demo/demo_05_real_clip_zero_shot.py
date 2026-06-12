"""Optional: use Hugging Face CLIP for zero-shot image classification."""

from __future__ import annotations

import argparse
import sys
from io import BytesIO
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_IMAGE_URL = (
    "https://images.cocodataset.org/val2017/000000039769.jpg"
)
LABELS = [
    "a photo of a robot",
    "a photo of a dog",
    "a photo of a red apple",
    "a photo of a laboratory",
    "a photo of a chair",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, help="Path to a local image.")
    return parser.parse_args()


def main() -> int:
    try:
        import requests
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"Missing package: {error.name}")
        print("Install dependencies with: pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    try:
        if args.image:
            if not args.image.is_file():
                print(f"Image path does not exist: {args.image}")
                print("Provide an existing --image path or omit it to use the public COCO sample.")
                return 1
            image = Image.open(args.image).convert("RGB")
            image_source = str(args.image)
        else:
            # Public sample from the COCO validation image server.
            response = requests.get(DEFAULT_IMAGE_URL, timeout=30)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGB")
            image_source = DEFAULT_IMAGE_URL

        print("Loading model. The first run downloads pretrained weights.")
        processor = CLIPProcessor.from_pretrained(MODEL_NAME)
        model = CLIPModel.from_pretrained(MODEL_NAME)
        inputs = processor(text=LABELS, images=image, return_tensors="pt", padding=True)

        with torch.inference_mode():
            outputs = model(**inputs)
            probabilities = outputs.logits_per_image.softmax(dim=1)[0]

        print(f"Model: {MODEL_NAME}")
        print(f"Image path: {image_source}")
        print("Labels:")
        for label in LABELS:
            print(f"- {label}")
        print("Probabilities:")
        for label, probability in zip(LABELS, probabilities.tolist()):
            print(f"- {label}: {probability:.4f}")
        print("Top-1 prediction:", LABELS[int(probabilities.argmax())])
        return 0
    except Exception as error:
        print(f"Real CLIP demo could not finish: {error}")
        print("Check the network/model access, then retry. The NumPy concept demos remain usable.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
