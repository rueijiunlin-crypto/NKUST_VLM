"""Reload a SmolVLA checkpoint, restore processors, and verify offline inference."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--dataset-revision", default="main")
    parser.add_argument("--episode", type=int, default=0)
    parser.add_argument("--index", type=int, default=0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float32", "float16", "bfloat16"], default="bfloat16")
    args = parser.parse_args()

    if not args.checkpoint.is_dir():
        raise FileNotFoundError(args.checkpoint)
    config_candidates = [args.checkpoint / "config.json", args.checkpoint / "policy_config.json"]
    if not any(path.is_file() for path in config_candidates):
        raise RuntimeError(f"No model config found in {args.checkpoint}")

    import torch
    from lerobot.datasets import LeRobotDataset
    from lerobot.policies.factory import make_pre_post_processors
    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

    if args.device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable; record Hardware blocked or choose --device cpu")

    dataset = LeRobotDataset(
        args.dataset_id, revision=args.dataset_revision, episodes=[args.episode]
    )
    # The official preprocessor adds the batch dimension to an unbatched Dataset v3 sample.
    observation = dataset[args.index]
    observation = {
        key: value
        for key, value in observation.items()
        if key.startswith("observation.") or key in {"task", "task_index", "robot_type"}
    }
    policy = SmolVLAPolicy.from_pretrained(str(args.checkpoint)).to(
        device=args.device, dtype=getattr(torch, args.dtype)
    ).eval()
    policy.config.device = args.device
    preprocessor, postprocessor = make_pre_post_processors(
        policy_cfg=policy.config,
        pretrained_path=str(args.checkpoint),
        dataset_stats=dataset.meta.stats,
        preprocessor_overrides={"device_processor": {"device": args.device}},
    )
    processed = preprocessor(observation)
    policy.reset()
    started = time.perf_counter()
    with torch.inference_mode():
        raw_action = policy.select_action(processed)
        action = postprocessor(raw_action)
    if args.device.startswith("cuda"):
        torch.cuda.synchronize()
    action_tensor = action if isinstance(action, torch.Tensor) else action.get("action")
    if not isinstance(action_tensor, torch.Tensor):
        raise TypeError(f"Unsupported postprocessed action: {type(action).__name__}")
    report = {
        "checkpoint": str(args.checkpoint.resolve()),
        "config_exists": True,
        "training_metadata_exists": (args.checkpoint.parents[2] / "run_metadata.json").is_file()
        if len(args.checkpoint.parents) > 2
        else False,
        "model_reload_succeeds": True,
        "observation_keys": sorted(observation),
        "raw_action_shape": list(raw_action.shape),
        "action_shape": list(action_tensor.shape),
        "finite": bool(torch.isfinite(action_tensor).all()),
        "inference_seconds": time.perf_counter() - started,
        "boundary": "log-only; no controller",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["finite"]:
        raise RuntimeError("Reloaded checkpoint produced non-finite action")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
