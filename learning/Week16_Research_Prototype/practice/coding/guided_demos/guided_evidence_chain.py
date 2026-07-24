"""Guided Code Reading：從研究問題追蹤到可驗證 evidence。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Experiment:
    research_question: str
    baseline: str
    method: str
    metric: str
    controlled_variables: tuple[str, ...]


def validate_evidence_chain(experiment: Experiment) -> list[str]:
    issues: list[str] = []
    if experiment.baseline == experiment.method:
        issues.append("baseline and method must be distinguishable")
    if not experiment.metric:
        issues.append("metric is required")
    if not experiment.controlled_variables:
        issues.append("controlled variables are required")
    return issues


def main() -> None:
    experiment = Experiment(
        research_question="Does freshness-aware frame dropping reduce unsafe stale actions?",
        baseline="FIFO processes every frame",
        method="latest-frame queue with freshness gate",
        metric="stale-action rate and task success rate",
        controlled_variables=("camera rate", "policy", "task cases", "hardware"),
    )
    print("Research question:", experiment.research_question)
    print("Comparison:", experiment.baseline, "vs.", experiment.method)
    print("Evidence:", experiment.metric)
    print("Controls:", ", ".join(experiment.controlled_variables))
    print("Validation issues:", validate_evidence_chain(experiment) or "none")


if __name__ == "__main__":
    main()
