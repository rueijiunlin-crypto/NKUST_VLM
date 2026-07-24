"""Dry-run or execute an official lerobot-train SmolVLA smoke test."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import shlex
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", default="lerobot/smolvla_base")
    parser.add_argument("--model-revision", default="main")
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--dataset-revision", default="main")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/smolvla_small"))
    parser.add_argument("--steps", type=int, choices=[20, 50, 100], default=20)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--seed", type=int, default=1000)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--execute", action="store_true", help="Default is a non-mutating dry-run.")
    return parser.parse_args()


def build_command(args: argparse.Namespace, policy_path: str) -> list[str]:
    return [
        "lerobot-train",
        f"--policy.path={policy_path}",
        f"--dataset.repo_id={args.dataset_id}",
        f"--dataset.revision={args.dataset_revision}",
        f"--output_dir={args.output_dir}",
        f"--job_name=smolvla_smoke_{args.steps}",
        f"--steps={args.steps}",
        f"--batch_size={args.batch_size}",
        f"--optimizer.lr={args.learning_rate}",
        f"--seed={args.seed}",
        f"--save_freq={args.steps}",
        "--save_checkpoint=true",
        f"--policy.device={args.device}",
        "--wandb.enable=false",
    ]


def main() -> int:
    args = parse_args()
    policy_path = args.model_id
    if args.execute:
        from huggingface_hub import snapshot_download

        policy_path = snapshot_download(repo_id=args.model_id, revision=args.model_revision)
    command = build_command(args, policy_path)
    print(f"model_id={args.model_id} model_revision={args.model_revision}")
    print(f"dataset_id={args.dataset_id} dataset_revision={args.dataset_revision}")
    print("command=" + " ".join(shlex.quote(item) for item in command))
    print(f"status={'executing' if args.execute else 'Not validated yet (dry-run)'}")
    if not args.execute:
        return 0

    args.output_dir.mkdir(parents=True, exist_ok=True)
    metadata = {
        **{key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        "resolved_policy_path": policy_path,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "lerobot_version": importlib.metadata.version("lerobot"),
        "torch_version": importlib.metadata.version("torch"),
        "command": command,
    }
    (args.output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    started = time.perf_counter()
    completed = subprocess.run(command, check=False)
    elapsed = time.perf_counter() - started
    metadata.update({"returncode": completed.returncode, "training_seconds": elapsed})
    (args.output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if completed.returncode:
        raise subprocess.CalledProcessError(completed.returncode, command)
    checkpoints = sorted(args.output_dir.glob("checkpoints/*/pretrained_model"))
    print(f"training_seconds={elapsed:.3f}")
    print(f"checkpoint_candidates={[str(path) for path in checkpoints]}")
    if not checkpoints:
        raise RuntimeError("Training returned success but no pretrained_model checkpoint was found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
