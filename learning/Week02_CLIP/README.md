# Week02 CLIP 基礎

## 學習定位

Week02 延續 Week01 Transformer（轉換器架構）的向量表示概念，進一步理解 CLIP（Contrastive Language-Image Pre-training，對比式圖文預訓練）如何把影像與文字對齊到 Shared Embedding Space（共同嵌入空間）。

本週重點不是從零訓練模型，而是讀懂圖文資料流、向量 shape（張量形狀）、Cosine Similarity（餘弦相似度）與 Zero-shot Classification（零樣本分類）。

## 與 Week01 的關係

Week01 說明文字如何經過 Token（詞元）、Embedding（嵌入向量）與 Encoder（編碼器）形成語意表示。Week02 將相同直覺擴展到兩種模態：

```text
Image
-> Image Encoder
-> Image Embedding

Text
-> Text Encoder
-> Text Embedding

Image Embedding + Text Embedding
-> Cosine Similarity
-> Matching Score
-> Zero-shot Classification / Image-Text Retrieval
```

## 檔案導覽

- `weekly_plan.md`：本週 7 天規劃、任務與驗收條件。
- `notes.md`：CLIP 正式教材與概念對應 Demo。
- `study_log.md`：學生實際執行、觀察、疑問與反思紀錄。
- `demo/`：快速呈現 CLIP 在做什麼（What）。
- `practice/concept/`：觀念題與完成後再查看的參考答案。
- `practice/coding/`：Guided Code Reading（引導式程式閱讀），逐步理解如何做到（How）。

## 建議使用方式

1. 先讀本頁與 `weekly_plan.md`。
2. 依序閱讀 `notes.md`。
3. 在每個概念段落後執行指定 `demo/`。
4. 進入 [`practice/`](./practice/README.md) 完成觀念練習與 Guided Code Reading。
5. 將真實輸出、理解與疑問寫入 `study_log.md`。

## 與 VLM / VLA 研究的關係

CLIP 建立圖文語意對齊能力，是理解 Vision-Language Model（視覺語言模型，VLM）的重要前置。後續 VLM 會把視覺表示接到語言模型，用於回答與推理；Vision-Language-Action Model（視覺語言動作模型，VLA）則再把語意理解連到動作決策。CLIP 本身不是聊天模型，也不是完整的 VLM 或 VLA。

## 銜接 Week03

Week03 Hugging Face（機器學習模型平台與工具庫）會進一步學習如何使用 `transformers`、processor（前處理器）與預訓練模型。完成本週後，應能理解真實 CLIP 程式中的輸入、輸出與相似度分數，而不只是呼叫模型 API。
