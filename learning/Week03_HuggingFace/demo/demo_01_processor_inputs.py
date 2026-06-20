"""檢查 Hugging Face CLIPProcessor 如何處理一張圖片與多個 labels。"""

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


def parse_args() -> argparse.Namespace: #parse_args() -> argparse.Namespace:是一個函數定義，表示該函數將返回一個argparse.Namespace對象。argparse.Namespace是一個簡單的類，用於存儲命令行參數的值。當你使用argparse模塊解析命令行參數時，解析器會返回一個Namespace對象，其中包含了所有解析到的參數及其對應的值。
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="傳入 CLIPProcessor 的候選文字 labels 或 prompts。",
    )
    return parser.parse_args()
"""這串程式碼定義了一個名為parse_args的函數，用於解析命令行參數。該函數使用argparse模塊創建了一個ArgumentParser對象，並添加了兩個參數："""


def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPProcessor
    except ImportError as error:
        print(f"缺少必要套件：{error.name}")
        print("請安裝：python -m pip install -r demo/requirements.txt")
        return 1
        #這段程式碼定義了一個名為main的函數，該函數首先嘗試導入PIL庫中的Image模塊和transformers庫中的CLIPProcessor模塊。
        #如果這些模塊未安裝，則會捕獲ImportError異常並打印錯誤信息，提示用戶安裝缺失的依賴項。接著，函數調用parse_args()來解析命令行參數，并檢查指定的圖像文件是否存在。
        #如果圖像文件不存在，則打印錯誤信息並返回1。
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        print("請改用 Week02 demo 圖片，或用 --image 指定另一張本機圖片。")
        return 1
        #如果圖像文件存在，則使用PIL庫中的Image模塊打開圖像文件並將其轉換為RGB格式。
        #接著，從命令行參數中獲取文本標籤列表。
    image = Image.open(args.image).convert("RGB")
    labels = args.labels
        #然後，使用CLIPProcessor從預訓練模型中加載處理器，並將文本標籤和圖像作為輸入傳遞給處理器。
        #處理器將返回一個包含處理後的張量的字典。
    print("正在載入 CLIPProcessor...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
        #最後，打印模型名稱、圖像路徑、文本標籤列表以及處理器輸出的張量的形狀和數據類型。
        #還提供了如何解讀這些張量形狀的說明。
    print(f"模型：{MODEL_NAME}")
    print(f"圖片：{args.image}")
    print("\n候選 labels / prompts：")
    for index, label in enumerate(labels):
        print(f"{index}: {label}")

    print("\nProcessor 輸出的 tensors：")
    for key, value in inputs.items():
        print(f"- {key}: shape={tuple(value.shape)}, dtype={value.dtype}")

    print("\n如何解讀 shape：")
    print("- input_ids: [num_texts, sequence_length]，代表文字數量與 token 序列長度")
    print("- attention_mask: [num_texts, sequence_length]，代表有效 token 與 padding")
    print("- pixel_values: [num_images, channels, height, width]，代表圖片 batch 與影像尺寸")
    print("- num_texts 應該等於上方 labels 數量。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
