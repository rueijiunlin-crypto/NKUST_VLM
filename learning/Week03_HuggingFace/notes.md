# Week03 Notes: Hugging Face CLIP 推論

## Level 1：為什麼 Week03 要學 Hugging Face？

Week02 已經理解 CLIP 的概念：圖片與文字會被轉成 embedding，並在共同向量空間中比較相似度。

Week03 要做的是把概念對應到真實工具：

```text
圖片檔案 + 文字 labels
→ CLIPProcessor
→ input tensors
→ CLIPModel
→ logits_per_image
→ softmax probability
→ top-k prediction
```

Hugging Face Transformers（模型載入與推論工具庫）的價值在於：

- 提供預訓練模型下載與載入介面。
- 提供 processor，降低圖片與文字前處理成本。
- 提供統一模型 API，方便後續切換 CLIP、LLaVA、Qwen-VL、PaliGemma 等模型。
- 適合作為 VLM / VLA 研究的模型實驗入口。

## Level 2：`CLIPProcessor` 做什麼？

`CLIPProcessor` 是前處理器，負責把人類可讀資料轉成模型可接受的 tensor。

輸入：

- 圖片：PIL Image 或圖片路徑讀取後的 RGB image。
- 文字：labels 或 prompts，例如 `a photo of a cat`。

輸出常見欄位：

| 欄位 | 意義 |
| ---- | ---- |
| `input_ids` | 文字 token 的 ID。 |
| `attention_mask` | 告訴模型哪些 token 是有效文字，哪些是 padding。 |
| `pixel_values` | 圖片經 resize、normalize 後的 tensor。 |

重要觀念：

> Processor 不是模型本身，它不負責判斷圖片內容，而是負責把圖片與文字整理成模型能吃的格式。

## Level 3：`CLIPModel` 做什麼？

`CLIPModel` 是真正的模型，包含 image encoder、text encoder 與圖文相似度計算相關輸出。

常見流程：

```python
outputs = model(**inputs)
```

常見輸出：

| 輸出 | 意義 |
| ---- | ---- |
| `logits_per_image` | 每張圖片對每個文字 prompt 的未正規化相似度分數。 |
| `logits_per_text` | 每個文字 prompt 對每張圖片的未正規化相似度分數。 |
| `image_embeds` | 圖片 embedding。 |
| `text_embeds` | 文字 embedding。 |

在 zero-shot image classification 中，最常使用的是：

```python
probabilities = outputs.logits_per_image.softmax(dim=1)
```

## Level 4：logits、probability 與 top-k

`logits_per_image` 是模型輸出的原始分數，還不是機率。

假設有 1 張圖片與 5 個 labels：

```text
logits_per_image shape = (1, 5)
```

代表：

| 維度 | 意義 |
| ---- | ---- |
| 第 0 維 | 圖片數量。 |
| 第 1 維 | 候選文字 labels 數量。 |

softmax 會把同一張圖片對所有 labels 的 logits 轉成相對分布：

```python
probabilities = logits_per_image.softmax(dim=1)
```

注意：

- probability 是候選 labels 之間的相對分布。
- 它不等於模型對真實世界的絕對信心。
- 若候選 labels 設計不好，top-1 仍可能不符合任務需求。

## Level 5：Prompt 會影響結果

CLIP 的 zero-shot classification 不是固定分類頭，而是由文字 prompt 定義候選類別。

例如同樣是 cat：

- `cat`
- `a photo of a cat`
- `a photo of two cats on a sofa`
- `a blurry photo of a cat`

這些 prompt 產生的 text embedding 可能不同，因此與圖片的相似度也可能不同。

實務上應避免只寫過度簡短或模糊的 label。較穩定的做法是：

- 使用完整描述句。
- 使用與任務場景一致的描述。
- 對重要類別設計多個 prompt，再比較或平均結果。

## Level 6：常見錯誤

### 圖片路徑錯誤

如果終端機位於：

```text
learning/Week03_HuggingFace
```

而圖片在：

```text
learning/Week02_CLIP/demo/000000039769.jpg
```

則路徑應寫成：

```powershell
--image ../Week02_CLIP/demo/000000039769.jpg
```

### 模型下載失敗

第一次執行 `from_pretrained()` 時會下載模型權重。若網路不穩，可能失敗。

可檢查：

- 網路是否正常。
- Hugging Face 是否可連線。
- 是否有公司或校園代理限制。
- 模型是否已被快取。

### SSL 錯誤

外部圖片網址可能遇到 SSL 憑證問題。較安全的解法是改用本地圖片，不建議直接關閉 SSL 驗證。

## Level 7：Week03 與後續 VLM 的關係

Hugging Face 是後續 VLM 實作的基礎工具鏈。Week03 學的是：

```text
如何載入模型
如何處理圖片與文字輸入
如何解讀模型輸出
如何記錄推論結果
```

這些能力會在 Week04 LLaVA（大型語言與視覺助手）、Week05 VLM Architecture 與後續機器人應用中重複使用。

## 本週尚未涵蓋

- 自行訓練或 fine-tune CLIP。
- 大規模資料集處理。
- LLaVA 的 vision encoder + projector + LLM 完整架構。
- ROS2 即時影像串接。
- VLA action 輸出與機器人控制。