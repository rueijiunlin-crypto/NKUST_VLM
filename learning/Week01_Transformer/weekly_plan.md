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
| Day 2 | 執行 Token / Embedding Demo 與第一個 Guided Demo | 將真實輸出與 shape 觀察寫入 `study_log.md` |
| Day 3 | 閱讀 QKV、Attention、Attention Matrix | 完成觀念練習 2 草稿 |
| Day 4 | 執行 Attention Overview Demo 與 QKV / Self-Attention Guided Demo | 記錄權重、shape 與資料流 |
| Day 5 | 閱讀 Self-Attention、Position Encoding、Multi-Head Attention | 畫出注意力與位置資訊流程 |
| Day 6 | 閱讀 Encoder、Decoder、Transformer 與 VLM / CLIP 的關係 | 完成 Encoder/Decoder 比較 |
| Day 7 | 完成觀念練習、Guided Code Reading、驗收清單與 Notion 紀錄 | 更新 `study_log.md` |

## 4. Demo（示範程式）執行順序

請在 `learning/Week01_Transformer/` 目錄下依序執行：

```powershell
python demo/demo_01_token_embedding.py
python demo/demo_02_attention_overview.py
python demo/demo_03_position_multihead.py
python demo/demo_04_transformer_flow.py
```

執行後請把真實輸出重點與觀察寫入 `study_log.md`。不要只記錄「成功」，也要寫出看到了什麼。

## 5. Practice 順序

1. [Practice Overview](./practice/README.md)
2. [Concept Practice](./practice/concept/concept_practice.md)
3. [Guided Code Reading Overview](./practice/coding/README.md)
4. [Coding Observation Tasks](./practice/coding/coding_practice.md)
5. [Guided Demos](./practice/coding/guided_demos/)
6. [Coding Observation Key](./practice/coding/coding_observation_key.md)

Week01 採用 Guided Code Reading Mode，不使用 `exercises/`、`solutions/` 或程式補空題。觀念參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

## 6. 驗收清單

- [✅] 閱讀 `README.md`。
- [✅] 閱讀 `weekly_plan.md`。
- [✅] 閱讀 `notes.md`。
- [✅] 執行 `demo/demo_01_token_embedding.py`。
- [✅] 執行 `demo/demo_02_attention_overview.py`。
- [✅] 執行 `demo/demo_03_position_multihead.py`。
- [✅] 執行 `demo/demo_04_transformer_flow.py`。
- [✅] 完成 [Concept Practice](./practice/concept/concept_practice.md)。
- [✅] 完成 [Coding Observation Tasks](./practice/coding/coding_practice.md)。
- [✅] 執行必要 [Guided Demos](./practice/coding/guided_demos/)。
- [✅] 在 `study_log.md` 記錄 Practice 的重要觀察與疑問。
- [✅] 已保留重構前 Demo 的輸出與觀察紀錄。
- [✅] 能口頭說明 Token -> Token ID -> Embedding -> QKV -> Attention 的流程。
- [✅] 能口頭說明 Attention Matrix、Position Encoding 與 Multi-Head Attention。
- [✅] 能比較 Encoder 與 Decoder。
- [✅] 能用 150 字說明 Transformer 與 CLIP 的關係。

## 7. Notion 紀錄項目

- 本週 5 個關鍵詞。
- Token -> Embedding -> QKV -> Attention 流程圖。
- Concept Practice 的重要理解與疑問。
- Demo 輸出與觀察紀錄。
- Guided Code Reading 的重要觀察與疑問。
- 一段「Transformer 與 CLIP 的關係」摘要。
- 本週最不熟的 3 個概念。

## 8. 完成 Week01 後銜接 Week02 CLIP

完成 Week01 後，應能理解文字如何被轉成向量序列，以及 Transformer 如何用 Attention 建立上下文表示。Week02 的 CLIP 會把這條線延伸到影像：圖片經過 Image Encoder 變成影像向量，文字經過 Text Encoder 變成文字向量，兩者再放到共同向量空間中比較相似度。

進入 Week02 前，請準備：

- 一張簡單圖片，用於圖文相似度測試。
- 5 個文字標籤，用於比較圖片與文字描述。
- 一段自己的解釋：為什麼 Transformer 能幫助 CLIP 處理文字與影像？
