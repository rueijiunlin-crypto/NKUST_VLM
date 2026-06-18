# Week03 Notes: Hugging Face CLIP 推論流程

Week03 接在 Week02 CLIP（對比式圖文預訓練）之後，目標不是訓練模型，而是看懂 Hugging Face Transformers（Hugging Face 轉換器工具庫）如何把圖片與文字送進 CLIP，並完成 zero-shot image classification（零樣本影像分類）。

本週主線：

```text
圖片 + 候選 labels/prompts
-> CLIPProcessor
-> input_ids / attention_mask / pixel_values
-> CLIPModel
-> logits_per_image
-> softmax(dim=1)
-> top-k prediction
```

## 1. 為什麼 Week03 要學 Hugging Face

Hugging Face 提供一致的模型載入、前處理與推論 API。對 VLM（視覺語言模型）與後續 VLA（視覺語言動作模型）研究來說，這週要先建立三個能力：

- 看懂 processor 如何把原始圖片與文字轉成 tensor（張量）。
- 看懂 model 如何輸出圖文相似度分數。
- 看懂 softmax、top-k 與 prompt 設計如何影響分類結果。

對應 Demo：

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：`CLIPProcessor` 會輸出哪些 keys，以及每個 tensor 的 shape。

## 2. `CLIPProcessor` 與 `CLIPModel` 的分工

`CLIPProcessor` 負責前處理，不負責判斷圖片內容。它會把文字和圖片整理成模型可讀的 PyTorch tensor（PyTorch 張量）。

| 輸入或輸出 | 角色 |
| --- | --- |
| 文字 labels/prompts | 經 tokenizer（詞元化器）轉成 token id。 |
| 圖片 | 轉成 RGB、resize、normalize，最後變成 `pixel_values`。 |
| `input_ids` | 每個文字 prompt 的 token id 序列。 |
| `attention_mask` | 標記哪些 token 是有效文字，哪些是 padding（補齊）。 |
| `pixel_values` | 模型需要的圖片 tensor。 |

`CLIPModel` 負責推論。它會把圖片與文字分別編碼成 embedding vector（嵌入向量），再計算圖片與每個文字 prompt 的相似度。

常見輸出：

| 輸出 | 意義 |
| --- | --- |
| `logits_per_image` | 每張圖片對每個文字 label 的原始相似度分數。 |
| `logits_per_text` | 每個文字 label 對每張圖片的原始相似度分數。 |
| `image_embeds` | 圖片 embedding vector。 |
| `text_embeds` | 文字 embedding vector。 |

對應 Demo：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：`logits_per_image` 的 shape 是否等於 `[圖片數量, labels 數量]`。

## 3. CLIP 推論中的 Tensor Shape 解讀

以下用本週 zero-shot image classification 流程解釋 shape，不把它變成抽象數學。

假設你送入 1 張圖片與 5 個候選 labels：

```python
labels = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
    "a photo of a laboratory",
]
```

常見 shape 會像這樣：

| Tensor | 範例 shape | 如何解讀 |
| --- | ---: | --- |
| `input_ids` | `[5, sequence_length]` | 5 代表 5 個文字 prompts；`sequence_length` 是每個 prompt 補齊後的 token 長度。 |
| `attention_mask` | `[5, sequence_length]` | 與 `input_ids` 同形狀；1 通常代表有效 token，0 通常代表 padding。 |
| `pixel_values` | `[1, 3, 224, 224]` | 1 張圖片、3 個 RGB channels、高 224、寬 224。 |
| `logits_per_image` | `[1, 5]` | 1 張圖片分別對 5 個 labels 的相似度分數。 |
| `probabilities` | `[5]` | 取出第 1 張圖片後，得到 5 個 labels 的相對機率分布。 |

幾個基本維度：

- batch dimension（批次維度）：一次送入幾筆資料。例如 1 張圖片就是 `num_images = 1`。
- sequence length（序列長度）：文字被 tokenizer 切成 token 後，補齊到同一長度。
- hidden dimension（隱藏維度）：模型內部 embedding vector 的長度。本週 demo 主要觀察輸入與輸出 shape，不要求手算 hidden dimension。

`logits_per_image` 為什麼是 `[num_images, num_texts]`？

因為 CLIP 會問：「每一張圖片，分別和每一段文字有多相似？」如果有 1 張圖片、5 個 labels，就會得到 `[1, 5]`。如果有 2 張圖片、5 個 labels，理論上會得到 `[2, 5]`。

`softmax(dim=1)` 為什麼沿著 label/text 維度？

`dim=1` 是 `logits_per_image` 的第二個維度，也就是 labels/texts。對 `[1, 5]` 來說，softmax 會把同一張圖片對 5 個 labels 的 logits 轉成相對分布。這正好符合分類問題：「在這些候選 labels 之間，哪一個最像？」

`[0]` 為什麼代表取出第 1 張圖片？

`logits.softmax(dim=1)` 的結果仍然保留圖片 batch 維度，例如 `[1, 5]`。`[0]` 取出第 1 張圖片的 probability vector，所以 shape 會變成 `[5]`。

## 4. 核心程式碼逐行解釋

本週 Demo 02 的核心推論流程是：

