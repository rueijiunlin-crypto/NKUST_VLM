"""Inspect official LeRobot metadata, then load one frame from one selected episode."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-id", default="lerobot/aloha_mobile_cabinet")
    parser.add_argument("--revision", default="main")
    parser.add_argument("--episode", type=int, default=0)
    parser.add_argument("--index", type=int, default=0, help="Index inside the selected dataset subset.")
    parser.add_argument("--cache-dir", type=Path)
    args = parser.parse_args()

    from lerobot.datasets import LeRobotDataset, LeRobotDatasetMetadata

    common = {"repo_id": args.dataset_id, "revision": args.revision}
    if args.cache_dir:
        common["root"] = args.cache_dir / args.revision.replace("/", "_")

    metadata_started = time.perf_counter()
    metadata = LeRobotDatasetMetadata(**common)
    metadata_seconds = time.perf_counter() - metadata_started
    print(f"dataset_id={args.dataset_id} revision={args.revision}")
    print(
        f"metadata: episodes={metadata.total_episodes} frames={metadata.total_frames} "
        f"fps={metadata.fps} robot_type={metadata.robot_type}"
    )
    print(f"camera_keys={metadata.camera_keys}")
    print(f"tasks={metadata.tasks}")
    print(f"features={metadata.features}")
    print(f"metadata_load_seconds={metadata_seconds:.3f}")

    load_started = time.perf_counter()
    dataset = LeRobotDataset(episodes=[args.episode], **common)
    sample = dataset[args.index]
    print(
        f"selected_episodes={dataset.episodes} num_episodes={dataset.num_episodes} "
        f"num_frames={dataset.num_frames} load_seconds={time.perf_counter()-load_started:.3f}"
    )
    for key, value in sorted(sample.items()):
        shape = tuple(value.shape) if hasattr(value, "shape") else None
        scalar = value.item() if hasattr(value, "numel") and value.numel() == 1 else None
        print(
            f"{key}: type={type(value).__name__} shape={shape} "
            f"dtype={getattr(value, 'dtype', None)} scalar={scalar}"
        )

    required_groups = {
        "image": any(key.startswith("observation.images.") for key in sample),
        "state": "observation.state" in sample,
        "action": "action" in sample,
        "task_or_language": "task" in sample or "task_index" in sample,
        "timestamp_or_frame": "timestamp" in sample or "frame_index" in sample,
    }
    print(f"required_groups={required_groups}")
    if not all(required_groups.values()):
        raise RuntimeError(f"Dataset sample is missing required groups: {required_groups}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
