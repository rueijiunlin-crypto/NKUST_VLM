# Week01 Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 閱讀進度

- [x] README.md
- [x] weekly_plan.md
- [x] notes.md
- [x] demo/demo_README.md

## Demo（示範程式）執行紀錄

以下為 Flat Integrated Demo 的學習紀錄；既有明確完成狀態已保留，原「結果」與「問題」內容已遷移至「問題／觀察」。

| Demo | 是否執行 | 問題／觀察 |
|---|---|---|
| demo/demo_01_token_embedding.py | ✅ | 原紀錄：完成；問題：no。 |
| demo/demo_02_attention_overview.py | ✅ | 原紀錄：完成；問題：no。 |
| demo/demo_03_position_multihead.py | ✅ | 原紀錄：完成；問題：no。 |
| demo/demo_04_transformer_flow.py | ✅ | 原紀錄：完成；問題：no。 |

## Practice 紀錄

| Practice | 是否完成 | 重要觀察 | 疑問 |
|---|---|---|---|
| Concept Practice | ✅ | 原紀錄：完成；錯誤修正：完成；備註：無。尚未整理具體觀察。 | 未記錄 |
| Guided Code Reading | ✅ | 原紀錄：完成；錯誤修正：完成；備註：無。尚未整理具體觀察。 | 未記錄 |

## 本週理解摘要

### 我目前能解釋

-

### 我仍不理解

-

### 下週前要釐清

-

## 個人概念紀錄

### Token（詞元）

文字的標籤，可透過分詞器將句子分小塊，並且賦予可對照的 ID。

修正版：Token 是模型處理文字的基本單位。原始文字無法直接送入 Transformer（轉換器架構），因此需要先透過 Tokenizer（分詞器）將句子切分成較小的單位，並轉換成對應的 Token ID（詞元編號）。

### Embedding（嵌入向量）

將 Token 轉換成機器可理解的數字向量。

修正版：Embedding 是 Token 的數學表示方式。每個 Token 都會被映射成高維向量，例如 DistilBERT 中每個 Token 會被轉換成 768 維向量。Transformer 並不是直接處理文字，而是處理這些 Embedding 向量。因此 Embedding 可以理解成 Token 的語意座標。

### Query（查詢）

我想找什麼。Q = E * Wq，Wq 由模型訓練而來，讓嵌入向量 E 變成搜尋模式。目前這個 Token 在理解自身時，希望從其他 Token 身上找到哪些資訊。

### Key（鍵）

我能提供什麼。K = E * Wk，讓嵌入向量 E 變成提供模式。每個 Token 的索引標籤，模型會利用 Query 與所有 Key 比較相似度，判斷哪些 Token 值得關注。

### Value（值）

我實際上是什麼。V = E * Wv，是真實攜帶的資訊。

### QKV 的關係

Q（Query）：我想找什麼資訊。

K（Key）：我有哪些資訊可以提供。

V（Value）：我真正攜帶的資訊內容。

Transformer 會先利用 Q x K^T 計算 Attention Score（注意力分數），再利用分數對 Value 加權。因此 Attention 的重點不是找到 Key，而是利用 Key 找到最有價值的 Value。

### Q x K^T

Q 與 K 的內積代表兩者的相似程度。Transformer 會利用 Query 與所有 Key 計算相似度。相似度越高，代表這個 Token 越值得關注。因此 Q x K^T 可以理解為 Attention Score 的來源。

### Softmax（柔性最大化函數）

Softmax 會把 Attention Score 轉換成權重分布。

1. 每個分數先做 e^x，放大數字差距，讓重要的 Token 得以突出。
2. 所有結果加總。
3. 每個值除以總和。

轉換後所有注意力權重加總為 1，因此可以理解為每個 Token 被關注的比例。

### Score x V

Softmax 產生的權重只代表關注程度。真正的資訊內容存在於 Value。Transformer 會利用權重對各個 Value 加權平均。因此 Attention 的目的不是找出最重要的 Token，而是根據重要程度融合不同 Token 的資訊，產生包含上下文語意的新向量表示。

### Attention（注意力機制）

根據任務從一句話裡面找重點。

修正版：Attention 的目的不是單純找重點，而是讓模型在處理某個 Token 時，決定應該參考哪些 Token。每個 Token 都可能有不同的注意力分布。