```python
with torch.inference_mode():
    outputs = model(**inputs)
    logits = outputs.logits_per_image
    probabilities = logits.softmax(dim=1)[0]
```

逐行解讀：

- `torch.inference_mode()`：推論時關閉梯度紀錄，降低記憶體與計算負擔。這週只做 inference（推論），不做 training（訓練）。
- `model(**inputs)`：Python dictionary unpacking（字典解包）。如果 `inputs` 內有 `input_ids`、`attention_mask`、`pixel_values`，這行等價於把它們分別傳入模型。
- `outputs.logits_per_image`：圖片對每個文字 label 的原始相似度分數。它還不是機率。
- `logits.softmax(dim=1)`：把同一張圖片對所有 labels 的 logits 轉成相對機率分布。
- `[0]`：取出第 1 張圖片的 probability vector。本週通常一次只送 1 張圖片。

Top-k 程式碼：

```python
top_k = min(args.top_k, len(labels))
top_indices = probabilities.topk(top_k).indices.tolist()
```

逐行解讀：

- `min(args.top_k, len(labels))`：避免使用者要求的 top-k 超過候選 labels 數量。例如只有 3 個 labels 時，不能取 top-5。
- `probabilities.topk(top_k)`：在 probability vector 中找出分數最高的前 k 個項目。
- `.indices`：取得前 k 名的索引，不是 label 字串本身。
- `.tolist()`：把 PyTorch tensor 轉成 Python list，方便後續用 `labels[index]` 印出 label 名稱。

重要觀念：`topk()` 回傳索引，是因為 tensor 只知道「第幾個位置」的數值最大；label 文字是我們另外保存在 Python list 裡的資料。

## 5. Softmax Probability 與候選 Labels 的關係

CLIP 的 softmax probability 是「目前候選 labels 之間的相對分布」，不是絕對真實機率，也不是模型對世界狀態的絕對信心。

同一張貓的圖片，如果候選 labels 是：

```text
cat / dog / car
```

`cat` 可能得到很高分，因為它明顯比 `dog` 和 `car` 更接近圖片。

但如果候選 labels 改成：

```text
a photo of a cat
a photo of two cats on a sofa
a close-up photo of a cat face
a blurry photo of a cat
```

softmax probability 可能會重新分配。因為現在候選項都與貓相關，模型要在更細的文字描述之間比較。Top-1 高只代表「在目前候選 prompt 中最相似」，不代表模型完整理解圖片，也不代表其他沒有列出的可能性不存在。

對應 Demo：

```powershell
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "cat" "dog" "car"
python demo/demo_02_clip_zero_shot_local.py --image ../Week02_CLIP/demo/000000039769.jpg --labels "a photo of a cat" "a photo of two cats on a sofa" "a blurry photo of a cat"
```

觀察重點：labels 改變後，top-1 與 probability 分布是否改變。

## 6. Prompt 設計與 Prompt Sensitivity

CLIP 的文字輸入不是單純的類別名稱，而是一段文字 prompt。不同 prompt 會產生不同 text embedding，因此可能改變圖文相似度。

常見 prompt sets：

| Prompt set | 範例 | 觀察目的 |
| --- | --- | --- |
| object-only labels | `cat`, `dog`, `sofa` | 測試最短標籤是否足夠。 |
| photo template labels | `a photo of a cat` | 接近 CLIP 常見訓練語境。 |
| scene-aware descriptions | `a photo of two cats on a pink sofa` | 測試場景描述是否改善或干擾結果。 |

對應 Demo：

```powershell
python demo/demo_03_prompt_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

觀察重點：

- 不同 prompt set 的 top-1 是否改變。
- probability 分布是否更集中或更分散。
- scene-aware prompt 是否真的比較穩定，還是因描述太細而造成誤判。

## 7. 常見執行問題

### 圖片路徑

建議從 `learning/Week03_HuggingFace` 執行：

```powershell
python demo/demo_01_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

如果圖片不存在，請改用自己的本機圖片：

```powershell
python demo/demo_01_processor_inputs.py --image demo/my_image.jpg
```

### 模型下載

`from_pretrained()` 會從 Hugging Face Model Hub 下載 `openai/clip-vit-base-patch32`。首次執行需要網路，之後通常會使用本機快取。

### CPU / GPU

本週 demo 可用 CPU 執行，只是首次下載與載入模型可能需要一些時間。若有 CUDA GPU，推論通常會更快，但本週不要求 GPU。

## 8. 與 Week04 LLaVA 的銜接

Week03 先學會 Hugging Face 的基本推論流程：processor、model、tensor input、model output、logits、softmax 與 top-k。Week04 LLaVA（大型語言與視覺助手）會延伸到更複雜的 VLM 架構：圖片不只是被分類，而是會進入 vision encoder（視覺編碼器）並與 language model（語言模型）互動。

本週尚未涵蓋：

- CLIP fine-tuning（微調）。
- Dataset training pipeline（資料集訓練流程）。
- LLaVA 的 projector、LLM 與多輪對話。
- ROS2（機器人作業系統第二版）、Isaac Sim（NVIDIA 機器人模擬器）或 VLA action output（動作輸出）。
