"""
demo_attention_matrix.py

用簡化矩陣展示 Attention Matrix（注意力矩陣）。
每一列代表一個 Query Token（查詢詞元）對所有 Key Token（鍵詞元）的注意力權重。
"""


def main() -> None:
    tokens = ["go", "to", "red", "door", "laboratory"]
    matrix = [
        [0.35, 0.30, 0.05, 0.10, 0.20],
        [0.20, 0.35, 0.05, 0.15, 0.25],
        [0.05, 0.05, 0.45, 0.35, 0.10],
        [0.05, 0.05, 0.25, 0.45, 0.20],
        [0.05, 0.05, 0.25, 0.35, 0.30],
    ]

    print("Attention Matrix（注意力矩陣）")
    print("query\\key".ljust(14) + "".join(token.rjust(12) for token in tokens))
    print("-" * 74)

    for query_token, row in zip(tokens, matrix):
        row_text = "".join(f"{weight:12.2f}" for weight in row)
        print(query_token.ljust(14) + row_text + f"   sum={sum(row):.2f}")

    print()
    print("說明：每一列加總為 1，代表某個 Query Token 如何分配注意力給所有 Key Token。")
    print("不同列的最高值不同，代表不同 Token 看到的重點不同。")


if __name__ == "__main__":
    main()
