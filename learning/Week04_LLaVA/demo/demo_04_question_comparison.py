"""對同一張圖片提出多個問題，比較 LLaVA 回答與幻覺風險。"""

from __future__ import annotations

import argparse
from pathlib import Path

from demo_03_llava_visual_qa import MODEL_NAME, ask_question, load_runtime


DEFAULT_QUESTIONS = [
    "Describe the main scene and visible objects.",
    "What colors can be verified from the image?",
    "What details cannot be confirmed from this image?",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument("--questions", nargs="+", default=DEFAULT_QUESTIONS)
    parser.add_argument("--model-id", default=MODEL_NAME)
    parser.add_argument("--max-new-tokens", type=int, default=80)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1
    if args.max_new_tokens <= 0 or any(not question.strip() for question in args.questions):
        print("問題不可為空白，且 --max-new-tokens 必須為正整數。")
        return 1

    try:
        from PIL import Image

        torch_module, processor, model, device_label = load_runtime(args.model_id)
    except (ImportError, RuntimeError) as error:
        print(error)
        return 1

    image = Image.open(args.image).convert("RGB")
    print(f"裝置：{device_label}")
    print(f"圖片：{args.image}")
    print(f"問題數量：{len(args.questions)}")

    for index, question in enumerate(args.questions, start=1):
        answer, token_count, elapsed = ask_question(
            torch_module,
            processor,
            model,
            image,
            question,
            args.max_new_tokens,
        )
        print(f"\n[問題 {index}] {question}")
        print(f"回答：{answer}")
        print(f"生成 token：{token_count}；推論時間：{elapsed:.2f} 秒")

    print("\n請把每個回答拆成 Supported／Uncertain／Contradicted 主張。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
