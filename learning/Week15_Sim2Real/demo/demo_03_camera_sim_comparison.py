"""Compare real/recorded camera images with simulator images using common metrics."""
import argparse
import json
import time
from pathlib import Path


def load_rgb(path):
    import cv2
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def stats(name, image):
    import numpy as np
    gray = image.mean(axis=2)
    return {
        "source": name,
        "shape": list(image.shape),
        "mean_rgb": image.mean(axis=(0, 1)).tolist(),
        "std_rgb": image.std(axis=(0, 1)).tolist(),
        "brightness_mean": float(gray.mean()),
        "brightness_std": float(gray.std()),
        "noise_proxy": float(np.diff(gray, axis=1).std()),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--real", required=True, help="Real camera frame or recorded image.")
    p.add_argument("--sim", required=True, help="Isaac Sim RGB frame.")
    p.add_argument("--output", default="camera_sim_metrics.json")
    args = p.parse_args()
    started = time.perf_counter()
    real, sim = load_rgb(args.real), load_rgb(args.sim)
    report = {"real": stats("real", real), "sim": stats("sim", sim)}
    report["absolute_mean_rgb_gap"] = [
        abs(a - b) for a, b in zip(report["real"]["mean_rgb"], report["sim"]["mean_rgb"])
    ]
    report["elapsed_seconds"] = time.perf_counter() - started
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
