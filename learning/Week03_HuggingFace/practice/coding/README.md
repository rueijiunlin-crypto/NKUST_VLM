# Week03 Coding Practice README

Week03 Coding Practice 採用 Guided Code Reading Mode（引導式程式閱讀模式）。請透過完整可執行程式理解 CLIP 推論流程、tensor shape、softmax/top-k 與 prompt 實驗，而不是從零補 TODO。

## 結構說明

| 路徑 | 用途 |
| --- | --- |
| `guided_demos/guided_01_processor_flow.py` | 觀察 `CLIPProcessor` 輸出的文字與圖片 tensor。 |
| `guided_demos/guided_02_logits_topk_flow.py` | 觀察 `logits_per_image`、`softmax(dim=1)` 與 `topk()`。 |
| `guided_demos/guided_03_prompt_effect_flow.py` | 比較不同 prompt set 的 top-1 與 probability 分布。 |
| `coding_practice.md` | 學生觀察與 prompt 實驗紀錄表。 |
| `coding_observation_key.md` | 觀察方向與理解說明。 |
| `requirements.txt` | 本練習需要的 Python 套件。 |

## 安裝方式

請從 `learning/Week03_HuggingFace` 執行：

```powershell
python -m pip install -r practice/coding/requirements.txt
```

Demo 與 guided demos 使用相同主要依賴；必要時也可安裝：

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
- GPU recommended：選用；本週練習可用 CPU 執行
- Expected runtime：首次執行需下載模型；之後通常較快
- Common errors：網路下載失敗、SSL 問題、圖片路徑錯誤、缺少 `torch` 或 `transformers`

## 執行指令

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_logits_topk_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_03_prompt_effect_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若 Week02 圖片不存在，請改用自己的圖片：

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image demo/my_image.jpg
```

## 觀察重點

- `input_ids.shape`
- `attention_mask.shape`
- `pixel_values.shape`
- `logits_per_image.shape`
- `probabilities.shape`
- labels 數量與 `logits_per_image.shape[1]` 的關係
- `top_k` 與 labels 數量的關係
- 不同 prompt set 的 top-1 是否改變
- 不同 prompt set 的 probability 分布是否更集中或更分散

請把觀察記錄到 `coding_practice.md`，再整理到 `../../study_log.md`。
