# Week02 Coding Observation Key

> 請先執行 Guided Demos 並完成自己的觀察，再閱讀本頁。本頁提供觀察方向，不是唯一標準答案。

## Vector Similarity

- 同維度向量才能逐項運算與計算內積。
- L2 normalization 後，每個向量的 norm 應接近 1。
- 對單位向量而言，dot product 等於 cosine similarity。
- 向量整體放大時，原始內積會改變，但餘弦相似度可保持不變。

## Image-Text Alignment

- 若 image embeddings shape 是 `(2, 3)`，text embeddings shape 是 `(3, 3)`，相乘時使用文字矩陣轉置，輸出為 `(2, 3)`。
- row 代表圖片，column 代表文字；每格表示一個圖文配對分數。
- 若資料依正配對順序排列，對角線通常是訓練希望提高的位置。

## Zero-shot Probabilities

- 一張圖片對五個標籤時，score shape 常為 `(1, 5)`。
- Softmax 應沿 label 軸執行，使每張圖片的候選機率加總為 1。
- 機率是候選集合內的相對分布；新增、刪除或改寫 prompt 都可能改變結果。

## CLIP Pipeline

- Image Encoder 與 Text Encoder 可先輸出不同特徵維度，再由 projection 映射到相同 `embedding_dim`。
- 正規化後的矩陣相乘建立所有圖文配對分數。
- image-to-text matrix 與 text-to-image matrix 互為轉置，但各自做 Softmax 時軸向與任務方向不同。

## 常見 Shape 誤解

- `(label_count, embedding_dim)` 中，label 數不是向量維度。
- `image_embeddings @ text_embeddings` 通常無法直接相乘；需要 `text_embeddings.T`。
- 一維 `(embedding_dim,)` 與二維 `(1, embedding_dim)` 會影響輸出 shape。

## 常見 Cosine Similarity 誤解

- Cosine similarity 不是距離單位，也不是未經轉換的機率。
- 只比較方向會忽略長度資訊；這是設計選擇，不是所有任務都一定最佳。
- 零向量不能正規化，實務上需避免除以零。

## 常見 Zero-shot 誤解

- Zero-shot 不代表模型從未在預訓練資料見過相關概念。
- Top-1 只表示目前候選中最高，不代表候選一定包含正確答案。
- Prompt wording（提示詞措辭）會影響文字 embedding 與最後分數。
