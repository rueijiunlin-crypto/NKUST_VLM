# Week01 Concept Practice（觀念練習）

請先閱讀 `notes.md` 並觀察 `demo/` 後再作答。本檔案是學生觀念作答檔，請保留自己的推理過程。

## Q1 Token、Token ID 與 Embedding

請用自己的話說明 Token（詞元）、Token ID（詞元識別碼）與 Embedding（嵌入向量）的差異。

學生作答：

-

自我檢查：

- [ ] 我能分辨文字切分結果、整數索引與向量表示。
- [ ] 我沒有把 Token ID 當成 Embedding。

## Q2 Query、Key、Value

請說明 Query（查詢）、Key（鍵）與 Value（值）在 Attention（注意力機制）中的角色。

學生作答：

-

自我檢查：

- [ ] 我能說明 Query 和 Key 如何產生分數。
- [ ] 我能說明 Value 為什麼會被加權加總。

## Q3 Attention Matrix

Attention Matrix（注意力矩陣）中的每一列通常代表什麼？為什麼 softmax（歸一化指數函數）的軸向很重要？

學生作答：

-

自我檢查：

- [ ] 我能說明每一列加總應接近 1。
- [ ] 我能指出錯誤軸向會造成錯誤的注意力分布。

## Q4 Self-Attention

Self-Attention（自注意力）和一般 Attention 的差異是什麼？

學生作答：

-

自我檢查：

- [ ] 我能說明 Q、K、V 來自同一序列時的意義。
- [ ] 我能說明它如何讓序列內不同位置互相參考。

## Q5 Position Encoding

為什麼 Transformer（轉換器）需要 Position Encoding（位置編碼）？

學生作答：

-

自我檢查：

- [ ] 我能說明注意力本身不直接知道順序。
- [ ] 我能說明位置資訊如何補進 token 表示。

## Q6 Multi-Head Attention

Multi-Head Attention（多頭注意力）為什麼要拆成多個 head（注意力頭）？

學生作答：

-

自我檢查：

- [ ] 我能說明不同 head 可關注不同關係。
- [ ] 我能說明最後需要 concat（串接）或投影回共同維度。

## Q7 Encoder 與 Decoder

請比較 Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）的用途。

學生作答：

-

自我檢查：

- [ ] 我能說明 Encoder 偏向理解輸入。
- [ ] 我能說明 Decoder 偏向逐步產生輸出。

## Q8 Transformer 與 VLM / CLIP

請說明 Transformer 和 Vision-Language Model（視覺語言模型，VLM）以及 CLIP（對比式圖文預訓練）的關係。

學生作答：

-

自我檢查：

- [ ] 我能說明文字與影像都可被轉成序列表示。
- [ ] 我能說明 CLIP 如何使用文字與影像 encoder 做對齊。

## 整合練習 A：Token、Token ID 與 Embedding

請用自己的話回答：

1. Token 和原始文字有什麼差異？
2. 為什麼模型需要 Embedding？
3. 如果一句話是「請帶我去實驗室」，你會如何直覺地切成 Token？

學生作答：

-

自我檢查：

- [ ] 回答有說明文字先被切分。
- [ ] 回答有說明 Token 會轉成數字與向量。

## 整合練習 B：QKV、Attention 與 Attention Matrix

請用 200 至 300 字回答：

1. Query、Key、Value 分別扮演什麼角色？
2. Attention Score（注意力分數）如何由 Q x K 產生？
3. Attention Matrix 如何表示每個 Token 對其他 Token 的關注？

學生作答：

-

自我檢查：

- [ ] 回答有說明 Q 和 K 比對產生分數。
- [ ] 回答有說明分數再加權 V。

## 整合練習 C：Self-Attention、Position Encoding 與 Multi-Head Attention

請回答：

1. Self-Attention 為什麼適合處理一句話內部的上下文？
2. Transformer 為什麼需要 Position Encoding？
3. Multi-Head Attention 為什麼比單一 Attention 更有彈性？

學生作答：

-

自我檢查：

- [ ] 回答有說明不同 Token 看到不同資訊。
- [ ] 回答有說明順序資訊。
- [ ] 回答有說明多視角關注。

## 整合練習 D：Transformer、VLM 與 CLIP

請回答：

1. Transformer Encoder 和 Transformer Decoder 的主要差異是什麼？
2. 為什麼 VLM 需要 Transformer？
3. Transformer 與 CLIP 的關係是什麼？

學生作答：

-

自我檢查：

- [ ] 回答有連結文字、影像與共同向量空間。
