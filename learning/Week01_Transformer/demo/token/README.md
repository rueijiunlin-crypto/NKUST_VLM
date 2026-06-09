# Token Demo（詞元示範程式）

## 對應概念

Token（詞元）與 Token ID（詞元編號）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/token/demo_tokenizer.py
```

## 預期輸出

- 原始句子。
- Token 列表。
- Token ID 列表。

## 觀察重點

- 原始文字如何被切成模型可處理的 Token。
- Token 如何被轉成整數 ID。
- Token 與 Token ID 是否一一對應。

## 執行後應回答的問題

1. Token 和原始文字有什麼差異？
2. Token ID 是語意本身，還是查表用的索引？
3. 為什麼下一步需要 Embedding（嵌入向量）？
