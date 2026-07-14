"""引導式程式閱讀：逐層驗證 JSON、欄位、型別與跨欄位規則。"""

from __future__ import annotations

import json


SAMPLE = '{"status":"found","target":"door","evidence":[],"uncertainty":"low"}'


def main() -> None:
    print("[步驟 1] JSON syntax")
    data = json.loads(SAMPLE)
    print("parsed:", data)

    print("\n[步驟 2] Required fields")
    required = {"status", "target", "evidence", "uncertainty"}
    missing = required - data.keys()
    print("missing:", sorted(missing))

    print("\n[步驟 3] Field types and enums")
    print("status allowed:", data["status"] in {"found", "not_found", "unknown"})
    print("evidence is list:", isinstance(data["evidence"], list))

    print("\n[步驟 4] Cross-field semantic rule")
    semantic_ok = not (data["status"] == "found" and not data["evidence"])
    print("found requires evidence:", semantic_ok)
    print("\nJSON 語法與欄位皆可正確，但跨欄位語意仍可能失敗。")


if __name__ == "__main__":
    main()
