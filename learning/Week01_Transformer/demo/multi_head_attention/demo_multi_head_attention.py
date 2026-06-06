"""
demo_multi_head_attention.py

用手動分數示範 Multi-Head Attention（多頭注意力）：
不同 head（頭）可以關注不同語意線索。
"""


def main() -> None:
    heads = {
        "Head 1 - target": {"go": 0.05, "to": 0.10, "red": 0.10, "door": 0.25, "laboratory": 0.50},
        "Head 2 - attribute": {"go": 0.05, "to": 0.05, "red": 0.60, "door": 0.20, "laboratory": 0.10},
        "Head 3 - landmark": {"go": 0.05, "to": 0.05, "red": 0.20, "door": 0.55, "laboratory": 0.15},
    }

    print("Multi-Head Attention（多頭注意力）")
    print("-" * 56)
    for head_name, scores in heads.items():
        focus = max(scores, key=scores.get)
        print(head_name)
        print("scores:", scores)
        print("focus:", focus)
        print()

    print("說明：多個 head 可以同時觀察目的地、屬性與地標，讓模型取得多視角上下文。")


if __name__ == "__main__":
    main()
