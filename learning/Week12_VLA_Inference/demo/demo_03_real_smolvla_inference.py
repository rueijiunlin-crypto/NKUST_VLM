"""Offline SmolVLA inference with official LeRobot pre/post processors; log only."""
from __future__ import annotations

import argparse
import time


def tensor_shapes(mapping):
    return {
        key: {"shape": list(value.shape), "dtype": str(value.dtype), "device": str(value.device)}
        for key, value in mapping.items()
        if hasattr(value, "shape") and hasattr(value, "dtype")
    }


def extract_action_tensor(action, torch):
    if isinstance(action, torch.Tensor):
        return action
    if isinstance(action, dict):
        return action.get("action")
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", default="lerobot/smolvla_base")
    parser.add_argument("--revision", default="main")
    parser.add_argument("--dataset-id", default="lerobot/svla_so100_pickplace")
    parser.add_argument("--dataset-revision", default="main")
    parser.add_argument("--episode", type=int, default=0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float32", "float16", "bfloat16"], default="bfloat16")
    parser.add_argument("--cache-dir")
    args = parser.parse_args()

    import torch
    from huggingface_hub import snapshot_download
    from lerobot.datasets import LeRobotDataset
    from lerobot.policies import make_pre_post_processors
    from lerobot.policies.smolvla import SmolVLAPolicy

    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable; record Hardware blocked or choose --device cpu")
    dtype = getattr(torch, args.dtype)
    resolved_model = snapshot_download(
        repo_id=args.model_id,
        revision=args.revision,
        cache_dir=args.cache_dir,
    )
    dataset = LeRobotDataset(
        args.dataset_id,
        revision=args.dataset_revision,
        episodes=[args.episode],
    )
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)
    observation = next(iter(loader))
    observation = {
        key: value
        for key, value in observation.items()
        if key.startswith("observation.") or key in {"task", "task_index", "robot_type"}
    }

    load_started = time.perf_counter()
    policy = SmolVLAPolicy.from_pretrained(resolved_model).to(device=args.device, dtype=dtype).eval()
    preprocessor, postprocessor = make_pre_post_processors(
        policy_cfg=policy.config,
        pretrained_path=resolved_model,
        dataset_stats=dataset.meta.stats,
        preprocessor_overrides={"device_processor": {"device": args.device}},
    )
    load_seconds = time.perf_counter() - load_started
    parameter_count = sum(parameter.numel() for parameter in policy.parameters())
    trainable_count = sum(parameter.numel() for parameter in policy.parameters() if parameter.requires_grad)

    processed = preprocessor(observation)
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
    policy.reset()
    warm_started = time.perf_counter()
    with torch.inference_mode():
        warm_action = postprocessor(policy.select_action(processed))
    if args.device.startswith("cuda"):
        torch.cuda.synchronize()
    warm_seconds = time.perf_counter() - warm_started

    policy.reset()
    started = time.perf_counter()
    with torch.inference_mode():
        raw_action = policy.select_action(processed)
        action = postprocessor(raw_action)
    if args.device.startswith("cuda"):
        torch.cuda.synchronize()
    inference_seconds = time.perf_counter() - started

    action_tensor = extract_action_tensor(action, torch)
    warm_action_tensor = extract_action_tensor(warm_action, torch)
    if not isinstance(action_tensor, torch.Tensor):
        raise TypeError(f"Postprocessor returned unsupported action type: {type(action).__name__}")
    if not isinstance(warm_action_tensor, torch.Tensor):
        raise TypeError(f"Warm-up postprocessor returned unsupported action type: {type(warm_action).__name__}")
    finite = bool(torch.isfinite(action_tensor).all())
    print(f"model_id={args.model_id} revision={args.revision} resolved_model={resolved_model}")
    print(f"dataset_id={args.dataset_id} dataset_revision={args.dataset_revision} episode={args.episode}")
    print(f"observation_keys={sorted(observation)}")
    print(f"raw_input_shapes={tensor_shapes(observation)}")
    print(f"processed_input_shapes={tensor_shapes(processed)}")
    print(f"device={args.device} dtype={args.dtype}")
    print(f"parameter_count={parameter_count} trainable_count={trainable_count}")
    print(
        f"chunk_size={getattr(policy.config, 'chunk_size', None)} "
        f"n_action_steps={getattr(policy.config, 'n_action_steps', None)}"
    )
    print(f"raw_action_shape={tuple(raw_action.shape)} action_shape={tuple(action_tensor.shape)} finite={finite}")
    print(
        f"load_seconds={load_seconds:.3f} warmup_seconds={warm_seconds:.3f} "
        f"inference_seconds={inference_seconds:.3f}"
    )
    if torch.cuda.is_available():
        print(f"peak_vram_mb={torch.cuda.max_memory_allocated() / 1024**2:.1f}")
    print(f"warmup_action_shape={tuple(warm_action_tensor.shape)}")
    print("output_mode=log-only; no controller is connected")
    if not finite:
        raise RuntimeError("Non-finite action rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
