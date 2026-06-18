# Week03 Demo README

`demo/` 只負責快速展示 Hugging Face CLIP 的主要現象，回答「這個流程在做什麼」。若要逐步閱讀資料流、shape tracing（張量形狀追蹤）與中間值，請搭配 `../practice/coding/guided_demos/`。

## 安裝方式

請從 `learning/Week03_HuggingFace` 執行：

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：`openai/clip-vit-base-patch32`
- Source：Hugging Face Model Hub，OpenAI CLIP 模型頁面
- Download size：約數百 MB，依 Hugging Face 快取狀態而定
- Requires login：通常不需要
- License / Terms：請以 Hugging Face 模型頁面與 OpenAI CLIP 授權說明為準
- CPU supported：可以
- GPU recommended：選用；本週 demo 可用 CPU 執行
- Expected runtime：首次執行需下載模型；之後通常較快
- Common errors：網路下載失敗、SSL 問題、圖片路徑錯誤、缺少 `torch` 或 `transformers`

## Demo 檔案清單

| Demo | 對應概念 | 執行指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_processor_inputs.py` | `CLIPProcessor` 前處理 | `python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg` | `input_ids`、`attention_mask`、`pixel_values` shape | 哪些 tensor 屬於文字，哪些屬於圖片。 |
| `demo_02_clip_zero_shot_local.py` | CLIP zero-shot classification | `python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg` | `logits_per_image`、probabilities、top-k labels | labels 數量如何影響 shape 與 top-k。 |
| `demo_03_prompt_comparison.py` | Prompt sensitivity | `python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg` | 不同 prompt set 的 top-k 結果 | prompt 改寫是否改變 top-1 或 probability 分布。 |

## Demo 01: Processor Inputs

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

應觀察：

- `input_ids` shape，例如 `[num_texts, sequence_length]`
- `attention_mask` shape，例如 `[num_texts, sequence_length]`
- `pixel_values` shape，例如 `[num_images, channels, height, width]`
- labels 數量是否等於 `input_ids.shape[0]`

執行後應能回答：

- `CLIPProcessor` 做了哪些前處理？
- 為什麼文字與圖片會變成不同 shape 的 tensor？

## Demo 02: Zero-shot Classification

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
```

自訂 labels：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of a robot" "a photo of a classroom"
```

應觀察：

- `logits_per_image` shape 是否為 `[num_images, num_texts]`
- `softmax(dim=1)` 如何把 logits 轉成 labels 之間的相對分布
- `topk().indices.tolist()` 回傳的是 label 索引

執行後應能回答：

- 為什麼 top-k 不能超過 labels 數量？
- 為什麼 top-1 高不代表絕對真實機率？

## Demo 03: Prompt Comparison

```powershell
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

應觀察：

- `object_only`、`photo_template`、`scene_aware` 的 top-1 是否不同。
- probability 分布是否更集中或更分散。
- 更細的 prompt 是否一定更好。

執行後應能回答：

- prompt 改寫如何改變 text embedding 與相似度？
- 哪一組 prompt 最穩定，哪一組最容易造成誤判？

## 常見問題

### Image path does not exist

請確認 `--image` 指向本機存在的圖片。若 Week02 圖片不存在，請改用自己的圖片：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image demo/my_image.jpg
```

### 首次執行較慢

第一次使用 `openai/clip-vit-base-patch32` 時會下載 processor 與模型權重。這是正常現象。

### SSL 或網路問題

本週 demo 使用本機圖片，不需要下載圖片 URL；若遇到 SSL 或 Hugging Face 下載問題，請先確認網路與 Python 憑證環境。
