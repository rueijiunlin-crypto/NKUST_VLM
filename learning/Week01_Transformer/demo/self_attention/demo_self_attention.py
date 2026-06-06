"""
demo_self_attention.py

用簡化分數展示 Self-Attention（自注意力）：
同一句話中的每個 Token（詞元）都可以關注其他 Token。
本範例不實作完整 Transformer（轉換器架構），目的是建立直覺。
"""


def print_attention(query_token: str, scores: dict[str, float]) -> None:
    """列出某個 query token 對其他 token 的注意力分布。"""
    print(f"Query token: {query_token}")
    print("-" * 42)
    for token, score in scores.items():
        bar = "#" * int(score * 40)
        print(f"attends to {token:12s} score={score:.2f} {bar}")
    print()


def main() -> None:
    tokens = ["go", "to", "red", "door", "laboratory"]

    attention_map = {
        "go": {
            "go": 0.30,
            "to": 0.30,
            "red": 0.10,
            "door": 0.10,
            "laboratory": 0.20,
        },
        "laboratory": {
            "go": 0.10,
            "to": 0.10,
            "red": 0.25,
            "door": 0.30,
            "laboratory": 0.25,
        },
    }

    print("Token（詞元）序列：")
    print(tokens)
    print()

    for query_token, scores in attention_map.items():
        print_attention(query_token, scores)

    print("說明：")
    print("Self-Attention（自注意力）讓同一段輸入中的 Token（詞元）彼此參考。")
    print("理解 laboratory 時，red 與 door 的分數較高，代表位置與物件線索很重要。")
    print("理解 go 時，to 與 laboratory 也有幫助，因為它們共同描述導航意圖。")


if __name__ == "__main__":
    main()
