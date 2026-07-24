"""驗證 VLM 語意輸出的 JSON 結構、型別與允許值。"""

from __future__ import annotations

import json


ALLOWED_STATUS = {"found", "not_found", "unknown"}
REQUIRED = {"status", "target", "evidence", "uncertainty"}


SAMPLES = [
    '{"status":"found","target":"door","evidence":["rectangular doorway"],"uncertainty":"low"}',
    '{"status":"found","target":"door"}',
    'The door is on the left.',
    '{"status":"certain","target":"door","evidence":[],"uncertainty":"none"}',
]


def validate(text: str) -> list[str]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        return [f"invalid JSON: {error.msg}"]
    if not isinstance(data, dict):
        return ["top-level value must be an object"]
    errors = [f"missing field: {key}" for key in sorted(REQUIRED - data.keys())]
    errors += [f"unexpected field: {key}" for key in sorted(data.keys() - REQUIRED)]
    if data.get("status") not in ALLOWED_STATUS:
        errors.append("status must be found, not_found, or unknown")
    if "evidence" in data and not isinstance(data["evidence"], list):
        errors.append("evidence must be an array")
    return errors


def main() -> None:
    for index, sample in enumerate(SAMPLES, start=1):
        errors = validate(sample)
        print(f"sample {index}: {'PASS' if not errors else 'FAIL'}")
        for error in errors:
            print(f"  - {error}")
    print("\nJSON 合法只代表結構通過，仍需檢查圖片證據與安全語意。")


if __name__ == "__main__":
    main()
