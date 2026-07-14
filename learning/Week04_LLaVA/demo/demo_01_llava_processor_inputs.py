"""觀察 LLaVA AutoProcessor 如何整理一張圖片與一個問題。"""

from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "llava-hf/llava-1.5-7b-hf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument(
        "--question",
        default="What is shown in this image?",
        help="放入多模態 prompt 的問題。",
    )
    parser.add_argument("--model-id", default=MODEL_NAME, help="Hugging Face Model ID。")
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
        print("請安裝：python -m pip install -r demo/requirements.txt")
        return 1

    image = Image.open(args.image).convert("RGB")
    prompt = f"USER: <image>\n{args.question.strip()} ASSISTANT:"

    print("正在載入 AutoProcessor（不載入完整 7B 生成模型）...")
    processor = AutoProcessor.from_pretrained(args.model_id)
    inputs = processor(images=image, text=prompt, return_tensors="pt")

    print(f"模型：{args.model_id}")
    print(f"圖片：{args.image}")
    print(f"圖片尺寸：{image.size}")
    print(f"Prompt：{prompt}")
    print("\nProcessor 輸出的 tensors：")
    for key, value in inputs.items():
        shape = tuple(value.shape) if hasattr(value, "shape") else "not a tensor"
        dtype = getattr(value, "dtype", type(value).__name__)
        print(f"- {key}: shape={shape}, dtype={dtype}")

    if "input_ids" in inputs:
        print(f"\ninput token count：{inputs['input_ids'].shape[1]}")
        print("input_ids 前 20 個值：", inputs["input_ids"][0, :20].tolist())
    print("\n觀察：<image> 是占位符，並不等於單一像素或單一 patch token。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
