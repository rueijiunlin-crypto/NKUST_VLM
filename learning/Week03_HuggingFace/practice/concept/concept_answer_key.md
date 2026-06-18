# Week03 Concept Answer Key

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

本檔提供理解方向，不會也不應覆蓋學生自己的觀察紀錄。

## 1. Token、Token ID、Tensor、Embedding Vector

- token（詞元）：文字被 tokenizer 切分後的單位，可能是一個完整單字，也可能是單字的一部分。
- token id（詞元識別碼）：token 在 vocabulary（詞彙表）中的整數編號。模型不能直接讀文字，所以先讀 token id。
- tensor（張量）：模型輸入與輸出的多維數值資料，例如 `input_ids` 是二維 tensor，`pixel_values` 是四維 tensor。
- embedding vector（嵌入向量）：模型內部用來表示語意或影像特徵的向量。token id 只是索引，embedding vector 才是模型用來計算相似度的表示。

常見誤解：`input_ids` 裡的整數不是語意向量本身，它們只是查表用的編號。

## 2. Padding 與 Attention Mask

同一個 batch 中的文字長度需要一致，所以 processor 會用 padding 把短 prompt 補到相同長度。`attention_mask` 通常用 1 標示有效 token，用 0 標示 padding，協助模型不要把補齊位置當成真正文字內容。

因此 `input_ids` 與 `attention_mask` 通常有相同 shape，例如 `[num_texts, sequence_length]`。

## 3. `logits_per_image` 的 Shape

若輸入 1 張圖片與 5 個候選 labels：

```text
logits_per_image shape = [1, 5]
```

第一個維度是圖片數量，第二個維度是文字 labels 數量。它表示每一張圖片分別對每一個 label 的相似度分數。

若輸入 2 張圖片與 5 個 labels，shape 會是 `[2, 5]`。

## 4. `softmax(dim=1)` 而不是 `softmax(dim=0)`

`dim=1` 對應 `logits_per_image` 的 labels/texts 維度。zero-shot classification 要比較的是同一張圖片在不同候選 labels 之間哪個最相似，所以應沿著 `dim=1` 做 softmax。

若在 `[1, num_texts]` 上誤用 `dim=0`，因為第一個維度只有 1 張圖片，每個 label 在該維度上幾乎都會各自變成 1，無法形成 labels 之間有意義的相對分布。

## 5. `topk()` 為什麼回傳索引

`probabilities` tensor 裡存的是數值，不是 label 字串。`topk()` 只能知道哪些位置的數值最大，所以回傳索引。例如索引 2 代表 `labels[2]` 這個候選 label。

`.tolist()` 會把 tensor 轉成 Python list，後續比較容易用：

```python
for index in top_indices:
    print(labels[index])
```

## 6. CLIP Zero-shot Classification 依賴候選 Labels

CLIP 在 zero-shot classification 中不是從世界上所有可能物件中自由回答，而是在使用者提供的候選 labels 之間比較圖文相似度。

同一張貓圖片：

- labels 是 `cat/dog/car` 時，`cat` 可能取得很高 probability。
- labels 都是貓相關細節時，例如 `a photo of a cat`、`a close-up photo of a cat`、`a photo of two cats on a sofa`，probability 會在這些相似候選之間重新分配。

所以 top-1 高只代表目前候選 prompts 中相對最相似，不代表模型完整理解圖片，也不代表沒有列出的答案不存在。

## 7. Week03 到 Week04 的銜接

Week03 的重點是建立 Hugging Face 推論流程的基本閱讀能力：processor 如何整理輸入、model 如何輸出結果、tensor shape 如何解讀。Week04 LLaVA 會更複雜，但仍會遇到類似問題：圖片如何前處理、視覺特徵如何進入模型、模型輸出如何被解讀。因此 Week03 是理解後續 VLM 架構的基礎。
