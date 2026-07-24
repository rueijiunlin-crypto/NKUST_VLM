"""使用 BLIP VQA base 對本機圖片提出一個問題。"""

from __future__ import annotations

import argparse
import time
from pathlib import Path


MODEL_ID = "Salesforce/blip-vqa-base"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--question", required=True)
    parser.add_argument("--model-id", default=MODEL_ID)
    parser.add_argument("--max-new-tokens", type=int, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file() or not args.question.strip() or args.max_new_tokens <= 0:
        print("圖片、非空問題與正整數 --max-new-tokens 為必要輸入。")
        return 1
    try:
        import torch
        from PIL import Image
        from transformers import BlipForQuestionAnswering, BlipProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}；請安裝 demo/requirements.txt")
        return 1

    device = "cuda" if torch.cuda.is_available() else "cpu"
    processor = BlipProcessor.from_pretrained(args.model_id)
    model = BlipForQuestionAnswering.from_pretrained(args.model_id).to(device)
    image = Image.open(args.image).convert("RGB")
    inputs = processor(images=image, text=args.question.strip(), return_tensors="pt").to(device)
    started = time.perf_counter()
    with torch.inference_mode():
        output_ids = model.generate(**inputs, max_new_tokens=args.max_new_tokens)
    elapsed = time.perf_counter() - started
    answer = processor.decode(output_ids[0], skip_special_tokens=True)
    print(f"model: {args.model_id}")
    print(f"question: {args.question.strip()}")
    print(f"input_ids: {tuple(inputs['input_ids'].shape)}")
    print(f"pixel_values: {tuple(inputs['pixel_values'].shape)}")
    print(f"answer: {answer}")
    print(f"inference_seconds: {elapsed:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
