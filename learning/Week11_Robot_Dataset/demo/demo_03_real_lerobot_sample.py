"""Inspect official LeRobot metadata, then load one frame from one selected episode."""
from __future__ import annotations

import argparse
import importlib.metadata
import time
from pathlib import Path


def describe_value(value):
    """Return compact nested summaries without dumping large tensors."""
    if isinstance(value, dict):
        return {key: describe_value(item) for key, item in value.items()}
    if hasattr(value, "shape"):
        return {"shape": list(value.shape), "dtype": str(getattr(value, "dtype", None))}
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-id", default="lerobot/aloha_mobile_cabinet")
    parser.add_argument(
        "--dataset-revision",
        "--revision",
        dest="dataset_revision",
        default="main",
        help="Dataset branch, tag, or commit SHA. --revision is a compatibility alias.",
    )
    parser.add_argument("--episode", type=int, default=0)
    parser.add_argument("--index", type=int, default=0, help="Index inside the selected dataset subset.")
    parser.add_argument("--cache-dir", type=Path)
    args = parser.parse_args()

    from lerobot.datasets import LeRobotDataset, LeRobotDatasetMetadata

    common = {"repo_id": args.dataset_id, "revision": args.dataset_revision}
    if args.cache_dir:
        common["root"] = args.cache_dir / args.dataset_revision.replace("/", "_")

    metadata_started = time.perf_counter()
    metadata = LeRobotDatasetMetadata(**common)
    metadata_seconds = time.perf_counter() - metadata_started
    print(f"lerobot_version={importlib.metadata.version('lerobot')}")
    print("dataset_format=LeRobotDataset v3.x")
    print(f"dataset_id={args.dataset_id} dataset_revision={args.dataset_revision}")
    print(
        f"metadata: episodes={metadata.total_episodes} frames={metadata.total_frames} "
        f"fps={metadata.fps} robot_type={metadata.robot_type}"
    )
    print(f"camera_keys={metadata.camera_keys}")
    print(f"tasks={metadata.tasks}")
    print(f"feature_schema={describe_value(metadata.features)}")
    print(f"normalization_stats={describe_value(metadata.stats)}")
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

    field_groups = {
        "image": any(key.startswith("observation.images.") for key in sample),
        "state": "observation.state" in sample,
        "action": "action" in sample,
        "task_or_language": "task" in sample or "task_index" in sample,
        "timestamp_or_frame": "timestamp" in sample or "frame_index" in sample,
    }
    for group, present in field_groups.items():
        print(f"{group}: {'present' if present else 'field not present'}")
    print("schema_note=Feature schema describes stored fields; it is not automatically the model input schema.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
