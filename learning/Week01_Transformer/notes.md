# Week01 Notes：Transformer 基礎

## 1. 為什麼先學 Transformer（轉換器架構）

Vision-Language Model（視覺語言模型，VLM）與 Vision-Language-Action Model（視覺語言動作模型，VLA）都需要把文字、影像與動作線索轉成模型可計算的表示。Transformer（轉換器架構）是理解這條資料流的基礎。

本週採用 Demo First（示範優先）學習模式：每個核心概念讀完後，立即執行對應 Demo（示範程式），用輸出結果確認自己是否真的理解。

本週主線：

```text
Text（文字）
-> Token（詞元）
-> Token ID（詞元編號）
-> Embedding（嵌入向量）
-> QKV（查詢、鍵、值）
-> Attention（注意力機制）
-> Self-Attention（自注意力）
-> Position Encoding（位置編碼）
-> Multi-Head Attention（多頭注意力）
-> Encoder（編碼器） / Decoder（解碼器）
```

---

## 2. Token（詞元）與 Token ID（詞元編號）

### 直覺理解

Token（詞元）是模型閱讀文字時的基本單位。人可以直接看懂一句話，但模型不能直接處理原始文字，必須先把文字切成 Token。

Token ID（詞元編號）是 Token 在 vocabulary（詞彙表）中的數字編號。模型真正接收的是數字，而不是原始文字。

### 技術原理

- 輸入：原始文字
- 輸出：Token 列表與 Token ID 列表
- 目的：把文字轉成模型可查表、可計算的離散編號
- 解決問題：原始文字無法直接進入神經網路
- 下一步：Token ID 會進入 Embedding（嵌入向量）

簡化流程：

```text
"take me to the laboratory"
-> ["take", "me", "to", "the", "laboratory"]
-> [0, 1, 4, 3, 2]
```

### 建議執行 Demo

Demo 名稱：`demo/token/demo_tokenizer.py`

執行指令：

```powershell
python demo\token\demo_tokenizer.py
```

觀察重點：

- 原始文字如何被切成 Token。
- Token 如何對應到 Token ID。
- Token 與 Token ID 是否一一對應。

預期輸出：

```text
Token（詞元）列表：
['take', 'me', 'to', 'the', 'laboratory']

Token ID（詞元編號）列表：
[...]
```

執行後應回答問題：

1. Token 和原始文字有什麼差異？
2. Token ID 的用途是什麼？
3. 為什麼下一步需要 Embedding（嵌入向量）？

### Application Relation（應用關聯）

在 VLM/VLA 中，文字問題、圖片描述與機器人指令都必須先被切成 Token。例如「拿起紅色杯子」需要先拆成語言單位，後續才可能連接到影像中的杯子與機器人動作。

---

## 3. Embedding（嵌入向量）

### 直覺理解

Embedding（嵌入向量）可以想成 Token 在模型空間中的語意座標。Token ID 只是編號，本身不代表語意；Embedding 會把編號轉成可計算的向量。

### 技術原理

- 輸入：Token ID（詞元編號）
- 輸出：Embedding Vector（嵌入向量）
- 目的：將離散編號轉成可運算的連續向量
- 解決問題：Token ID 無法表示語意相似度與上下文關係
- 下一步：Embedding 會被轉成 Query（查詢）、Key（鍵）、Value（值）

簡化流程：

```text
Token ID -> Embedding Table（嵌入表） -> Embedding Vector
```

如果一個句子有 5 個 Token，每個 Token 是 768 維向量，則模型看到的是：

```text
5 x 768
```

### 建議執行 Demo

Demo 名稱：`demo/embedding/demo_embedding.py`

執行指令：

```powershell
python demo\embedding\demo_embedding.py
```

若尚未安裝套件：

```powershell
pip install transformers torch
```

注意：第一次執行可能需要下載 `distilbert-base-uncased` 模型與 tokenizer（分詞器）檔案。

觀察重點：

