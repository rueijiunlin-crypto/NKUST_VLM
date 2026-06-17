> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

# Week03 Concept Answer Key

## 1. Hugging Face 在本週的角色是什麼？

Hugging Face 是模型工具鏈與模型平台，協助我們下載、載入與使用預訓練模型。本週透過 `transformers` 套件載入 CLIP 的 processor 與 model，並用統一 API 完成本地圖片 zero-shot 推論。

常見誤解：Hugging Face 不是單一模型，它是模型、資料集、工具與推論流程的生態系。

## 2. `CLIPProcessor` 與 `CLIPModel` 分別做什麼？

`CLIPProcessor` 負責前處理，將文字 prompt 轉成 token tensor，將圖片轉成 pixel tensor。`CLIPModel` 負責模型推論，將處理後的輸入送入 image encoder 與 text encoder，並輸出圖文相似度相關結果。

## 3. `input_ids`、`attention_mask`、`pixel_values` 分別代表什麼？

| 欄位 | 來源 | 意義 |
| ---- | ---- | ---- |
| `input_ids` | 文字 | token 對應的整數 ID。 |
| `attention_mask` | 文字 | 標示哪些 token 有效，哪些是 padding。 |
| `pixel_values` | 圖片 | 圖片經 resize、normalize 後的 tensor。 |

## 4. `logits_per_image` 在 zero-shot classification 中代表什麼？

`logits_per_image` 是每張圖片對每個文字 prompt 的原始相似度分數。若輸入 1 張圖片與 5 個 labels，shape 通常是 `(1, 5)`。它還不是機率，需要經過 softmax 才會得到候選 labels 之間的相對分布。

## 5. softmax probability 為什麼不是絕對真實機率？

Softmax probability 是在你提供的候選 labels 之間做相對分配。如果你更換或新增 labels，原本的機率分布可能改變。因此它不代表模型對真實世界的絕對信心，只代表在目前候選文字中哪一個分數較高。

## 6. 為什麼 prompt 改寫會影響 CLIP 結果？

CLIP 會把文字 prompt 轉成 text embedding。不同 prompt 的 token 與語意不同，得到的 text embedding 也會不同，因此與圖片向量的相似度也可能改變。多物件圖片或特定場景應使用更明確的描述，例如 `a photo of two cats on a pink sofa` 通常比只寫 `cat` 更貼近整張圖語意。

## 7. Week03 如何銜接 Week04 LLaVA？

Week03 學的是真實模型工具鏈：如何載入模型、處理圖片與文字輸入、解讀模型輸出。Week04 LLaVA 會在類似的模型載入與前處理基礎上，進一步理解 vision encoder、projector 與 LLM 的連接方式，使模型能產生自然語言回答。