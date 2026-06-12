請在目前 repository `rueijiunlin-crypto/NKUST_VLM` 中建立 Week02 CLIP 學習內容。

執行前請先讀取並遵守 repository 內最新的 `AGENTS.md`。所有檔案結構、命名、文件格式、練習模式、Demo 規範、study_log 規範與專案排除項目，均以 `AGENTS.md` 為最高優先規範。若本指令與 `AGENTS.md` 有衝突，請以 `AGENTS.md` 為準。

本任務不要修改 `AGENTS.md`。請只建立 Week02 的正式學習內容。

---

## 1. 任務目標

建立：

```text
learning/Week02_CLIP/
```

Week02 主題是 CLIP（Contrastive Language-Image Pre-training，對比式圖文預訓練）。

本週目標是讓學生理解：

1. CLIP 如何把影像與文字分別編碼成向量。
2. Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）的角色。
3. Shared Embedding Space（共同嵌入空間）的用途。
4. Cosine Similarity（餘弦相似度）如何比較影像與文字向量。
5. Zero-shot Classification（零樣本分類）的基本流程。
6. Contrastive Learning（對比式學習）的直覺。
7. CLIP 如何銜接後續 VLM（Vision-Language Model，視覺語言模型）與 VLA（Vision-Language-Action Model，視覺語言動作模型）。

請參考 Week01 的結構與風格：

```text
learning/Week01_Transformer/
```

但不要直接複製 Week01 內容。

---

## 2. 必須遵守的專案限制

請遵守 `AGENTS.md` 中的專案範圍與排除項目。

Week02 內容必須聚焦於：

* CLIP
* image-text alignment（圖文對齊）
* image embedding（影像嵌入向量）
* text embedding（文字嵌入向量）
* cosine similarity
* zero-shot classification
* VLM / VLA 的前置理解

不得新增以下內容作為教材主題、Demo 主題或實驗主題：

* 船體
* 浮力
* USV
* 海浪
* 海事機器人
* 船體控制
* 與本 VLM / VLA 學習主線無關的內容

---

## 3. 建立資料夾結構

請依照 `AGENTS.md` 的每週資料夾規範建立 Week02。Week02 採用 Guided Code Reading Mode（引導式程式閱讀模式），不採用 Implementation Practice Mode（實作練習模式），因此不需要建立 `exercises/`、`solutions/` 或 TODO 補空題。

請建立：

```text
learning/Week02_CLIP/
├── README.md
├── weekly_plan.md
├── notes.md
├── study_log.md
├── demo/
│   ├── demo_README.md
│   ├── requirements.txt
│   ├── demo_01_text_image_embedding.py
│   ├── demo_02_cosine_similarity.py
│   ├── demo_03_zero_shot_classification.py
│   ├── demo_04_clip_flow.py
│   └── demo_05_real_clip_zero_shot.py
└── practice/
    ├── README.md
    ├── concept/
    │   ├── concept_practice.md
    │   └── concept_answer_key.md
    └── coding/
        ├── README.md
        ├── requirements.txt
        ├── coding_practice.md
        ├── coding_observation_key.md
        └── guided_demos/
            ├── 01_vector_similarity_reading.py
            ├── 02_text_image_alignment_reading.py
            ├── 03_zero_shot_reading.py
            └── 04_clip_pipeline_reading.py
```

注意：

* `demo/requirements.txt` 用於 demo 依賴，包含 NumPy 與真實 CLIP demo 所需套件。
* `practice/coding/requirements.txt` 用於 guided demos，至少包含 NumPy。
* 不要建立 `practice/coding/exercises/`。
* 不要建立 `practice/coding/solutions/`。
* 不要建立 `practice/coding/coding_answer_key.md`，因為本週採 Guided Code Reading Mode，請使用 `coding_observation_key.md`。

---

## 4. README.md 要求

`README.md` 是 Week02 的學習入口，請依 `AGENTS.md` 的 README 規範撰寫。

內容至少包含：

1. Week02 學習定位。
2. Week02 與 Week01 Transformer（轉換器架構）的關係。
3. CLIP 的核心資料流：

```text
Image
-> Image Encoder
-> Image Embedding

Text
-> Text Encoder
-> Text Embedding

Image Embedding + Text Embedding
-> Cosine Similarity
-> Matching Score
-> Zero-shot Classification / Image-Text Retrieval
```

