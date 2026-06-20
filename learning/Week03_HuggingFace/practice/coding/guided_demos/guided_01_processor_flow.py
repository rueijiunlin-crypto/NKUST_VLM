"""引導式程式閱讀：觀察 CLIPProcessor 的文字與圖片 tensors。"""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "cat",
    "a photo of a cat",
    "a photo of two cats on a pink sofa",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_LABELS, help="要觀察的 prompts。")
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"缺少必要套件：{error.name}")
        print("請安裝：python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1

    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    print("[步驟 1] 輸入 labels")
    for index, label in enumerate(args.labels):
        print(f"{index}: {label}")

    print("\n[步驟 2] 執行 CLIPProcessor")
    inputs = processor(text=args.labels, images=image, return_tensors="pt", padding=True)

    print("\n[步驟 3] Tensor keys 與 shapes")
    for key, value in inputs.items():
        print(f"{key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n[步驟 4] Token ids 與 attention mask")
    print("input_ids[0]:", inputs["input_ids"][0].tolist())
    print("attention_mask[0]:", inputs["attention_mask"][0].tolist())

    print("\n觀察問題：")
    print("- 增加 labels 時，哪一個維度會改變？")
    print("- 為什麼 input_ids 與 attention_mask 有相同 shape？")
    print("- pixel_values 如何表示圖片 batch、channels、高度與寬度？")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
