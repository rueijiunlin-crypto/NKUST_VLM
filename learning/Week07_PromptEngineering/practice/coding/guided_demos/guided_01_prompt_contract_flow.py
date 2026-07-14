"""引導式程式閱讀：逐步組裝角色、任務、證據邊界與輸出契約。"""

from __future__ import annotations


def build_prompt(target: str) -> str:
    sections = [
        "ROLE: Analyze exactly one indoor camera frame.",
        f"TASK: Determine whether the target '{target}' is visibly present.",
        "EVIDENCE: Use only visible pixels; do not infer hidden objects.",
        "OUTPUT: JSON fields status, target, evidence, uncertainty.",
        "UNKNOWN: Use status=unknown when image evidence is insufficient.",
        "SAFETY: Do not output velocity, steering, or path-safety claims.",
    ]
    return "\n".join(sections)


def main() -> None:
    prompt = build_prompt("exit")
    for index, line in enumerate(prompt.splitlines(), start=1):
        name, value = line.split(":", 1)
        print(f"[{index}] {name:8} -> {value.strip()}")
    print("\n請逐段移除並判斷失去哪一項可測試契約。")


if __name__ == "__main__":
    main()
