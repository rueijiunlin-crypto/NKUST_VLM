"""觀察 Hugging Face CLIPProcessor 如何輸出圖文輸入張量。"""

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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    return parser.parse_args()


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}")
        print("請安裝依賴：python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"圖片路徑不存在：{args.image}")
        print("若 Week02 範例圖片不存在，請改用自己的本地圖片路徑。")
        return 1

    image = Image.open(args.image).convert("RGB")

    print("正在載入 processor（前處理器）。第一次執行可能會下載檔案。")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    inputs = processor(
        text=DEFAULT_LABELS,
        images=image,
        return_tensors="pt",
        padding=True,
    )

    print(f"模型：{MODEL_NAME}")
    print(f"圖片路徑：{args.image}")
    print("候選 labels（標籤）：")
    for label in DEFAULT_LABELS:
        print(f"- {label}")

    print("\nProcessor 輸出 keys（欄位）與 shape（形狀）：")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n解讀：")
    print("- input_ids / attention_mask 來自文字 prompts（提示詞）。")
    print("- pixel_values 來自圖片 resize（調整尺寸）與 normalization（正規化）後的結果。")
    print("- 這些 tensor（張量）才是送進 CLIPModel 的實際輸入。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
