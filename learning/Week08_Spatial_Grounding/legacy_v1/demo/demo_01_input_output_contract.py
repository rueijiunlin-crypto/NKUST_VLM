"""展示 Week08 Image Caption／Visual QA 共用的輸入輸出契約。"""

from __future__ import annotations

import json
from datetime import datetime, timezone


def main() -> None:
    request = {
        "task": "vqa",
        "image": "demo/example.jpg",
        "question": "What objects are visible?",
    }
    result = {
        "schema_version": "1.0",
        "observation_id": "week08-example-001",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task": request["task"],
        "status": "ok",
        "source_image": request["image"],
        "question": request["question"],
        "answer": "example answer; not produced by a model",
        "model_id": "dry-run",
    }
    print("Request:")
    print(json.dumps(request, ensure_ascii=False, indent=2))
    print("\nResult:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("\n觀察：caption 與 vqa 共用 envelope，但 question 規則不同。")


if __name__ == "__main__":
    main()
