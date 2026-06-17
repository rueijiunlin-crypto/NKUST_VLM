# Week03 Weekly Plan: Hugging Face（模型平台）CLIP（對比式圖文預訓練）推論

## 本週目標

- 說明 Hugging Face 在 VLM（視覺語言模型）/ VLA（視覺語言動作模型）學習中的角色。
- 分辨 `CLIPProcessor` 與 `CLIPModel` 的職責。
- 能用本地圖片與自訂 labels（候選標籤）執行真實 CLIP zero-shot classification（零樣本分類）。
- 能解釋 `logits_per_image`、softmax probability（softmax 機率分布）與 top-k prediction（前 k 名預測）。
- 能說明 prompt（提示詞）設計如何影響 zero-shot 結果。
- 能記錄模型下載、快取、路徑與 SSL（安全通訊憑證）/ network（網路）相關問題。

## 必學概念

- Hugging Face Transformers（模型載入與推論工具庫）
- Processor（處理器）與 tokenizer（詞元化器）/ image preprocessing（影像前處理）
- PyTorch tensor（PyTorch 張量）與 batch dimension（批次維度）
- `CLIPModel.from_pretrained()` 與 `CLIPProcessor.from_pretrained()`
- `logits_per_image` 與 `logits_per_text`
- Softmax probability（softmax 機率分布）與 top-k prediction（前 k 名預測）
- Prompt engineering（提示詞工程）與 prompt sensitivity（提示詞敏感性）

## 建議 7 天學習順序

1. Day 1：閱讀 `README.md` 與 `notes.md` Level 1-2，畫出 Hugging Face CLIP 推論流程。
2. Day 2：閱讀 Level 3 並執行 Demo 01，記錄 processor（前處理器）輸出的 tensor keys（張量欄位）與 shape（形狀）。
3. Day 3：閱讀 Level 4 並執行 Demo 02，使用本地圖片完成 zero-shot classification（零樣本分類）。
4. Day 4：閱讀 Level 5 並執行 Demo 03，比較不同 prompt（提示詞）對結果的影響。
5. Day 5：閱讀 Level 6-7，整理 logits（未正規化分數）、probability（機率分布）、top-k（前 k 名）與常見錯誤。
6. Day 6：完成 Concept Practice（觀念練習）與 Guided Code Reading（引導式程式閱讀），記錄中間值與疑問。
7. Day 7：整理 `study_log.md` 與 Notion，完成本週摘要與驗收。

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

若 `../Week02_CLIP/demo/000000039769.jpg` 不存在，請改用自己的本地圖片路徑，例如 `--image demo/my_image.jpg`；不要改用外部圖片 URL，避免 SSL 或 network 問題。

若要測試自訂 labels，可在 Demo 02 加上：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of a robot" "a photo of a classroom"
```

## Practice 順序

1. [Practice Overview（練習總覽）](./practice/README.md)
2. [Concept Practice（觀念練習）](./practice/concept/concept_practice.md)
3. [Coding Practice（程式練習）](./practice/coding/coding_practice.md)
4. [Guided Demos（引導式示範程式）](./practice/coding/guided_demos/)

參考答案請完成練習後再查看：

- [Concept Answer Key（觀念參考答案）](./practice/concept/concept_answer_key.md)
- [Coding Observation Key（程式觀察參考方向）](./practice/coding/coding_observation_key.md)

## Guided Code Reading Mode

本週採 Guided Code Reading Mode（引導式程式閱讀模式）。`demo/` 用來快速觀察概念現象，`practice/coding/guided_demos/` 用來閱讀更完整的資料流、shape tracing（張量形狀追蹤）與中間值說明。本週不要求從零實作 Hugging Face 推論程式。

## 任務清單

- [ ] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [ ] 安裝 Week03 demo dependencies（Demo 依賴套件）。
- [ ] 執行 Demo 01，記錄 processor（前處理器）輸出。
- [ ] 執行 Demo 02，完成本地圖片 zero-shot classification（零樣本分類）。
- [ ] 執行 Demo 03，觀察 prompt（提示詞）改寫對結果的影響。
- [ ] 完成 Concept Practice（觀念練習）。
- [ ] 完成 Guided Code Reading（引導式程式閱讀）。
- [ ] 更新 `study_log.md` 與 Notion。
- [ ] 進行 ChatGPT 驗收。

## 驗收條件

- [ ] 能說明 Hugging Face 在本週任務中的角色。
- [ ] 能說明 `CLIPProcessor` 與 `CLIPModel` 的分工。
- [ ] 能使用本地圖片執行真實 CLIP zero-shot 推論。
- [ ] 能解釋 `logits_per_image` 的 shape（形狀）與意義。
- [ ] 能說明 softmax probability 是候選 labels 之間的相對分布。
- [ ] 能說明 prompt（提示詞）改寫為什麼會影響結果。
- [ ] 能記錄並處理常見問題，例如模型下載、圖片路徑或 SSL 錯誤。
- [ ] 能說明 Week03 如何銜接 Week04 LLaVA。

## Notion 紀錄項目

- Hugging Face CLIP 推論流程圖。
- Processor / Model / Output（輸出）對照表。
- Demo 01-03 的輸出與 shape 觀察。
- Prompt comparison（提示詞比較）結果。
- 常見錯誤與修正方式。
- 一段「Hugging Face 如何支援後續 VLM / VLA 實作」的說明。

## 銜接 Week04 LLaVA

完成 Week03 後，Week04 將進入 LLaVA（大型語言與視覺助手）。進入 Week04 前，應先能解釋：圖片如何被 processor 轉成模型輸入、視覺模型如何輸出 logits 或 visual features（視覺特徵），以及為什麼真實 VLM 需要把視覺表示接到 LLM（大型語言模型）。
