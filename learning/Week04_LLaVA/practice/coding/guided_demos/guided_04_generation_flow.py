"""Trace deterministic toy autoregressive generation one token at a time."""

from __future__ import annotations

import argparse


VOCABULARY = ["a", "red", "door", "is", "visible", "<eos>"]
TARGET_SEQUENCE = ["a", "red", "door", "is", "visible", "<eos>"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-new-tokens", type=int, default=10)
    return parser.parse_args()


def toy_logits(step: int) -> dict[str, float]:
    """Return hand-authored scores to isolate the decoding mechanism."""
    preferred = TARGET_SEQUENCE[min(step, len(TARGET_SEQUENCE) - 1)]
    return {
        token: (5.0 if token == preferred else -float(index + 1))
        for index, token in enumerate(VOCABULARY)
    }


def main() -> None:
    args = parse_args()
    if args.max_new_tokens <= 0:
        raise ValueError("--max-new-tokens must be positive")

    generated: list[str] = []
    stop_reason = "max_new_tokens"
    for step in range(args.max_new_tokens):
        # Step 1: the model would compute next-token logits from all context.
        logits = toy_logits(step)
        # Step 2: greedy decoding selects the token with the largest score.
        next_token = max(logits, key=logits.get)
        top_scores = sorted(logits.items(), key=lambda item: item[1], reverse=True)[:3]
        print(f"step={step} top_scores={top_scores} selected={next_token}")
        # Step 3: append the selected token so it becomes future context.
        if next_token == "<eos>":
            stop_reason = "eos_token"
            break
        generated.append(next_token)

    print()
    print(f"generated text: {' '.join(generated)}")
    print(f"stop reason: {stop_reason}")
    print("Warning: these logits are hand-authored and never inspect an image.")
    print("Fluent output alone is not evidence of visual grounding.")


if __name__ == "__main__":
    main()
