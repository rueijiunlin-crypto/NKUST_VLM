# Week03 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
| --- | --- | --- | --- |
| 待填 | 待填 | 待填 | 待填 |

## 閱讀進度

- [✅] README.md
- [✅] weekly_plan.md
- [✅] notes.md
- [✅] demo/demo_README.md
- [ ] practice/README.md
- [ ] practice/concept/concept_practice.md
- [ ] practice/coding/README.md
- [ ] practice/coding/coding_practice.md

## Demo 執行結果

| Demo | 是否執行 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| `demo_01_processor_inputs.py` | 完成 | 無 | 無 |
| `demo_02_clip_zero_shot_local.py` | 完成 | 本次圖片在 CLIP zero-shot 推論中，最高分為「a photo of a pink sofa」，機率為 0.4980；第二高為「a photo of a cat」，機率為 0.4922。兩者差距極小，表示模型同時捕捉到圖片中的沙發與貓特徵。若圖片內容確實包含貓與粉紅色沙發，這是合理結果，也說明 CLIP 的 zero-shot 結果會受到候選 prompts 的描述方式影響。 | 無 |
| `demo_03_prompt_comparison.py` | 完成 | 無 | 無 |

## Tensor Shape 觀察

| 欄位 | 實際 shape | 我目前的理解 | 疑問 |
| --- | --- | --- | --- |
| `input_ids.shape` | (5,8) | 5 個文字 prompts，每個 prompt 整理成 8 個 token 長度 | 待填 |
| `attention_mask.shape` | (5,8) | 這個 shape 跟 input_ids 一樣，代表每個 token 位置是否有效，並且告訴模型，這個位置要不要看 | 待填 |
| `pixel_values.shape` | (1,3,224,224) | 1 張圖片、3 個 RGB 色彩通道、高度 224、寬度 224，這表示圖片已經被 CLIPProcessor 處理成 CLIP 模型需要的固定格式。 | 待填 |
| `logits_per_image.shape` | (1,5) | 1 張圖片、對 5 個文字 prompts 各有 1 個相似度分數 | 待填 |
| `probabilities.shape` | (5,) | 第 0 張圖片對 5 個 labels 的機率分布 | 待填 |

## Practice 結果摘要

| Practice | 是否完成 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| Concept Practice | 待填 | 待填 | 待填 |
| Coding Practice: Processor Flow | 待填 | 待填 | 待填 |
| Coding Practice: Logits and Top-k Flow | 待填 | 待填 | 待填 |
| Coding Practice: Prompt Experiment | 待填 | 待填 | 待填 |

## Prompt 實驗紀錄

| Prompt set | Top-1 label | Top-k labels | Probability 分布觀察 | 可能原因 |
| --- | --- | --- | --- | --- |
| object-only | sofa | sofa、cat、laboratory | 分布集中在 sofa，sofa=0.7193，cat=0.2505，其他類別很低 | 單字 prompt 缺少語境，模型可能更容易受到畫面中面積較大或視覺特徵明顯的沙發影響 |

| photo-template | a photo of a cat | a photo of a cat、a photo of a sofa、a photo of a robot | 分布轉向 cat，cat=0.7964，sofa=0.1877，其他類別很低 | `a photo of ...` 比單字更接近 CLIP 訓練時常見的自然語言描述，因此文字與圖片特徵更容易對齊 |

| scene-aware | a photo of two cats on a pink sofa | a photo of two cats on a pink sofa、a photo of a pink sofa without animals、a photo of a dog on a sofa | 分布高度集中，第一名=0.9993，其他候選幾乎為 0 | prompt 同時描述主要物件與場景，例如 cats 與 pink sofa，因此比單一物件描述更貼近整張圖片內容 |
| optional extra | 待填 | 待填 | 待填 | 待填 |

## 錯誤紀錄

| 錯誤訊息或現象 | 發生位置 | 修正方式 | 是否解決 |
| --- | --- | --- | --- |
| 待填 | 待填 | 待填 | 待填 |

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
