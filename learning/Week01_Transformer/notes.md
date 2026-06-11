# Week01 Notes: Transformer 基礎

## 學習主線

Transformer（轉換器架構）可以把一串輸入轉成一串帶有上下文的向量表示。對 Vision-Language Model（視覺語言模型，VLM）與 Vision-Language-Action Model（視覺語言動作模型，VLA）而言，這個能力很重要，因為影像、文字與任務描述都需要被轉成模型可比較、可推理的表示。

本週資料流如下：

```text
Text -> Token -> Token ID -> Embedding -> QKV -> Attention
-> Self-Attention -> Position Encoding -> Multi-Head Attention
-> Transformer Encoder / Transformer Decoder
```

閱讀每個概念後，請回到 [`practice/`](./practice/README.md) 完成對應練習。`demo/` 用來快速觀察概念現象（What），`practice/coding/guided_demos/` 用來追蹤 shape、中間值與內部資料流（How）；Week01 不使用程式補空題。

---

## Token

### Level 1：直覺理解

Token（詞元）是模型讀文字時看到的基本單位。人看到一句話，會直接理解字詞；模型不能直接理解原始文字，所以要先把文字切成較小的片段。

### Level 2：技術原理

Tokenizer（分詞器）會依照詞彙表與切分規則，把文字切成 Token。Token 可能是一個英文單字、一個中文字、一段子詞，或特殊符號。不同模型的 Tokenizer 規則不同，所以同一句話在不同模型中可能被切成不同 Token。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_01_token_embedding.py
```

觀察輸入句子如何被切成 Token，以及每個 Token 如何對應到後續的數字 ID。

### Level 4：Application Relation

在 VLM 中，文字指令會先被切成 Token；影像通常會被切成 Patch（影像切塊）。兩者都是把原始資料轉成序列，讓 Transformer 能處理跨位置、跨模態的關係。

### Level 5：驗收問題

1. Token 和原始文字有什麼差異？
2. 為什麼模型不直接讀完整句子？
3. 同一句話在不同 Tokenizer 中一定會切成相同 Token 嗎？

---

## Token ID

### Level 1：直覺理解

Token ID（詞元編號）是 Token 在詞彙表中的數字代號。模型真正接收的是數字，不是文字本身。

### Level 2：技術原理

Tokenizer 會把每個 Token 查表轉成整數 ID。這些 ID 會再送進 Embedding Table（嵌入表），查出對應的向量。Token ID 本身沒有語意距離，真正的語意表示來自 Embedding。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_01_token_embedding.py
```

觀察 Token 列表與 Token ID 列表是否一一對應。

### Level 4：Application Relation

在 CLIP（對比式圖文預訓練）的文字編碼器中，文字也會經過 Token ID 再轉成向量。理解 Token ID 能幫助 Week02 追蹤文字如何進入共同向量空間。

### Level 5：驗收問題

1. Token ID 是語意本身，還是查表用的索引？
2. 為什麼 Token ID 不能直接拿來計算語意相似度？
3. Token ID 與 Embedding 的關係是什麼？

---

## Embedding

### Level 1：直覺理解

Embedding（嵌入向量）是 Token 的數字向量表示。可以把它想成 Token 在語意空間中的座標。

### Level 2：技術原理

Embedding Table 會把每個 Token ID 對應到一個向量。模型訓練時會調整這些向量，使語意或使用情境相近的 Token 在向量空間中更容易被模型利用。

常見形狀如下：

```text
(batch_size, token_count, embedding_dim)
```

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_01_token_embedding.py
```

觀察 Token 數量、Embedding 維度，以及輸出張量形狀。

### Level 4：Application Relation

VLM 會把文字 Token 與影像 Patch 都轉成向量表示。當資料都變成向量序列後，Transformer 才能用 Attention 建立文字、影像區域與語意之間的關係。

### Level 5：驗收問題

1. Embedding 解決了 Token ID 的什麼限制？
2. Embedding shape 中每個維度代表什麼？
3. 為什麼 CLIP 需要文字與影像的向量表示？

---

## Query / Key / Value

### Level 1：直覺理解

Query（查詢）表示「我正在找什麼」，Key（鍵）表示「我能被怎麼找到」，Value（值）表示「我真正提供的內容」。

### Level 2：技術原理

Transformer 會用三組可訓練權重，把 Embedding 投影成 Q、K、V：

```text
Q = XWq
K = XWk
V = XWv
```

Q 與 K 做相似度計算，得到 Attention Score（注意力分數）；分數經過 Softmax（柔性最大化函數）後會加權 V，產生新的上下文表示。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_02_attention_overview.py
```

