"""對同一張圖片提出多個問題，比較 LLaVA 回答與幻覺風險。"""

from __future__ import annotations

import argparse
from pathlib import Path

from demo_03_llava_visual_qa import MODEL_NAME, ask_question, load_runtime


DEFAULT_QUESTIONS = [
    ("global description", "Describe the main scene and visible objects."),
    ("object question", "What objects are visible?"),
    ("attribute question", "What colors can be verified from the image?"),
    ("uncertainty question", "What details cannot be confirmed from this image?"),
    (
        "robot manipulation candidate",
        "Which visible objects could potentially be manipulated by a robot?",
    ),
    (
        "robot spatial relation",
        "Where is one visible object relative to another visible object?",
    ),
    (
        "robot metric boundary",
        "Can the exact 3D position of an object be known from this RGB image alone?",
    ),
    (
        "robot reachability boundary",
        "Is an object reachable by a robot? State what information is missing.",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument(
        "--questions",
        nargs="+",
        help="自訂問題；省略時執行一般與 robot-oriented 預設問題組。",
    )
    parser.add_argument("--model-id", default=MODEL_NAME)
    parser.add_argument("--max-new-tokens", type=int, default=80)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1
    question_items = (
        [("custom", question) for question in args.questions]
        if args.questions
        else DEFAULT_QUESTIONS
    )
    if args.max_new_tokens <= 0 or any(
        not question.strip() for _, question in question_items
    ):
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
    print(f"問題數量：{len(question_items)}")

    for index, (category, question) in enumerate(question_items, start=1):
        answer, token_count, elapsed = ask_question(
            torch_module,
            processor,
            model,
            image,
            question,
            args.max_new_tokens,
        )
        print(f"\n[問題 {index}] 類型：{category}")
        print(f"問題：{question}")
        print(f"回答：{answer}")
        print(f"生成 token：{token_count}；推論時間：{elapsed:.2f} 秒")
        print(
            "主張判讀欄：Supported / Uncertain / Contradicted / "
            "Requires Additional Sensor or Robot State"
        )

    print("\n不要只比較回答長度；請把回答拆成可驗證的獨立主張。")
    print("精確 3D、robot coordinate、reachability 與安全動作不能由單張 RGB 直接確認。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