4. 檔案導覽。
5. 建議閱讀順序。
6. 與 VLM / VLA 碩士研究主線的關係。
7. 說明 Week02 如何銜接 Week03 Hugging Face（機器學習模型平台與工具庫）。

---

## 5. weekly_plan.md 要求

`weekly_plan.md` 只放 Week02 的課程規劃、任務與驗收條件，不要放完整教材、完整答案或學生作答。

內容至少包含：

1. 本週目標。
2. 必學概念。
3. 建議 7 天學習順序。
4. Demo 執行順序。
5. Practice 順序。
6. Guided Code Reading Mode 說明。
7. 任務清單。
8. 驗收條件。
9. Notion（知識管理平台）紀錄項目。
10. Week02 完成後如何銜接 Week03 Hugging Face。

驗收條件至少包含：

```markdown
- [ ] 能說明 CLIP 的基本任務是圖文對齊。
- [ ] 能說明 Image Encoder 與 Text Encoder 的角色。
- [ ] 能說明共同向量空間的用途。
- [ ] 能說明 cosine similarity 如何比較圖片與文字。
- [ ] 能說明 zero-shot classification 的流程。
- [ ] 能說明 contrastive learning 的直覺。
- [ ] 能執行必要 NumPy concept demos。
- [ ] 能選擇性執行 real CLIP demo，或能說明未執行原因。
- [ ] 能完成 Concept Practice。
- [ ] 能完成 Guided Code Reading。
- [ ] 能用自己的話說明 CLIP 和 VLM / VLA 的關係。
- [ ] 能說明 Week02 如何銜接 Week03 Hugging Face。
```

注意：不得在建立檔案時把任務勾選成完成，除非使用者已明確回報完成。

---

## 6. notes.md 要求

`notes.md` 是正式教材，請寫成可閱讀教材，不要只列大綱。

至少包含以下章節：

```markdown
# Week02 Notes: CLIP 基礎

## Level 1：CLIP 是什麼
## Level 2：為什麼需要圖文共同向量空間
## Level 3：Image Encoder 與 Text Encoder
## Level 4：Cosine Similarity
## Level 5：Zero-shot Classification
## Level 6：Contrastive Learning 的直覺
## Level 7：CLIP 與 VLM 的關係
## Level 8：CLIP 在機器人語意理解中的用途
## Level 9：本週常見誤解
## Level 10：Week02 驗收問題
```

請明確說明：

* CLIP 不是「查資料庫」。
* CLIP 不是聊天模型。
* CLIP 不是完整 VLM assistant。
* CLIP 是把圖片與文字各自編碼成向量，再比較相似度。
* CLIP 可以做 image-text retrieval（圖文檢索）、zero-shot classification（零樣本分類）與語意檢索。
* 後續 VLM / VLA 會把 CLIP 類似的圖文對齊能力擴展到回答、推理與動作決策。

---

## 7. Demo 要求

Week02 Demo 採用 Flat Integrated Demo（扁平整合式 Demo）結構。

Demo 分成兩層：

1. NumPy Concept Demo（NumPy 概念示範）：建立資料流直覺。
2. Real CLIP Demo（真實 CLIP 模型示範）：可選進階項，可下載真實模型。

請建立以下檔案並確保可執行。

---

### demo_01_text_image_embedding.py

目的：用簡化資料展示 image embedding 與 text embedding。

要求：

* 使用 NumPy。
* 不下載模型。
* 展示 image embedding shape。
* 展示 text embedding shape。
* 展示每個 label 對應的文字向量。
* 說明為什麼圖片與文字需要轉成同維度向量才能比較。

---

### demo_02_cosine_similarity.py

目的：展示 cosine similarity 的計算流程。

要求輸出：

* dot product（內積）
* norm（向量長度）
* cosine similarity
* 每個文字標籤與圖片向量的相似度排序

---

### demo_03_zero_shot_classification.py

目的：用假向量展示 zero-shot classification 流程。

文字標籤可使用：

```text
a photo of a robot
a photo of a dog
a photo of a red apple
a photo of a laboratory
a photo of a chair
```

要求輸出：

* 每個 label 的 similarity score
* softmax 後的 probability
* top-1 prediction

---

### demo_04_clip_flow.py

目的：整合展示 CLIP 資料流。

要求輸出：

```text
Image -> Image Encoder -> Image Embedding
Text Labels -> Text Encoder -> Text Embeddings
Similarity Matrix
Prediction
```

---

### demo_05_real_clip_zero_shot.py

