# Week03 Hugging Face

## 本週定位

Week03 將 Week02 的 CLIP 概念對應到 Hugging Face 實作流程。重點不是重新學 CLIP 理論，而是理解真實模型如何被下載、載入、前處理、推論與解讀輸出。

本週核心問題：

> Week02 學到的 image embedding、text embedding、similarity、softmax 與 zero-shot classification，在 Hugging Face 程式中分別對應到哪些物件與輸出？

## 學習目標

- 理解 Hugging Face 在 VLM / VLA 碩士研究中的角色。
- 能使用 `transformers` 載入 `CLIPProcessor` 與 `CLIPModel`。
- 能用本地圖片與自訂文字 labels 完成 zero-shot image classification（零樣本影像分類）。
- 能解釋 processor、input tensors、logits、probability 與 top-k prediction。
- 能說明模型下載、快取、硬體需求與常見錯誤。
- 能把 Hugging Face 推論流程銜接到後續 VLM、ROS2 或 Isaac Sim 應用。

## 必懂概念

- Hugging Face Transformers（模型載入與推論工具庫）
- Processor（處理器）：負責將圖片與文字轉成模型可接受的 tensor
- PyTorch（深度學習框架）推論
- `CLIPModel` 與 `CLIPProcessor`
- `logits_per_image`、`softmax`、probability 與 top-k
- 本地圖片路徑、模型快取與網路下載
- GPU / CPU 推論差異

## 檔案導覽

| 檔案或資料夾 | 用途 |
| ------------ | ---- |
| `weekly_plan.md` | Week03 任務、Demo 順序與驗收條件。 |
| `notes.md` | Hugging Face 與 CLIP 推論正式教材。 |
| `study_log.md` | 學生學習紀錄與驗收狀態。 |
| `demo/` | Hugging Face CLIP 推論 Demo。 |
| `practice/` | 觀念練習與程式閱讀練習。 |

## 建議學習順序

1. 閱讀 `notes.md` Level 1-3，理解 Hugging Face、Processor 與 Model 的分工。
2. 執行 `demo_01_processor_inputs.py`，觀察文字與圖片被轉成哪些 tensor。
3. 執行 `demo_02_clip_zero_shot_local.py`，完成本地圖片 zero-shot classification。
4. 執行 `demo_03_prompt_comparison.py`，觀察 prompt 改寫如何影響結果。
5. 完成 `practice/` 中的觀念與程式閱讀練習。
6. 更新 `study_log.md`，完成 ChatGPT 驗收。

## 本週產出

- 一份可執行的本地圖片與自訂 labels zero-shot CLIP 推論結果。
- 一份 prompt 設計對結果影響的比較觀察紀錄。
- 一段說明：Hugging Face 如何把 Week02 的 CLIP 概念轉成實際程式流程。
