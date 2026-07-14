"""展示從 Camera frame 到文字回答的端到端 VLM 資料流。"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frames", type=int, default=1)
    parser.add_argument("--image-tokens", type=int, default=576)
    parser.add_argument("--text-tokens", type=int, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if min(args.frames, args.image_tokens, args.text_tokens) <= 0:
        print("所有參數必須為正整數。")
        return 1
    visual_positions = args.frames * args.image_tokens
    total_positions = visual_positions + args.text_tokens
    stages = [
        ("1. Camera", f"{args.frames} RGB frame(s)"),
        ("2. Preprocess", "resize / normalize / batch"),
        ("3. Vision Encoder", f"{visual_positions} visual positions"),
        ("4. Connector", "map / compress visual features"),
        ("5. Multimodal Context", f"about {total_positions} positions"),
        ("6. Language Model", "next-token generation"),
        ("7. Validator", "grounding / schema / safety checks"),
        ("8. Answer", "accepted, retried, or rejected"),
    ]
    for name, output in stages:
        print(f"{name:24} -> {output}")
    print("\n觀察：VLM 原始回答不是機器人可直接執行的控制命令。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
