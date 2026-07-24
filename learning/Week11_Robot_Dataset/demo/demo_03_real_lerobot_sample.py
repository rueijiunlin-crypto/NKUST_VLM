"""Read one item from an official LeRobot dataset; no full-dataset preload."""
import argparse
import time


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset-id", default="lerobot/aloha_sim_insertion_human")
    p.add_argument("--revision")
    p.add_argument("--episode", type=int, default=0)
    p.add_argument("--index", type=int, default=0)
    p.add_argument("--cache-dir")
    args = p.parse_args()
    from lerobot.datasets.lerobot_dataset import LeRobotDataset

    started = time.perf_counter()
    kwargs = {"repo_id": args.dataset_id, "episodes": [args.episode]}
    if args.revision:
        kwargs["revision"] = args.revision
    if args.cache_dir:
        kwargs["root"] = args.cache_dir
    dataset = LeRobotDataset(**kwargs)
    sample = dataset[args.index]
    print(f"dataset={args.dataset_id} revision={args.revision or 'default'} episode={args.episode}")
    print(f"length={len(dataset)} fps={getattr(dataset, 'fps', 'unknown')} load_seconds={time.perf_counter()-started:.3f}")
    for key, value in sorted(sample.items()):
        shape = tuple(value.shape) if hasattr(value, "shape") else None
        print(f"{key}: type={type(value).__name__} shape={shape} dtype={getattr(value, 'dtype', None)}")


if __name__ == "__main__":
    main()
