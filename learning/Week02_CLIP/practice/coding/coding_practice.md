# Week02 Coding Practice（觀察任務）

本檔案是 Guided Code Reading Mode 的練習索引與學生紀錄表，不要求補寫程式碼。

## 練習清單

| 順序 | Guided Demo | 學習目標 | 執行結果 |
|---|---|---|---|
| 1 | `guided_demos/01_vector_similarity_reading.py` | 追蹤內積、norm、正規化與餘弦相似度 |  |
| 2 | `guided_demos/02_text_image_alignment_reading.py` | 理解圖文 embedding 與相似度矩陣 shape |  |
| 3 | `guided_demos/03_zero_shot_reading.py` | 追蹤 logits、Softmax 與 top-1 |  |
| 4 | `guided_demos/04_clip_pipeline_reading.py` | 串接 Encoder、投影、正規化與圖文配對 |  |

## 執行方式

```powershell
python practice/coding/guided_demos/01_vector_similarity_reading.py
python practice/coding/guided_demos/02_text_image_alignment_reading.py
python practice/coding/guided_demos/03_zero_shot_reading.py
python practice/coding/guided_demos/04_clip_pipeline_reading.py
```

## 學生觀察欄位

### 1. Vector Similarity

- 兩個向量的 shape：
- 正規化前後的 norm：
- dot product 與 cosine similarity 的關係：
- 修改第二個向量後的變化：

### 2. Image-Text Alignment

- image/text embeddings 的 shape：
- similarity matrix 的 shape：
- 每一列與每一欄分別代表：
- 哪些位置是預期正配對：

### 3. Zero-shot Classification

- similarity scores 的 shape：
- Softmax 使用的 axis：
- probability 每列總和：
- 修改 prompt 後的變化：

### 4. CLIP Pipeline

- 原始特徵與 projection 後 shape：
- L2 normalization 的作用：
- image-to-text 與 text-to-image 矩陣關係：
- 對角線分數代表：

## 錯誤紀錄

| 日期 | 檔案 | 錯誤訊息 | 修正方式 | 尚未解決 |
|---|---|---|---|---|
|  |  |  |  |  |

## 自我檢查

- [ ] 我能說明 embedding 維度為何必須一致。
- [ ] 我能解釋相似度矩陣每個軸的意義。
- [ ] 我能說明 Softmax 軸向錯誤會造成什麼結果。
- [ ] 我能說明 top-1 是候選集合內的最高分。
- [ ] 我能指出正配對在相似度矩陣中的位置。
- [ ] 我已將自己的觀察寫入 `study_log.md`。
