"""引導式程式閱讀：以簡單規則檢查 claim record 是否可追溯。"""

from __future__ import annotations


REQUIRED = ["claim", "source_location", "evidence", "scope", "limitation"]
RECORDS = [
    {
        "claim": "Connector reduces trainable parameters.",
        "source_location": "Table 2",
        "evidence": "parameter counts under matched models",
        "scope": "reported configurations",
        "limitation": "does not establish lower inference latency",
    },
    {
        "claim": "The model is better.",
        "source_location": "",
        "evidence": "",
        "scope": "all tasks",
        "limitation": "",
    },
]


def validate(record: dict[str, str]) -> list[str]:
    errors = [field for field in REQUIRED if not record.get(field, "").strip()]
    if record.get("claim", "").lower().endswith("better."):
        errors.append("claim is underspecified: better on what metric and setting?")
    return errors


def main() -> None:
    for index, record in enumerate(RECORDS, start=1):
        errors = validate(record)
        print(f"record {index}: {'PASS' if not errors else 'FAIL'}")
        for error in errors:
            print(f"  - {error}")
    print("\n可追溯紀錄需包含來源位置、證據、適用範圍與限制。")


if __name__ == "__main__":
    main()
