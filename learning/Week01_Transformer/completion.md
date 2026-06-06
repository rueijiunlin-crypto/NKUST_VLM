# Week01 Completion

## 閱讀完成

* [✅] README.md
* [ ] notes.md

---

## Tasks 完成

* [ ] 觀念練習 1
* [ ] 觀念練習 2
* [ ] 觀念練習 3
* [ ] 觀念練習 4
* [ ] Demo 觀察任務
* [ ] 程式練習 1
* [ ] 程式練習 2
* [ ] 程式練習 3

---

## Demo 完成

* [✅] demo/token/demo_tokenizer.py
* [✅] demo/embedding/demo_embedding.py
* [ ] demo/qkv/demo_qkv.py
* [ ] demo/attention/demo_attention.py
* [ ] demo/attention/demo_attention_matrix.py
* [ ] demo/self_attention/demo_self_attention.py
* [ ] demo/position_encoding/demo_position_encoding.py
* [ ] demo/multi_head_attention/demo_multi_head_attention.py
* [ ] demo/encoder_decoder/demo_encoder_decoder_flow.py

---

## 我的理解

### Token（詞元）

請用自己的話說明：文字的標籤，可透過分詞器將句子分小塊，並且賦予他可對照的id

修正版:
Token（詞元）是模型處理文字的基本單位。

原始文字無法直接送入 Transformer（轉換器），
因此需要先透過 Tokenizer（分詞器）將句子切分成較小的單位，
並轉換成對應的 Token ID。

---

### Embedding（嵌入向量）

請用自己的話說明：將token轉換成機器可理解的數字向量

修正版:
Embedding（嵌入向量）是 Token 的數學表示方式。

每個 Token 都會被映射成高維向量，
例如 DistilBERT 中每個 Token 會被轉換成 768 維向量。

Transformer 並不是直接處理文字，
而是處理這些 Embedding 向量。

因此 Embedding 可以理解成：

Token 的語意座標。

---

### Query（查詢）

請用自己的話說明：

---

### Key（鍵）

請用自己的話說明：

---

### Value（值）

請用自己的話說明：

---

### Attention（注意力機制）

請用自己的話說明：

---

### Attention Matrix（注意力矩陣）

請用自己的話說明：

---

### Self-Attention（自注意力）

請用自己的話說明：

---

### Position Encoding（位置編碼）

請用自己的話說明：

---

### Multi-Head Attention（多頭注意力）

請用自己的話說明：

---

### Transformer Encoder（轉換器編碼器）

請用自己的話說明：

---

### Transformer Decoder（轉換器解碼器）

請用自己的話說明：

---

### 本週與 VLM（視覺語言模型）的關係

請用自己的話說明：

---

### Transformer 與 CLIP（對比式圖文預訓練）的關係

請用自己的話說明：

---

## Notion 更新

* [ ] Learning Roadmap
* [ ] Experiment Log
* [ ] Weekly Review

---

## ChatGPT 驗收

* [ ] 未驗收
* [ ] Pass
* [ ] Minor Revision
* [ ] Major Revision

---

## ChatGPT 評語

（由 ChatGPT 填寫）
