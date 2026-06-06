"""
demo_position_encoding.py

用簡化 sin/cos 數值展示 Position Encoding（位置編碼）如何讓 Transformer（轉換器架構）
知道 Token（詞元）在序列中的位置。
"""

import math


def position_encoding(position: int, dim: int = 4) -> list[float]:
    values = []
    for i in range(dim):
        scale = 10000 ** (2 * (i // 2) / dim)
        angle = position / scale
        values.append(math.sin(angle) if i % 2 == 0 else math.cos(angle))
    return values


def main() -> None:
    tokens = ["go", "to", "laboratory"]

    print("Token with Position Encoding（位置編碼）")
    print("-" * 56)
    for position, token in enumerate(tokens):
        encoded = position_encoding(position)
        rounded = [round(value, 4) for value in encoded]
        print(f"position {position}: token={token:12s} encoding={rounded}")

    print()
    print("說明：即使 Token Embedding 相同，不同位置也會加入不同位置訊號。")
    print("這讓 Transformer 能分辨 go to laboratory 與 laboratory to go 的順序差異。")


if __name__ == "__main__":
    main()
