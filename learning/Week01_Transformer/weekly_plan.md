# Week01 Weekly Plan: Transformer 基礎

## 1. Week01 學習目標

- 說明 Token（詞元）、Token ID（詞元編號）與 Embedding（嵌入向量）的資料流。
- 說明 Query（查詢）、Key（鍵）、Value（值）如何形成 Attention（注意力機制）。
- 讀懂 Attention Matrix（注意力矩陣）中每個 Token 的關注關係。
- 分辨 Self-Attention（自注意力）、Position Encoding（位置編碼）與 Multi-Head Attention（多頭注意力）的用途。
- 分辨 Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）。
- 說明 Transformer 與 Vision-Language Model（視覺語言模型，VLM）、Vision-Language-Action Model（視覺語言動作模型，VLA）及 CLIP（對比式圖文預訓練）的關係。

## 2. 本週核心概念

- Token 與 Token ID
- Embedding
- Query / Key / Value
- Attention
- Self-Attention
- Attention Matrix
- Position Encoding
- Multi-Head Attention
- Transformer Encoder
- Transformer Decoder
- Transformer 與 VLM / CLIP 的關係

## 3. 建議 7 天學習安排

| Day | 建議內容 | 產出 |
|---|---|---|
| Day 1 | 閱讀 `README.md`，讀 `notes.md` 的 Token、Token ID、Embedding | 100 字資料流摘要 |
| Day 2 | 執行 Token 與 Embedding Demo | 將真實輸出與觀察寫入 `study_log.md` |
| Day 3 | 閱讀 QKV、Attention、Attention Matrix | 完成觀念練習 2 草稿 |
| Day 4 | 執行 QKV 與 Attention 相關 Demo | 記錄分數、矩陣與觀察問題 |
| Day 5 | 閱讀 Self-Attention、Position Encoding、Multi-Head Attention | 畫出注意力與位置資訊流程 |
| Day 6 | 閱讀 Encoder、Decoder、Transformer 與 VLM / CLIP 的關係 | 完成 Encoder/Decoder 比較 |
| Day 7 | 完成觀念練習、程式練習、驗收清單與 Notion 紀錄 | 更新 `study_log.md` |

## 4. Demo（示範程式）執行順序

請在 `learning/Week01_Transformer/` 目錄下依序執行：

```powershell
python demo/token/demo_tokenizer.py
python demo/embedding/demo_embedding.py
python demo/qkv/demo_qkv.py
python demo/attention/demo_attention.py
python demo/attention/demo_attention_matrix.py
python demo/self_attention/demo_self_attention.py
python demo/position_encoding/demo_position_encoding.py
python demo/multi_head_attention/demo_multi_head_attention.py
python demo/encoder_decoder/demo_encoder_decoder_flow.py
```

執行後請把真實輸出重點與觀察寫入 `study_log.md`。不要只記錄「成功」，也要寫出看到了什麼。

## 5. 觀念練習

### 練習 1：Token、Token ID 與 Embedding

請用自己的話回答：

1. Token 和原始文字有什麼差異？
2. 為什麼模型需要 Embedding？
3. 如果一句話是「請帶我去實驗室」，你會如何直覺地切成 Token？

驗收標準：回答需說明「文字先被切分，再轉成數字與向量」。

### 練習 2：QKV、Attention 與 Attention Matrix

請用 200 至 300 字回答：

1. Query、Key、Value 分別扮演什麼角色？
2. Attention Score（注意力分數）如何由 Q x K 產生？
3. Attention Matrix 如何表示每個 Token 對其他 Token 的關注？

驗收標準：回答需包含「Q 和 K 比對產生分數，分數再加權 V」。

### 練習 3：Self-Attention、Position Encoding 與 Multi-Head Attention

請回答：

1. Self-Attention 為什麼適合處理一句話內部的上下文？
2. Transformer 為什麼需要 Position Encoding？
3. Multi-Head Attention 為什麼比單一 Attention 更有彈性？

驗收標準：回答需說明「不同 Token 看到不同資訊」、「順序資訊」與「多視角關注」。

### 練習 4：Transformer、VLM 與 CLIP

請回答：

1. Transformer Encoder 和 Transformer Decoder 的主要差異是什麼？
2. 為什麼 VLM 需要 Transformer？
3. Transformer 與 CLIP 的關係是什麼？

驗收標準：回答需連結文字、影像與共同向量空間。

## 6. 程式練習

### 程式練習 1：簡易 Token 與詞彙表

建立一個簡單 Python（程式語言）檔案，例如 `simple_tokenizer.py`，完成以下功能：

1. 輸入英文句子 `take me to the laboratory`。
2. 用空白切分成 Token。
3. 建立 vocabulary（詞彙表），把每個 Token 對應到整數 ID。
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

### 程式練習 2：簡易 Attention 權重直覺

建立 `simple_attention_demo.py`，模擬「注意力權重」概念。

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

驗收標準：能用程式輸出說明 Attention 是「加權參考其他 Token」。

### 程式練習 3：簡易 QKV 分數

建立 `simple_qkv_score.py`，手動設定一個 Query 向量與三個 Key 向量，計算 Q x K 分數。

驗收標準：能說明分數最高的 Key 為什麼最接近 Query。

## 7. 驗收清單

- [✅] 閱讀 `README.md`。
- [✅] 閱讀 `weekly_plan.md`。
- [✅] 閱讀 `notes.md`。
- [✅] 執行 `demo/token/demo_tokenizer.py`。
- [✅] 執行 `demo/embedding/demo_embedding.py`。
- [✅] 執行 `demo/qkv/demo_qkv.py`。
- [✅] 執行 `demo/attention/demo_attention.py`。
- [✅] 執行 `demo/attention/demo_attention_matrix.py`。
- [✅] 執行 `demo/self_attention/demo_self_attention.py`。
- [✅] 執行 `demo/position_encoding/demo_position_encoding.py`。
- [✅] 執行 `demo/multi_head_attention/demo_multi_head_attention.py`。
- [✅] 執行 `demo/encoder_decoder/demo_encoder_decoder_flow.py`。
- [ ] 完成 4 題觀念練習。
- [ ] 完成 3 題程式練習。
- [✅] 將 Demo（示範程式）輸出與觀察記錄到 `study_log.md`。
- [✅] 能口頭說明 Token -> Token ID -> Embedding -> QKV -> Attention 的流程。
- [✅] 能口頭說明 Attention Matrix、Position Encoding 與 Multi-Head Attention。
- [✅] 能比較 Encoder 與 Decoder。
- [✅] 能用 150 字說明 Transformer 與 CLIP 的關係。

## 8. Notion 紀錄項目

- 本週 5 個關鍵詞。
- Token -> Embedding -> QKV -> Attention 流程圖。
- 4 題觀念練習答案。
- Demo 輸出與觀察紀錄。
- 3 題程式練習結果。
- 一段「Transformer 與 CLIP 的關係」摘要。
- 本週最不熟的 3 個概念。

## 9. 完成 Week01 後銜接 Week02 CLIP

完成 Week01 後，應能理解文字如何被轉成向量序列，以及 Transformer 如何用 Attention 建立上下文表示。Week02 的 CLIP 會把這條線延伸到影像：圖片經過 Image Encoder 變成影像向量，文字經過 Text Encoder 變成文字向量，兩者再放到共同向量空間中比較相似度。

進入 Week02 前，請準備：

- 一張簡單圖片，用於圖文相似度測試。
- 5 個文字標籤，用於比較圖片與文字描述。
- 一段自己的解釋：為什麼 Transformer 能幫助 CLIP 處理文字與影像？
