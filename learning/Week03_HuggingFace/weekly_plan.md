# Week03 Weekly Plan: Hugging Face CLIP 推論

## 本週目標

- 說明 Hugging Face 在 VLM / VLA 學習中的角色。
- 分辨 `CLIPProcessor` 與 `CLIPModel` 的職責。
- 能用本地圖片與自訂 labels 執行真實 CLIP zero-shot classification。
- 能解釋 `logits_per_image`、softmax probability 與 top-k prediction。
- 能說明 prompt 設計如何影響 zero-shot 結果。
- 能記錄模型下載、快取、路徑與 SSL / network 相關問題。

## 必學概念

- Hugging Face Transformers（模型載入與推論工具庫）
- Processor（處理器）與 tokenizer / image preprocessing
- PyTorch tensor（張量）與 batch dimension（批次維度）
- `CLIPModel.from_pretrained()` 與 `CLIPProcessor.from_pretrained()`
- `logits_per_image` 與 `logits_per_text`
- Softmax probability 與 top-k prediction
- Prompt engineering（提示詞工程）與 prompt sensitivity（提示詞敏感性）

## 建議 7 天學習順序

| Day | 建議內容 | 產出 |
| --- | --- | --- |
| Day 1 | 閱讀 `README.md` 與 `notes.md` Level 1-2 | 畫出 Hugging Face CLIP 推論流程 |
| Day 2 | 閱讀 Level 3，執行 Demo 01 | 記錄 processor 輸出的 tensor keys 與 shape |
| Day 3 | 閱讀 Level 4，執行 Demo 02 | 使用本地圖片完成 zero-shot classification |
| Day 4 | 閱讀 Level 5，執行 Demo 03 | 比較不同 prompt 對結果的影響 |
| Day 5 | 閱讀 Level 6-7 | 整理 logits、probability、top-k 與常見錯誤 |
| Day 6 | 完成 Concept Practice 與 Guided Code Reading | 記錄中間值與疑問 |
| Day 7 | 整理 `study_log.md` 與 Notion | 完成本週摘要與驗收 |

## Demo 執行順序

請先安裝依賴：

```powershell
cd learning/Week03_HuggingFace
python -m pip install -r demo/requirements.txt
```

依序執行：

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若尚未有本地圖片，請先放一張 `.jpg` 或 `.png` 到 `demo/`，再將 `--image` 改成該圖片路徑。

## Practice 順序

1. [Practice Overview](./practice/README.md)
2. [Concept Practice](./practice/concept/concept_practice.md)
3. [Coding Practice](./practice/coding/coding_practice.md)
4. [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

## Guided Code Reading Mode

本週採 Guided Code Reading Mode。程式已完整提供，學習者應執行、閱讀註解、追蹤 processor 輸出、模型輸出與 top-k 計算流程。本週不要求從零實作 Hugging Face 推論程式。

## 任務清單

- [ ] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [ ] 安裝 Week03 demo dependencies。
- [ ] 執行 Demo 01，記錄 processor 輸出。
- [ ] 執行 Demo 02，完成本地圖片 zero-shot classification。
- [ ] 執行 Demo 03，觀察 prompt 改寫對結果的影響。
- [ ] 完成 Concept Practice。
- [ ] 完成 Guided Code Reading。
- [ ] 更新 `study_log.md` 與 Notion。
- [ ] 進行 ChatGPT 驗收。

## 驗收條件

- [ ] 能說明 Hugging Face 在本週任務中的角色。
- [ ] 能說明 `CLIPProcessor` 與 `CLIPModel` 的分工。
- [ ] 能使用本地圖片執行真實 CLIP zero-shot 推論。
- [ ] 能解釋 `logits_per_image` 的 shape 與意義。
- [ ] 能說明 softmax probability 是候選 labels 之間的相對分布。
- [ ] 能說明 prompt 改寫為什麼會影響結果。
- [ ] 能記錄並處理常見問題，例如模型下載、圖片路徑或 SSL 錯誤。
- [ ] 能說明 Week03 如何銜接 Week04 LLaVA。

## Notion 紀錄項目

- Hugging Face CLIP 推論流程圖。
- Processor / Model / Output 對照表。
- Demo 01-03 的輸出與 shape 觀察。
- Prompt comparison 結果。
- 常見錯誤與修正方式。
- 一段「Hugging Face 如何支援後續 VLM / VLA 實作」的說明。

## 銜接 Week04 LLaVA

完成 Week03 後，Week04 將進入 LLaVA。進入 Week04 前，應先能解釋：圖片如何被 processor 轉成模型輸入、視覺模型如何輸出 logits 或 visual features，以及為什麼真實 VLM 需要把視覺表示接到 LLM。