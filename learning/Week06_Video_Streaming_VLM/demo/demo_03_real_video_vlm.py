"""Run Qwen2.5-VL on a local video with explicit FPS or frame-count sampling."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", default="Qwen/Qwen2.5-VL-3B-Instruct")
    parser.add_argument("--revision", default="main")
    parser.add_argument("--video", type=Path, required=True)
    sampling = parser.add_mutually_exclusive_group()
    sampling.add_argument("--fps", type=float, help="Sampling FPS, e.g. 1, 2, or 4.")
    sampling.add_argument("--frames", type=int, help="Exact target frame count, e.g. 2, 4, 8, or 16.")
    parser.add_argument("--question", default="Describe the events in temporal order.")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--dtype", choices=["auto", "float16", "bfloat16", "float32"], default="auto")
    parser.add_argument("--max-pixels", type=int, default=360 * 420)
    parser.add_argument("--max-new-tokens", type=int, default=128)
    return parser.parse_args()


def video_metadata(path: Path) -> tuple[float, float, int]:
    import cv2

    capture = cv2.VideoCapture(str(path))
    if not capture.isOpened():
        raise RuntimeError(f"Cannot open video: {path}")
    source_fps = float(capture.get(cv2.CAP_PROP_FPS))
    source_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    duration = source_frames / source_fps if source_fps > 0 else 0.0
    return duration, source_fps, source_frames


def main() -> int:
    args = parse_args()
    if not args.video.is_file():
        raise FileNotFoundError(args.video)
    if args.fps is not None and args.fps <= 0:
        raise ValueError("--fps must be positive")
    if args.frames is not None and args.frames < 2:
        raise ValueError("--frames must be at least 2; qwen-vl-utils rounds to an even frame factor")

    import torch
    from qwen_vl_utils import process_vision_info
    from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

    duration, source_fps, source_frames = video_metadata(args.video)
    dtype = "auto" if args.dtype == "auto" else getattr(torch, args.dtype)
    sampling_key = "nframes" if args.frames is not None else "fps"
    sampling_value = args.frames if args.frames is not None else (args.fps or 2.0)
    video_item = {
        "type": "video",
        "video": args.video.resolve().as_uri(),
        sampling_key: sampling_value,
        "max_pixels": args.max_pixels,
    }
    messages = [{"role": "user", "content": [video_item, {"type": "text", "text": args.question}]}]

    load_started = time.perf_counter()
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        args.model_id,
        revision=args.revision,
        torch_dtype=dtype,
        device_map=args.device,
    ).eval()
    processor = AutoProcessor.from_pretrained(args.model_id, revision=args.revision)
    load_seconds = time.perf_counter() - load_started

    prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    images, videos, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
    sampled_shape = tuple(videos[0].shape)
    inputs = processor(
        text=[prompt],
        images=images,
        videos=videos,
        padding=True,
        return_tensors="pt",
        **video_kwargs,
    ).to(model.device)

    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    started = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(**inputs, max_new_tokens=args.max_new_tokens, do_sample=False)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    inference_seconds = time.perf_counter() - started
    generated = output[:, inputs.input_ids.shape[1] :]
    answer = processor.batch_decode(
        generated, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]

    print(f"model_id={args.model_id}")
    print(f"revision={args.revision} device={model.device} dtype={next(model.parameters()).dtype}")
    print(f"video={args.video} duration_seconds={duration:.3f} source_fps={source_fps:.3f}")
    print(f"source_frames={source_frames} sampling={sampling_key}:{sampling_value}")
    print(f"sampled_frames={sampled_shape[0]} sampled_video_shape={sampled_shape}")
    print(f"processor_input_shapes={{{', '.join(f'{k!r}: {tuple(v.shape)!r}' for k, v in inputs.items() if hasattr(v, 'shape'))}}}")
    print(f"load_seconds={load_seconds:.3f} inference_seconds={inference_seconds:.3f}")
    print(f"generated_tokens={generated.shape[1]}")
    if torch.cuda.is_available():
        print(f"peak_vram_mb={torch.cuda.max_memory_allocated() / 1024**2:.1f}")
    print(f"answer={answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
