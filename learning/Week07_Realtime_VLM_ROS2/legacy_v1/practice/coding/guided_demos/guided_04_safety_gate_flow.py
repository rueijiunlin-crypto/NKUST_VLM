"""引導式程式閱讀：追蹤 VLM 語意結果通過多層安全檢查。"""

from __future__ import annotations


CHECKS = [
    ("schema", True, "required fields and types"),
    ("grounding", True, "visible evidence supports target"),
    ("uncertainty", True, "uncertainty is within policy"),
    ("freshness", False, "camera timestamp is stale"),
    ("navigation", False, "not evaluated because freshness failed"),
]


def main() -> None:
    allowed = True
    for name, passed, detail in CHECKS:
        if not allowed:
            print(f"[SKIP] {name:12} {detail}")
            continue
        print(f"[{'PASS' if passed else 'FAIL'}] {name:12} {detail}")
        allowed = passed
    print(f"\nfinal semantic handoff allowed: {allowed}")
    print("失敗後停止下游檢查，可避免把過期影像轉成導航目標。")


if __name__ == "__main__":
    main()
