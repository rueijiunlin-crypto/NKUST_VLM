"""Run grounded visual question answering with the real LLaVA checkpoint."""
import argparse
import time
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--image", type=Path, required=True)
    p.add_argument("--question", default="What visible objects could a robot manipulate, and what remains uncertain?")
    p.add_argument("--model-id", default="llava-hf/llava-1.5-7b-hf")
    p.add_argument("--revision", default="main")
    p.add_argument("--device", choices=["auto", "cpu", "cuda"], default="auto")
    p.add_argument("--dtype", choices=["auto", "float16", "bfloat16", "float32"], default="auto")
    p.add_argument("--max-new-tokens", type=int, default=80)
    return p.parse_args()


def main():
    args = parse_args()
    if not args.image.is_file():
        raise FileNotFoundError(args.image)
    import torch
    from PIL import Image
    from transformers import AutoProcessor, LlavaForConditionalGeneration

    device_map = args.device
    if device_map == "auto":
        device_map = "auto" if torch.cuda.is_available() else "cpu"
    dtype = "auto" if args.dtype == "auto" else getattr(torch, args.dtype)
    load_started = time.perf_counter()
    print(f"model={args.model_id} revision={args.revision} device={device_map} requested_dtype={args.dtype}")
    processor = AutoProcessor.from_pretrained(args.model_id, revision=args.revision)
    model = LlavaForConditionalGeneration.from_pretrained(
        args.model_id, revision=args.revision, torch_dtype=dtype, device_map=device_map, low_cpu_mem_usage=True
    ).eval()
    load_seconds = time.perf_counter() - load_started
    prompt = f"USER: <image>\n{args.question.strip()} ASSISTANT:"
    inputs = processor(images=Image.open(args.image).convert("RGB"), text=prompt, return_tensors="pt")
    model_device = next(model.parameters()).device
    inputs = {name: tensor.to(model_device) for name, tensor in inputs.items()}
    print({name: tuple(tensor.shape) for name, tensor in inputs.items()})
    print(
        f"resolved_device={model_device} resolved_dtype={next(model.parameters()).dtype} "
        f"gpu={torch.cuda.get_device_name() if torch.cuda.is_available() else 'none'}"
    )
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    started = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(**inputs, max_new_tokens=args.max_new_tokens, do_sample=False)
    elapsed = time.perf_counter() - started
    generated = output[:, inputs["input_ids"].shape[1]:]
    print(processor.batch_decode(generated, skip_special_tokens=True)[0].strip())
    print(
        f"load_seconds={load_seconds:.3f} inference_seconds={elapsed:.3f} "
        f"input_tokens={inputs['input_ids'].shape[1]} output_tokens={generated.shape[1]}"
    )
    if torch.cuda.is_available():
        print(f"peak_memory_mb={torch.cuda.max_memory_allocated()/1024**2:.1f}")
    print("boundary=semantic-output-only; additional geometry, state, validation and safety are required")


if __name__ == "__main__":
    main()
