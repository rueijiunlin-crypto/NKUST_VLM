# Week01 Transformer 基礎

## 本週定位

本週目標是用一週時間建立 Transformer（轉換器架構）的基本直覺，讓後續學習 CLIP（對比式圖文預訓練）、LLaVA（大型語言與視覺助手）與 VLM（視覺語言模型）時，不會只是在背模型名稱。

本週不追求完整論文級推導，但會說明理解 Transformer 必要的數學直覺：QKV、Attention Score、Softmax（柔性最大化函數）、Attention Matrix（注意力矩陣）、Position Encoding（位置編碼）與 Multi-Head Attention（多頭注意力）。

## 學習目標

完成本週後，應能做到：

- 說明 Token（詞元）如何把文字切成模型可處理的單位。
- 說明 Token ID（詞元編號）如何作為模型輸入的中介。
- 說明 Embedding（嵌入向量）如何把 Token 轉成向量。
- 說明 Query（查詢）、Key（鍵）、Value（值）如何形成 Attention（注意力機制）。
- 說明 Attention Matrix（注意力矩陣）如何觀察不同 Token 的關注關係。
- 說明 Position Encoding（位置編碼）為什麼能補足順序資訊。
- 說明 Multi-Head Attention（多頭注意力）如何提供多視角理解。
- 說明 Attention 與 Self-Attention（自注意力）的直覺與技術作用。
- 分辨 Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）的用途。
- 說明為什麼 VLM 需要 Transformer。
- 說明 Transformer 與 CLIP 的關係。

## 必懂概念

### Token（詞元）

Token 是模型讀取文字的基本單位。模型不直接讀「一句話」，而是先把句子切成 Token，再轉成數字與向量。

### Embedding（嵌入向量）

Embedding 是 Token 的向量表示。它讓模型可以用數值方式比較不同文字之間的語意關係。

### Query（查詢）、Key（鍵）、Value（值）

QKV 是 Attention 的準備步驟。Query 表示目前要找什麼，Key 表示可被比對的特徵，Value 表示真正被取用的內容。

### Attention（注意力機制）

Attention 的核心想法是：模型在理解某個位置的內容時，會決定要把注意力放在哪些其他位置。

### Attention Matrix（注意力矩陣）

Attention Matrix 顯示每個 Token 對其他 Token 的注意力分布。

### Self-Attention（自注意力）

Self-Attention 是同一段輸入內部彼此互相參考。例如一句話中的每個 Token 都會看其他 Token，判斷哪些字對理解自己最重要。

### Position Encoding（位置編碼）

Position Encoding 讓 Transformer 知道 Token 或影像 Patch（影像切塊）的位置與順序。

### Multi-Head Attention（多頭注意力）

Multi-Head Attention 讓模型用多個 head（頭）同時觀察不同關係，例如目標、顏色、位置與動作。

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
| Day 1 | 讀 Token、Token ID 與 Embedding，執行 `demo/token/`、`demo/embedding/` | 100 字概念摘要 |
| Day 2 | 讀 QKV 與 Attention，執行 `demo/qkv/`、`demo/attention/` | 一張注意力直覺圖 |
| Day 3 | 讀 Self-Attention、Attention Matrix、Position Encoding 與 Multi-Head Attention | 一張注意力矩陣觀察紀錄 |
| Day 4 | 讀 Encoder 與 Decoder | Encoder/Decoder 比較表 |
| Day 5 | 讀 VLM 為什麼需要 Transformer | 150 字短文 |
| Day 6 | 完成觀念練習與 Demo 觀察紀錄 | 題目回答與 `study_log.md` |
| Day 7 | 完成 review.md | 本週驗收清單 |

## 本週學習驗收清單

- [ ] 我能用自己的話解釋 Token（詞元）。
- [ ] 我能用自己的話解釋 Token ID（詞元編號）。
- [ ] 我能用自己的話解釋 Embedding（嵌入向量）。
- [ ] 我能說明 Query（查詢）、Key（鍵）、Value（值）。
- [ ] 我能說明 Attention（注意力機制）解決了什麼問題。
- [ ] 我能說明 Attention Matrix（注意力矩陣）如何閱讀。
- [ ] 我能分辨 Attention 與 Self-Attention（自注意力）。
- [ ] 我能說明 Position Encoding（位置編碼）的用途。
- [ ] 我能說明 Multi-Head Attention（多頭注意力）的用途。
- [ ] 我能說明 Encoder 與 Decoder 的差異。
- [ ] 我能說明為什麼 VLM 需要 Transformer。
- [ ] 我能說明 Transformer 與 CLIP 的關係。
- [ ] 我完成 4 題觀念練習、Demo 觀察任務與 3 題程式練習。

## Notion 紀錄項目

- 本週 5 個關鍵詞
- 一張 Transformer 資料流圖
- 4 題觀念練習答案
- Demo 輸出與觀察紀錄
- 3 題程式練習結果
- 一段「Transformer 與 CLIP 的關係」摘要
