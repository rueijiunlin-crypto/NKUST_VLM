"""展示 Camera-to-Structured-Perception 的可驗證資料流。"""

from __future__ import annotations

import argparse
import json


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
        ("5. Language Model", f"about {total_positions} context positions"),
        ("6. Validator", "grounding / schema / uncertainty checks"),
        ("7. Structured Result", "accepted, retried, or rejected"),
    ]
    for name, output in stages:
        print(f"{name:24} -> {output}")
    result = {
        "detected_semantic_objects": ["cup", "box"],
        "relative_relations": [{"subject": "cup", "relation": "left_of", "object": "box"}],
        "uncertain": ["exact_depth", "robot_coordinate", "reachability"],
        "missing_information": ["depth", "camera_pose", "robot_state"],
    }
    print("\n示意 Structured Perception Result（不是模型偵測結果）：")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("\n觀察：合法 JSON 不代表內容正確，仍需 Grounding 與 schema 驗證。")
    print("本 Demo 不假裝由 RGB 取得真實深度、robot coordinate 或 reachability。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
