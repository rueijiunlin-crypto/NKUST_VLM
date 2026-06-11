# Week01 Coding Practice（觀察任務）

本檔案不要求補寫程式碼。請執行完整範例、追蹤 shape（張量形狀）、觀察中間值，並用自己的話記錄資料如何流動。

## 執行順序

| 順序 | Guided Demo | 觀察主題 | 執行結果 |
|---|---|---|---|
| 1 | `guided_demos/01_token_embedding_reading.py` | 文字到 Embedding |  |
| 2 | `guided_demos/02_position_encoding_reading.py` | 加入位置資訊 |  |
| 3 | `guided_demos/03_qkv_reading.py` | 線性投影產生 Q、K、V |  |
| 4 | `guided_demos/04_self_attention_reading.py` | 分數、權重與上下文 |  |
| 5 | `guided_demos/05_multi_head_attention_reading.py` | 拆 head 與合併 head |  |
| 6 | `guided_demos/06_encoder_decoder_reading.py` | Encoder memory 與 Decoder 取用 |  |

## 觀察任務

### 1. Token、Token ID 與 Embedding

執行：

```bash
python guided_demos/01_token_embedding_reading.py
```

記錄：

* Token ID 的 shape。
* Embedding table 與查表結果的 shape。
* 重複 Token 是否取得相同的初始向量。
* 將句子中的 `robot` 改成 `camera` 後，詞彙表與 ID 如何改變。

### 2. Position Encoding

執行：

```bash
python guided_demos/02_position_encoding_reading.py
```

記錄：

* Token Embedding、Position Encoding 與相加後結果的 shape。
* 同一個向量放在不同位置後為何不再相同。
* 將 `SEQUENCE_LENGTH` 改為 `4` 後，新增了哪些位置資訊。

### 3. QKV 投影

執行：

```bash
python guided_demos/03_qkv_reading.py
```

記錄：

* 輸入 `X` 與 Q、K、V 的 shape。
* 權重矩陣如何改變最後一個維度。
* 修改 `W_V` 的縮放值後，哪一個結果會直接改變。

### 4. Self-Attention

執行：

```bash
python guided_demos/04_self_attention_reading.py
```

記錄：

* `Q @ K.T` 為何得到方形矩陣。
* Softmax 後每列加總是否接近 1。
* 每個 Query 最關注哪一個 Key。
* 修改第一個輸入向量後，分數、權重與輸出如何連動。

### 5. Multi-Head Attention

執行：

```bash
python guided_demos/05_multi_head_attention_reading.py
```

記錄：

* `d_model`、`NUM_HEADS` 與 `head_dim` 的關係。
* split heads 前後各軸代表什麼。
* 將 `NUM_HEADS` 改為 `4` 後，head_dim 如何變化。
* 合併後為何能回到原本的 `d_model`。

### 6. Encoder / Decoder

執行：

```bash
python guided_demos/06_encoder_decoder_reading.py
```

記錄：

* Encoder input 與 Encoder memory 的 shape。
* Decoder Query 如何對 Encoder memory 產生權重。
* Cross-Attention 輸出如何保留 Decoder 序列長度。
* 修改 Decoder Query 後，權重分布如何改變。

## 整體資料流

執行全部程式後，用自己的話補完：

```text
文字
-> Token
-> Token ID
-> Embedding
-> 加入 Position Encoding
-> 產生 Q、K、V
-> 計算 Attention Weights
-> 加權 Value
-> Multi-Head 組合
-> Encoder memory
-> Decoder 取用 context
```

## 執行紀錄

| 日期 | 檔案 | 修改的參數 | 觀察到的變化 | 尚未理解 |
|---|---|---|---|---|
|  |  |  |  |  |
