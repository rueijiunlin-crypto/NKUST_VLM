# Week01 Coding Answer Key（程式參考說明）

> 請先完成 exercises/ 中的練習檔案，再查看本程式練習參考說明。

## 1. token_practice.py

TODO 重點是建立 vocabulary（詞彙表）、把 token 轉成 Token ID，再用 ID 還原 token。常見錯誤是直接把字串當成模型輸入，或以為 ID 的大小代表語意大小。

## 2. embedding_practice.py

TODO 重點是用 Token ID 對 embedding table 做索引。輸入 shape 通常是 `(seq_len,)`，輸出會變成 `(seq_len, embedding_dim)`。常見錯誤是把 one-hot、Token ID 與 Embedding 混在一起。

## 3. qkv_practice.py

TODO 重點是用同一個輸入 `x` 乘上三組不同權重，得到 Q、K、V。若 `x` 是 `(seq_len, d_model)`，權重是 `(d_model, d_k)`，輸出就是 `(seq_len, d_k)`。

## 4. attention_matrix_practice.py

TODO 重點是計算 `scores = Q @ K.T / sqrt(d_k)`，再沿最後一個軸做 softmax。若 Q 和 K 都是 `(seq_len, d_k)`，則 `Q @ K.T` 是 `(seq_len, seq_len)`。

常見錯誤：

- 忘記轉置 K，導致 shape 不一致。
- softmax 軸向錯誤，導致不是每個 query 對所有 key 的分布。
- 忘記除以 `sqrt(d_k)`，分數可能過大。

## 5. self_attention_practice.py

TODO 重點是先由 `x` 產生 Q、K、V，再計算 attention weights，最後 `weights @ V`。輸出 shape 應回到 `(seq_len, d_v)`。

## 6. position_encoding_practice.py

TODO 重點是建立和 embedding 相同 shape 的位置資訊，然後相加。常見錯誤是位置編碼 shape 無法 broadcast（廣播）到 embedding shape。

## 7. multi_head_attention_practice.py

TODO 重點是把 `d_model` 拆成多個 head，每個 head 有 `head_dim = d_model // num_heads`。常見錯誤是 `d_model` 不能被 `num_heads` 整除，或 reshape 後的軸順序錯誤。

## 8. encoder_decoder_practice.py

TODO 重點是用簡化流程理解 Encoder 負責產生輸入表示，Decoder 使用自己的輸入並參考 Encoder 輸出。常見錯誤是把 Encoder 輸出與 Decoder 輸入混成同一件事。
