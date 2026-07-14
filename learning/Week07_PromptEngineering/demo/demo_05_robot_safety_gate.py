"""展示語意輸出進入 ROS2／導航前的最小安全閘門。"""

from __future__ import annotations


OUTPUTS = [
    {"status": "found", "target": "exit", "evidence": ["exit sign"], "uncertainty": "low"},
    {"status": "found", "target": "exit", "evidence": [], "uncertainty": "high"},
    {"status": "unknown", "target": None, "evidence": [], "uncertainty": "high"},
]


def gate(result: dict[str, object]) -> tuple[bool, str]:
    if result.get("status") != "found":
        return False, "target not confirmed"
    if not result.get("evidence"):
        return False, "no visible evidence"
    if result.get("uncertainty") != "low":
        return False, "uncertainty is not low"
    return True, "semantic target may enter downstream verification"


def main() -> None:
    for index, result in enumerate(OUTPUTS, start=1):
        allowed, reason = gate(result)
        print(f"case {index}: allowed={allowed}; reason={reason}")
    print("\n通過此 gate 仍不代表路徑安全；導航與控制需要自己的驗證。")


if __name__ == "__main__":
    main()
