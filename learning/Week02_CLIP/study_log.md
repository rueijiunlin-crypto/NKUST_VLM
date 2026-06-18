# Week02 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
| --- | --- | --- | --- |
| 本週 | 分段完成 | 閱讀 Week02 CLIP 教材、執行 Demo、完成 Practice 與 ChatGPT 驗收 | 已完成 Week02 核心學習 |

## 閱讀進度

- [✅] README.md
- [✅] weekly_plan.md
- [✅] notes.md
- [✅] demo/demo_README.md
- [✅] practice/README.md
- [✅] practice/concept/concept_practice.md
- [✅] practice/coding/coding_practice.md

## Demo 執行結果

| Demo | 是否執行 | 問題／觀察 |
| --- | --- | --- |
| `demo_01_text_image_embedding.py` | 完成 | 理解圖片與文字最後都會被轉成同維度 embedding，維度相同才可進行相似度比較。 |
| `demo_02_cosine_similarity.py` | 完成 | 理解 dot product、norm 與 cosine similarity 的關係，知道 CLIP 比較的是向量方向相似度。 |
| `demo_03_zero_shot_classification.py` | 完成 | 理解 zero-shot classification 會把候選類別寫成 prompt，再透過相似度與 softmax 取得 top-1。 |
| `demo_04_clip_flow.py` | 完成 | 理解 image/text embedding、normalization、similarity matrix 與 argmax 預測流程。 |
| `demo_05_real_clip_zero_shot.py` | 完成 | 使用本地圖片成功執行真實 CLIP Demo，觀察到多物件圖片中 top-1 會受候選 prompt 與畫面主體比例影響。 |

## Practice 結果摘要

| Practice | 是否完成 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| Concept Practice | 完成 | 已能用自己的話說明 CLIP、Image Encoder、Text Encoder、Shared Embedding Space、Cosine Similarity、Zero-shot Classification、Contrastive Learning 與 VLM / VLA 的關係。 | 無重大疑問。 |
| Guided Code Reading | 完成 | 已理解 shape、normalization、similarity matrix、softmax、top-1 prediction 與真實 CLIP Demo 的輸入流程。 | 後續需在 Week03 進一步理解 Hugging Face Processor 與模型輸出欄位。 |

## 本週理解摘要

### 我目前能解釋

- CLIP 的核心任務是將圖片與文字轉換成向量後，在共同向量空間中做語意相似度比較。
- Image Encoder 會將圖片轉成 image embedding，Text Encoder 會將文字 token 轉成 text embedding。
- 共同向量空間的重點不是只讓向量能做內積，而是讓語意相符的圖片與文字靠近，語意不符者遠離。
- Cosine Similarity 用來比較圖片向量與文字向量的方向相似度，分數主要用於候選文字之間的相對排序。
- Zero-shot Classification 不代表模型沒有訓練，而是代表新任務不需要額外提供訓練樣本或重新訓練分類頭。
- Contrastive Learning 透過 positive pair 與 negative pair，讓正確圖文配對相似度提高、錯誤圖文配對相似度降低。
- CLIP 可以視為基礎型 VLM，但它主要負責圖文對齊，不具備完整語言生成、長篇推理或機器人 action 輸出。

### 我仍不理解

- Hugging Face 中 `CLIPProcessor` 如何同時處理圖片與文字。
- `logits_per_image`、`logits_per_text`、softmax probability 與 label prompt 之間的細節關係。
- 真實模型下載、快取與本地圖片推論流程。

### 下週前要釐清

- 如何用 Hugging Face 正確載入 `CLIPModel` 與 `CLIPProcessor`。
- 如何用本地圖片與自訂 labels 做真實 zero-shot classification。
- 如何解讀模型輸出 logits、probability 與 top-k 結果。

## 個人概念紀錄

### CLIP

- 將圖片與文字分別經過編碼器轉換成向量，並透過對比式學習讓語意相符的圖文向量靠近、語意不符的圖文向量遠離。

### Image Encoder

- Image Encoder 負責將圖像轉換成 image embedding。
- 常見架構包含 CNN 與 ViT。
- CNN 透過卷積逐層抽取局部特徵，例如邊緣、紋理、形狀與物件特徵。
- ViT 會將圖片切成多個 patch，再透過 Transformer 建立不同區域之間的關係。
- 在 CLIP 中，Image Encoder 的輸出會被投影到與文字向量相同維度的共同向量空間。

### Text Encoder

- Text Encoder 負責將文字描述轉換成 text embedding。
- 文字會先被拆分成 token，再轉成 token embedding。
- 這些 token embedding 會經過 Transformer Encoder，讓模型理解詞與詞之間的語意關係。
- 最後輸出代表整句文字語意的向量，並投影到與圖片向量相同的共同向量空間。

### Shared Embedding Space

- Shared Embedding Space 是圖片向量與文字向量共同存在的向量空間。
- 經過 CLIP 訓練後，語意相近的圖片與文字會在這個空間中靠近。
- 語意不相符的圖片與文字會在這個空間中遠離。
- 因此，模型可以用 cosine similarity 比較圖片與文字的相似度。

### Cosine Similarity

