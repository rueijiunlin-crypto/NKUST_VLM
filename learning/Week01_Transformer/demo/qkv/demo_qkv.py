"""
demo_qkv.py

用小型數字示範 Query（查詢）、Key（鍵）、Value（值）如何產生 Attention Score（注意力分數）。
本 Demo 不實作完整 Transformer（轉換器架構），重點是觀察 Q x K 的直覺。
"""


def dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def main() -> None:
    tokens = ["go", "to", "red", "door", "laboratory"]

    query = {"laboratory": [0.9, 0.1]}
    keys = {
        "go": [0.2, 0.8],
        "to": [0.3, 0.7],
        "red": [0.8, 0.2],
        "door": [0.95, 0.1],
        "laboratory": [1.0, 0.0],
    }
    values = {
        "go": "action",
        "to": "direction",
        "red": "attribute",
        "door": "landmark",
        "laboratory": "target",
    }

    print("Query token: laboratory")
    print("Q vector:", query["laboratory"])
    print()
    print("Q x K scores:")
    print("-" * 42)

    scores = {}
    for token in tokens:
        scores[token] = dot(query["laboratory"], keys[token])
        print(f"{token:12s} K={keys[token]} score={scores[token]:.3f} value={values[token]}")

    best = max(scores, key=scores.get)
    print()
    print("Highest score:", best)
    print("說明：Q 和 K 越相似，分數越高；分數會用來決定要加權取用多少 Value（值）。")


if __name__ == "__main__":
    main()
