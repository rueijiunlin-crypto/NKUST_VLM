"""Implementation Practice：完成 Caption／VQA 共用 pipeline 與結果 envelope。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=["caption", "vqa"], required=True)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--question")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def validate_request(task: str, image: Path, question: str | None, dry_run: bool) -> None:
    """TODO：檢查圖片、caption question 與 vqa question 規則。"""
    raise NotImplementedError


def run_model(task: str, image: Path, question: str | None) -> tuple[str, str]:
    """TODO：依 task 載入正確 BLIP model，回傳 answer 與 model_id。"""
    raise NotImplementedError


def build_result(
    task: str,
    image: Path,
    question: str | None,
    answer: str,
    model_id: str,
) -> dict[str, object]:
    """TODO：建立 schema_version=1.0 的完整結果 envelope。"""
    raise NotImplementedError


def main() -> int:
    args = parse_args()
    validate_request(args.task, args.image, args.question, args.dry_run)
    if args.dry_run:
        answer, model_id = "dry-run answer", "dry-run"
    else:
        answer, model_id = run_model(args.task, args.image, args.question)
    result = build_result(args.task, args.image, args.question, answer, model_id)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
