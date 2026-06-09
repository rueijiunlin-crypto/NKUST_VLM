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
* [✅] demo/qkv/demo_qkv.py
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

請用自己的話說明：我想找啥? Q=E*Wq Wq由模型訓練而來
讓嵌入向量E變成搜尋模式
目前這個 Token 在理解自身時，
希望從其他 Token 身上找到哪些資訊。

---

### Key（鍵）

請用自己的話說明：我能提供啥? K=E*Wk 
讓嵌入向量E變成提供模式
每個 Token 的索引標籤。

模型會利用 Query 與所有 Key 比較相似度，
判斷哪些 Token 值得關注。

---

### Value（值）

請用自己的話說明：我實際上是啥 V=E*Wv
真實攜帶的資訊

---

#### QKV 的關係

Q（Query）：
我想找什麼資訊。

K（Key）：
我有哪些資訊可以提供。

V（Value）：
我真正攜帶的資訊內容。

Transformer 會先利用：

Q × Kᵀ

計算 Attention Score（注意力分數）。

再利用分數對 Value 加權。

因此：

Attention 的重點不是找到 Key，

而是利用 Key 找到最有價值的 Value。

---

### Q × Kᵀ

我的理解：

Q 與 K 的內積代表兩者的相似程度。

Transformer 會利用 Query 與所有 Key 計算相似度。

相似度越高，
代表這個 Token 越值得關注。

因此 Q×Kᵀ 可以理解為：

Attention Score 的來源。

---

### Softmax(柔性最大化函數）)

我的理解：

Softmax 會把 Attention Score 轉換成權重分布。

步驟：

1. 每個分數先做 e^x ，為了放大數字的差距，讓重要的token得以突出
2. 所有結果加總
3. 每個值除以總和

轉換後所有(注意力)權重加總為 1。 

因此可以理解為：

每個 Token 被關注的比例。

---

### Score × V

我的理解：

Softmax 產生的權重只代表關注程度。

真正的資訊內容存在於 Value。

Transformer 會利用權重對各個 Value 加權平均。

因此 Attention 的目的不是找出最重要的 Token，

而是根據重要程度融合不同 Token 的資訊，

產生包含上下文語意的新向量表示。

---
### Attention（注意力機制）

請用自己的話說明：根據任務從一句話裡面找重點

修正版:
Attention 的目的不是單純找重點。

而是讓模型在處理某個 Token 時，
決定應該參考哪些 Token。

每個 Token 都可能有不同的注意力分布。

完整流程:
Embedding
-> Q, K, V
-> Q x K^T
-> Attention Score（注意力分數）
-> Softmax（柔性最大化函數）
-> Attention Weight（注意力權重）
-> Weighted Sum of V（加權 Value）
-> Contextual Representation（上下文表示）

當我注意力轉換完成後，他可以讓我單獨的token變成包含前後文意思的token
---

### Attention Matrix（注意力矩陣）

請用自己的話說明：透過轉換矩陣找哪個字跟哪個字比較有關連

---

### Self-Attention（自注意力）

請用自己的話說明：讓她自己比較每個

---

### Attention 的最終目的

我的理解：

Attention 並不是單純找出重要的 Token。

而是利用注意力權重，
融合其他 Token 的資訊。

經過 Attention 後，

原本只代表單字本身的 Embedding，
會變成包含上下文資訊的新向量表示。

因此相同的 Token，
在不同句子中也能擁有不同的語意。

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
