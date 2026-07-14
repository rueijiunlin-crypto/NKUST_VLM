"""引導式程式閱讀：用相同欄位建立可維護的論文比較矩陣。"""

from __future__ import annotations


PAPERS = {
    "CLIP": {
        "input": "image-text pairs",
        "alignment": "contrastive objective",
        "output": "shared embeddings / similarity",
        "evaluation": "zero-shot transfer",
    },
    "LLaVA": {
        "input": "image-instruction-response data",
        "alignment": "projection + instruction tuning",
        "output": "generated text",
        "evaluation": "multimodal instruction following",
    },
}


def main() -> None:
    fields = ["input", "alignment", "output", "evaluation"]
    for field in fields:
        print(f"[{field}]")
        for paper, values in PAPERS.items():
            print(f"  {paper:6}: {values[field]}")
    print("\n比較欄位由研究問題決定；不要把缺失資訊自行補成論文事實。")


if __name__ == "__main__":
    main()
