"""引導式程式閱讀：觀察 LLaVA AutoProcessor 的多模態輸入資料流。"""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "llava-hf/llava-1.5-7b-hf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument("--question", default="What is shown in this image?")
    parser.add_argument("--model-id", default=MODEL_NAME)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1
    if not args.question.strip():
        print("問題不可為空白。")
        return 1

    try:
        from PIL import Image
        from transformers import AutoProcessor
    except ImportError as error:
        print(f"缺少必要套件：{error.name}")
        print("請安裝：python -m pip install -r practice/coding/requirements.txt")
        return 1

    # 步驟 1：建立人類可讀的圖片與文字輸入。
    image = Image.open(args.image).convert("RGB")
    prompt = f"USER: <image>\n{args.question.strip()} ASSISTANT:"
    print("[步驟 1] 原始輸入")
    print(f"image path: {args.image}")
    print(f"image size: {image.size}")
    print(f"prompt: {prompt}")

    # 步驟 2：載入 checkpoint 對應的 Processor，不載入生成模型權重。
    print("\n[步驟 2] 載入 AutoProcessor")
    processor = AutoProcessor.from_pretrained(args.model_id)
    print(f"processor class: {processor.__class__.__name__}")
    print(f"tokenizer class: {processor.tokenizer.__class__.__name__}")
    print(f"image processor class: {processor.image_processor.__class__.__name__}")

    # 步驟 3：同一次呼叫產生文字與圖片 tensor。
    print("\n[步驟 3] 執行多模態前處理")
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    for key, value in inputs.items():
        shape = tuple(value.shape) if hasattr(value, "shape") else "not a tensor"
        dtype = getattr(value, "dtype", type(value).__name__)
        print(f"{key}: shape={shape}, dtype={dtype}")

    # 步驟 4：檢查文字 token，但不把 Token ID 誤認成 embedding vector。
    print("\n[步驟 4] Token IDs 與解碼結果")
    token_ids = inputs["input_ids"][0]
    preview_ids = token_ids[:30].tolist()
    print(f"input_ids 前 30 個值: {preview_ids}")
    print("decoded preview:", processor.tokenizer.decode(preview_ids))
    print("attention_mask 前 30 個值:", inputs["attention_mask"][0, :30].tolist())

    print("\n觀察問題：")
    print("- input_ids 與 attention_mask 為什麼 shape 相同？")
    print("- pixel_values 的四個維度分別代表什麼？")
    print("- Token ID 為什麼不是 LLM hidden vector？")
    print("- Processor 成功為什麼不代表完整 7B 模型已載入？")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
