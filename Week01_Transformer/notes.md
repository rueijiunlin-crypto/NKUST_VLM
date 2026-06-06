# Week01 Notes：Transformer 基礎

## Token（詞元）

Token 是模型處理文字時的基本單位。它可能是一個字、一個詞，或是一段子詞。模型不直接理解原始文字，而是先把文字切成 Token，再轉成數字編號。

## Embedding（嵌入向量）

Embedding 是 Token 的向量表示。它的作用是把離散的文字單位轉成可以計算的數值空間，讓語意相近的內容在向量空間中更容易被模型比較。

## Attention（注意力機制）

Attention 讓模型在處理某個 Token 時，可以判斷其他 Token 對它有多重要。直覺上，它是在回答：「我現在理解這個詞時，應該看句子中的哪些部分？」

## Transformer Encoder（轉換器編碼器）

Encoder 主要用於理解輸入內容。它會接收一整段輸入，透過 Attention 建立上下文表示。CLIP 的文字編碼器與影像編碼器都可以用類似的表示學習概念來理解資料。

## Transformer Decoder（轉換器解碼器）

Decoder 主要用於產生輸出內容，例如回答問題或生成描述。許多大型語言模型會使用 Decoder 架構，根據前面的上下文逐步產生下一個 Token。

## 為什麼 VLM 需要 Transformer

VLM 需要同時處理影像與文字。Transformer 擅長建立不同元素之間的關係，因此可以用來理解文字 Token、影像 Patch（影像切塊），以及兩者之間的語意對齊。這使得模型能回答「圖片中有什麼」、「物體在哪裡」或「這個場景適合執行什麼任務」等問題。

## 與 CLIP 的銜接

CLIP 的核心概念是把圖片與文字放到共同向量空間中比較相似度。要理解 CLIP，需要先理解 Embedding 與 Attention 如何產生可比較的表示。
