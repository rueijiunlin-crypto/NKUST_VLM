"""
demo_attention.py

建立簡化版 Attention（注意力機制）範例。
本範例不實作完整 Transformer（轉換器架構），只用手動分數展示模型如何決定關注哪些資訊。
"""


def main() -> None:
    tokens = ["take", "me", "to", "the", "laboratory"]

    attention_scores = {
        "take": 0.15,
        "me": 0.05,
        "to": 0.20,
        "the": 0.10,
        "laboratory": 0.50,
    }

    print("Token（詞元）與 Attention Score（注意力分數）：")
    print("-" * 42)
    for token in tokens:
        score = attention_scores[token]
        bar = "#" * int(score * 40)
        print(f"{token:12s} score={score:.2f} {bar}")
    print()

    most_important = max(attention_scores, key=attention_scores.get)

    print("最重要的 Token（詞元）：")
    print(most_important)
    print()

    print("說明：")
    print("Attention（注意力機制）會替不同 Token 分配重要性分數。")
    print("在這個例子中，laboratory 的分數最高，代表模型在理解指令時最需要關注目的地資訊。")
    print("真實 Transformer（轉換器架構）會由模型計算這些分數，而不是人工指定。")


if __name__ == "__main__":
    main()
