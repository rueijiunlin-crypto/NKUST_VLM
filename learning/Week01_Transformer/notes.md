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

## Week01 學習目標

完成 Week01 後，應能用自己的話說明：

- 文字如何從原始輸入轉成 Token（詞元）、Token ID（詞元編號）與 Embedding（嵌入向量）。
- Position Encoding（位置編碼）為什麼能補足 Transformer（轉換器架構）本身缺少的順序資訊。
- Query（查詢）、Key（鍵）、Value（值）各自負責什麼。
- Attention Score（注意力分數）、Softmax（柔性最大化函數）、Attention Weight（注意力權重）與 Value（值）加權總和之間的關係。
- Self-Attention Matrix（自注意力矩陣）的列與欄分別代表什麼。
- Encoder（編碼器）與 Decoder（解碼器）的用途差異。
- Transformer Block（轉換器區塊）的基本流程如何把輸入更新成帶有上下文的表示。

---

## 2. Token（詞元）與 Token ID（詞元編號）

### 直覺理解

Token（詞元）是模型閱讀文字時的基本單位。人可以直接看懂一句話，但模型不能直接處理原始文字，必須先把文字切成 Token。

Token ID（詞元編號）是 Token 在 vocabulary（詞彙表）中的數字編號。模型真正接收的是數字，而不是原始文字。

### 技術原理

Token（詞元）與 Token ID（詞元編號）是文字進入模型前的第一個轉換。Token 負責把原始文字切成可管理的單位，Token ID 則把這些單位對應到 vocabulary（詞彙表）中的編號。要特別注意：Token ID 是詞彙表編號，不是位置編號；位置資訊會在 Position Encoding（位置編碼）處理。

Token（詞元）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 原始文字 |
| 輸出 | Token 列表 |
| 目的 | 把文字切成模型可處理的基本單位 |
| 解決問題 | 原始字串長短不一，模型無法直接計算 |
| 下一步 | Token ID（詞元編號） |

Token ID（詞元編號）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Token（詞元） |
| 輸出 | 詞彙表中的整數編號 |
| 目的 | 讓模型能用編號查找對應向量 |
| 解決問題 | Token 仍是文字符號，不能直接做神經網路運算 |
| 下一步 | Embedding（嵌入向量） |

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
4. 文字指令進入 VLM（視覺語言模型）前，為什麼也需要先 Token 化？

### Application Relation（應用關聯）

在 VLM/VLA 中，文字問題、圖片描述與機器人指令都必須先被切成 Token。例如「拿起紅色杯子」需要先拆成語言單位，後續才可能連接到影像中的杯子與機器人動作。

---

## 3. Embedding（嵌入向量）

### 直覺理解

Embedding（嵌入向量）可以想成 Token 在模型空間中的語意座標。Token ID 只是編號，本身不代表語意；Embedding 會把編號轉成可計算的向量。

### 技術原理

Embedding Table（嵌入表）像是一張可訓練的查找表。Token ID（詞元編號）進來後，模型會用這個編號取出一列向量；這個向量才是後續 Attention（注意力機制）能運算的資料。

Embedding（嵌入向量）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Token ID（詞元編號） |
| 輸出 | Embedding Vector（嵌入向量） |
| 目的 | 將離散編號轉成可運算的連續向量 |
| 解決問題 | Token ID 只是編號，無法表示語意相似度與上下文關係 |
| 下一步 | Query（查詢）、Key（鍵）、Value（值） |

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
4. CLIP（對比式圖文預訓練）的文字編碼器為什麼需要 Embedding？

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

Q、K、V 通常由 Embedding（嵌入向量）經過不同的線性轉換得到。三者來源相同，但用途不同：Q 負責提出需求，K 負責被比對，V 負責提供最後要被整合的內容。

Query（查詢）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Embedding Vector（嵌入向量） |
| 輸出 | Query Vector（查詢向量） |
| 目的 | 表示目前 Token 想尋找的資訊 |
| 解決問題 | 模型需要知道「現在這個位置要問什麼」 |
| 下一步 | 與 Key（鍵）計算 Attention Score（注意力分數） |

Key（鍵）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Embedding Vector（嵌入向量） |
| 輸出 | Key Vector（鍵向量） |
| 目的 | 表示每個 Token 可被比對的特徵 |
| 解決問題 | 模型需要知道「其他位置提供什麼線索可供查詢」 |
| 下一步 | 與 Query（查詢）做相似度比對 |

