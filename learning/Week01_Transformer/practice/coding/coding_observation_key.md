# Week01 Coding Observation Key（觀察指引）

本文件不是標準答案。它提供觀察重點、shape 變化與常見誤解，協助檢查是否沿著正確資料流閱讀程式。

## 1. Token / Embedding

觀察重點：

* Token ID 是查表索引，不是語意向量。
* Embedding lookup 會把 `(sequence_length,)` 轉成 `(sequence_length, embedding_dim)`。
* 相同 Token ID 會查到相同的初始 Embedding。

常見誤解：

* Token ID 數字較接近，不代表語意較接近。
* Embedding table 的列數是 vocabulary size，不是句子長度。

## 2. Position Encoding

觀察重點：

* Position Encoding 與 Token Embedding shape 相同，才能逐元素相加。
* 相加不會增加新的軸，輸出仍是 `(sequence_length, embedding_dim)`。
* 位置訊號讓相同內容在不同位置具有不同表示。

常見誤解：

* Position Encoding 不是 Token ID。
* 位置資訊不是串接在 Embedding 後方，本例使用逐元素相加。

## 3. QKV

資料流：

```text
X(sequence_length, d_model)
@ W(d_model, projection_dim)
-> Q / K / V(sequence_length, projection_dim)
```

觀察重點：

* Q、K、V 來自同一輸入，但使用不同投影矩陣。
* Q 與 K 負責比對，V 保存要被加權取用的內容。

常見誤解：

* Q、K、V 不是三份原封不動的 Embedding。
* 調整 Value 投影不會直接改變 Q 與 K。

## 4. Self-Attention

shape 變化：

```text
Q(sequence_length, d_k)
@ K.T(d_k, sequence_length)
-> scores(sequence_length, sequence_length)
-> weights(sequence_length, sequence_length)
@ V(sequence_length, d_v)
-> context(sequence_length, d_v)
```

觀察重點：

* Attention Matrix 的列代表 Query，欄代表 Key。
* Softmax 沿最後一軸計算，因此每列權重加總接近 1。
* Attention 輸出是所有 Value 的加權組合，不只是取最大值。

## 5. Multi-Head Attention

shape 變化：

```text
(sequence_length, d_model)
-> (num_heads, sequence_length, head_dim)
-> 每個 head 分別做 Attention
-> (sequence_length, d_model)
```

觀察重點：

* `d_model` 必須可被 `num_heads` 整除。
* head 數增加時，每個 head 的維度通常會縮小。
* concat 只負責合併各 head，真實模型通常還會再做輸出投影。

## 6. Encoder / Decoder

觀察重點：

* Encoder memory 保存來源序列的上下文表示。
* Decoder Query 數量決定 Cross-Attention 輸出的序列長度。
* Cross-Attention 的 Key 與 Value 來自 Encoder memory，Query 來自 Decoder。

常見誤解：

* Encoder 不是把整段輸入壓成單一數字。
* Decoder 不只是複製 Encoder 輸出，而是根據自己的 Query 選擇 context。

## 整體檢查方向

若能沿著每個程式回答以下問題，就已掌握本練習的主要目的：

1. 每一步的輸入與輸出 shape 是什麼？
2. 哪一個矩陣乘法改變了最後一個維度？
3. 哪一步建立 Token 彼此之間的關係？
4. 哪一步把權重轉成新的上下文表示？
5. 修改小參數時，變化如何沿著後續資料流傳遞？
