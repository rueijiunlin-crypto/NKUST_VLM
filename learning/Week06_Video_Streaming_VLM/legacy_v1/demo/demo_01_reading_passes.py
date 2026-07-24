"""展示 VLM 論文的三階段閱讀順序與每階段產物。"""

from __future__ import annotations


PASSES = [
    ("Pass 1: Orientation", "title, abstract, figures, conclusion", "one-sentence problem and claim"),
    ("Pass 2: Evidence", "method, data, experiments, ablations", "claim-to-evidence table"),
    ("Pass 3: Reproduction", "appendix, implementation, limitations", "reproduction and risk checklist"),
]


def main() -> None:
    for name, read, output in PASSES:
        print(name)
        print(f"  read   : {read}")
        print(f"  produce: {output}")
    print("\n閱讀順序不是固定頁碼；目標是逐步建立可驗證的理解。")


if __name__ == "__main__":
    main()
