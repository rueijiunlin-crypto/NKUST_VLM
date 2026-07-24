"""展示結構失敗、未知狀態與語意風險的 retry／reject 決策。"""

from __future__ import annotations


CASES = [
    ("invalid_json", False, False, False),
    ("valid_but_unknown", True, False, True),
    ("valid_without_grounding", True, False, False),
    ("valid_and_grounded", True, True, False),
]


def decide(schema_ok: bool, grounded: bool, unknown: bool, attempt: int = 1) -> str:
    if not schema_ok:
        return "retry_format" if attempt < 2 else "reject"
    if unknown:
        return "request_new_observation"
    if not grounded:
        return "reject_unsupported_claim"
    return "accept_semantic_result"


def main() -> None:
    for name, schema_ok, grounded, unknown in CASES:
        print(f"{name:26} -> {decide(schema_ok, grounded, unknown)}")
    print("\n重試應針對可修正失敗；不能要求模型把未知硬改成 found。")


if __name__ == "__main__":
    main()
