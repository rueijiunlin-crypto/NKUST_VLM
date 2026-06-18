# Week03 Hugging Face CLIP 推論流程

## 本週定位

Week03 延續 Week02 CLIP（對比式圖文預訓練）的概念，改用 Hugging Face Transformers（Hugging Face 轉換器工具庫）執行真實 CLIP zero-shot image classification（零樣本影像分類）demo。

本週重點不是只把 demo 跑起來，而是要能說清楚：

- `CLIPProcessor` 如何把圖片與文字 labels 轉成 tensor（張量）。
- `CLIPModel` 如何輸出 `logits_per_image`。
- `input_ids`、`attention_mask`、`pixel_values` 的 shape 代表什麼。
- `softmax(dim=1)[0]` 每一段的意義。
- `topk().indices.tolist()` 為什麼回傳 label 索引。
- prompt 改寫如何影響 CLIP 的 zero-shot 結果。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 本週學習順序、demo 執行順序、practice 任務與驗收條件。 |
| `notes.md` | Hugging Face CLIP 推論流程、tensor shape、softmax/top-k 與 prompt 實驗教材。 |
| `study_log.md` | 學生實際執行 demo、practice、prompt 實驗與疑問紀錄。 |
| `demo/` | 快速展示 CLIPProcessor、zero-shot classification 與 prompt comparison。 |
| `practice/` | Concept Practice 與 Guided Code Reading Mode 的觀察任務。 |

## 建議使用方式

1. 閱讀 `weekly_plan.md`，確認本週任務與驗收條件。
2. 閱讀 `notes.md` 第 1-4 節，先理解 processor、model、tensor shape 與核心程式碼。
3. 執行 `demo/demo_01_processor_inputs.py`，觀察 processor 輸出的 tensor keys 與 shape。
4. 執行 `demo/demo_02_clip_zero_shot_local.py`，觀察 `logits_per_image`、softmax probability 與 top-k。
5. 執行 `demo/demo_03_prompt_comparison.py`，比較不同 prompt set 的 top-1 與 probability 分布。
6. 完成 `practice/concept/concept_practice.md` 與 `practice/coding/coding_practice.md`。
7. 將觀察、錯誤與問題記錄到 `study_log.md`。

## Demo 主線

請從 `learning/Week03_HuggingFace` 執行：

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若 Week02 圖片不存在，可改用自己的本機圖片：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image demo/my_image.jpg
```

## 與 VLM/VLA 碩士研究的關聯

Hugging Face 是後續 VLM（視覺語言模型）與 VLA（視覺語言動作模型）研究常用的模型載入與推論工具鏈。Week03 先建立可重現的 CLIP 推論觀念，之後銜接 LLaVA（大型語言與視覺助手）、VLM Architecture（視覺語言模型架構）與機器人系統整合時，才不會只停留在「呼叫模型」而看不懂資料流。

## 本週完成後應具備的能力

- 能解釋 `CLIPProcessor` 與 `CLIPModel` 的分工。
- 能讀懂 `input_ids`、`attention_mask`、`pixel_values` 的 shape。
- 能解釋 `logits_per_image` 為什麼是 `[num_images, num_texts]`。
- 能解釋 `softmax(dim=1)[0]` 與候選 labels 的關係。
- 能用 `topk().indices.tolist()` 找出前 k 名 label 的索引。
- 能設計至少 3 組 prompt sets，觀察 prompt 改寫是否影響 CLIP 結果。
