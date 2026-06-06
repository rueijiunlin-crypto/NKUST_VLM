# Week01 Transformer 基礎

## 學習目標

本週目標是理解 Transformer（轉換器架構）如何處理文字序列，並建立後續學習 CLIP（對比式圖文預訓練）與 VLM（視覺語言模型）的基礎。

## 必懂概念

- Token（詞元）：模型處理文字時的基本單位。
- Embedding（嵌入向量）：將 Token 轉成可計算的向量表示。
- Attention（注意力機制）：讓模型判斷不同 Token 之間的重要關係。
- Transformer Encoder（轉換器編碼器）：適合理解輸入內容並產生表示。
- Transformer Decoder（轉換器解碼器）：適合根據上下文產生輸出文字。

## 實作任務

- 整理 Token、Embedding、Attention 的簡短筆記。
- 畫出 Encoder 與 Decoder 的資料流。
- 說明為什麼 VLM 需要 Transformer。
- 準備 Week02 CLIP 的銜接問題。

## 驗收標準

- 能解釋文字如何從 Token 變成 Embedding。
- 能說明 Attention 的直覺作用。
- 能分辨 Encoder 與 Decoder 的用途。
- 能說明 Transformer 為什麼能支援影像與文字對齊。

## Notion 紀錄項目

- 本週學到的 5 個關鍵詞
- 一張 Transformer 資料流圖
- 一段「為什麼 VLM 需要 Transformer」的短文
- 下週想問 CLIP 的問題
