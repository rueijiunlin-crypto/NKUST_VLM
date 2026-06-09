# Week01 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 閱讀進度

- [x] README.md
- [ ] weekly_plan.md
- [ ] notes.md
- [ ] demo/demo_README.md

## Demo（示範程式）執行結果

| Demo | 是否執行 | 結果 | 問題 |
|---|---|---|---|
| demo/token/demo_tokenizer.py | [x] | 透過分詞器將句子分成 Token，並賦予編號。 | 無 |
| demo/embedding/demo_embedding.py | [x] | 將分類好的 Token 轉換為數字向量。 | 無 |
| demo/qkv/demo_qkv.py | [x] | 將數字向量轉換成 Q、K、V 三種向量，供注意力機制使用。 | 無 |
| demo/attention/demo_attention.py | [x] | 在一句話中根據任務找出關聯較高的 Token。 | 無 |
| demo/attention/demo_attention_matrix.py | [ ] |  |  |
| demo/self_attention/demo_self_attention.py | [ ] |  |  |
| demo/position_encoding/demo_position_encoding.py | [ ] |  |  |
| demo/multi_head_attention/demo_multi_head_attention.py | [ ] |  |  |
| demo/encoder_decoder/demo_encoder_decoder_flow.py | [ ] |  |  |

## 個人概念紀錄

### Token（詞元）

文字的標籤，可透過分詞器將句子分小塊，並且賦予可對照的 ID。

修正版：Token 是模型處理文字的基本單位。原始文字無法直接送入 Transformer（轉換器架構），因此需要先透過 Tokenizer（分詞器）將句子切分成較小的單位，並轉換成對應的 Token ID（詞元編號）。

### Embedding（嵌入向量）

將 Token 轉換成機器可理解的數字向量。

修正版：Embedding 是 Token 的數學表示方式。每個 Token 都會被映射成高維向量，例如 DistilBERT 中每個 Token 會被轉換成 768 維向量。Transformer 並不是直接處理文字，而是處理這些 Embedding 向量。因此 Embedding 可以理解成 Token 的語意座標。

### Query（查詢）

我想找什麼。Q = E * Wq，Wq 由模型訓練而來，讓嵌入向量 E 變成搜尋模式。目前這個 Token 在理解自身時，希望從其他 Token 身上找到哪些資訊。

### Key（鍵）

我能提供什麼。K = E * Wk，讓嵌入向量 E 變成提供模式。每個 Token 的索引標籤，模型會利用 Query 與所有 Key 比較相似度，判斷哪些 Token 值得關注。

### Value（值）

我實際上是什麼。V = E * Wv，是真實攜帶的資訊。

### QKV 的關係

Q（Query）：我想找什麼資訊。

K（Key）：我有哪些資訊可以提供。

V（Value）：我真正攜帶的資訊內容。

Transformer 會先利用 Q x K^T 計算 Attention Score（注意力分數），再利用分數對 Value 加權。因此 Attention 的重點不是找到 Key，而是利用 Key 找到最有價值的 Value。

### Q x K^T

Q 與 K 的內積代表兩者的相似程度。Transformer 會利用 Query 與所有 Key 計算相似度。相似度越高，代表這個 Token 越值得關注。因此 Q x K^T 可以理解為 Attention Score 的來源。

### Softmax（柔性最大化函數）

Softmax 會把 Attention Score 轉換成權重分布。

1. 每個分數先做 e^x，放大數字差距，讓重要的 Token 得以突出。
2. 所有結果加總。
3. 每個值除以總和。

轉換後所有注意力權重加總為 1，因此可以理解為每個 Token 被關注的比例。

### Score x V

Softmax 產生的權重只代表關注程度。真正的資訊內容存在於 Value。Transformer 會利用權重對各個 Value 加權平均。因此 Attention 的目的不是找出最重要的 Token，而是根據重要程度融合不同 Token 的資訊，產生包含上下文語意的新向量表示。

### Attention（注意力機制）

根據任務從一句話裡面找重點。

修正版：Attention 的目的不是單純找重點，而是讓模型在處理某個 Token 時，決定應該參考哪些 Token。每個 Token 都可能有不同的注意力分布。

完整流程：

```text
Embedding
-> Q, K, V
-> Q x K^T
-> Attention Score
-> Softmax
-> Attention Weight
-> Weighted Sum of V
-> Contextual Representation
```

當注意力轉換完成後，可以讓單獨的 Token 變成包含前後文意思的 Token。

### Attention Matrix（注意力矩陣）

透過轉換矩陣找哪個字跟哪個字比較有關聯。

### Self-Attention（自注意力）

讓同一段輸入中的每個 Token 互相比較。

### Attention 的最終目的

Attention 並不是單純找出重要的 Token，而是利用注意力權重融合其他 Token 的資訊。經過 Attention 後，原本只代表單字本身的 Embedding 會變成包含上下文資訊的新向量表示。因此相同的 Token 在不同句子中也能擁有不同的語意。

### Position Encoding（位置編碼）

賦予token順序，將位置向量與嵌入向量相加後得到

Token Embedding + Position Encoding
→ 帶有位置資訊的輸入向量

### Multi-Head Attention（多頭注意力）

讓每個token可以讀取每個token在幹嘛

讓每個 token 從不同角度去關注其他 token，取得上下文關係。
單頭 attention：
只用一種角度看 token 之間的關係。

多頭 attention：
用多組 Q、K、V 同時看不同關係。

### Transformer Encoder（轉換器編碼器）

讓輸入的內容可以轉換成機器能夠理解的數字向量

更正:將已經轉成向量的 token，進一步加工成具有上下文語意的向量表示。

### Transformer Decoder（轉換器解碼器）

將機器預測要回答的內容轉換為文字並且輸出給用戶看

根據前面已知的內容與 Encoder 輸出的語意資訊，逐步預測下一個 token，最後產生文字輸出。

### 本週與 VLM（視覺語言模型）的關係

理解文字是如何輸入並轉換成電腦可以讀取以及理解的內容

文字如何被切成 token，
token 如何變成 embedding，
embedding 如何透過 attention 和 encoder 形成語意表示，
最後 decoder 如何產生文字回答。

### Transformer 與 CLIP（對比式圖文預訓練）的關係

待完成。

## Notion 更新

- [ ] Learning Roadmap
- [ ] Experiment Log
- [ ] Weekly Review

## ChatGPT 驗收

- [ ] 未驗收
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

## 下週目標

-
