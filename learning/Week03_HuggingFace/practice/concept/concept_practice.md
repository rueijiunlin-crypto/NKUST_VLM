# Week03 Concept Practice

請先閱讀 `../../notes.md`，再完成本檔。這裡是學生作答檔，請不要把參考答案直接寫在題目後面；完成後再查看 `concept_answer_key.md`。

## 1. Token、Token ID、Tensor、Embedding Vector

請用自己的話分辨下列四個名詞：

| 名詞 | 你的解釋 | 在 Week03 CLIP 流程中的例子 |
| --- | --- | --- |
| token（詞元） | 將句子拆分後的單位 | 句子被拆分成4~5個token |
| token id（詞元識別碼） | 該token的代號，用於後續對照嵌入向量表 | 無 |
| tensor（張量） | 二維以上的向量，每個數字各有他代表的含意 | 可能代表他有含幾種顏色，有多少維度 |
| embedding vector（嵌入向量） | 該圖片或文字的實際語意，供模型閱讀使用 | 張量內的維度就是指嵌入向量是幾維的 |

提示：

- token 是文字切分後的單位。
- token id 是 tokenizer 給 token 的整數編號。
- tensor 是模型實際接收或輸出的多維資料容器。
- embedding vector 是模型內部用來表示語意的向量。

自我檢查：

- [✅] 我沒有把 token id 誤認為 embedding vector。
- [✅] 我能說明 `input_ids` 為什麼是 tensor。

## 2. Padding 與 Attention Mask

假設兩個 prompts 長度不同：

```text
cat
a photo of two cats on a pink sofa
```

請回答：

1. 為什麼 processor 需要 padding（補齊）？
2. `attention_mask` 如何協助模型分辨有效 token 與 padding？
3. 如果沒有 `attention_mask`，模型可能會把 padding 當成什麼？

學生作答：

- 因為不同維度的向量無法被讀取，所以需要補齊
- 他也是一個向量，會標示出實際需要被讀取的token的位置
- 他會把補齊的內容當成一種嵌入向量去訓練

自我檢查：

- [✅] 我能解釋 `input_ids` 與 `attention_mask` 為什麼通常有相同 shape。
- [✅] 我能說明不同長度文字如何被放進同一個 batch。

## 3. `logits_per_image` 的 Shape

假設輸入 1 張圖片與 5 個候選 labels，請填空：

```text
logits_per_image shape = [____, ____]
```

請解釋兩個維度各代表什麼：

- 應當填入(1,5)，一代表著一張圖片，並且有五個候選的標籤

延伸題：如果一次輸入 2 張圖片與 5 個 labels，`logits_per_image` shape 會變成什麼？為什麼？

學生作答：

- (2,5)，因為有兩張圖片以及五個候選標籤

自我檢查：

- [✅] 我能說明第一個維度是圖片數量。
- [✅] 我能說明第二個維度是文字 labels 數量。

## 4. 為什麼是 `softmax(dim=1)` 而不是 `softmax(dim=0)`

在 Week03 demo 中，`logits_per_image` 通常是 `[1, num_texts]`。

請回答：

1. `dim=1` 對應哪一個維度？
2. 為什麼 zero-shot classification 要沿著 labels/texts 維度做 softmax？
3. 如果誤用 `dim=0`，在只有 1 張圖片時可能會造成什麼不合理的結果？

學生作答：

- 對應的是

自我檢查：

- [ ] 我能說明 softmax probability 是候選 labels 之間的相對分布。
- [ ] 我知道 softmax probability 不是絕對真實機率。

## 5. `topk()` 為什麼回傳索引

Demo 02 使用：

```python
top_indices = probabilities.topk(top_k).indices.tolist()
```

請回答：

1. `probabilities` 這個 tensor 裡面存的是 label 名稱，還是數值？
2. 為什麼 `topk()` 回傳的是索引，而不是 label 字串？
3. 程式如何用索引找回真正的 label 名稱？

學生作答：

-

自我檢查：

- [ ] 我能說明 `labels[index]` 的用途。
- [ ] 我能說明 `.tolist()` 為什麼方便後續輸出。

## 6. CLIP Zero-shot Classification 為什麼依賴候選 Labels

請用一個例子說明：同一張貓的圖片，在候選 labels 是 `cat/dog/car` 時，和候選 labels 是更細的貓相關描述時，softmax probability 為什麼可能改變？

學生作答：

-

引導問題：

- Top-1 高是否代表模型完整理解圖片？
- 如果正確答案沒有出現在候選 labels 中，CLIP 會怎麼做？
- prompt 改寫可能如何改變 text embedding？

自我檢查：

- [ ] 我能說明 CLIP 會在目前候選 labels 之間比較。
- [ ] 我能說明 top-1 是相對最相似，不是絕對保證。

## 7. Week03 到 Week04 的銜接

請用 3-5 句話說明：Week03 學到的 processor、tensor shape、model output 與推論流程，如何幫助你理解 Week04 LLaVA（大型語言與視覺助手）？

學生作答：

-