Value（值）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Embedding Vector（嵌入向量） |
| 輸出 | Value Vector（值向量） |
| 目的 | 提供最後真正被加權整合的內容 |
| 解決問題 | 分數只代表重要性，模型仍需要可取用的資訊內容 |
| 下一步 | 依 Attention Weight（注意力權重）做加權總和 |

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
4. 若影像 Patch（影像切塊）也有 QKV，模型可以用它判斷哪些影像區域彼此相關？

### Application Relation（應用關聯）

QKV 是 Transformer 建立上下文關係的基礎。對 VLM 來說，文字 Token 或影像 Patch（影像切塊）都可以透過 QKV 判斷彼此關聯；對 VLA 來說，語言指令、視覺目標與動作線索也需要類似的關注機制。

---

## 5. Attention（注意力機制）

### 直覺理解

Attention 是模型決定「目前應該關注哪些資訊」的方法。理解一句話時，不是每個 Token 都同等重要。

例如理解 `laboratory` 時，`red` 與 `door` 可能提供位置線索，因此分數應較高。

### 技術原理

Attention（注意力機制）不是只找出最高分 Token，而是把所有 Token 的 Value（值）依重要程度重新混合。這讓目前 Token 的新表示同時帶有自己與其他相關 Token 的資訊。

Attention（注意力機制）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Query（查詢）、Key（鍵）、Value（值） |
| 輸出 | 加權後的上下文表示 |
| 目的 | 讓模型根據目前需求整合重要資訊 |
| 解決問題 | 單一 Token 表示缺少上下文，無法理解和其他 Token 的關係 |
| 下一步 | 多個 Token 互相計算時形成 Attention Matrix（注意力矩陣） |

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

### Softmax 與 Value 加權總和

Attention Score（注意力分數）不是最後結果。Score 只表示 Query（查詢）和每個 Key（鍵）的相似程度；分數可能很大、很小，也不一定能直接解釋成比例。

Softmax（柔性最大化函數）會把這些分數轉成總和為 1 的 Attention Weight（注意力權重）。權重越大，代表該 Token 的 Value（值）在最後表示中占比越高。

模型不是只選最高分 Token，而是用權重加總所有 Value：

```text
scores = [0.2, 0.8, 1.5]
weights = softmax(scores) = [0.15, 0.27, 0.58]
new_vector = 0.15 * V1 + 0.27 * V2 + 0.58 * V3
```

這個 `new_vector` 比原本單一 Token 的 Embedding（嵌入向量）更有上下文資訊，因為它不只保留目前 Token 的線索，也混入其他相關 Token 的內容。例如理解 `laboratory` 時，模型可以同時吸收 `red`、`door` 等線索，而不是孤立地看 `laboratory` 這個詞。

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
4. 在圖文模型中，Attention 可以幫助模型關注圖片或文字中的哪些線索？

### Application Relation（應用關聯）

Attention 讓模型能找出語言或影像中對任務最重要的線索。機器人聽到「把紅色杯子放到盤子旁邊」時，需要關注物件、顏色、動作與位置關係。

---

## 6. Self-Attention（自注意力）與 Attention Matrix（注意力矩陣）

### 直覺理解

Self-Attention 是同一段輸入內的 Token 彼此互相參考。每個 Token 都是 Query，也都有自己的 Key 與 Value。

Attention Matrix（注意力矩陣）記錄了「每個 Token 看其他 Token 的程度」。不同 Token 的任務不同，因此看到的資訊也不同。

### 技術原理

Self-Attention（自注意力）是 Attention（注意力機制）的一種特例：Q、K、V 都來自同一個輸入序列。Attention Matrix（注意力矩陣）則是觀察 Self-Attention 的主要方式。

Self-Attention（自注意力）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 同一序列中所有 Token 的 Q、K、V |
| 輸出 | 每個 Token 的上下文表示 |
| 目的 | 讓序列內每個位置都能整合其他位置資訊 |
| 解決問題 | 逐字處理無法捕捉長距離關係 |
| 下一步 | Attention Matrix（注意力矩陣）與 Position Encoding（位置編碼） |

Attention Matrix（注意力矩陣）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 每個 Query Token 對所有 Key Token 的 Attention Weight（注意力權重） |
| 輸出 | `token_count x token_count` 的權重矩陣 |
| 目的 | 呈現每個 Token 看其他 Token 的程度 |
| 解決問題 | Attention 的分布不容易只靠文字描述觀察 |
| 下一步 | 檢查順序資訊是否需要 Position Encoding（位置編碼）補足 |

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
4. 在 Vision Transformer（視覺轉換器）中，Self-Attention 可以用來觀察哪些 Patch 關係？

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
4. 若矩陣顯示某個 Token 長期關注位置詞，這對理解指令有什麼幫助？

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