觀察指定 Query token 與每個 Key 的分數，並判斷分數最高的 Token 是否符合直覺。

### Level 4：Application Relation

在 VLM 中，文字 Token 可能需要關注影像中的某個區域；在 VLA 中，任務文字可能需要關注與動作決策相關的視覺線索。QKV 是這種「尋找並取用資訊」的核心機制。

### Level 5：驗收問題

1. Q、K、V 分別扮演什麼角色？
2. 為什麼不是直接用 Embedding 做輸出？
3. Q 與 K 的分數高，代表模型接下來會如何使用 V？

---

## Attention

### Level 1：直覺理解

Attention（注意力機制）讓模型在理解某個 Token 時，決定要多參考哪些其他 Token。

### Level 2：技術原理

核心公式是：

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

`QK^T` 產生相似度分數，`sqrt(d_k)` 用於縮放分數，Softmax 把分數轉成加總為 1 的權重，最後用權重加總 Value。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_02_attention_overview.py
```

觀察每個 Token 的 Attention Score，並說明分數最高的 Token 為什麼重要。

### Level 4：Application Relation

Attention 讓 VLM 能在文字描述與影像區域之間建立關聯。例如理解「red door」時，模型需要把顏色、物件與位置線索連在一起。

### Level 5：驗收問題

1. Attention 是單純找最大值，還是加權融合資訊？
2. Softmax 在 Attention 中扮演什麼角色？
3. 為什麼 Attention 的輸出會包含上下文？

---

## Self-Attention

### Level 1：直覺理解

Self-Attention（自注意力）是同一段輸入內部的 Token 彼此互相參考。

### Level 2：技術原理

同一個輸入序列會同時產生 Q、K、V。每個 Token 都會拿自己的 Query 去比對所有 Token 的 Key，再依權重加總所有 Token 的 Value。輸出不再只是單字本身，而是帶有上下文的表示。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_02_attention_overview.py
```

觀察每個 Query token 關注哪些 Key token。

### Level 4：Application Relation

Vision Transformer（視覺轉換器）也使用 Self-Attention，讓影像 Patch 彼此交換資訊。這能幫助模型理解局部區域如何組成整體場景。

### Level 5：驗收問題

1. Self-Attention 與一般 Attention 的差異是什麼？
2. 為什麼同一個 Token 在不同句子中會有不同表示？
3. Self-Attention 如何幫助理解上下文？

---

## Attention Matrix

### Level 1：直覺理解

Attention Matrix（注意力矩陣）像是一張表，顯示每個 Token 在理解自己時，分別關注其他 Token 的比例。

### Level 2：技術原理

矩陣的 row（列）通常代表 Query token，column（欄）代表 Key token。每一列經過 Softmax 後通常加總為 1，表示該 Query 對所有 Key 的注意力分布。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_02_attention_overview.py
```

觀察矩陣每一列的權重分布，並找出每個 Query token 最關注哪個 Key token。

### Level 4：Application Relation

Attention Matrix 是觀察 Transformer 行為的入門方式。對 VLM 而言，類似的注意力分布可用來思考文字是否關注到正確的影像區域。

### Level 5：驗收問題

1. Attention Matrix 的 row 與 column 分別代表什麼？
2. 為什麼每一列通常會加總為 1？
3. 如何從矩陣判斷某個 Token 最關注誰？

---

## Position Encoding

### Level 1：直覺理解

Position Encoding（位置編碼）告訴 Transformer 每個 Token 或 Patch 的位置。沒有位置資訊時，「dog bites man」和「man bites dog」會更難區分。

### Level 2：技術原理

Self-Attention 本身主要看 Token 之間的關係，沒有天然的順序感。因此模型會把位置資訊加到 Embedding 上：

```text
Token Embedding + Position Encoding -> Position-Aware Representation
```

位置編碼可以是固定的 sin/cos 函數，也可以是訓練出來的向量。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_03_position_multihead.py
```

觀察不同位置的向量數值如何不同。

### Level 4：Application Relation

影像 Patch 也需要位置資訊。VLM 若只知道 Patch 內容卻不知道位置，就難以理解「左上角」、「旁邊」、「前方」這類空間關係。

### Level 5：驗收問題

