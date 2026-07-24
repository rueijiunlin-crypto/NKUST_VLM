"""快速比較四種常見 Vision-Language Model 架構家族。"""

from __future__ import annotations

import argparse


ARCHITECTURES = [
    ("Dual Encoder", "Image Encoder + Text Encoder", "representation / score", "CLIP"),
    ("Projector-based", "Vision Encoder + Projector + LLM", "generative text", "LLaVA"),
    ("Query-based", "Vision Encoder + Query Connector + LLM", "generative text", "BLIP-2"),
    ("Cross-Attention", "Vision Encoder + Cross-Attention + LM", "generative text", "Flamingo"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-action-context",
        action="store_true",
        help="顯示未來 VLA action output 的介面比較。",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"{'Family':18} {'Core components':42} {'Output':16} Example")
    print("-" * 95)
    for family, components, output, example in ARCHITECTURES:
        print(f"{family:18} {components:42} {output:16} {example}")
    print("\n觀察：不是所有 VLM 都把圖片 token 直接串到 LLM 前面。")
    print("架構選擇會改變輸出型態、訓練方式、序列成本與可用任務。")
    print("representation output 是向量／分數；generative output 是文字 token。")
    if args.include_action_context:
        print(
            "未來 VLA 的 action output 需對應動作表示與機器人狀態；"
            "不能把生成文字直接視為可執行馬達命令。"
        )


if __name__ == "__main__":
    main()
