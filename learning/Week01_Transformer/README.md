# Week01 Transformer 基礎

## 本週定位

本週目標是用一週時間建立 Transformer（轉換器架構）的基本直覺，讓後續學習 CLIP（對比式圖文預訓練）、LLaVA（大型語言與視覺助手）與 VLM（視覺語言模型）時，不會只是在背模型名稱。

本週不追求很深的數學推導，而是先理解資料如何從文字變成模型能處理的向量，以及模型如何透過 Attention（注意力機制）理解上下文關係。

## 學習目標

完成本週後，應能做到：

- 說明 Token（詞元）如何把文字切成模型可處理的單位。
- 說明 Embedding（嵌入向量）如何把 Token 轉成向量。
- 說明 Attention 與 Self-Attention（自注意力）的直覺作用。
- 分辨 Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）的用途。
- 說明為什麼 VLM 需要 Transformer。
- 說明 Transformer 與 CLIP 的關係。

## 必懂概念

### Token（詞元）

Token 是模型讀取文字的基本單位。模型不直接讀「一句話」，而是先把句子切成 Token，再轉成數字與向量。

### Embedding（嵌入向量）

Embedding 是 Token 的向量表示。它讓模型可以用數值方式比較不同文字之間的語意關係。

### Attention（注意力機制）

Attention 的核心想法是：模型在理解某個位置的內容時，會決定要把注意力放在哪些其他位置。

### Self-Attention（自注意力）

Self-Attention 是同一段輸入內部彼此互相參考。例如一句話中的每個 Token 都會看其他 Token，判斷哪些字對理解自己最重要。

### Transformer Encoder（轉換器編碼器）

Encoder 擅長理解輸入並產生表示，常用於分類、檢索、比對與特徵抽取。

### Transformer Decoder（轉換器解碼器）

Decoder 擅長根據上下文逐步產生文字，常用於問答、摘要、對話與描述生成。

## 為什麼 VLM 需要 Transformer

VLM 需要同時處理影像與文字。影像可以被切成 Patch（影像切塊），文字可以被切成 Token，兩者都能轉成向量序列。Transformer 擅長處理序列中的關係，因此能協助模型學習影像區域、文字描述與語意概念之間的對應。

## Transformer 與 CLIP 的關係

CLIP 使用影像編碼器與文字編碼器，把圖片與文字轉成可比較的向量。Transformer 的觀念能幫助理解文字如何被編碼，也能幫助理解影像如何被 Vision Transformer（視覺轉換器）切成 Patch 後進行表示學習。學完本週後，Week02 會接著學習「圖片與文字如何被放到共同向量空間」。

## 建議一週安排

| 日期 | 建議內容 | 產出 |
|---|---|---|
| Day 1 | 讀 Token 與 Embedding | 100 字概念摘要 |
| Day 2 | 讀 Attention 與 Self-Attention | 一張注意力直覺圖 |
| Day 3 | 讀 Encoder 與 Decoder | Encoder/Decoder 比較表 |
| Day 4 | 讀 VLM 為什麼需要 Transformer | 150 字短文 |
| Day 5 | 完成觀念練習 | 三題回答 |
| Day 6 | 完成程式練習 | 兩個簡單 Python 練習 |
| Day 7 | 完成 review.md | 本週驗收清單 |

## 本週學習驗收清單

- [ ] 我能用自己的話解釋 Token（詞元）。
- [ ] 我能用自己的話解釋 Embedding（嵌入向量）。
- [ ] 我能說明 Attention（注意力機制）解決了什麼問題。
- [ ] 我能分辨 Attention 與 Self-Attention（自注意力）。
- [ ] 我能說明 Encoder 與 Decoder 的差異。
- [ ] 我能說明為什麼 VLM 需要 Transformer。
- [ ] 我能說明 Transformer 與 CLIP 的關係。
- [ ] 我完成 3 題觀念練習與 2 題程式練習。

## Notion 紀錄項目

- 本週 5 個關鍵詞
- 一張 Transformer 資料流圖
- 3 題觀念練習答案
- 2 題程式練習結果
- 一段「Transformer 與 CLIP 的關係」摘要
