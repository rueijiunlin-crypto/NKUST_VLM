# Week03 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
| --- | --- | --- | --- |
|  |  |  |  |

## 閱讀進度

- [ ] README.md
- [ ] weekly_plan.md
- [ ] notes.md
- [ ] demo/demo_README.md
- [ ] practice/README.md
- [ ] practice/concept/concept_practice.md
- [ ] practice/coding/README.md
- [ ] practice/coding/coding_practice.md

## Demo 執行結果

| Demo | 是否執行 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| `demo_01_processor_inputs.py` |  |  |  |
| `demo_02_clip_zero_shot_local.py` |  |  |  |
| `demo_03_prompt_comparison.py` |  |  |  |

## Tensor Shape 觀察

| 欄位 | 實際 shape | 我目前的理解 | 疑問 |
| --- | --- | --- | --- |
| `input_ids.shape` |  |  |  |
| `attention_mask.shape` |  |  |  |
| `pixel_values.shape` |  |  |  |
| `logits_per_image.shape` |  |  |  |
| `probabilities.shape` |  |  |  |

## Practice 結果摘要

| Practice | 是否完成 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| Concept Practice |  |  |  |
| Coding Practice: Processor Flow |  |  |  |
| Coding Practice: Logits and Top-k Flow |  |  |  |
| Coding Practice: Prompt Experiment |  |  |  |

## Prompt 實驗紀錄

| Prompt set | Top-1 label | Top-k labels | Probability 分布觀察 | 可能原因 |
| --- | --- | --- | --- | --- |
| object-only |  |  |  |  |
| photo-template |  |  |  |  |
| scene-aware |  |  |  |  |
| optional extra |  |  |  |  |

## 錯誤紀錄

| 錯誤訊息或現象 | 發生位置 | 修正方式 | 是否解決 |
| --- | --- | --- | --- |
|  |  |  |  |

## 本週理解摘要

### 我目前能解釋

-

### 我仍不理解

-

### 下週前要釐清

-

## 一分鐘回顧

請用自己的話總結 Week03 CLIP 推論流程。

```text
圖片 + labels/prompts
->
CLIPProcessor
->
input_ids / attention_mask / pixel_values
->
CLIPModel
->
logits_per_image
->
softmax(dim=1)[0]
->
top-k labels
```

## Notion 更新

- [ ] Learning Roadmap
- [ ] Experiment Log
- [ ] Weekly Review

## ChatGPT 驗收

- [ ] Pass
- [ ] Minor Revision
- [ ] Major Revision

## 下一步

-
