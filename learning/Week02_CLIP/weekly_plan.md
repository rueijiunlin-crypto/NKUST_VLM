# Week02 Weekly Plan: CLIP 基礎

## 本週目標

- 說明 CLIP 的基本任務是 image-text alignment（圖文對齊）。
- 分辨 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）的角色。
- 解釋共同嵌入空間、餘弦相似度與零樣本分類。
- 用直覺說明 Contrastive Learning（對比式學習）。
- 說明 CLIP 與 VLM / VLA 的關係。

## 必學概念

- Image Embedding（影像嵌入向量）與 Text Embedding（文字嵌入向量）
- Shared Embedding Space（共同嵌入空間）
- L2 normalization（L2 正規化）
- Cosine Similarity（餘弦相似度）
- Softmax（柔性最大化函數）與 Zero-shot Classification（零樣本分類）
- Positive Pair（正樣本配對）與 Negative Pair（負樣本配對）

## 建議 7 天學習順序

| Day | 建議內容 | 產出 |
| --- | --- | --- |
| Day 1 | 閱讀 `README.md` 與 `notes.md` Level 1-2 | 畫出 CLIP 核心資料流 |
| Day 2 | 閱讀 Level 3，執行 Demo 01 | 記錄 image/text embedding shape |
| Day 3 | 閱讀 Level 4，執行 Demo 02 | 記錄內積、norm 與相似度排序 |
| Day 4 | 閱讀 Level 5，執行 Demo 03 | 記錄 score、probability 與 top-1 |
| Day 5 | 閱讀 Level 6，執行 Demo 04 | 解釋正負配對與整體 pipeline |
| Day 6 | 完成 Concept Practice 與 Guided Code Reading | 記錄中間值與疑問 |
| Day 7 | 選做真實 CLIP Demo、整理 `study_log.md` 與 Notion | 完成本週摘要與驗收 |

## Demo 執行順序

請在 `learning/Week02_CLIP/` 下執行：

```powershell
python demo/demo_01_text_image_embedding.py
python demo/demo_02_cosine_similarity.py
python demo/demo_03_zero_shot_classification.py
python demo/demo_04_clip_flow.py
```

選做 / 進階：

```powershell
python demo/demo_05_real_clip_zero_shot.py --image demo/000000039769.jpg
```

## Practice 順序

1. [Practice Overview](./practice/README.md)
2. [Concept Practice](./practice/concept/concept_practice.md)
3. [Coding Practice](./practice/coding/coding_practice.md)
4. [Guided Demos](./practice/coding/guided_demos/)
5. [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

## Guided Code Reading Mode

本週採 Guided Code Reading Mode。程式已完整提供，學習者應執行、閱讀逐步註解、追蹤 shape 與中間值，再修改小參數觀察變化。本週不使用 `exercises/`、`solutions/` 或 TODO 補空題。

## 任務清單

- [✅] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [✅] 執行 4 個必要 NumPy Demo。
- [✅] 保存重要輸出並記錄觀察。
- [✅] 完成 Concept Practice。
- [✅] 完成 4 個 Guided Demo 的觀察任務。
- [✅] 選擇性執行真實 CLIP Demo，或記錄未執行原因。
- [✅] 更新 `study_log.md` 與 Notion。
- [✅] 進行 ChatGPT 驗收。

## 驗收條件

- [✅] 能說明 CLIP 的基本任務是圖文對齊。
- [✅] 能說明 Image Encoder 與 Text Encoder 的角色。
- [✅] 能說明共同向量空間的用途。
- [✅] 能說明 cosine similarity 如何比較圖片與文字。
- [✅] 能說明 zero-shot classification 的流程。
- [✅] 能說明 contrastive learning 的直覺。
- [✅] 能執行必要 NumPy concept demos。
- [✅] 能選擇性執行 real CLIP demo，或能說明未執行原因。
- [✅] 能完成 Concept Practice。
- [✅] 能完成 Guided Code Reading。
- [✅] 能用自己的話說明 CLIP 和 VLM / VLA 的關係。
- [✅] 能說明 Week02 如何銜接 Week03 Hugging Face。

## Notion 紀錄項目

- CLIP 核心資料流圖。
- Image Encoder / Text Encoder 比較。
- 共同嵌入空間與餘弦相似度摘要。
- Demo 與 Guided Demo 的輸出、shape、觀察與問題。
- 一段「CLIP 如何支援 VLM / VLA」的說明。
- 真實 CLIP Demo 執行狀態或未執行原因。

## 銜接 Week03 Hugging Face

完成 Week02 後，Week03 將把概念對應到 Hugging Face 的 `CLIPModel`、`CLIPProcessor`、模型下載與推論流程。進入 Week03 前，應先能解釋 logits（未正規化分數）、probability（機率）與 label prompt（標籤提示詞）在零樣本分類中的角色。

## ChatGPT 驗收結果

- 驗收狀態：Pass。
- 驗收日期：完成 Week02 後。
- 評語：已能說明 CLIP 的核心資料流、Image/Text Encoder、共同向量空間、cosine similarity、zero-shot classification、contrastive learning，以及 CLIP 與 VLM / VLA 的邊界。已完成 NumPy Demo、真實 CLIP Demo 與 Practice 作答。