完整流程：

```text
Embedding
-> Q, K, V
-> Q x K^T
-> Attention Score
-> Softmax
-> Attention Weight
-> Weighted Sum of V
-> Contextual Representation
```

當注意力轉換完成後，可以讓單獨的 Token 變成包含前後文意思的 Token。

Self-Attention：
同一份資料內部互相比對，用來理解上下文。

Cross-Attention：
不同資料來源互相比對，用來對齊資訊。

Attention：
以上兩者的總稱，不一定只代表交叉對比。

### Attention Matrix（注意力矩陣）

透過轉換矩陣找哪個字跟哪個字比較有關聯。

### Self-Attention（自注意力）

讓同一段輸入中的每個 Token 互相比較。

### Attention 的最終目的

Attention 並不是單純找出重要的 Token，而是利用注意力權重融合其他 Token 的資訊。經過 Attention 後，原本只代表單字本身的 Embedding 會變成包含上下文資訊的新向量表示。因此相同的 Token 在不同句子中也能擁有不同的語意。

### Position Encoding（位置編碼）

賦予token順序，將位置向量與嵌入向量相加後得到

Token Embedding + Position Encoding
→ 帶有位置資訊的輸入向量

### Multi-Head Attention（多頭注意力）

讓每個token可以讀取每個token在幹嘛

讓每個 token 從不同角度去關注其他 token，取得上下文關係。
單頭 attention：
只用一種角度看 token 之間的關係。

多頭 attention：
用多組 Q、K、V 同時看不同關係。

### Transformer Encoder（轉換器編碼器）

讓輸入的內容可以轉換成機器能夠理解的數字向量

更正:將已經轉成向量的 token，進一步加工成具有上下文語意的向量表示。

### Transformer Decoder（轉換器解碼器）

將機器預測要回答的內容轉換為文字並且輸出給用戶看

根據前面已知的內容與 Encoder 輸出的語意資訊，逐步預測下一個 token，最後產生文字輸出。

### 本週與 VLM（視覺語言模型）的關係

理解文字是如何輸入並轉換成電腦可以讀取以及理解的內容

文字如何被切成 token，
token 如何變成 embedding，
embedding 如何透過 attention 和 encoder 形成語意表示，
最後 decoder 如何產生文字回答。

### Transformer 與 CLIP（對比式圖文預訓練）的關係

轉換器主要是做編碼，CLIP則是運用到視覺與文字編碼器去做對比

## Notion 更新

- [ ] Learning Roadmap
- [ ] Experiment Log
- [ ] Weekly Review

## ChatGPT 驗收

- [ ] 未驗收
- [x] Pass
- [ ] Minor Revision
- [ ] Major Revision

## ChatGPT 評語

Week01 已達成驗收標準，可以進入 Week02 CLIP（對比式圖文預訓練）。本週內容已能對應 `weekly_plan.md` 的核心目標：說明 Token（詞元）、Token ID（詞元編號）、Embedding（嵌入向量）的資料流，理解 Query（查詢）、Key（鍵）、Value（值）如何形成 Attention（注意力機制），並能分辨 Self-Attention（自注意力）、Position Encoding（位置編碼）、Multi-Head Attention（多頭注意力）、Encoder（編碼器）與 Decoder（解碼器）的功能。

從 `concept_practice.md` 來看，Q1 至 Q8 已完成作答與修正版整理。特別是 Q3、Q4、Q5、Q6 與 Q8 已補上較精準的說法，能看出已理解 Attention Matrix（注意力矩陣）的 row（列）代表單一 Query token 對所有 Key token 的注意力分布，也理解 CLIP 不是查詢模型資料庫，而是把影像與文字編碼到共同向量空間後比較相似度。

從 Week01 架構來看，`README.md`、`weekly_plan.md`、`notes.md`、`demo/` 與 `practice/` 的分工清楚。`practice/README.md` 已修正為 Guided Code Reading Mode（引導式程式閱讀模式），不再混用 `exercises/`、`solutions/` 或 TODO 補空題，符合目前 Week01 的學習定位。

