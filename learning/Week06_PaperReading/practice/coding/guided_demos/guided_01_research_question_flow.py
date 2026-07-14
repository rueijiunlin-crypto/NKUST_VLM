"""引導式程式閱讀：把寬泛主題逐步轉成可驗證研究問題。"""

from __future__ import annotations


STEPS = [
    ("Topic", "VLM for indoor navigation"),
    ("Problem", "semantic target descriptions may be ambiguous"),
    ("Gap", "unclear robustness under viewpoint and wording changes"),
    ("Question", "How does prompt wording affect target grounding accuracy?"),
    ("Variables", "prompt style; grounding accuracy; failure type"),
    ("Evidence", "controlled image-question pairs and error taxonomy"),
]


def main() -> None:
    for index, (label, value) in enumerate(STEPS, start=1):
        print(f"[{index}] {label:10}: {value}")
    print("\n研究主題不是研究問題；問題必須對應可觀察變數與證據。")


if __name__ == "__main__":
    main()
