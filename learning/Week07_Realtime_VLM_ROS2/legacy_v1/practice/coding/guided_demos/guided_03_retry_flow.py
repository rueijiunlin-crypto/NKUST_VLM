"""引導式程式閱讀：區分 format retry、new observation 與 reject。"""

from __future__ import annotations


FAILURES = [
    ("syntax", "invalid JSON", "retry with exact format reminder"),
    ("schema", "missing required field", "retry with missing-field feedback"),
    ("unknown", "image evidence insufficient", "request a new observation"),
    ("grounding", "claim not supported by image", "reject unsupported claim"),
    ("safety", "contains direct motor command", "reject and log safety violation"),
]


def main() -> None:
    for layer, failure, action in FAILURES:
        print(f"layer={layer:10} failure={failure:30} action={action}")
    print("\nRetry 次數必須有上限，且未知狀態不能靠文字重試變成已確認。")


if __name__ == "__main__":
    main()
