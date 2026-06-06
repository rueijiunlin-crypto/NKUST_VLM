# Week01 Tasks：Transformer 基礎

本週任務分成觀念練習與程式練習。目標不是寫出完整 Transformer，而是建立足夠清楚的直覺，能銜接 Week02 CLIP（對比式圖文預訓練）。

## 觀念練習 1：Token 與 Embedding

請用自己的話回答：

1. Token（詞元）和原始文字有什麼差異？
2. 為什麼模型需要 Embedding（嵌入向量）？
3. 如果一句話是「請帶我去實驗室」，你會如何直覺地切成 Token？

驗收標準：回答需能說明「文字先被切分，再轉成向量」這個流程。

## 觀念練習 2：Attention 與 Self-Attention

請用 150 至 250 字說明：

- Attention（注意力機制）在解決什麼問題？
- Self-Attention（自注意力）為什麼適合處理一句話內部的上下文？

驗收標準：回答需包含「理解某個位置時，需要參考其他位置」的概念。

## 觀念練習 3：Transformer、VLM 與 CLIP

請回答以下問題：

1. Transformer Encoder（轉換器編碼器）和 Transformer Decoder（轉換器解碼器）的主要差異是什麼？
2. 為什麼 Vision-Language Model（視覺語言模型）需要 Transformer？
3. Transformer 與 CLIP 的關係是什麼？

驗收標準：回答需能連結文字、影像與共同向量空間。

## 程式練習 1：簡易 Token 與詞彙表

建立一個簡單 Python（程式語言）檔案，例如 `simple_tokenizer.py`，完成以下功能：

1. 輸入一句英文句子：`take me to the laboratory`
2. 用空白切分成 Token。
3. 建立 vocabulary（詞彙表），把每個 Token 對應到一個整數 ID。
4. 印出 Token 列表與 ID 列表。

參考方向：

```python
sentence = "take me to the laboratory"
tokens = sentence.split()
vocab = {token: idx for idx, token in enumerate(sorted(set(tokens)))}
ids = [vocab[token] for token in tokens]
print(tokens)
print(ids)
```

驗收標準：能看到文字被切成 Token，並被轉成數字 ID。

## 程式練習 2：簡易 Attention 權重直覺

建立一個簡單 Python 檔案，例如 `simple_attention_demo.py`，不用實作完整 Transformer，只需要模擬「注意力權重」的概念。

任務：

1. 建立 Token：`["go", "to", "red", "door", "laboratory"]`
2. 假設模型正在理解 `laboratory`。
3. 手動指定注意力分數，例如 `red=0.2`、`door=0.4`、`go=0.2`、`to=0.1`、`laboratory=0.1`。
4. 印出分數最高的 Token，並用一句話解釋為什麼它重要。

參考方向：

```python
tokens = ["go", "to", "red", "door", "laboratory"]
attention = {
    "go": 0.2,
    "to": 0.1,
    "red": 0.2,
    "door": 0.4,
    "laboratory": 0.1,
}
most_important = max(attention, key=attention.get)
print(f"Most important token: {most_important}")
print("The token helps locate the target in the instruction.")
```

驗收標準：能用程式輸出說明 Attention 是「加權參考其他 Token」的概念。

## 本週學習驗收清單

- [ ] 完成觀念練習 1。
- [ ] 完成觀念練習 2。
- [ ] 完成觀念練習 3。
- [ ] 完成程式練習 1。
- [ ] 完成程式練習 2。
- [ ] 能口頭說明 Token → Embedding → Attention 的流程。
- [ ] 能口頭說明 Encoder 與 Decoder 的差異。
- [ ] 能用 150 字說明 Transformer 與 CLIP 的關係。

## 建議提交到 Notion 的內容

- 三題觀念練習答案
- 兩題程式練習執行結果
- 一張 Token → Embedding → Attention 流程圖
- 本週最不熟的三個概念
