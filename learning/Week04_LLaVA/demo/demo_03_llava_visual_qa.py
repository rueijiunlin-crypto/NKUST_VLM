"""使用 Hugging Face LLaVA 1.5 執行選做的單張圖片視覺問答。"""

from __future__ import annotations

import argparse
import time
from pathlib import Path
from typing import Any


MODEL_NAME = "llava-hf/llava-1.5-7b-hf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument(
        "--question",
        default="What is shown in this image?",
        help=(
            "影像問題。機器人導向範例：Which visible objects could potentially "
            "be manipulated by a robot, and what information is still missing?"
        ),
    )
    parser.add_argument("--model-id", default=MODEL_NAME)
    parser.add_argument("--max-new-tokens", type=int, default=80)
    return parser.parse_args()


def load_runtime(model_id: str) -> tuple[Any, Any, Any, str]:
    """載入套件、Processor 與模型，供 Demo 03／04 共用。"""
    try:
        import torch
        from transformers import AutoProcessor, LlavaForConditionalGeneration
    except ImportError as error:
        raise RuntimeError(
            "缺少套件，請安裝：python -m pip install -r demo/requirements.txt"
        ) from error

    if torch.cuda.is_available():
        dtype = torch.float16
        device_map = "auto"
        device_label = torch.cuda.get_device_name(0)
    else:
        dtype = torch.float32
        device_map = "cpu"
        device_label = "CPU（7B 模型會非常慢）"

    print(f"正在載入 Processor 與模型：{model_id}")
    processor = AutoProcessor.from_pretrained(model_id)
    model = LlavaForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
        device_map=device_map,
    )
    return torch, processor, model, device_label


def ask_question(
    torch_module: Any,
    processor: Any,
    model: Any,
    image: Any,
    question: str,
    max_new_tokens: int,
    show_shapes: bool = False,
) -> tuple[str, int, float]:
    """對已載入的同一模型提出一個問題，避免問題比較時重複載入。"""
    prompt = f"USER: <image>\n{question.strip()} ASSISTANT:"
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    input_device = next(model.parameters()).device
    inputs = {name: tensor.to(input_device) for name, tensor in inputs.items()}

    if show_shapes:
        print(f"Prompt：{prompt}")
        for name, tensor in inputs.items():
            print(f"- {name}: shape={tuple(tensor.shape)}, dtype={tensor.dtype}")

    started = time.perf_counter()
    with torch_module.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
    elapsed = time.perf_counter() - started

    prompt_length = inputs["input_ids"].shape[1]
    new_token_ids = output_ids[:, prompt_length:]
    answer = processor.batch_decode(new_token_ids, skip_special_tokens=True)[0].strip()
    return answer, new_token_ids.shape[1], elapsed


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1
    if not args.question.strip() or args.max_new_tokens <= 0:
        print("問題不可為空白，且 --max-new-tokens 必須為正整數。")
        return 1

    try:
        from PIL import Image

        torch_module, processor, model, device_label = load_runtime(args.model_id)
    except (ImportError, RuntimeError) as error:
        print(error)
        return 1

    image = Image.open(args.image).convert("RGB")
    print(f"裝置：{device_label}")
    print(f"圖片：{args.image}")
    answer, token_count, elapsed = ask_question(
        torch_module,
        processor,
        model,
        image,
        args.question,
        args.max_new_tokens,
        show_shapes=True,
    )
    print(f"生成 token 數量：{token_count}")
    print(f"推論時間：{elapsed:.2f} 秒")
    print(f"回答：{answer}")
    print("請逐項核對回答是否具有可見影像依據。")
    print(
        "若回答涉及精確深度、robot coordinate、reachability 或動作安全，"
        "請標為 Uncertain／Requires Additional Sensor or Robot State，"
        "不要只因語句流暢就視為 Supported。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
