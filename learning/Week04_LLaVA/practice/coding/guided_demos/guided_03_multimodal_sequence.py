"""Show how one image placeholder can expand to multiple sequence positions."""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image-tokens", type=int, default=4)
    parser.add_argument("--question", default="what is visible")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.image_tokens <= 0:
        raise ValueError("--image-tokens must be positive")
    question_tokens = args.question.strip().split()
    if not question_tokens:
        raise ValueError("--question must contain text")

    # Step 1: this is the human-readable prompt contract.
    prompt = f"USER: <image> {args.question.strip()} ASSISTANT:"

    # Step 2: represent special/text tokens in a compact educational tokenizer.
    prefix = ["[USER]"]
    image_positions = [f"[IMG_{index}]" for index in range(args.image_tokens)]
    suffix = [f"[TXT:{token}]" for token in question_tokens] + ["[ASSISTANT]"]

    # Step 3: the processor conceptually inserts many image embeddings.
    sequence = prefix + image_positions + suffix

    print(f"prompt: {prompt}")
    print(f"literal <image> count: {prompt.count('<image>')}")
    print(f"inserted image positions: {len(image_positions)}")
    print(f"text/special positions: {len(prefix) + len(suffix)}")
    print(f"total sequence length: {len(sequence)}")
    print()
    for position, token in enumerate(sequence):
        token_type = "IMAGE" if token.startswith("[IMG_") else "TEXT/SPECIAL"
        print(f"position={position:02d} type={token_type:12s} token={token}")
    print()
    print("Observation: one textual placeholder can map to many embedding positions.")
    print("Real token layouts depend on the checkpoint processor and model config.")


if __name__ == "__main__":
    main()
