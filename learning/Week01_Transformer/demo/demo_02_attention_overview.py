"""快速展示不同 Query 會得到不同 Attention 重點。"""


def show_focus(query: str, weights: dict[str, float]) -> None:
    focus = max(weights, key=weights.get)
    print(f"{query:>10s} -> {weights} -> focus: {focus}")


def main() -> None:
    tokens = ["go", "to", "red", "door"]
    attention = {
        "go": {"go": 0.25, "to": 0.35, "red": 0.10, "door": 0.30},
        "door": {"go": 0.05, "to": 0.10, "red": 0.35, "door": 0.50},
    }

    print("Tokens:", tokens)
    for query, weights in attention.items():
        show_focus(query, weights)

    print("\n觀察：Self-Attention 讓同一句話中的 Token 依目前 Query 參考不同資訊。")
    print("Q、K 用來決定關注關係，V 提供最後要融合的內容。")


if __name__ == "__main__":
    main()
