"""引導式程式閱讀：檢查方法元件是否有對應實驗。"""

from __future__ import annotations


COMPONENTS = {
    "vision encoder": ["main benchmark", "encoder ablation"],
    "connector": ["connector ablation", "parameter / compute comparison"],
    "instruction data": ["data ablation", "instruction-following evaluation"],
}


def main() -> None:
    for component, expected in COMPONENTS.items():
        print(f"Method component: {component}")
        for experiment in expected:
            print(f"  expected evidence: {experiment}")
    print("\n若核心元件沒有對應 ablation 或控制比較，因果主張應降低信心。")


if __name__ == "__main__":
    main()
