"""展示如何把論文主張拆成所需證據，而不是只抄摘要。"""

from __future__ import annotations


ROWS = [
    ("method improves transfer", "comparison on multiple downstream datasets", "baseline fairness"),
    ("connector is efficient", "trainable parameters + compute + performance", "hardware and data scale"),
    ("model follows visual instructions", "qualitative cases + task benchmarks", "cherry-picking / judge bias"),
]


def main() -> None:
    print(f"{'Claim':32} {'Required evidence':48} Threat")
    print("-" * 115)
    for claim, evidence, threat in ROWS:
        print(f"{claim:32} {evidence:48} {threat}")
    print("\n主張必須對應方法、表格、圖或附錄中的可定位證據。")


if __name__ == "__main__":
    main()