- Token 數量。
- Embedding 維度。
- Embedding Shape（嵌入向量形狀）代表什麼。

預期輸出：

```text
Embedding Shape（嵌入向量形狀）：
(batch_size, token_count, embedding_dim)
```

執行後應回答問題：

1. Embedding Shape 中三個數字分別代表什麼？
2. 為什麼 Token ID 不能直接代表語意？
3. Embedding 如何接到 QKV？

### Application Relation（應用關聯）

CLIP（對比式圖文預訓練）的文字編碼器、LLaVA（大型語言與視覺助手）的語言輸入，以及 OpenVLA（開源視覺語言動作模型）的文字指令，都需要先把文字轉成向量表示。

---

## 4. QKV：Query（查詢）、Key（鍵）、Value（值）

### 直覺理解

QKV 是 Attention（注意力機制）的核心準備步驟。可以用圖書館類比：

- Query（查詢）：你正在找什麼書。
- Key（鍵）：每本書的索引標籤。
- Value（值）：書本真正的內容。

你會先用查詢去比對索引標籤，找到相關書，再讀取書本內容。模型也是先用 Query 比對 Key，再決定要取用多少 Value。

### 技術原理

- 輸入：Embedding Vector（嵌入向量）
- 輸出：Query、Key、Value 三組向量
- 目的：讓模型能比較「目前位置想找什麼」與「其他位置提供什麼」
- 解決問題：Embedding 本身還沒有決定上下文中誰該關注誰
- 下一步：Q 與 K 會計算 Attention Score（注意力分數）

簡化流程：

```text
Embedding
-> Query（查詢）
-> Key（鍵）
-> Value（值）
```

### 建議執行 Demo

Demo 名稱：`demo/qkv/demo_qkv.py`

執行指令：

```powershell
python demo\qkv\demo_qkv.py
```

觀察重點：

- 每個 Token 如何有自己的 Q、K、V。
- Q 和 K 的內積如何形成分數。
- Value 是後續被加權整合的內容。

預期輸出：

```text
Query token: laboratory
Q x K scores:
...
```

執行後應回答問題：

1. Query、Key、Value 各自的角色是什麼？
2. 為什麼不能只用 Embedding，還需要 QKV？
3. 圖書館類比中，Query、Key、Value 分別對應什麼？

### Application Relation（應用關聯）

QKV 是 Transformer 建立上下文關係的基礎。對 VLM 來說，文字 Token 或影像 Patch（影像切塊）都可以透過 QKV 判斷彼此關聯；對 VLA 來說，語言指令、視覺目標與動作線索也需要類似的關注機制。

---

## 5. Attention（注意力機制）

### 直覺理解

Attention 是模型決定「目前應該關注哪些資訊」的方法。理解一句話時，不是每個 Token 都同等重要。

例如理解 `laboratory` 時，`red` 與 `door` 可能提供位置線索，因此分數應較高。

### 技術原理

- 輸入：Query、Key、Value
- 輸出：加權後的上下文表示
- 目的：讓模型根據目前需求選擇重要資訊
- 解決問題：單一 Token 表示缺少上下文
- 下一步：多個 Token 互相計算時形成 Attention Matrix（注意力矩陣）

核心公式：

