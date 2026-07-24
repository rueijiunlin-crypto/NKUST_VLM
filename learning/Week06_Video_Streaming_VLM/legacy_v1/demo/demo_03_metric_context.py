"""展示同一數字在缺少 metric context 時為何無法比較。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Result:
    model: str
    score: float
    dataset: str
    split: str
    metric: str
    setting: str


RESULTS = [
    Result("Model-A", 85.0, "Dataset-X", "test", "accuracy", "zero-shot"),
    Result("Model-B", 87.0, "Dataset-X", "validation", "accuracy", "fine-tuned"),
    Result("Model-C", 85.0, "Dataset-Y", "test", "F1", "zero-shot"),
]


def comparable(left: Result, right: Result) -> list[str]:
    fields = ["dataset", "split", "metric", "setting"]
    return [field for field in fields if getattr(left, field) != getattr(right, field)]


def main() -> None:
    for result in RESULTS:
        print(result)
    print()
    for other in RESULTS[1:]:
        differences = comparable(RESULTS[0], other)
        print(f"{RESULTS[0].model} vs {other.model}: differing context = {differences}")
    print("\n分數大小不能脫離 dataset、split、metric 與 evaluation setting 解讀。")


if __name__ == "__main__":
    main()
