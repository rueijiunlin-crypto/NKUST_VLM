# Week03 Weekly Plan: Hugging Face CLIP 推論流程

## 本週目標

- 理解 Hugging Face Transformers（Hugging Face 轉換器工具庫）在 VLM（視覺語言模型）研究中的基本角色。
- 能清楚區分 `CLIPProcessor` 與 `CLIPModel` 的分工。
- 能執行本機圖片的 CLIP zero-shot image classification（零樣本影像分類）。
- 能解讀 `input_ids`、`attention_mask`、`pixel_values`、`logits_per_image` 與 `probabilities` 的 shape。
- 能解釋 `softmax(dim=1)[0]`、`topk().indices.tolist()` 與 labels 索引的關係。
- 能自行設計 prompt 實驗，記錄 top-1、top-k 與 probability 分布變化。

## 必學概念

- Hugging Face `from_pretrained()` 模型載入流程。
- Processor（前處理器）、tokenizer（詞元化器）、image preprocessing（影像前處理）。
- PyTorch tensor（PyTorch 張量）、batch dimension（批次維度）、sequence length（序列長度）。
- `logits_per_image` 與 `[num_images, num_texts]`。
- Softmax probability（softmax 相對機率）不是絕對真實機率。
- Top-k prediction（前 k 名預測）與 label index（標籤索引）。
- Prompt sensitivity（提示詞敏感性）。

## 建議學習順序

1. 閱讀 `README.md`，確認 Week03 主線與檔案用途。
2. 閱讀 `notes.md` 第 1-3 節，理解 `CLIPProcessor`、`CLIPModel` 與 tensor shape。
3. 執行 Demo 01，記錄 processor 輸出的 keys 與 shape。
4. 閱讀 `notes.md` 第 4-5 節，理解核心程式碼、softmax 與 top-k。
5. 執行 Demo 02，記錄 `logits_per_image`、probability 與 top-k 結果。
6. 閱讀 `notes.md` 第 6 節，理解 prompt 設計與 prompt sensitivity。
7. 執行 Demo 03，並完成 Coding Practice 中的自訂 prompt 實驗。
8. 完成 Concept Practice 與 Guided Code Reading 觀察表。
9. 在 `study_log.md` 記錄 demo、practice、prompt 實驗與未解問題。

## Demo 執行順序

請從 `learning/Week03_HuggingFace` 執行：

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

自訂 labels 範例：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "cat" "dog" "car"
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of two cats on a sofa" "a blurry photo of a cat"
```

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

## 任務清單

- [ ] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [ ] 安裝 demo / practice 所需依賴。
- [ ] 執行 Demo 01，記錄 `input_ids`、`attention_mask`、`pixel_values` shape。
- [ ] 執行 Demo 02，記錄 `logits_per_image`、`probabilities`、top-k 結果。
- [ ] 執行 Demo 03，觀察不同 prompt set 的 top-1 與 probability 分布。
- [ ] 完成 Concept Practice。
- [ ] 完成 Coding Practice 的 prompt 實驗設計與觀察紀錄。
- [ ] 在 `study_log.md` 記錄 demo 與 practice 結果。
- [ ] 更新 Notion 學習狀態。
- [ ] 進行 ChatGPT 驗收。

## 驗收條件

- [ ] 能解釋 `CLIPProcessor` 與 `CLIPModel` 的分工。
- [ ] 能看懂 `input_ids`、`attention_mask`、`pixel_values` 的 shape。
- [ ] 能解釋 `logits_per_image` 為什麼是 `[num_images, num_texts]`。
- [ ] 能解釋 `softmax(dim=1)[0]` 每一段的意義。
- [ ] 能解釋 `topk().indices.tolist()` 回傳的是 label 索引。
- [ ] 能說明 CLIP 的 softmax probability 是候選 labels 之間的相對分布。
- [ ] 能完成至少 3 組 prompt sets 的比較，並記錄 top-1、top-k、probability 分布。
- [ ] 能說明哪一組 prompt 較穩定、哪一組較容易造成誤判，以及可能原因。
- [ ] `study_log.md` 已記錄實際觀察與尚未解決的問題。

## 銜接 Week04 LLaVA

完成 Week03 後，Week04 將進入 LLaVA（大型語言與視覺助手）。本週的 processor、tensor input、model output、logits 與推論觀念，會成為理解 LLaVA 中 vision encoder（視覺編碼器）、projector（投影器）與 language model（語言模型）互動的基礎。
