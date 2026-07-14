"""以固定欄位快速比較 CLIP 與 LLaVA 原始論文的研究設計。"""

from __future__ import annotations


ROWS = [
    ("Research problem", "transferable visual representations from text", "multimodal instruction following"),
    ("Core architecture", "image encoder + text encoder", "vision encoder + projection + LLM"),
    ("Core objective", "contrastive image-text alignment", "visual instruction tuning / generation"),
    ("Typical output", "similarity / zero-shot classifier", "open-ended generated answer"),
    ("Evidence focus", "transfer across many datasets", "multimodal chat and task evaluation"),
]


def main() -> None:
    for field, clip, llava in ROWS:
        print(f"[{field}]")
        print(f"  CLIP : {clip}")
        print(f"  LLaVA: {llava}")
    print("\n比較論文時使用相同欄位，避免只比較模型名稱或單一分數。")


if __name__ == "__main__":
    main()