```text
score = Q x K^T
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

變數說明：

- Q：Query（查詢），目前位置想找的資訊。
- K：Key（鍵），其他位置可被比對的特徵。
- `K^T`：Key Matrix Transpose（鍵矩陣轉置），方便 Query 同時比對多個 Key。
- `d_k`：Key 的維度，用於縮放分數，避免分數過大。
- Softmax（柔性最大化函數）：把分數轉成總和為 1 的權重。
- V：Value（值），真正被加權整合的內容。

計算流程圖：

```text
Embedding
-> Q, K, V
-> Q x K^T
-> Attention Score（注意力分數）
-> Softmax（柔性最大化函數）
-> Attention Weight（注意力權重）
-> Weighted Sum of V（加權 Value）
-> Contextual Representation（上下文表示）
```

### 建議執行 Demo

Demo 名稱：`demo/attention/demo_attention.py`

執行指令：

```powershell
python demo\attention\demo_attention.py
```

觀察重點：

- 哪個 Token 的 Attention Score 最高。
- 分數最高的 Token 是否符合任務直覺。
- Attention 如何把「重要性」變成可觀察的分數。

預期輸出：

```text
Token（詞元）與 Attention Score（注意力分數）：
...
最重要的 Token（詞元）：
laboratory
```

執行後應回答問題：

1. Attention Score 代表什麼？
2. 為什麼要用 Q 和 K 做內積？
3. 為什麼 Attention Score 最後要加權 V？

### Application Relation（應用關聯）

Attention 讓模型能找出語言或影像中對任務最重要的線索。機器人聽到「把紅色杯子放到盤子旁邊」時，需要關注物件、顏色、動作與位置關係。

---

## 6. Self-Attention（自注意力）與 Attention Matrix（注意力矩陣）

### 直覺理解

Self-Attention 是同一段輸入內的 Token 彼此互相參考。每個 Token 都是 Query，也都有自己的 Key 與 Value。

Attention Matrix（注意力矩陣）記錄了「每個 Token 看其他 Token 的程度」。不同 Token 的任務不同，因此看到的資訊也不同。

### 技術原理

- 輸入：同一序列中所有 Token 的 Q、K、V
- 輸出：每個 Token 的上下文表示與 Attention Matrix
- 目的：讓序列內每個位置都能整合其他位置資訊
- 解決問題：逐字處理無法捕捉長距離關係
- 下一步：加入 Position Encoding（位置編碼），讓模型知道順序

如果有 5 個 Token，Attention Matrix 大小是：

```text
5 x 5
```

每一列代表一個 Query Token 看所有 Key Token 的權重。

### 建議執行 Demo

Demo 名稱：`demo/self_attention/demo_self_attention.py`

執行指令：

```powershell
python demo\self_attention\demo_self_attention.py
```

觀察重點：

- 每個 Query token 是否有不同注意力分布。
- `laboratory` 是否較關注 `red`、`door` 等線索。
- Self-Attention 如何讓同一句話內部互相參考。

預期輸出：

```text
Query token: laboratory
attends to red / door / laboratory
```

執行後應回答問題：

1. 為什麼說每個 Token 都是 Query？
2. Attention Matrix 的列與欄分別代表什麼？
3. 為什麼不同 Token 會看到不同資訊？

### 建議執行 Demo

Demo 名稱：`demo/attention/demo_attention_matrix.py`

執行指令：

```powershell
python demo\attention\demo_attention_matrix.py
```

觀察重點：

- Attention Matrix 是否每一列加總為 1。
- 每個 Query Token 的最高權重落在哪個 Key Token。
- 矩陣如何呈現全句上下文關係。

預期輸出：

```text
Attention Matrix:
query\key      go      to     red    door laboratory
...
```

執行後應回答問題：

1. Attention Matrix 為什麼是方形矩陣？
2. 每一列加總為 1 代表什麼？
3. Attention Matrix 如何幫助觀察 Self-Attention？

### Application Relation（應用關聯）

Vision Transformer（視覺轉換器）會讓影像 Patch 彼此做 Self-Attention。室內導覽或桌面操作任務中，模型需要理解不同物件與區域的關係，Attention Matrix 是觀察這種關係的入口。

---

## 7. Position Encoding（位置編碼）

### 直覺理解

Transformer 本身很擅長看關係，但它不像 RNN（循環神經網路）一樣天生逐步讀取序列。因此，若沒有 Position Encoding（位置編碼），模型只看到一堆 Token，卻不知道順序。

例如：

```text
dog bites man
man bites dog
```

兩句話 Token 相同，但順序不同，意思完全不同。

### 技術原理

- 輸入：Embedding Vector 與位置索引
- 輸出：加入位置資訊的向量
- 目的：讓模型知道 Token 或 Patch 的順序
- 解決問題：Self-Attention 本身不包含順序感
- 下一步：位置化後的表示可進入 Multi-Head Attention（多頭注意力）

簡化流程：

```text
Token Embedding + Position Encoding -> Position-Aware Representation
```

常見作法包含可學習位置向量，或使用 sin/cos 週期函數建立位置訊號。

### 建議執行 Demo

Demo 名稱：`demo/position_encoding/demo_position_encoding.py`

執行指令：

```powershell
python demo\position_encoding\demo_position_encoding.py
```

觀察重點：

- 同一個 Token 在不同位置加入的位置值不同。
- Position Encoding 如何讓位置 0、1、2 有差異。
- 文字順序為什麼會影響語意。

預期輸出：

```text
position 0: [...]
position 1: [...]
position 2: [...]
```

執行後應回答問題：

1. Transformer 為什麼不知道 Token 順序？
2. Position Encoding 解決了什麼問題？
3. 影像 Patch 為什麼也需要位置資訊？

### Application Relation（應用關聯）

在影像中，Patch 的位置會影響物件與場景結構；在機器人任務中，「杯子在盤子旁邊」和「盤子在杯子旁邊」也依賴位置與關係。Position Encoding 是讓 Transformer 保留順序與空間線索的基礎。

---

## 8. Multi-Head Attention（多頭注意力）

### 直覺理解

Multi-Head Attention 讓模型用多組不同視角同時看資料。單一 head（頭）可能關注目的地，另一個 head 可能關注顏色，另一個 head 可能關注動作。

### 技術原理

- 輸入：加入位置資訊的 Q、K、V
- 輸出：多個 head 的上下文表示合併結果
- 目的：讓模型從多種關係角度理解序列
- 解決問題：單一注意力分布可能不足以捕捉多種關係
- 下一步：進入 Encoder 或 Decoder 層

簡化流程：

```text
Q, K, V
-> Head 1 Attention
-> Head 2 Attention
-> Head 3 Attention
-> concat（串接）
-> output projection（輸出投影）
```

### 建議執行 Demo

Demo 名稱：`demo/multi_head_attention/demo_multi_head_attention.py`

執行指令：

```powershell
python demo\multi_head_attention\demo_multi_head_attention.py
```

觀察重點：

- 不同 head 關注不同 Token。
- 多個 head 的觀察結果如何互補。
- Multi-Head Attention 為什麼比單一 Attention 更有彈性。

預期輸出：

```text
Head 1 focus: laboratory
Head 2 focus: red
Head 3 focus: door
```

執行後應回答問題：

1. 為什麼需要多個 head？
2. 不同 head 可以學到哪些不同關係？
3. Multi-Head Attention 如何銜接 Encoder？

### Application Relation（應用關聯）

VLM/VLA 任務通常同時包含物件、顏色、位置、語言動作與場景關係。Multi-Head Attention 讓模型能同時從多種角度整理這些線索。

---

## 9. Transformer Encoder（轉換器編碼器）

### 直覺理解

Encoder（編碼器）偏向理解輸入。它把文字、圖片或特徵序列讀完後，整理成可分類、檢索或比對的表示。

### 技術原理

- 輸入：Token 或影像特徵序列
- 輸出：上下文化表示
- 目的：產生適合理解與比對的表示
- 解決問題：原始輸入缺少整體語意整理
- 下一步：可用於 CLIP 圖文相似度或傳給 Decoder

Encoder 常包含：

- Multi-Head Attention（多頭注意力）
- Feed Forward Network（前饋網路）
- Residual Connection（殘差連接）
- Layer Normalization（層正規化）

### 建議執行 Demo

Demo 名稱：`demo/encoder_decoder/demo_encoder_decoder_flow.py`

執行指令：

```powershell
python demo\encoder_decoder\demo_encoder_decoder_flow.py
```

觀察重點：

- Encoder 的輸入是完整指令。
- Encoder 的輸出是整理後的 representation（表示）。
- Encoder 適合檢索、分類、相似度比對。

預期輸出：

```text
Encoder mode:
input instruction -> contextual representation
```

執行後應回答問題：

1. Encoder 偏向理解還是生成？
2. Encoder 的輸出可用於什麼任務？
3. CLIP 為什麼需要 Image Encoder 與 Text Encoder？

### Application Relation（應用關聯）

CLIP 使用 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）把圖片與文字放進共同向量空間。機器人語意導覽也可用 Encoder 建立場景與文字目標的表示。

---

## 10. Transformer Decoder（轉換器解碼器）

### 直覺理解

Decoder（解碼器）偏向產生輸出。它根據上下文與已經產生的 Token，一步一步預測下一個 Token。

### 技術原理

- 輸入：上下文表示與已產生 Token
- 輸出：下一個 Token 或動作文字描述
- 目的：根據已知資訊逐步生成回答、描述或任務計畫
- 解決問題：模型需要把理解結果轉成可讀文字或行動描述
- 下一步：可連接 VLA 的動作規劃或控制模組

Decoder 常使用 Masked Self-Attention（遮罩自注意力），避免生成時偷看未來 Token。

### 建議執行 Demo

Demo 名稱：`demo/encoder_decoder/demo_encoder_decoder_flow.py`

執行指令：

```powershell
python demo\encoder_decoder\demo_encoder_decoder_flow.py
```

觀察重點：

- Decoder 如何根據 context（上下文）和已產生 Token 決定下一步。
- Decoder 的輸出偏向文字或動作描述。
- Decoder 與 Encoder 的任務差異。

預期輸出：

```text
Decoder mode:
context + generated tokens -> next token/action description
```

執行後應回答問題：

1. Decoder 偏向理解還是生成？
2. 為什麼生成文字需要一步一步進行？
3. LLaVA 或 OpenVLA 如何使用 Decoder 類能力？

### Application Relation（應用關聯）

LLaVA 類模型需要根據影像與問題生成文字回答。OpenVLA 則需要把視覺與語言理解轉成動作描述，例如「移動到桌前」或「抓取紅色杯子」。

---

## 11. Transformer 與 CLIP 的銜接

CLIP 的核心是把圖片與文字編碼成可比較的向量。Week01 的 Token、Embedding、Attention、Encoder 等概念，會在 Week02 轉成「圖片與文字如何進入共同向量空間」的問題。

銜接流程：

```text
Week01 Transformer
-> Text Encoder / Image Encoder
-> Image-Text Similarity（圖文相似度）
-> CLIP（對比式圖文預訓練）
```

---

## 12. 本週已掌握內容

完成本週後，應能掌握：

- Token 與 Token ID 如何把文字轉成模型可處理的編號。
- Embedding 如何把 Token ID 轉成向量。
- QKV 如何準備 Attention 計算。
- Attention 如何透過 Q x K 產生分數並加權 V。
- Attention Matrix 如何呈現每個 Token 對其他 Token 的關注。
- Self-Attention 如何讓同一序列內部互相參考。
- Position Encoding 為什麼能補足順序資訊。
- Multi-Head Attention 為什麼能提供多視角理解。
- Encoder 偏向理解，Decoder 偏向生成。

## 13. 本週尚未涵蓋內容

本週尚未深入涵蓋：

- Layer Normalization（層正規化）的數學細節。
- Feed Forward Network（前饋網路）的完整運作。
- Residual Connection（殘差連接）的訓練穩定性。
- Cross-Attention（交叉注意力）如何連接影像與文字。
- CLIP 的 contrastive learning（對比式學習）損失函數。
- 真實大型 VLM/VLA 的完整訓練流程。

## 14. 下一週預告

下一週將學習 CLIP（對比式圖文預訓練）：

- 圖片如何被 Image Encoder（影像編碼器）轉成向量。
- 文字如何被 Text Encoder（文字編碼器）轉成向量。
- 圖片向量與文字向量如何進入共同向量空間。
- Similarity（相似度）如何用於圖文檢索與零樣本分類。