目前可以給予 Pass。後續若要讓學習紀錄更完整，可再把 4 個 demo 與 6 個 guided demos 的實際輸出數值補進 Demo 執行紀錄，例如 Token IDs、Embedding shape、Attention weights、row sum、head split shape、Encoder memory 與 Decoder context；但這屬於紀錄精緻化，不影響本週概念驗收。

## 問題紀錄

- Demo 執行紀錄目前已標示完成，但部分欄位仍以「原紀錄：完成；問題：no」呈現，尚未完整寫出每個 demo 的實際輸出重點。
- Practice 紀錄已標示 Concept Practice 與 Guided Code Reading 完成，但「重要觀察」欄位仍偏摘要式，尚未逐項列出 shape、中間值與資料流觀察。
- 個人概念紀錄中部分早期說法仍保留原始表述，例如「Embedding 是機器可理解的數字向量」，雖然後方已有修正版，但日後複習時應優先看修正版。
- Notion 更新項目尚未勾選，若後續要做週週追蹤，建議補上 Learning Roadmap、Experiment Log 與 Weekly Review。

## 修正方式

- 將 Demo 執行紀錄從「完成 / no」逐步補成具體觀察，例如：Token 如何被轉成 Token ID、Embedding table 查表結果的 shape、Attention weights 每列加總是否接近 1、Multi-Head Attention 拆 head 與合併後的 shape。
- 在 Guided Code Reading 的紀錄中補上 6 個 guided demos 的重點觀察：Token ID shape、Position Encoding 相加結果、Q/K/V shape、Self-Attention row sum、head_dim 計算、Encoder memory 與 Decoder cross-attention 的關係。
- 後續複習時以「修正版」作為主要理解依據，避免回到早期不精準說法。
- 完成 Week02 CLIP 前，先把 Transformer -> CLIP 的連接整理成一段固定說法：文字與影像都能被編碼成向量，CLIP 將兩者對齊到共同向量空間，再用相似度比較圖文是否匹配。

## 本週最重要的理解

Week01 最重要的理解是：Transformer 並不是直接理解原始文字，而是先將文字切成 Token，再轉成 Token ID 與 Embedding，讓文字變成模型可計算的向量序列。接著，每個 token 的 embedding 會透過不同的權重矩陣產生 Q、K、V，並利用 Q 與 K 的相似度計算 Attention Score，再經過 Softmax 形成 Attention Weight，最後對 V 做加權融合，產生包含上下文資訊的 contextual representation（上下文表示）。

Self-Attention 的重點是同一序列內部互相參考，Position Encoding 補足 Transformer 本身沒有順序感的問題，Multi-Head Attention 則讓模型能從多個角度同時觀察 token 之間的關係。Encoder 偏向把輸入加工成可被後續模組使用的語意表示，Decoder 則根據已知內容與上下文逐步產生輸出。

這些概念會直接銜接 Week02 CLIP：文字經過 Text Encoder 形成文字向量，影像經過 Image Encoder 形成影像向量，兩者被放到共同向量空間中比較相似度。也就是說，Week01 建立的是後續理解 VLM / VLA 的基礎資料流。

## 一分鐘回顧

本週核心資料流可以整理為：原始文字先經過 Tokenizer 被切成 Token，再轉成 Token ID，接著透過 Embedding table 變成向量。加入 Position Encoding 後，模型可以同時取得語意與順序資訊。每個向量再被投影成 Q、K、V，透過 Q x K^T 計算注意力分數，經 Softmax 轉成權重後，對 V 做加權加總，形成具有上下文語意的新表示。多個 head 可以同時觀察不同關係，Encoder 將輸入整理成語意表示，Decoder 則利用這些表示逐步產生輸出。這套流程是理解 CLIP、VLM 與 VLA 的基礎。

## 下週目標

- 進入 Week02 CLIP，理解 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）的角色。
- 學會共同向量空間、cosine similarity（餘弦相似度）與圖文對齊的基本概念。
- 實作或執行一個簡單 CLIP demo，觀察圖片向量與文字向量如何比較相似度。
- 準備一張簡單圖片與 5 個文字標籤，用於測試 zero-shot classification（零樣本分類）。
- 將 Week01 的 Transformer 資料流與 Week02 的 CLIP 圖文對齊流程串成一張筆記圖。
