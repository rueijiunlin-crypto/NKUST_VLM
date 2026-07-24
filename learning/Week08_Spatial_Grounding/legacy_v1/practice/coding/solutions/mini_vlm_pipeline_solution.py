"""Implementation Practice solution：Caption／VQA pipeline 與結果 envelope。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


CAPTION_MODEL = "Salesforce/blip-image-captioning-base"
VQA_MODEL = "Salesforce/blip-vqa-base"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=["caption", "vqa"], required=True)
    parser.add_argument("--image", type=Path, required=True)
    parser.add_argument("--question")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def validate_request(task: str, image: Path, question: str | None, dry_run: bool) -> None:
    if not dry_run and not image.is_file():
        raise ValueError(f"image does not exist: {image}")
    if task == "caption" and question is not None:
        raise ValueError("caption task must not include --question")
    if task == "vqa" and not (question and question.strip()):
        raise ValueError("vqa task requires a non-empty --question")


def run_model(task: str, image: Path, question: str | None) -> tuple[str, str]:
    try:
        import torch
        from PIL import Image
        from transformers import (
            BlipForConditionalGeneration,
            BlipForQuestionAnswering,
            BlipProcessor,
        )
    except ImportError as error:
        raise RuntimeError("install practice/coding/requirements.txt") from error

    device = "cuda" if torch.cuda.is_available() else "cpu"
    raw_image = Image.open(image).convert("RGB")
    model_id = CAPTION_MODEL if task == "caption" else VQA_MODEL
    processor = BlipProcessor.from_pretrained(model_id)
    if task == "caption":
        model = BlipForConditionalGeneration.from_pretrained(model_id).to(device)
        inputs = processor(images=raw_image, return_tensors="pt").to(device)
    else:
        model = BlipForQuestionAnswering.from_pretrained(model_id).to(device)
        inputs = processor(images=raw_image, text=question, return_tensors="pt").to(device)
    with torch.inference_mode():
        output_ids = model.generate(**inputs, max_new_tokens=40)
    return processor.decode(output_ids[0], skip_special_tokens=True), model_id


def build_result(
    task: str,
    image: Path,
    question: str | None,
    answer: str,
    model_id: str,
) -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task": task,
        "status": "ok" if answer.strip() else "unknown",
        "source_image": str(image),
        "question": question.strip() if question else None,
        "answer": answer.strip(),
        "model_id": model_id,
    }


def main() -> int:
    args = parse_args()
    try:
        validate_request(args.task, args.image, args.question, args.dry_run)
        if args.dry_run:
            answer, model_id = "dry-run answer", "dry-run"
        else:
            answer, model_id = run_model(args.task, args.image, args.question)
        result = build_result(args.task, args.image, args.question, answer, model_id)
    except (ValueError, RuntimeError) as error:
        print(f"error: {error}")
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
