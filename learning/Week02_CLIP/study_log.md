# Week02 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
| --- | --- | --- | --- |
| | | | |

## 閱讀進度

- [✅] README.md
- [✅] weekly_plan.md
- [✅] notes.md
- [✅] demo/demo_README.md

## Demo 執行結果

| Demo | 是否執行 | 問題／觀察 |
| --- | --- | --- |
| demo/demo_01_text_image_embedding.py | 完成 | 文字與圖像如何對比 |
| demo/demo_02_cosine_similarity.py | 完成 | 看到如何去對比文字與圖片 |
| demo/demo_03_zero_shot_classification.py | 完成 | |
| demo/demo_04_clip_flow.py | 完成 | |
| demo/demo_05_real_clip_zero_shot.py | 完成 | 了解到CLIP在分類時遇到多重目標的缺點 |

## Practice 結果摘要

| Practice | 是否完成 | 重要觀察 | 疑問 |
| --- | --- | --- | --- |
| Concept Practice | 完成 | 無 | 無 |
| Guided Code Reading | 完成 | 無 | 無 |

## 本週理解摘要

### 我目前能解釋

-

### 我仍不理解

-

### 下週前要釐清

-

## 個人概念紀錄

### CLIP

- 將文字與圖像經過編碼器後的向量做對比，來使兩者對齊

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

- [ ] Learning Roadmap
- [ ] Experiment Log
- [ ] Weekly Review

## ChatGPT 驗收

- [x] 未驗收
- [ ] Pass
- [ ] Minor Revision
- [ ] Major Revision

## ChatGPT 評語

（由學生或 ChatGPT 填寫）

## 問題紀錄

-

## 修正方式

-

## 本週最重要的理解

### CLIP 限制

| 限制 | 說明 |
| --- | --- |
| 候選文字依賴 | 結果高度受 labels / prompt 設計影響 |
| 單一 Top-1 不一定代表完整內容 | 圖中有多個物件時，最高分只代表最相似描述 |
| 背景可能干擾判斷 | 大面積背景或顯眼顏色可能壓過小目標 |
| 不擅長精準定位 | CLIP 不會直接給 bounding box（邊界框） |
| 細粒度分類不穩 | 對非常接近的類別、專業場域、微小差異可能不準 |
| 分數是相對比較 | Softmax（歸一化機率函數）分數取決於你給了哪些候選 labels |

## 一分鐘回顧

請用自己的話總結本週核心資料流、架構或概念。

## 下週目標

-
