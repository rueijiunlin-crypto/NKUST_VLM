"""
demo_embedding.py

使用 Hugging Face Transformers（模型工具套件）展示：
Token（詞元）如何進入模型，並取得 Embedding（嵌入向量）的 shape（形狀）。

執行前建議安裝：
    pip install transformers torch
"""


def main() -> None:
    sentence = "take me to the laboratory"
    model_name = "distilbert-base-uncased"

    try:
        import torch
        from transformers import AutoModel, AutoTokenizer
    except ImportError as error:
        print("無法匯入必要套件。")
        print("請先安裝 Hugging Face Transformers（模型工具套件）與 PyTorch（深度學習框架）：")
        print("pip install transformers torch")
        raise SystemExit(1) from error

    print("載入模型：")
    print(model_name)
    print()

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.eval()

    encoded = tokenizer(sentence, return_tensors="pt")
    token_ids = encoded["input_ids"][0]
    tokens = tokenizer.convert_ids_to_tokens(token_ids)

    with torch.no_grad():
        outputs = model(**encoded)

    embeddings = outputs.last_hidden_state
    token_count = embeddings.shape[1]
    embedding_dim = embeddings.shape[2]

    print("輸入文字：")
    print(sentence)
    print()

    print("Token（詞元）列表：")
    print(tokens)
    print()

    print("Embedding Shape（嵌入向量形狀）：")
    print(tuple(embeddings.shape))
    print()

    print("Token 數量：")
    print(token_count)
    print()

    print("Embedding 維度：")
    print(embedding_dim)
    print()

    print("說明：")
    print("Embedding（嵌入向量）會把 Token（詞元）轉成模型可以計算的向量表示。")
    print("每個 Token 都會有一個向量，模型會用這些向量理解語意與上下文關係。")


if __name__ == "__main__":
    main()