1. Transformer 為什麼需要額外加入位置資訊？
2. Token Embedding 和 Position Encoding 如何合併？
3. 影像 Patch 的位置資訊為什麼重要？

---

## Multi-Head Attention

### Level 1：直覺理解

Multi-Head Attention（多頭注意力）讓模型用多個視角同時看同一段輸入。不同 head（頭）可以關注不同關係。

### Level 2：技術原理

每個 head 都有自己的 Q、K、V 投影，會產生各自的 Attention 結果。模型再把多個 head 的輸出 concat（串接）起來，經過輸出投影形成最後表示。

```text
Q, K, V -> Head 1 / Head 2 / ... -> concat -> output projection
```

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_03_position_multihead.py
```

觀察不同 head 的關注目標是否不同。

### Level 4：Application Relation

VLM 同時需要處理物件、屬性、位置與文字語意。Multi-Head Attention 讓模型有機會在不同 head 中分別捕捉這些關係。

### Level 5：驗收問題

1. 為什麼多個 head 比單一 Attention 更有彈性？
2. 不同 head 一定會學到完全不同的概念嗎？
3. Multi-Head Attention 如何幫助 VLM 處理多種線索？

---

## Transformer Encoder

### Level 1：直覺理解

Transformer Encoder（轉換器編碼器）擅長理解輸入，把文字或影像轉成可比較、可檢索、可分類的表示。

### Level 2：技術原理

Encoder 通常由 Multi-Head Self-Attention、Feed Forward Network（前饋神經網路）、Residual Connection（殘差連接）與 Layer Normalization（層正規化）堆疊而成。它看見完整輸入後，產生上下文表示。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_04_transformer_flow.py
```

觀察 Encoder mode 如何把輸入轉成 contextual representation（上下文表示）。

### Level 4：Application Relation

CLIP 的 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）會把圖片和文字轉成可比較的向量。Week02 會延伸這個觀念到圖文相似度。

### Level 5：驗收問題

1. Encoder 的主要任務是理解還是生成？
2. CLIP 為什麼適合使用 Encoder 產生圖文向量？
3. Encoder 輸出的表示可以用在哪些任務？

---

## Transformer Decoder

### Level 1：直覺理解

Transformer Decoder（轉換器解碼器）擅長逐步產生輸出，例如下一個字、回答或動作描述。

### Level 2：技術原理

Decoder 常使用 Masked Self-Attention（遮罩自注意力），避免生成時偷看未來 Token。它也可以透過 Cross-Attention（交叉注意力）參考 Encoder 輸出的上下文。

### Level 3：實作驗證

Demo（示範程式）路徑：

```powershell
python demo/demo_04_transformer_flow.py
```

觀察 Decoder mode 如何根據 context（上下文）與已產生 Token 推出下一步。

### Level 4：Application Relation

LLaVA 這類模型常需要根據影像與文字上下文生成回答；VLA 模型也可能根據觀察與指令生成動作序列。Decoder 的逐步生成概念能幫助理解這類模型。

### Level 5：驗收問題

1. Decoder 的主要任務是理解還是生成？
2. Masked Self-Attention 為什麼不能看未來 Token？
3. Decoder 與 Encoder 的差異是什麼？

---

## Transformer 與 VLM / CLIP 的關係

### Level 1：直覺理解

Transformer 是 VLM 與 CLIP 的基礎工具之一。它讓模型能處理文字序列、影像 Patch 序列，以及兩者的關係。

### Level 2：技術原理

CLIP 使用影像編碼器與文字編碼器，把圖片與文字轉成同一個向量空間中的表示。Transformer 的 Token、Embedding、Attention 與 Encoder 概念，能解釋文字如何被編碼，也能延伸到 Vision Transformer 如何處理影像 Patch。

### Level 3：實作驗證

建議先依序完成以下 Demo：

```powershell
python demo/demo_01_token_embedding.py
python demo/demo_02_attention_overview.py
python demo/demo_03_position_multihead.py
python demo/demo_04_transformer_flow.py
```

完成後，用一段話描述資料如何從文字進入 Transformer。

### Level 4：Application Relation

Week01 建立的是「序列如何變成上下文向量」的基礎。Week02 CLIP 會接著學「影像向量與文字向量如何被放到共同向量空間比較」。

### Level 5：驗收問題

1. 為什麼學 CLIP 前要先理解 Transformer？
2. 影像 Patch 與文字 Token 有什麼相似之處？
3. CLIP 的共同向量空間和 Week01 哪些概念最相關？
