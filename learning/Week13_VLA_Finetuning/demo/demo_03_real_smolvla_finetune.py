"""Build or execute a pinned, small SmolVLA fine-tuning command."""
import argparse
import json
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", default="lerobot/smolvla_base")
    p.add_argument("--dataset-id", required=True)
    p.add_argument("--output-dir", default="outputs/smolvla_small")
    p.add_argument("--steps", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--device", default="cuda")
    p.add_argument("--execute", action="store_true", help="Default is dry-run.")
    args = p.parse_args()
    cmd = [
        "lerobot-train",
        f"--policy.path={args.model_id}",
        f"--dataset.repo_id={args.dataset_id}",
        f"--output_dir={args.output_dir}",
        f"--steps={args.steps}",
        f"--batch_size={args.batch_size}",
        f"--policy.device={args.device}",
    ]
    print("command=" + " ".join(shlex.quote(x) for x in cmd))
    print(f"status={'executing' if args.execute else 'Not validated yet (dry-run)'}")
    if args.execute:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
        metadata = vars(args) | {"started_utc": datetime.now(timezone.utc).isoformat()}
        Path(args.output_dir, "run_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
