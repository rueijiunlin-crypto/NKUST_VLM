"""驗證 Week08 結果 envelope 的欄位、型別與跨欄位規則。"""

from __future__ import annotations

import json


REQUIRED = {
    "schema_version", "observation_id", "timestamp_utc", "task", "status",
    "source_image", "question", "answer", "model_id",
}


def validate(result: dict[str, object]) -> list[str]:
    errors = [f"missing: {key}" for key in sorted(REQUIRED - result.keys())]
    if result.get("task") not in {"caption", "vqa"}:
        errors.append("task must be caption or vqa")
    if result.get("status") not in {"ok", "unknown", "error"}:
        errors.append("invalid status")
    if result.get("task") == "caption" and result.get("question") is not None:
        errors.append("caption question must be null")
    if result.get("task") == "vqa" and not result.get("question"):
        errors.append("vqa requires a question")
    if result.get("status") == "ok" and not str(result.get("answer", "")).strip():
        errors.append("ok result requires an answer")
    return errors


def main() -> None:
    samples = [
        {"schema_version":"1.0","observation_id":"1","timestamp_utc":"2026-01-01T00:00:00+00:00","task":"caption","status":"ok","source_image":"a.jpg","question":None,"answer":"a room","model_id":"demo"},
        {"schema_version":"1.0","observation_id":"2","timestamp_utc":"2026-01-01T00:00:00+00:00","task":"vqa","status":"ok","source_image":"a.jpg","question":None,"answer":"door","model_id":"demo"},
    ]
    for index, sample in enumerate(samples, start=1):
        errors = validate(sample)
        print(json.dumps(sample, ensure_ascii=False))
        print(f"sample {index}: {'PASS' if not errors else 'FAIL'} {errors}")


if __name__ == "__main__":
    main()
