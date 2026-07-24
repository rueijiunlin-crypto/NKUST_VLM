"""Guided Code Reading：觀察 camera、robot state 與 command 的時間對齊。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class TimedSample:
    source: str
    timestamp_s: float
    payload: str


def age_ms(reference_s: float, sample: TimedSample) -> float:
    return (reference_s - sample.timestamp_s) * 1000.0


def main() -> None:
    decision_time_s = 10.120
    samples = [
        TimedSample("camera", 10.080, "frame_1042"),
        TimedSample("joint_state", 10.115, "q=[0.1, -0.3, 0.7]"),
        TimedSample("last_command", 10.060, "move_left"),
    ]
    freshness_budget_ms = {"camera": 80.0, "joint_state": 30.0, "last_command": 100.0}

    print(f"decision timestamp: {decision_time_s:.3f}s")
    for sample in samples:
        sample_age = age_ms(decision_time_s, sample)
        is_fresh = sample_age <= freshness_budget_ms[sample.source]
        print(
            f"{sample.source:12s} age={sample_age:5.1f}ms "
            f"budget={freshness_budget_ms[sample.source]:5.1f}ms fresh={is_fresh}"
        )
    print("Observation is valid only when required fields, frame IDs, units, and timestamps are explicit.")


if __name__ == "__main__":
    main()
