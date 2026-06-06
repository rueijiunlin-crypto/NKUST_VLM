"""
demo_tokenizer.py

示範文字如何變成 Token（詞元）與 Token ID（詞元編號）。
本範例使用簡化版空白切分，目的是建立直覺，不代表真實大型模型的完整 Tokenizer（分詞器）行為。
"""


def simple_tokenize(sentence: str) -> list[str]:
    """使用空白切分英文句子，回傳 Token（詞元）列表。"""
    return sentence.lower().split()


def build_vocab(tokens: list[str]) -> dict[str, int]:
    """建立簡單 vocabulary（詞彙表），把每個 Token 對應到整數 ID。"""
    unique_tokens = sorted(set(tokens))
    return {token: index for index, token in enumerate(unique_tokens)}


def main() -> None:
    sentence = "take me to the laboratory"
    tokens = simple_tokenize(sentence)
    vocab = build_vocab(tokens)
    token_ids = [vocab[token] for token in tokens]

    print("輸入文字：")
    print(sentence)
    print()

    print("Token（詞元）列表：")
    print(tokens)
    print()

    print("Token ID（詞元編號）列表：")
    print(token_ids)
    print()

    print("說明：")
    print("文字不會直接進入模型。模型會先把文字切成 Token（詞元），再把每個 Token 對應到數字 ID。")
    print("真實模型會使用自己的 Tokenizer（分詞器），切分方式可能比這個空白切分範例更細。")


if __name__ == "__main__":
    main()
