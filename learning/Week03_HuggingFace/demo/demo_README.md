# Week03 Demo README（示範程式總覽）

本資料夾展示如何使用 Hugging Face（模型平台）`transformers` 執行真實 CLIP（對比式圖文預訓練）zero-shot image classification（零樣本影像分類）。

`demo/` 的責任是快速展示概念現象，也就是回答「這個流程在做什麼」。若要閱讀更完整的 shape tracing（張量形狀追蹤）、中間值與 step-by-step comments（逐步註解），請進入 `../practice/coding/guided_demos/`。

## 安裝依賴

請在 `learning/Week03_HuggingFace/` 下執行：

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset（模型 / 資料集）：`openai/clip-vit-base-patch32`
- Source（來源）：Hugging Face Model Hub（模型中心）上的 OpenAI CLIP 模型頁面
- Download size（下載大小）：約數百 MB，依 Hugging Face 快取與版本而定。
- Requires login（是否需要登入）：通常不需要。
- License / Terms（授權 / 條款）：請以 Hugging Face 模型頁面與 OpenAI CLIP 原始授權說明為準。
- CPU supported（是否支援 CPU）：支援，但第一次載入與推論可能較慢。
- GPU recommended（是否建議 GPU）：非必要；若有 CUDA GPU（NVIDIA 平行運算 GPU）可加速。
- Expected runtime（預期執行時間）：第一次執行需下載權重，之後通常數秒到數十秒內完成，依網路與硬體而定。
- Common errors（常見錯誤）：模型下載失敗、SSL（安全通訊憑證）錯誤、圖片路徑錯誤、套件未安裝。

若 Week02 範例圖片不存在，請改用自己的本地圖片路徑，例如 `--image demo/my_image.jpg`。本週 Demo 不依賴外部圖片 URL（網址），避免 SSL 或 network（網路）問題。

## Demo 檔案清單

### `demo_01_processor_inputs.py`

- 對應概念：Processor（前處理器）輸出。
- 執行指令：`python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg`
- 預期輸出：`input_ids`、`attention_mask`、`pixel_values` 的 shape（形狀）。
- 執行後應回答：哪些 tensor 來自文字？哪些 tensor 來自圖片？

### `demo_02_clip_zero_shot_local.py`

- 對應概念：Zero-shot classification（零樣本分類）。
- 執行指令：`python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg`
- 預期輸出：`logits_per_image`、softmax probability（softmax 機率分布）、top-k prediction（前 k 名預測）。
- 執行後應回答：labels（候選標籤）數量如何影響輸出 shape？

### `demo_03_prompt_comparison.py`

- 對應概念：Prompt sensitivity（提示詞敏感性）。
- 執行指令：`python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg`
- 預期輸出：不同 prompt set（提示詞集合）的 Top-1 與 probability。
- 執行後應回答：為什麼 prompt 改寫會影響結果？

## Demo 01：觀察 Processor 輸入

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- `input_ids` shape（形狀）
- `attention_mask` shape
- `pixel_values` shape
- 圖片與文字如何變成 tensor（張量）

## Demo 02：本地圖片 Zero-shot Classification（零樣本分類）

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
```

也可以使用自訂 labels：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of a robot" "a photo of a classroom"
```

觀察重點：

- `logits_per_image` shape
- softmax probability（softmax 機率分布）
- top-k prediction（前 k 名預測）
- 候選 labels 如何影響結果

## Demo 03：Prompt Comparison（提示詞比較）

```powershell
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- 同一張圖片在不同 prompt set（提示詞集合）下的結果差異
- 為什麼 prompt 設計會影響 zero-shot classification（零樣本分類）

## 常見問題

### Image path does not exist（圖片路徑不存在）

請確認目前終端機所在位置，以及 `--image` 後面的相對路徑是否正確。若 Week02 範例圖片不存在，請改用自己的本地圖片路徑，例如 `--image demo/my_image.jpg`。

### 第一次執行很慢

第一次執行會下載 `openai/clip-vit-base-patch32` 權重與 processor（前處理器）檔案，時間取決於網路速度。

### SSL 或外部圖片下載錯誤

本週 Demo 預設使用本地圖片路徑，不依賴外部圖片 URL。若遇到 SSL 問題，請改用本地圖片。
