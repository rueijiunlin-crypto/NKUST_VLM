"""Offline SmolVLA inference on one LeRobot observation; never sends robot commands."""
import argparse
import time


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", default="lerobot/smolvla_base")
    p.add_argument("--revision", default="main")
    p.add_argument("--dataset-id", default="lerobot/aloha_sim_insertion_human")
    p.add_argument("--episode", type=int, default=0)
    p.add_argument("--index", type=int, default=0)
    p.add_argument("--device", default="cuda")
    p.add_argument("--dtype", choices=["float32", "float16", "bfloat16"], default="bfloat16")
    args = p.parse_args()
    import torch
    from lerobot.datasets.lerobot_dataset import LeRobotDataset
    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

    dataset = LeRobotDataset(args.dataset_id, episodes=[args.episode])
    observation = dataset[args.index]
    dtype = getattr(torch, args.dtype)
    print(f"model={args.model_id} revision={args.revision} device={args.device} dtype={args.dtype}")
    policy = SmolVLAPolicy.from_pretrained(args.model_id, revision=args.revision)
    policy = policy.to(device=args.device, dtype=dtype).eval()
    batch = {}
    for key, value in observation.items():
        if isinstance(value, torch.Tensor) and not key.startswith("action"):
            batch[key] = value.unsqueeze(0).to(args.device)
    print({k: tuple(v.shape) for k, v in batch.items()})
    started = time.perf_counter()
    with torch.inference_mode():
        action = policy.select_action(batch)
    if args.device.startswith("cuda"):
        torch.cuda.synchronize()
    print(f"action_shape={tuple(action.shape)} finite={bool(torch.isfinite(action).all())}")
    print(f"inference_seconds={time.perf_counter()-started:.3f}")
    if torch.cuda.is_available():
        print(f"peak_memory_mb={torch.cuda.max_memory_allocated()/1024**2:.1f}")
    print("output_mode=log-only; no controller is connected")


if __name__ == "__main__":
    main()
