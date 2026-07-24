"""使用 BLIP base 模型對本機圖片產生 Image Caption。"""

from __future__ import annotations

import argparse
import time
from pathlib import Path


MODEL_ID = "Salesforce/blip-image-captioning-base"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--model-id", default=MODEL_ID)
    parser.add_argument("--max-new-tokens", type=int, default=40)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file() or args.max_new_tokens <= 0:
        print("圖片必須存在，且 --max-new-tokens 必須為正整數。")
        return 1
    try:
        import torch
        from PIL import Image
        from transformers import BlipForConditionalGeneration, BlipProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}；請安裝 demo/requirements.txt")
        return 1

    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = BlipProcessor.from_pretrained(args.model_id)
    model = BlipForConditionalGeneration.from_pretrained(args.model_id).to(device)
    image = Image.open(args.image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    started = time.perf_counter()
    with torch.inference_mode():
        output_ids = model.generate(**inputs, max_new_tokens=args.max_new_tokens)
    elapsed = time.perf_counter() - started
    caption = processor.decode(output_ids[0], skip_special_tokens=True)
    print(f"model: {args.model_id}")
    print(f"device: {device}")
    print(f"pixel_values: {tuple(inputs['pixel_values'].shape)}")
    print(f"caption: {caption}")
    print(f"inference_seconds: {elapsed:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
