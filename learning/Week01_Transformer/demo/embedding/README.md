# Embedding Demo

## 對應概念

Embedding（嵌入向量）。

## 執行指令

```powershell
python demo\embedding\demo_embedding.py
```

若尚未安裝套件：

```powershell
pip install transformers torch
```

第一次執行可能需要下載 `distilbert-base-uncased` 模型與 tokenizer（分詞器）。

## 預期輸出

- Token（詞元）列表
- Embedding Shape（嵌入向量形狀）
- Token 數量
- Embedding 維度

## 觀察重點

- 每個 Token 如何對應到一個向量。
- `batch_size`、`token_count`、`embedding_dim` 分別代表什麼。

## 執行後應回答的問題

1. Embedding Shape 中三個數字分別代表什麼？
2. 為什麼 Token ID 不能直接代表語意？
3. Embedding 如何接到 Query（查詢）、Key（鍵）、Value（值）？
