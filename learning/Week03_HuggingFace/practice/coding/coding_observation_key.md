# Week03 Coding Observation Key

> 請先完成 `coding_practice.md` 的觀察紀錄，再查看本觀察參考方向。本檔只提供理解線索，不代表你的實際執行結果。

## 1. Processor 輸出應如何理解？

`CLIPProcessor` 會同時處理文字與圖片：

| Key | 常見 shape | 來源 | 觀察方向 |
| --- | ---------- | ---- | -------- |
| `input_ids` | `(labels 數量, token 長度)` | 文字 | 每個 prompt 會被 tokenizer（詞元化器）轉成 token ID。 |
| `attention_mask` | `(labels 數量, token 長度)` | 文字 | 標示哪些 token 是有效內容，哪些是 padding（補齊）。 |
| `pixel_values` | `(圖片數量, 3, 224, 224)` | 圖片 | 圖片會被 resize（調整尺寸）、normalize（正規化）並轉成模型輸入張量。 |

重點不是背 shape，而是能說明「文字走文字前處理，圖片走圖片前處理，最後一起交給 `CLIPModel`」。

## 2. Labels 數量如何影響 `logits_per_image`？

若輸入 1 張圖片與 5 個 labels，`logits_per_image` 通常是 `(1, 5)`。第二個維度會跟候選文字數量一致，因為 CLIP 會比較每張圖片與每個文字 prompt 的相似度。

因此，當你把 labels 改成 3 個或 8 個時，`logits_per_image` 的第二個維度也應跟著改變。

## 3. Top-k 如何從 probability 取得？

Demo 02 的流程是：

```text
logits_per_image
→ softmax(dim=1)
→ probabilities
→ topk(k)
→ top-k labels
```

`top-k` 不是模型另外輸出的欄位，而是從 probability 排序後挑出前 k 個候選 labels。若候選 labels 改變，probability 與 top-k 也可能改變。

## 4. Prompt 改寫為什麼會改變結果？

CLIP 的文字端會把整句 prompt 轉成 text embedding（文字嵌入向量）。`cat`、`a photo of a cat`、`a photo of two cats on a pink sofa` 對模型而言不是完全相同的文字輸入，因此與圖片 embedding（圖片嵌入向量）的相似度可能不同。

觀察 Demo 03 時，請特別比較：

- 簡短 object label 是否容易忽略場景。
- photo template 是否比單字更接近 CLIP 預訓練資料的描述方式。
- scene-aware prompt 是否更能描述整張圖片，而不是只描述單一物件。

## 5. 常見誤解

- Softmax probability 不是現實世界的絕對真實機率，而是在目前候選 labels 之間的相對分布。
- `CLIPProcessor` 不會判斷圖片內容；它只負責前處理。
- `CLIPModel` 的輸出需要搭配 labels 與 prompt 設計解讀，不能只看最大值就忽略候選集合。
- 本週程式是推論與流程理解，不是 fine-tuning（微調）或模型訓練。
