"""快速展示位置資訊與多頭注意力的用途。"""


def main() -> None:
    tokens = ["red", "door", "ahead"]
    positioned_tokens = [f"position={index}, token={token}" for index, token in enumerate(tokens)]
    heads = {
        "Head 1 - object": {"red": 0.20, "door": 0.65, "ahead": 0.15},
        "Head 2 - direction": {"red": 0.10, "door": 0.25, "ahead": 0.65},
    }

    print("Position information:")
    for item in positioned_tokens:
        print(" ", item)

    print("\nMulti-Head focus:")
    for head, weights in heads.items():
        print(f" {head}: {max(weights, key=weights.get)}")

    print("\n觀察：位置資訊保留順序；不同 head 可以同時關注物件與方向。")


if __name__ == "__main__":
    main()
