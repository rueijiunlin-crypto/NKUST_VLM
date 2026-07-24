"""比較模糊 Prompt 與具有輸出契約的 Prompt 版本。"""

from __future__ import annotations


PROMPTS = {
    "v1_vague": "Find the door and tell me where to go.",
    "v2_bounded": (
        "Analyze one image. Find a door only when supported by visible image evidence. "
        "Return status, target, evidence, uncertainty. "
        "Use unknown when evidence is insufficient. Do not output movement commands."
    ),
}


CHECKS = {
    "mentions evidence": ("visible", "evidence"),
    "defines unknown": ("unknown",),
    "defines output fields": ("status", "target", "uncertainty"),
    "blocks direct control": ("do not output movement",),
}


def score(prompt: str) -> tuple[int, list[str]]:
    lowered = prompt.lower()
    passed = [name for name, terms in CHECKS.items() if all(term in lowered for term in terms)]
    return len(passed), passed


def main() -> None:
    for version, prompt in PROMPTS.items():
        points, passed = score(prompt)
        print(f"[{version}] score={points}/{len(CHECKS)}")
        print(prompt)
        print("explicit checks:", passed)
        print()
    print("Prompt 靜態檢查不能取代模型實驗，但能先發現缺少的契約。")


if __name__ == "__main__":
    main()
