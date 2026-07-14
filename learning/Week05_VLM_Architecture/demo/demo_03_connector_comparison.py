"""比較 Projector 與 Query Connector 對 token 數量及維度的影響。"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vision-tokens", type=int, default=576)
    parser.add_argument("--query-tokens", type=int, default=32)
    parser.add_argument("--vision-hidden", type=int, default=1024)
    parser.add_argument("--language-hidden", type=int, default=4096)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if min(vars(args).values()) <= 0:
        print("所有參數必須為正整數。")
        return 1
    print("Input vision features:")
    print(f"  [1, {args.vision_tokens}, {args.vision_hidden}]")
    print("\nLinear / MLP Projector:")
    print(f"  [1, {args.vision_tokens}, {args.language_hidden}]")
    print("  token count usually preserved; hidden size changed")
    print("\nQuery-based Connector:")
    print(f"  [1, {args.query_tokens}, {args.language_hidden}]")
    print("  learned queries summarize visual features into fewer positions")
    ratio = args.vision_tokens / args.query_tokens
    print(f"\nIllustrative position reduction: {ratio:.1f}x")
    print("較少位置可降低序列成本，但壓縮也可能遺失細節。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
