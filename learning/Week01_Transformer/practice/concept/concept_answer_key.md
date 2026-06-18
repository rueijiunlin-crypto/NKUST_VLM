# Week01 Concept Answer Key（觀念參考答案）

> 請先完成 concept_practice.md 的作答，再查看本參考答案。

## Q1 Token、Token ID 與 Embedding

Token 是文字被切分後的單位，例如字、詞或子詞。Token ID 是把 token 對應到詞彙表中的整數編號。Embedding 是根據 Token ID 查表或計算得到的向量，模型實際處理的是向量，不是原始文字或整數本身。

常見錯誤是把 Token ID 當成語意向量。Token ID 只是索引，數字大小通常不代表語意距離。

## Q2 Query、Key、Value

Query 表示目前位置想找什麼資訊，Key 表示各位置提供什麼線索，Value 表示真正會被加權取出的內容。Attention 會用 Query 和 Key 計算相似度，再用 softmax 轉成權重，最後對 Value 做加權加總。

## Q3 Attention Matrix

Attention Matrix 的第 i 列通常表示第 i 個 token 對所有 token 的注意力分布。若 softmax 沿錯誤軸向計算，權重可能變成每一欄加總為 1，而不是每個 query 對所有 key 的分布，會造成語意解讀錯誤。

## Q4 Self-Attention

Self-Attention 是 Q、K、V 都來自同一個序列的 Attention。它讓序列中每個位置都能參考其他位置，因此模型能捕捉上下文關係。

## Q5 Position Encoding

Transformer 的 Attention 主要根據 token 之間的相似度運作，本身不直接包含順序資訊。Position Encoding 會把位置資訊加入 embedding，讓模型知道 token 的相對或絕對位置。

## Q6 Multi-Head Attention

Multi-Head Attention 會把表示拆成多個 head，讓不同 head 可以關注不同關係，例如局部相鄰、長距依賴或語意角色。各 head 的輸出通常會串接，再經過線性投影回模型維度。

## Q7 Encoder 與 Decoder

Encoder 主要負責理解輸入序列，輸出上下文化表示。Decoder 主要負責根據已產生內容與必要的上下文逐步產生輸出。在生成任務中，Decoder 通常會使用 mask 避免看到未來 token。

## Q8 Transformer 與 VLM / CLIP

VLM 需要同時處理文字與影像。Transformer 可作為文字 encoder，也可處理影像 patch 序列。CLIP 透過文字 encoder 和影像 encoder 取得兩種 embedding，並訓練它們在共同空間中對齊。
