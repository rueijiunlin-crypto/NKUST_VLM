"""引導式程式閱讀：觀察 CLIPProcessor 如何把文字與圖片轉成 tensor。"""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="逐步閱讀 CLIPProcessor 輸出，作為 Week03 guided practice（引導式練習）。"
    )
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}")
        print("請安裝依賴：python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"圖片路徑不存在：{args.image}")
        print("請使用本地圖片路徑，例如：--image demo/my_image.jpg")
        return 1

    print("[Step 1] 載入本地圖片，並轉成 RGB image（紅綠藍影像）。")
    image = Image.open(args.image).convert("RGB")
    print(f"圖片載入後尺寸：{image.size}")

    print("\n[Step 2] 載入 CLIPProcessor。第一次執行可能會下載檔案。")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    print("\n[Step 3] 將 labels（候選標籤）與圖片送進 processor。")
    inputs = processor(text=DEFAULT_LABELS, images=image, return_tensors="pt", padding=True)

    print("\n[Step 4] 觀察 processor 輸出 keys（欄位）與 tensor shapes（張量形狀）。")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n[Observation 觀察]")
    print("- input_ids 與 attention_mask 來自文字 labels。")
    print("- pixel_values 來自圖片 resize（調整尺寸）、normalization（正規化）與 tensor conversion（張量轉換）。")
    print("- 這些 tensor 還不是 prediction（預測），而是 CLIPModel 的輸入。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