目的：使用真實 CLIP 模型做 zero-shot classification。

此 demo 是 optional / advanced（選做 / 進階），不得阻塞 Week02 基礎學習。

優先使用 Hugging Face Transformers 載入：

```text
openai/clip-vit-base-patch32
```

支援執行方式：

```bash
python demo/demo_05_real_clip_zero_shot.py
python demo/demo_05_real_clip_zero_shot.py --image assets/sample_image.jpg
```

若未提供 `--image`，程式可以使用預設測試圖片，或自動下載一張公開可存取圖片。若自動下載圖片，請在程式註解與 `demo_README.md` 說明圖片來源。

文字標籤可使用：

```text
a photo of a robot
a photo of a dog
a photo of a red apple
a photo of a laboratory
a photo of a chair
```

要求輸出：

```text
Model: openai/clip-vit-base-patch32
Image path: ...
Labels:
- ...
Probabilities:
- label: probability
Top-1 prediction: ...
```

錯誤處理要求：

* 若缺少 `torch`、`transformers`、`PIL` 或 `requests`，請提示安裝方式。
* 若模型下載失敗，請提示先執行 NumPy concept demos。
* 若圖片路徑不存在，請提示使用者放入圖片或改用預設範例。
* 不得因 real CLIP demo 失敗導致整個 Week02 建置被視為失敗。

---

### demo_README.md

請逐一列出：

* Demo 名稱
* 對應概念
* 執行指令
* 預期輸出
* 觀察重點
* 與 Week02 CLIP 的關係
* 與 VLM / VLA 的關係

請分成：

```markdown
## NumPy Concept Demo
```

以及：

```markdown
## Real CLIP Demo（Optional / Advanced）
```

並清楚說明 real CLIP demo 會下載模型、需要網路、CPU 可跑但較慢、可能需要較長執行時間。

---

### demo/requirements.txt

請建立：

```text
numpy
torch
transformers
pillow
requests
```

並在 `demo_README.md` 說明：

* 只跑 `demo_01` 到 `demo_04` 時只需要 NumPy。
* 跑 `demo_05_real_clip_zero_shot.py` 時才需要 torch、transformers、pillow、requests。
* 第一次執行 real CLIP demo 會下載模型。

---

## 8. Practice 要求

Week02 採用 Guided Code Reading Mode。

### practice/README.md

請說明：

* 本週 practice 是 Week02 的練習入口。
* Concept Practice 用於確認觀念。
* Coding Practice 用於觀察 CLIP 資料流與 shape。
* Guided Demos 是完整可執行程式，不要求學生補空。
* Coding Observation Key 是觀察方向，不是唯一標準答案。

不得使用 `exercises/`、`solutions/` 或 TODO 補空題。

---

### practice/concept/concept_practice.md

請建立 8 題觀念題，至少包含：

1. CLIP 的基本任務是什麼？
2. Image Encoder 與 Text Encoder 分別做什麼？
3. 什麼是共同向量空間？
4. Cosine Similarity 在 CLIP 中的用途是什麼？
5. Zero-shot Classification 的流程是什麼？
6. Contrastive Learning 的直覺是什麼？
7. CLIP 和一般分類模型差在哪？
8. CLIP 與 VLM / VLA 的關係是什麼？

每題都要包含：

```markdown
學生作答：

自我檢查：
- [ ] ...
- [ ] ...
```

不得替學生填入答案。

---

### practice/concept/concept_answer_key.md

請提供參考答案。

開頭必須提醒：

```markdown
> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。
```

參考答案應說明概念、常見誤解與推理方式。

---

### practice/coding/README.md

請說明：

* 本週採用 Guided Code Reading Mode。
* guided demos 的執行方式。
* 安裝方式。
* 觀察重點。
* 不需要從零實作 CLIP。
* 不需要補 TODO。
* 若後續要進入實作週次，才會使用 Implementation Practice Mode。

---

### practice/coding/requirements.txt

請建立：

```text
numpy
```

---

### practice/coding/coding_practice.md

請建立 guided demos 的練習索引與學生觀察紀錄表。

內容至少包含：

* 練習清單
* 採用的 Coding Practice 模式
* 對應 guided demos
* 執行方式
* 學習目標
* 學生觀察欄位
* 錯誤紀錄欄位
* 自我檢查項目

不得放完整答案。

---

### practice/coding/coding_observation_key.md

