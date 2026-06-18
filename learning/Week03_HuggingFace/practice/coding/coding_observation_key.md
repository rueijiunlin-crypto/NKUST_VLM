# Week03 Coding Observation Key

> 請先完成 `coding_practice.md` 的觀察紀錄，再查看本檔。本檔提供觀察方向與理解線索，不應取代學生自己的執行紀錄。

## 1. Processor Tensor Shape

請優先檢查下列欄位，而不是只看 top-1 結果。

| 欄位 | 典型 shape | 觀察方向 |
| --- | --- | --- |
| `input_ids.shape` | `[num_texts, sequence_length]` | 第一個維度應等於 labels/prompts 數量。 |
| `attention_mask.shape` | `[num_texts, sequence_length]` | 通常與 `input_ids` 相同，用來標示有效 token 與 padding。 |
| `pixel_values.shape` | `[num_images, channels, height, width]` | CLIP ViT-B/32 常見為 `[1, 3, 224, 224]`。 |

觀察重點：

- `sequence_length` 可能因 tokenizer 與 padding 設定而改變。
- `attention_mask` 不是文字內容本身，而是告訴模型哪些位置要注意。
- `pixel_values` 已經不是原始圖片檔，而是 resize 與 normalize 後的 tensor。

## 2. `logits_per_image` 與 Labels 數量

| 欄位 | 觀察方向 |
| --- | --- |
| `logits_per_image.shape` | 應接近 `[num_images, num_texts]`。 |
| labels 數量 | 應對應 `logits_per_image.shape[1]`。 |
| 圖片數量 | 應對應 `logits_per_image.shape[0]`。 |

如果輸入 1 張圖片與 5 個 labels，`logits_per_image` 應是 `[1, 5]`。這代表同一張圖片分別對 5 個文字 prompt 產生相似度分數。

## 3. Softmax 與 Probability

`softmax(dim=1)` 是沿著 labels/texts 維度正規化。對 `[1, 5]` 來說，它會讓同一張圖片對 5 個 labels 的分數形成相對分布。

請觀察：

| 欄位 | 觀察方向 |
| --- | --- |
| `probabilities.shape` | 使用 `[0]` 後通常是 `[num_texts]`。 |
| probability 加總 | 同一張圖片的 labels probability 通常加總約為 1。 |
| top-1 probability | 高分只代表目前候選 labels 中相對最高。 |

提醒：softmax probability 不是絕對真實機率。候選 labels 改變時，probability 會重新分配。

## 4. Top-k 與 Labels 數量

觀察欄位：

| 欄位 | 觀察方向 |
| --- | --- |
| `top_k` | 使用者要求印出的前 k 名。 |
| `len(labels)` | 候選 labels 數量。 |
| `min(args.top_k, len(labels))` | 避免 top-k 超過 labels 數量。 |
| `topk().indices.tolist()` | 回傳前 k 名在 probability vector 裡的位置索引。 |

如果 labels 是：

```python
labels = ["cat", "dog", "car"]
```

而 `topk()` 回傳 `[0, 1]`，代表前兩名對應 `labels[0]` 與 `labels[1]`，也就是 `cat` 與 `dog`。索引不是 label 名稱本身。

## 5. Prompt Set 觀察

請比較至少三組 prompt set：

| Prompt set | 觀察方向 |
| --- | --- |
| object-only | 短 label 是否已足夠讓 CLIP 判斷主要物件。 |
| photo-template | `a photo of ...` 是否讓結果更穩定。 |
| scene-aware | 更細的場景描述是否改善結果，或因描述太細造成誤判。 |

請特別記錄：

- 不同 prompt set 的 top-1 是否改變。
- 不同 prompt set 的 probability 分布是否更集中或更分散。
- top-1 改變時，是因為正確描述更精準，還是候選 labels 競爭關係改變。
- 如果候選 labels 都不理想，CLIP 仍會在其中選出相對最像的一個。

## 6. 常見誤解修正

- `CLIPProcessor` 不負責判斷圖片內容，它只做文字與圖片前處理。
- `CLIPModel` 輸出的 logits 不是機率，需要經過 softmax 才變成相對分布。
- `softmax(dim=1)` 是在同一張圖片的 labels 之間比較，不是在不同圖片之間比較。
- `[0]` 是取出 batch 中第 1 張圖片的結果。
- `topk()` 回傳索引，必須再用 `labels[index]` 找回文字 label。
- Top-1 高不代表模型完整理解圖片，只代表在目前候選 prompts 中相對最相似。
