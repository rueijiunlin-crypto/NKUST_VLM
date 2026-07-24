"""Inspect a real SmolVLA config without loading weights."""
import argparse
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model-id", default="lerobot/smolvla_base")
    p.add_argument("--revision", default="main")
    p.add_argument("--cache-dir")
    args = p.parse_args()
    from huggingface_hub import hf_hub_download

    path = hf_hub_download(args.model_id, "config.json", revision=args.revision, cache_dir=args.cache_dir)
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"model={args.model_id} revision={args.revision} config={path}")
    for key in ("type", "n_obs_steps", "chunk_size", "n_action_steps", "input_features", "output_features"):
        print(f"{key}={config.get(key, 'not-declared')}")
    print("weights_loaded=false device=none dtype=none")


if __name__ == "__main__":
    main()
