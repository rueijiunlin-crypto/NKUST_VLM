"""Qwen2.5-VL real-video inference. Downloads only when explicitly executed."""
import argparse
import time


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", default="Qwen/Qwen2.5-VL-3B-Instruct")
    p.add_argument("--revision", default="main")
    p.add_argument("--video", required=True)
    p.add_argument("--question", default="Describe the temporally ordered events.")
    p.add_argument("--device", default="auto")
    p.add_argument("--dtype", choices=["auto", "float16", "bfloat16", "float32"], default="auto")
    p.add_argument("--max-new-tokens", type=int, default=128)
    return p.parse_args()


def main():
    args = parse_args()
    import torch
    from qwen_vl_utils import process_vision_info
    from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

    dtype = "auto" if args.dtype == "auto" else getattr(torch, args.dtype)
    print(f"model={args.model_id} revision={args.revision} device={args.device} dtype={args.dtype}")
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        args.model_id, revision=args.revision, torch_dtype=dtype, device_map=args.device
    )
    processor = AutoProcessor.from_pretrained(args.model_id, revision=args.revision)
    messages = [{"role": "user", "content": [
        {"type": "video", "video": args.video},
        {"type": "text", "text": args.question},
    ]}]
    prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    images, videos = process_vision_info(messages)
    inputs = processor(text=[prompt], images=images, videos=videos, padding=True, return_tensors="pt")
    inputs = inputs.to(model.device)
    print({k: tuple(v.shape) for k, v in inputs.items() if hasattr(v, "shape")})
    started = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(**inputs, max_new_tokens=args.max_new_tokens)
    elapsed = time.perf_counter() - started
    generated = output[:, inputs.input_ids.shape[1]:]
    print(processor.batch_decode(generated, skip_special_tokens=True)[0])
    print(f"inference_seconds={elapsed:.3f}")
    if torch.cuda.is_available():
        print(f"peak_memory_mb={torch.cuda.max_memory_allocated()/1024**2:.1f}")


if __name__ == "__main__":
    main()
