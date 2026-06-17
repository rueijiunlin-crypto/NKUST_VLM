# Week03 Concept Practice

請先用自己的話作答，再使用自我檢查項目確認是否涵蓋關鍵概念。

## 1. Hugging Face 在本週的角色是什麼？

提示：它負責模型下載、載入、推論流程中的哪一部分？

學生作答：

自我檢查：

- [ ] 我有說明 Hugging Face 是模型工具鏈，不是模型本身。
- [ ] 我有提到它能協助載入預訓練模型與 processor。

## 2. `CLIPProcessor` 與 `CLIPModel` 分別做什麼？

提示：一個負責前處理，一個負責模型推論。

學生作答：

自我檢查：

- [ ] 我有說明 processor 負責圖片與文字前處理。
- [ ] 我有說明 model 負責輸出 logits 或 embeddings。

## 3. `input_ids`、`attention_mask`、`pixel_values` 分別代表什麼？

提示：哪些來自文字？哪些來自圖片？

學生作答：

自我檢查：

- [ ] 我有區分文字 tensor 與圖片 tensor。
- [ ] 我有說明 `pixel_values` 是圖片前處理後的模型輸入。

## 4. `logits_per_image` 在 zero-shot classification 中代表什麼？

提示：它的 shape 通常和圖片數量、label 數量有關。

學生作答：

自我檢查：

- [ ] 我有提到它是每張圖片對每個文字 prompt 的原始分數。
- [ ] 我沒有把 logits 直接當成機率。

## 5. softmax probability 為什麼不是絕對真實機率？

提示：它和候選 labels 的集合有關。

學生作答：

自我檢查：

- [ ] 我有說明 probability 是候選 labels 之間的相對分布。
- [ ] 我知道更換 labels 可能改變分數。

## 6. 為什麼 prompt 改寫會影響 CLIP 結果？

提示：不同文字會產生不同 text embedding。

學生作答：

自我檢查：

- [ ] 我有說明 prompt 會影響 text embedding。
- [ ] 我有提到多物件或特定場景應使用更明確的描述。

## 7. Week03 如何銜接 Week04 LLaVA？

提示：LLaVA 也需要 processor、vision encoder、model loading 與輸出解讀。

學生作答：

自我檢查：

- [ ] 我有說明 Week03 是真實模型工具鏈基礎。
- [ ] 我有提到 Week04 會進一步把視覺表示接到 LLM。