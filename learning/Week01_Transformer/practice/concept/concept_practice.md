# Week01 Concept Practice（觀念練習）

請先閱讀 `notes.md` 並觀察 `demo/` 後再作答。本檔案是學生觀念作答檔，請保留自己的推理過程。

## Q1 Token、Token ID 與 Embedding

請用自己的話說明 Token（詞元）、Token ID（詞元識別碼）與 Embedding（嵌入向量）的差異。

學生作答：

- token是將句子拆分後的單位
- token id則是一個索引，連接token與embedding
- 嵌入向量則是將token轉換成機器能肉理解的數字向量

自我檢查：

- [✅] 我能分辨文字切分結果、整數索引與向量表示。
- [✅] 我沒有把 Token ID 當成 Embedding。

## Q2 Query、Key、Value

請說明 Query（查詢）、Key（鍵）與 Value（值）在 Attention（注意力機制）中的角色。

學生作答：

- Q代表我現在要找甚麼?
- K代表我要找的token與token之間的關聯性有多少?
- V代表該token裡面實際有的內容

自我檢查：

- [✅] 我能說明 Query 和 Key 如何產生分數。
- [✅] 我能說明 Value 為什麼會被加權加總。

## Q3 Attention Matrix

Attention Matrix（注意力矩陣）中的每一列通常代表什麼？為什麼 softmax（歸一化指數函數）的軸向很重要？

學生作答：

- 代表每一個token看其他token時的權重分數
 修正版:某一個 token 在理解自己時，對其他所有 token 的注意力分布
- 因為 attention score 必須沿著正確方向正規化。通常是對每一列做 softmax，讓同一個 Query token 對所有 Key token 的注意力權重加總為 1，形成可解釋的注意力分布。

自我檢查：

- [✅] 我能說明每一列加總應接近 1。
- [✅] 我能指出錯誤軸向會造成錯誤的注意力分布。

## Q4 Self-Attention

Self-Attention（自注意力）和一般 Attention 的差異是什麼？

學生作答：

- 修正版:Self-Attention（自注意力）是 Attention 的一種形式，差別在於 Self-Attention 的 Q、K、V 都來自同一個輸入序列。

一般 Attention 可以讓不同序列互相參考，例如 Decoder 參考 Encoder 的輸出；Self-Attention 則是讓同一句話中的 token 彼此參考。

因此 Self-Attention 可以讓序列中不同位置的 token 建立上下文關係，例如 laboratory 可以注意到 take me to，進而理解它是句子中的目標地點。


自我檢查：

- [✅] 我能說明 Q、K、V 來自同一序列時的意義。
- [✅] 我能說明它如何讓序列內不同位置互相參考。

## Q5 Position Encoding

為什麼 Transformer（轉換器）需要 Position Encoding（位置編碼）？

學生作答：

- 轉換器他沒只能把句子拆成一個一個的token，如果沒有位置編碼他沒辦法有順序的概念，無法讓他有上下文的概念

- 修正版:Transformer 的 Attention 本身主要根據 token 向量之間的相似度建立關係，但它不直接知道 token 的先後順序。因此如果沒有 Position Encoding，模型雖然能比較 token 之間的關聯，卻無法分辨同一批 token 的排列順序差異。

Position Encoding 的作用是把位置資訊加入 Embedding，讓模型在做 Attention 時，同時能利用語意資訊與順序資訊。例如「robot follows person」和「person follows robot」包含類似 token，但順序不同，語意也不同。

自我檢查：

- [✅] 我能說明注意力本身不直接知道順序。
- [✅] 我能說明位置資訊如何補進 token 表示。

## Q6 Multi-Head Attention

Multi-Head Attention（多頭注意力）為什麼要拆成多個 head（注意力頭）？

學生作答：

- 為了讓他可以應對不同的分類，當搜尋的目標不同時，token的權重分數都會不同

- 修正版:Multi-Head Attention（多頭注意力）會把 attention 拆成多個 head（注意力頭），讓模型可以同時從不同角度學習 token 之間的關係。

不同 head 會使用不同的 Q、K、V 參數，因此每個 head 看到的關聯重點可能不同。例如有的 head 可能關注動作與目標的關係，有的 head 可能關注修飾詞與名詞的關係，有的 head 可能關注長距離上下文。

最後，每個 head 得到的輸出會被 concat（串接）起來，再經過 linear layer（線性層）整合成最後的 attention 輸出。

自我檢查：

- [✅] 我能說明不同 head 可關注不同關係。
- [✅] 我能說明最後需要 concat（串接）或投影回共同維度。

## Q7 Encoder 與 Decoder

請比較 Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）的用途。

學生作答：

- 編碼器主要是讓輸入的文字可以轉換成機器能夠理解的向量，解碼器則負責結合輸入的內容以及任務目標，去預測要回復給用戶的token

自我檢查：

- [✅] 我能說明 Encoder 偏向理解輸入。
- [✅] 我能說明 Decoder 偏向逐步產生輸出。

## Q8 Transformer 與 VLM / CLIP

請說明 Transformer 和 Vision-Language Model（視覺語言模型，VLM）以及 CLIP（對比式圖文預訓練）的關係。

學生作答：

- 編碼器的的用途是將文字或是圖片進行拆解並且轉換成機器能夠讀取的向量，vlm是根據讀取到的圖片以及任務目標進行編碼，並且最後透過解碼器輸出或是給其他機構進行端對端的指令，CLIP則是將文字或圖片進行編碼，編碼完成後去對比已訓練好的模型數據庫，找到該目標對應的圖片或是文字
- 修正版:Transformer 是許多 VLM 與 CLIP 的基礎。文字可以被切成 token 並轉成 embedding，影像也可以被切成 patch 或轉成影像特徵，最後都能形成向量表示。

VLM 會結合影像與文字資訊，讓模型能根據圖片內容與文字任務進行回答、描述或推理。CLIP 則使用 Image Encoder 和 Text Encoder，分別把圖片與文字轉成向量，並把它們對齊到共同向量空間。推論時，CLIP 不是查資料庫，而是比較圖片向量與文字向量的相似度，找出最匹配的文字描述或圖片。

自我檢查：

- [✅] 我能說明文字與影像都可被轉成序列表示。
- [✅ ] 我能說明 CLIP 如何使用文字與影像 encoder 做對齊。