請提供觀察方向，不是唯一標準答案。

內容可包含：

* vector similarity 應觀察什麼
* image-text alignment 應觀察什麼
* zero-shot probabilities 應觀察什麼
* CLIP pipeline 應觀察什麼
* 常見 shape 誤解
* 常見 cosine similarity 誤解
* 常見 zero-shot 誤解

---

### guided_demos

請建立以下完整可執行程式：

```text
practice/coding/guided_demos/
├── 01_vector_similarity_reading.py
├── 02_text_image_alignment_reading.py
├── 03_zero_shot_reading.py
└── 04_clip_pipeline_reading.py
```

每個檔案都必須：

* 有清楚 docstring
* 有 `main()`
* 有 `if __name__ == "__main__": main()`
* 有中間值 print
* 有 shape print
* 有 step-by-step comments
* 能對應 `notes.md` 中的概念與資料流

---

## 9. study_log.md 要求

請建立 Week02 的學習紀錄模板。

注意：不得假裝學生已完成任何項目。所有任務、Demo 與 Practice 預設未完成。

內容至少包含：

```markdown
# Week02 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 閱讀進度

- [ ] README.md
- [ ] weekly_plan.md
- [ ] notes.md
- [ ] demo/demo_README.md

## Demo 執行結果

| Demo | 是否執行 | 問題／觀察 |
|---|---|---|
| demo/demo_01_text_image_embedding.py |  |  |
| demo/demo_02_cosine_similarity.py |  |  |
| demo/demo_03_zero_shot_classification.py |  |  |
| demo/demo_04_clip_flow.py |  |  |
| demo/demo_05_real_clip_zero_shot.py | optional / advanced |  |

## Practice 結果摘要

| Practice | 是否完成 | 重要觀察 | 疑問 |
|---|---|---|---|
| Concept Practice |  |  |  |
| Guided Code Reading |  |  |  |

## 本週理解摘要

### 我目前能解釋

-

### 我仍不理解

-

### 下週前要釐清

-

## 個人概念紀錄

### CLIP

-

### Image Encoder

-

### Text Encoder

-

### Shared Embedding Space

-

### Cosine Similarity

-

### Zero-shot Classification

-

### Contrastive Learning

-

### CLIP 與 VLM / VLA 的關係

-

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

-

## 一分鐘回顧

請用自己的話總結本週核心資料流、架構或概念。

## 下週目標

-
```

---

## 10. 執行與驗證

建立完成後，請執行以下 NumPy demos：

```bash
python learning/Week02_CLIP/demo/demo_01_text_image_embedding.py
python learning/Week02_CLIP/demo/demo_02_cosine_similarity.py
python learning/Week02_CLIP/demo/demo_03_zero_shot_classification.py
python learning/Week02_CLIP/demo/demo_04_clip_flow.py
```

請執行以下 guided demos：

```bash
python learning/Week02_CLIP/practice/coding/guided_demos/01_vector_similarity_reading.py
python learning/Week02_CLIP/practice/coding/guided_demos/02_text_image_alignment_reading.py
python learning/Week02_CLIP/practice/coding/guided_demos/03_zero_shot_reading.py
python learning/Week02_CLIP/practice/coding/guided_demos/04_clip_pipeline_reading.py
```

Real CLIP demo 可選擇性執行：

```bash
python learning/Week02_CLIP/demo/demo_05_real_clip_zero_shot.py
```

若 real CLIP demo 因套件、網路、模型下載或硬體限制無法執行，請回報原因即可，不要視為 Week02 建置失敗。

---

## 11. 完成後回報格式

請用以下格式回報：

```markdown
## Week02_CLIP 建置結果

### 已讀取並遵守的規範
- AGENTS.md：已讀取 / 未找到 / 有衝突，說明：

### 新增檔案
- ...

### NumPy Concept Demo 執行狀態
- demo_01_text_image_embedding.py：
- demo_02_cosine_similarity.py：
- demo_03_zero_shot_classification.py：
- demo_04_clip_flow.py：

### Real CLIP Demo 執行狀態
- demo_05_real_clip_zero_shot.py：

### Guided Demo 執行狀態
- 01_vector_similarity_reading.py：
- 02_text_image_alignment_reading.py：
- 03_zero_shot_reading.py：
- 04_clip_pipeline_reading.py：

### 是否有未完成項目
- ...

### 建議學生下一步
- ...
```

請開始建立 `learning/Week02_CLIP/`。
