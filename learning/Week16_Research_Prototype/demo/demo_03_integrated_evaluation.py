"""Evaluate recorded pipeline events without commanding a robot."""
import argparse
import json
import statistics
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--events", required=True, help="JSONL with valid, latency_ms, success, safety_rejected.")
    p.add_argument("--output", default="prototype_metrics.json")
    args = p.parse_args()
    rows = [json.loads(line) for line in Path(args.events).read_text(encoding="utf-8").splitlines() if line.strip()]
    if not rows:
        raise ValueError("No evaluation events.")
    latencies = sorted(float(r["latency_ms"]) for r in rows)
    percentile = lambda q: latencies[min(len(latencies) - 1, round(q * (len(latencies) - 1)))]
    report = {
        "samples": len(rows),
        "valid_rate": statistics.fmean(bool(r.get("valid")) for r in rows),
        "success_rate": statistics.fmean(bool(r.get("success")) for r in rows),
        "safety_rejection_rate": statistics.fmean(bool(r.get("safety_rejected")) for r in rows),
        "latency_ms": {"p50": percentile(.50), "p95": percentile(.95), "p99": percentile(.99)},
        "execution_boundary": "recorded-events-only; no controller",
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