- Cosine Similarity（餘弦相似度）用來比較兩個向量的方向是否接近。
- 在 CLIP 中，圖片向量與文字向量會先經過 normalization（正規化），再計算相似度。
- 相似度越高，代表圖片與文字在語意上越接近。
- 它比較的是向量方向，而不是單純比較向量長度。
- 因此，CLIP 可以用 cosine similarity 判斷「這張圖片比較接近哪一句文字描述」。

### Zero-shot Classification

- 零樣本分類是指模型不需要針對新類別重新訓練，就能直接用文字描述作為分類候選。
- CLIP 會將圖片與每個文字 prompt 都轉成向量，並計算相似度。
- 相似度最高的文字描述，就會被當作模型的分類結果。
- Zero-shot 不代表模型完全沒有訓練，而是代表在這個新任務上不需要額外提供訓練樣本。

### Contrastive Learning

- Contrastive Learning（對比式學習）是 CLIP 用來訓練圖文對齊能力的方法。
- 在一個 batch 中，正確配對的圖片與文字稱為 positive pair（正樣本配對）。
- 錯誤配對的圖片與文字稱為 negative pair（負樣本配對）。
- 訓練目標是讓 positive pair 的相似度提高，讓 negative pair 的相似度降低。
- 透過大量圖文配對資料訓練後，模型會學會將語意相同的圖片與文字放到共同向量空間中的相近位置。

### CLIP 與 VLM / VLA 的關係

- CLIP 可以視為基礎型 VLM，因為它同時處理圖片與文字。
- CLIP 的主要功能是圖文對齊與相似度比較，例如判斷一張圖片最接近哪一段文字描述。
- 但 CLIP 本身不具備完整的語言生成能力，不能像現代 VLM 一樣進行看圖問答、長篇描述或多步推理。
- 現代 VLM 通常會使用 CLIP 或 CLIP-like vision encoder 作為視覺端，先將圖片轉換成可被語言模型理解的視覺表示。
- VLM 會在視覺表示後接上 LLM，使模型能根據圖片內容產生文字回答。
- VLA 則是在 VLM 的基礎上進一步加入 action 輸出，讓模型能根據視覺與語言指令產生機器人動作。

## Notion 更新

- [✅] Learning Roadmap
- [✅] Experiment Log
- [✅] Weekly Review

## ChatGPT 驗收

- [ ] 未驗收
- [✅] Pass
- [ ] Minor Revision
- [ ] Major Revision

## ChatGPT 評語

Week02 驗收通過。學生已能說明 CLIP 的核心資料流、Image Encoder 與 Text Encoder 的角色、共同向量空間、cosine similarity、zero-shot classification、contrastive learning，以及 CLIP 與 VLM / VLA 的差異。Demo 與 Practice 均已完成，真實 CLIP Demo 中也能觀察並解釋多物件圖片造成 top-1 受 prompt 與畫面主體影響的限制。下一週可進入 Hugging Face，將 Week02 概念對應到 `CLIPProcessor`、`CLIPModel`、logits、probability 與本地圖片推論流程。

## 問題紀錄

- 真實 CLIP Demo 下載 COCO 範例圖片時遇到 SSL 憑證錯誤，已改用本地圖片路徑執行。
- 一開始對 zero-shot 的理解偏向「零成本分類」，後續已修正為「新任務不需要額外訓練樣本」。
- 真實圖片同時包含貓與粉紅沙發時，模型 top-1 選到粉紅沙發，已理解這是候選 prompt 與畫面主體造成的相對排序問題。

## 修正方式

- 使用 `--image demo/000000039769.jpg` 指定本地圖片，避開外部圖片下載問題。
- 補充 zero-shot、shared embedding space、cosine similarity 與 CLIP 限制的精確說法。
- 將 CLIP 的用途限定為圖文對齊與相似度比較，不直接等同完整 VLM / VLA。

## 本週最重要的理解

### CLIP 限制

| 限制 | 說明 |
| --- | --- |
| 候選文字依賴 | 結果高度受 labels / prompt 設計影響。 |
| 單一 Top-1 不一定代表完整內容 | 圖中有多個物件時，最高分只代表最相似描述。 |
| 背景可能干擾判斷 | 大面積背景或顯眼顏色可能壓過小目標。 |
| 不擅長精準定位 | CLIP 不會直接給 bounding box（邊界框）。 |
| 細粒度分類不穩 | 對非常接近的類別、專業場域、微小差異可能不準。 |
| 分數是相對比較 | Softmax（歸一化機率函數）分數取決於你給了哪些候選 labels。 |

## 一分鐘回顧

CLIP 會將圖片與文字分別經過 Image Encoder 與 Text Encoder 轉成 embedding，並投影到 shared embedding space。透過 contrastive learning，正確圖文配對會靠近、錯誤圖文配對會遠離。推論時，模型會計算圖片與候選文字 prompt 的相似度，再用 softmax 與 top-1 選出最相近的文字描述。CLIP 能支援 zero-shot classification，但結果會受 prompt、候選 labels 與畫面內容影響，因此不等同於精準物件偵測或完整 VLM / VLA。

## 下週目標

- 進入 Week03 Hugging Face。
- 學會 `CLIPProcessor` 如何處理圖片與文字。
- 學會 `CLIPModel` 如何輸出 logits 與 probability。
- 用本地圖片與自訂 labels 完成真實 CLIP zero-shot 推論。
