"""估算圖片數量、解析度與文字長度對多模態 token budget 的影響。"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images", type=int, default=1)
    parser.add_argument("--image-size", type=int, default=336)
    parser.add_argument("--patch-size", type=int, default=14)
    parser.add_argument("--text-tokens", type=int, default=128)
    parser.add_argument("--query-tokens", type=int)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if min(args.images, args.image_size, args.patch_size, args.text_tokens) <= 0:
        print("參數必須為正整數。")
        return 1
    if args.image_size % args.patch_size:
        print("--image-size 必須可被 --patch-size 整除。")
        return 1
    raw_per_image = (args.image_size // args.patch_size) ** 2
    connector_positions = args.query_tokens or raw_per_image
    visual = args.images * connector_positions
    total = visual + args.text_tokens
    print(f"raw patch positions / image : {raw_per_image}")
    print(f"connector positions / image : {connector_positions}")
    print(f"all visual positions         : {visual}")
    print(f"text positions               : {args.text_tokens}")
    print(f"estimated total positions    : {total}")
    print("\n此數值是架構比較用估算，不代表任何 checkpoint 的精確實作。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
