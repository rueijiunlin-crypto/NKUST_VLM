# Week03 Demo README

本資料夾展示如何使用 Hugging Face `transformers` 執行真實 CLIP zero-shot image classification。

## 安裝依賴

請在 `learning/Week03_HuggingFace/` 下執行：

```powershell
python -m pip install -r demo/requirements.txt
```

## Demo 01：觀察 Processor 輸入

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- `input_ids` shape
- `attention_mask` shape
- `pixel_values` shape
- 圖片與文字如何變成 tensor

## Demo 02：本地圖片 Zero-shot Classification

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- `logits_per_image` shape
- softmax probability
- top-k prediction
- 候選 labels 如何影響結果

## Demo 03：Prompt Comparison

```powershell
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- 同一張圖片在不同 prompt set 下的結果差異
- 為什麼 prompt 設計會影響 zero-shot classification

## 常見問題

### Image path does not exist

請確認目前終端機所在位置，以及 `--image` 後面的相對路徑是否正確。

### 第一次執行很慢

第一次執行會下載 `openai/clip-vit-base-patch32` 權重與 processor 檔案，時間取決於網路速度。

### SSL 或外部圖片下載錯誤

本週 Demo 預設使用本地圖片路徑，不依賴外部圖片 URL。若遇到 SSL 問題，請改用本地圖片。