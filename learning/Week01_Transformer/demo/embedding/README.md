# Embedding Demo（嵌入向量示範程式）

## 對應概念

Embedding（嵌入向量）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/embedding/demo_embedding.py
```

若缺少套件，可能需要先安裝：

```powershell
pip install transformers torch
```

## 預期輸出

- Token 列表。
- Token ID 列表。
- Embedding shape（嵌入向量形狀）。
- 部分 Embedding 數值。

## 觀察重點

- 每個 Token 如何被轉成向量。
- `batch_size`、`token_count`、`embedding_dim` 分別代表什麼。
- Embedding 為什麼比 Token ID 更適合送入模型。

## 執行後應回答的問題

1. Embedding shape 中每個維度代表什麼？
2. 為什麼 Token ID 不能直接代表語意？
3. Embedding 如何銜接到 Query（查詢）、Key（鍵）、Value（值）？
