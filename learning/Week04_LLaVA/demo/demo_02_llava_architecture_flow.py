"""快速展示 LLaVA 的端到端架構與示意 shape，不載入大型模型。"""

from __future__ import annotations

import argparse


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image-size", type=positive_int, default=336)
    parser.add_argument("--patch-size", type=positive_int, default=14)
    parser.add_argument("--vision-hidden", type=positive_int, default=1024)
    parser.add_argument("--language-hidden", type=positive_int, default=4096)
    parser.add_argument("--text-tokens", type=positive_int, default=12)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.image_size % args.patch_size != 0:
        print("--image-size 必須可被 --patch-size 整除。")
        return 1

    grid = args.image_size // args.patch_size
    image_tokens = grid * grid
    total_tokens = image_tokens + args.text_tokens

    print("LLaVA architecture overview（示意 shape）")
    print(f"1. Image tensor       : [1, 3, {args.image_size}, {args.image_size}]")
    print(f"2. Patch grid         : {grid} x {grid} = {image_tokens} patches")
    print(f"3. Vision Encoder     : [1, {image_tokens}, {args.vision_hidden}]")
    print(f"4. Projector output   : [1, {image_tokens}, {args.language_hidden}]")
    print(f"5. Text embeddings    : [1, {args.text_tokens}, {args.language_hidden}]")
    print(f"6. Multimodal context : about [1, {total_tokens}, {args.language_hidden}]")
    print("7. LLM output         : autoregressively generated answer tokens")
    print("\n觀察：Projector 改變表示空間與最後一維，不直接生成句子。")
    print("注意：實際 token 數量由 checkpoint 與前處理設定決定。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
