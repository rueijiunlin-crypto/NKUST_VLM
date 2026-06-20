# Week03 Coding Practice: Guided Code Reading Mode

本週 Coding Practice 採用 Guided Code Reading Mode（引導式程式閱讀模式）。重點不是從零實作 CLIP，而是透過可執行程式觀察 Hugging Face CLIP 推論流程、tensor shape、softmax/top-k 與 prompt 改寫效果。

請從 `learning/Week03_HuggingFace` 執行指令，並把觀察記錄在本檔與 `../../study_log.md`。本檔不得填入參考答案，只記錄你的實際觀察與問題。

## 練習清單

| 練習 | 模式 | 對應檔案 | 學習目標 |
| --- | --- | --- | --- |
| Processor Flow | Guided Code Reading | `guided_demos/guided_01_processor_flow.py` | 觀察 `input_ids`、`attention_mask`、`pixel_values`。 |
| Logits and Top-k Flow | Guided Code Reading | `guided_demos/guided_02_logits_topk_flow.py` | 觀察 `logits_per_image`、`softmax(dim=1)`、`topk()`。 |
| Prompt Effect Flow | Guided Code Reading | `guided_demos/guided_03_prompt_effect_flow.py` | 比較不同 prompt set 對 top-1 與 probability 分布的影響。 |
| 自訂 Prompt 實驗 | Guided Code Reading | `demo/demo_02_clip_zero_shot_local.py` 或 `demo/demo_03_prompt_comparison.py` | 自行設計 prompt sets 並分析穩定性。 |

## 執行方式

安裝依賴：

```powershell
python -m pip install -r practice/coding/requirements.txt
python -m pip install -r demo/requirements.txt
```

執行 Guided Demos：

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_logits_topk_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_03_prompt_effect_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若 Week02 圖片不存在，可以使用自己的本機圖片：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image demo/my_image.jpg
```

## 1. Processor Shape 觀察

請執行 Demo 01 或 guided demo 01，記錄輸出：

| Key | 實際 shape | 這個 shape 的意義 | 疑問 |
| --- | --- | --- | --- |
| `input_ids.shape` | `[num_texts, sequence_length]` | 第一個維度應等於 labels/prompts 數量。 | 待填 |
| `attention_mask.shape` | `[num_texts, sequence_length]` | 通常與 `input_ids` 相同，用來標示有效 token 與 padding。 | 待填 |
| `pixel_values.shape` | `[num_images, channels, height, width]` | CLIP ViT-B/32 常見為 `[1, 3, 224, 224]`。 | 待填 |

引導問題：

- `input_ids.shape[0]` 是否等於 labels 數量？
- `attention_mask` 為什麼和 `input_ids` shape 相同？
- `pixel_values` 的 channels 為什麼通常是 3？

## 2. Logits、Softmax 與 Top-k 觀察

請執行 Demo 02 或 guided demo 02，記錄：

| Labels 數量 | `logits_per_image.shape` | `probabilities.shape` | `top_k` | top-k 是否被限制在 labels 數量內 |
| ---: | --- | --- | ---: | --- |
| 5 | (1,5) | (5,) | 3 | 是 |

請記錄 labels 與 probabilities 的對應：

| Label index | Label / prompt | Probability |
| ---: | --- | ---: |
| 0 | a photo of a cat | 0.4922 |
| 1 | a photo of a dog | 0.0025 |
| 2 | a photo of a pink sofa | 0.4980 |
| 3 | a photo of a robot | 0.0068 |
| 4 | a photo of a laboratory | 0.0005 |

引導問題：

- `softmax(dim=1)[0]` 中的 `dim=1` 與 `[0]` 各代表什麼？
- `topk().indices.tolist()` 回傳的 index 如何對應到 label？
- Top-1 高是否代表模型對圖片有絕對信心？

## 3. 自訂 Prompt 設計實驗

請自選一張圖片，或使用 Week02 demo 圖片。你需要設計至少 3 組 label/prompt sets，並比較結果。

至少包含：

- object-only labels，例如 `cat`, `dog`, `sofa`
- `a photo of ...` template labels，例如 `a photo of a cat`
- scene-aware descriptions，例如 `a photo of two cats on a pink sofa`

可使用 Demo 02 分別執行不同 labels：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "cat" "dog" "sofa"
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of a dog" "a photo of a sofa"
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of two cats on a pink sofa" "a photo of a dog on a sofa" "a photo of an empty sofa"
```

請填寫你的 prompt sets：

| Prompt set | Labels / prompts | 設計理由 |
| --- | --- | --- |
| object-only | 待填 | 待填 |
| photo-template | 待填 | 待填 |
| scene-aware | 待填 | 待填 |
| optional extra | 待填 | 待填 |

## 4. Prompt 實驗結果紀錄

請記錄每組 prompt set 的 top-1、top-k 與 probability 分布：

| Prompt set | Top-1 label | Top-1 probability | Top-k labels | Probability 分布觀察 |
| --- | --- | ---: | --- | --- |
| object-only | 待填 | 待填 | 待填 | 待填 |
| photo-template | 待填 | 待填 | 待填 | 待填 |
| scene-aware | 待填 | 待填 | 待填 | 待填 |
| optional extra | 待填 | 待填 | 待填 | 待填 |

請回答：

1. prompt 改寫是否影響 top-1？如果有，可能原因是什麼？
2. 哪一組 prompt 的 probability 分布最集中？這是否一定代表最好？
3. 哪一組 prompt 最穩定？哪一組最容易造成誤判？
4. 若候選 labels 缺少正確描述，CLIP 會如何選擇？

學生觀察：

-

## 錯誤紀錄欄位

| 錯誤訊息或現象 | 發生在哪個檔案或指令 | 可能原因 | 修正方式 |
| --- | --- | --- | --- |
| 待填 | 待填 | 待填 | 待填 |

## 自我檢查項目

- [ ] 我能說明 `input_ids.shape`、`attention_mask.shape`、`pixel_values.shape`。
- [ ] 我能說明 labels 數量如何影響 `logits_per_image.shape`。
- [ ] 我能說明 `softmax(dim=1)[0]`。
- [ ] 我能說明 `topk()` 回傳的是 label index。
- [ ] 我完成至少 3 組 prompt sets 的比較。
- [ ] 我在 `../../study_log.md` 記錄了 prompt 實驗結果與疑問。