Position Encoding（位置編碼）會加到 Token Embedding（詞元嵌入向量）上，形成同時包含語意與位置的表示。它補足的是「順序」或「空間位置」，不是詞彙表編號。

Position Encoding（位置編碼）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Embedding Vector（嵌入向量）與位置索引 |
| 輸出 | 加入位置資訊的向量 |
| 目的 | 讓模型知道 Token 或 Patch（影像切塊）的順序與位置 |
| 解決問題 | Self-Attention（自注意力）本身不包含順序感 |
| 下一步 | 位置化後的表示進入 Multi-Head Attention（多頭注意力） |

簡化流程：

```text
Token Embedding + Position Encoding -> Position-Aware Representation（具位置感知的表示）
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
4. 若沒有位置資訊，圖片中的上下左右關係可能會出現什麼問題？

### Application Relation（應用關聯）

在影像中，Patch 的位置會影響物件與場景結構；在機器人任務中，「杯子在盤子旁邊」和「盤子在杯子旁邊」也依賴位置與關係。Position Encoding 是讓 Transformer 保留順序與空間線索的基礎。

---

## 8. Multi-Head Attention（多頭注意力）

### 直覺理解

Multi-Head Attention 讓模型用多組不同視角同時看資料。單一 head（頭）可能關注目的地，另一個 head 可能關注顏色，另一個 head 可能關注動作。

### 技術原理

Multi-Head Attention（多頭注意力）會把 Q、K、V 分成多個 head（頭）各自做 Attention（注意力機制），再把結果串接並投影回模型需要的維度。不同 head 可以學到不同關係，不需要人工指定每個 head 看什麼。

Multi-Head Attention（多頭注意力）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 加入位置資訊的 Q、K、V |
| 輸出 | 多個 head 的上下文表示合併結果 |
| 目的 | 讓模型從多種關係角度理解序列 |
| 解決問題 | 單一注意力分布可能不足以捕捉多種關係 |
| 下一步 | 進入 Encoder（編碼器）或 Decoder（解碼器）層 |

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
4. 在 VLM 任務中，多個 head 可能分別關注哪些文字或影像線索？

### Application Relation（應用關聯）

VLM/VLA 任務通常同時包含物件、顏色、位置、語言動作與場景關係。Multi-Head Attention 讓模型能同時從多種角度整理這些線索。

---

## 9. Transformer Encoder（轉換器編碼器）

### 直覺理解

Encoder（編碼器）偏向理解輸入。它把文字、圖片或特徵序列讀完後，整理成可分類、檢索或比對的表示。

### 技術原理

Encoder（編碼器）通常接收完整輸入序列，透過多層 Transformer Block（轉換器區塊）更新每個 Token 的表示。它的重點是理解與表示，不是逐步生成。

Encoder（編碼器）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | Token 或影像特徵序列 |
| 輸出 | 上下文化表示 |
| 目的 | 產生適合理解、分類、檢索與比對的表示 |
| 解決問題 | 原始輸入缺少整體語意整理 |
| 下一步 | 可用於 CLIP（對比式圖文預訓練）圖文相似度，或傳給 Decoder（解碼器） |

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
3. CLIP 為什麼需要 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）？
4. 若要做圖文檢索，為什麼 Encoder 型表示很重要？

### Application Relation（應用關聯）

CLIP 使用 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）把圖片與文字放進共同向量空間。機器人語意導覽也可用 Encoder 建立場景與文字目標的表示。

---

## 10. Transformer Decoder（轉換器解碼器）

### 直覺理解

Decoder（解碼器）偏向產生輸出。它根據上下文與已經產生的 Token，一步一步預測下一個 Token。

### 技術原理

Decoder（解碼器）通常會看上下文與已經生成的 Token，並預測下一個 Token。它的重點是生成，因此需要 Masked Self-Attention（遮罩自注意力）避免看到未來答案。

Decoder（解碼器）的概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 上下文表示與已產生 Token |
| 輸出 | 下一個 Token 或動作文字描述 |
| 目的 | 根據已知資訊逐步生成回答、描述或任務計畫 |
| 解決問題 | 模型需要把理解結果轉成可讀文字或行動描述 |
| 下一步 | 可連接 VLA（視覺語言動作模型）的動作規劃或控制模組 |

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
4. 若模型要把影像理解轉成回答文字，Decoder 負責哪一段工作？

### Application Relation（應用關聯）

LLaVA 類模型需要根據影像與問題生成文字回答。OpenVLA 則需要把視覺與語言理解轉成動作描述，例如「移動到桌前」或「抓取紅色杯子」。

---

## 11. Transformer Block（轉換器區塊）整體流程

Transformer Block（轉換器區塊）可以理解成 Transformer 中重複堆疊的基本單位。前面的 Token、Embedding、QKV、Attention、Position Encoding 與 Multi-Head Attention，最後都會在這個區塊中組成完整流程。

基本流程：

```text
Input
-> Multi-Head Attention
-> Add & Norm
-> Feed Forward Network
-> Add & Norm
-> Output
```

各步驟的作用：

- Multi-Head Attention（多頭注意力）：讓 Token 彼此交換資訊，從多個 head（頭）觀察不同關係。
- Add & Norm（相加與正規化）：透過 Residual Connection（殘差連接）保留原始資訊，並用 Layer Normalization（層正規化）穩定訓練。
- Feed Forward Network（前饋網路）：對每個 Token 的特徵做進一步轉換，提升表示能力。
- Output（輸出）：得到更新後、帶有上下文的 Token 表示，可進入下一個 Transformer Block、Encoder（編碼器）輸出層或 Decoder（解碼器）生成流程。

概念定位：

| 項目 | 說明 |
|---|---|
| 輸入 | 加入位置資訊後的 Token 表示 |
| 輸出 | 更新後、帶有上下文的 Token 表示 |
| 目的 | 將注意力交換與特徵轉換組成可堆疊的模型單元 |
| 解決問題 | 單次 Attention 只能交換資訊，還需要穩定訓練與特徵轉換 |
| 下一步 | 多層堆疊形成 Encoder（編碼器）或 Decoder（解碼器） |

---

## 12. Transformer 與 CLIP 的銜接

CLIP 的核心是把圖片與文字編碼成可比較的向量。Week01 的 Token、Embedding、Attention、Encoder 等概念，會在 Week02 轉成「圖片與文字如何進入共同向量空間」的問題。

銜接流程：

```text
Week01 Transformer
-> Text Encoder / Image Encoder
-> Image-Text Similarity（圖文相似度）
-> CLIP（對比式圖文預訓練）
```

---

## 13. Week01 合格檢查表

請先不要查答案，試著用自己的話回答：

- Token ID（詞元編號）是位置編號還是詞彙表編號？
- Embedding Table（嵌入表）的用途是什麼？
- Position Encoding（位置編碼）加在模型流程的哪裡？
- Q、K、V 分別代表什麼？
- Attention Score（注意力分數）和 Attention Weight（注意力權重）有什麼差別？
- 為什麼 Attention（注意力機制）最後要加權 Value（值）？
- Attention Matrix（注意力矩陣）的每一列代表什麼？
- Multi-Head Attention（多頭注意力）為什麼需要多個 head（頭）？
- Encoder（編碼器）和 Decoder（解碼器）的主要差異是什麼？
- Transformer Block（轉換器區塊）的基本流程是什麼？

---

## 14. 本週已掌握內容

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
- Transformer Block 如何用 Multi-Head Attention、Add & Norm 與 Feed Forward Network 更新 Token 表示。

## 15. 本週尚未涵蓋內容

已學會內容：

- 文字如何轉成 Token（詞元）、Token ID（詞元編號）與 Embedding（嵌入向量）。
- Query（查詢）、Key（鍵）、Value（值）如何形成 Attention（注意力機制）。
- Softmax（柔性最大化函數）如何把分數轉成 Attention Weight（注意力權重），並加權 Value（值）。
- Self-Attention（自注意力）與 Attention Matrix（注意力矩陣）的基本閱讀方式。
- Position Encoding（位置編碼）、Multi-Head Attention（多頭注意力）、Encoder（編碼器）、Decoder（解碼器）與 Transformer Block（轉換器區塊）的基本用途。

尚未深入內容：

- Layer Normalization（層正規化）的數學細節。
- Feed Forward Network（前饋網路）的完整運作。
- Residual Connection（殘差連接）的訓練穩定性。
- Cross-Attention（交叉注意力）如何連接影像與文字。
- CLIP 的 contrastive learning（對比式學習）損失函數。
- 真實大型 VLM/VLA 的完整訓練流程。

下一週將銜接 CLIP（對比式圖文預訓練）與 Vision Transformer（視覺轉換器）的方向：

- 文字與圖片如何各自被 Encoder（編碼器）轉成向量。
- 圖片如何被切成 Patch（影像切塊）並進入 Transformer。
- 圖文向量如何進入共同向量空間並進行相似度比較。

## 16. 下一週預告

下一週將學習 CLIP（對比式圖文預訓練）：

- 圖片如何被 Image Encoder（影像編碼器）轉成向量。
- 文字如何被 Text Encoder（文字編碼器）轉成向量。
- 圖片向量與文字向量如何進入共同向量空間。
- Similarity（相似度）如何用於圖文檢索與零樣本分類。
