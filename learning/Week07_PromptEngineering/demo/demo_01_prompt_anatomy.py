"""展示適合 VLM 機器人語境的 Prompt 組成。"""

from __future__ import annotations


PARTS = [
    ("role", "You analyze one camera frame for indoor semantic navigation."),
    ("task", "Identify the requested landmark if visibly supported."),
    ("evidence boundary", "Use only visible image evidence; do not infer hidden objects."),
    ("output contract", "Return JSON with status, target, evidence, and uncertainty."),
    ("unknown policy", "If evidence is insufficient, set status to unknown."),
    ("safety boundary", "Do not issue motor commands or claim a path is safe."),
]


def main() -> None:
    for index, (name, text) in enumerate(PARTS, start=1):
        print(f"[{index}] {name}")
        print(f"    {text}")
    print("\nPrompt 是可測試的輸入契約，不是越長越好。")


if __name__ == "__main__":
    main()
