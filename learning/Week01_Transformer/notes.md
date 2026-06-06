# Week01 Notes：Transformer 基礎

## 1. 為什麼先學 Transformer

Vision-Language Model（視覺語言模型）通常需要同時理解圖片與文字。圖片可以表示成一串影像特徵，文字可以表示成一串文字特徵，而 Transformer（轉換器架構）正是擅長處理「序列資料」與「元素之間關係」的架構。

對 VLM 初學者來說，本週最重要的不是背公式，而是理解三件事：

- 文字如何變成模型能處理的數字。
- 模型如何判斷句子中哪些部分彼此有關。
- 這套機制如何延伸到圖片與文字對齊。

## 2. Token（詞元）

Token 是模型處理文字時的基本單位。它可能是一個中文字、一個英文單字、一段子詞，或是標點符號。

例如句子：

```text
請帶我去實驗室
```

可能被切成：

```text
請 / 帶 / 我 / 去 / 實驗室
```

真正的模型會依照自己的 Tokenizer（分詞器）切分文字，所以不同模型切出來的 Token 不一定完全相同。

重要觀念：

- 模型不是直接理解原始文字。
- 文字會先被切成 Token。
- Token 會被轉成數字編號，再轉成向量。

## 3. Embedding（嵌入向量）

Embedding 是 Token 的向量表示。向量可以想成一串數字，模型用這串數字表示某個 Token 的語意特徵。

直覺例子：

- 「實驗室」和「研究室」在語意上可能比較接近。
- 「椅子」和「桌子」都屬於室內物件，語意上也可能比較接近。
- 「導航」和「前往」都和移動任務有關。

Embedding 的目的不是讓人直接閱讀，而是讓模型能計算、比較與更新語意表示。

## 4. Attention（注意力機制）

Attention 是 Transformer 的核心。它的直覺是：模型在理解某個 Token 時，會去看其他 Token，並判斷哪些資訊比較重要。

例如句子：

```text
請帶我去紅色門旁邊的實驗室
```

模型理解「實驗室」時，可能需要注意：

- 「紅色門」：提供位置線索。
- 「旁邊」：提供空間關係。
- 「去」：表示這是導航任務。

Attention 讓模型不只逐字閱讀，而是能建立上下文關係。

## 5. Self-Attention（自注意力）

Self-Attention 是 Attention 的一種形式，意思是同一段輸入內部的 Token 彼此互相參考。

如果輸入是一句話，每個 Token 都會問：

```text
我要理解自己時，應該參考句子中的哪些 Token？
```

Self-Attention 對 VLM 很重要，因為影像也可以被切成多個 Patch（影像切塊）。模型可以讓不同 Patch 彼此參考，理解物件位置、場景結構與上下文。

## 6. Transformer Encoder（轉換器編碼器）

Encoder 的主要任務是理解輸入並產生表示。它會接收完整輸入，經過多層 Self-Attention 與前饋網路後，輸出每個位置的上下文表示。

常見用途：

- 文字分類
- 句子表示
- 圖文檢索
- 影像特徵抽取
- 語意比對

在 CLIP（對比式圖文預訓練）中，文字與圖片都需要被編碼成向量，這就是 Encoder 思想很重要的地方。

## 7. Transformer Decoder（轉換器解碼器）

Decoder 的主要任務是產生輸出。它通常根據已經產生的內容，一次預測下一個 Token。

常見用途：

- 對話生成
- 圖片問答
- 影像描述
- 任務指令生成
- 機器人動作文字規劃

在 LLaVA（大型語言與視覺助手）這類模型中，影像特徵會被接到大型語言模型，讓 Decoder 類模型根據圖片與文字問題產生回答。

## 8. Encoder 與 Decoder 的簡單比較

| 項目 | Encoder | Decoder |
|---|---|---|
| 主要目的 | 理解輸入 | 產生輸出 |
| 常見任務 | 分類、檢索、特徵抽取 | 問答、描述、對話 |
| 典型輸入 | 完整句子或影像特徵 | 上下文與已產生文字 |
| 與 VLM 的關係 | 建立圖片或文字表示 | 根據圖片與問題生成回答 |

## 9. 為什麼 VLM 需要 Transformer

VLM 要處理兩種資料：

- 文字：由 Token 組成的序列。
- 影像：可切成 Patch 或轉成影像特徵序列。

Transformer 擅長處理序列與序列內部關係，因此可以用來：

- 理解文字指令。
- 理解影像中的物件與區域。
- 對齊圖片與文字的語意。
- 支援視覺問答與影像描述。
- 讓機器人把自然語言指令和視覺場景連起來。

對你的研究方向來說，Transformer 是理解「使用者說什麼」與「機器人看到什麼」之間關係的基礎。

## 10. Transformer 與 CLIP 的關係

CLIP 的目標是讓圖片與文字可以互相比較。它通常包含：

- Image Encoder（影像編碼器）：把圖片轉成向量。
- Text Encoder（文字編碼器）：把文字轉成向量。
- Similarity（相似度）：比較圖片向量與文字向量是否接近。

Transformer 與 CLIP 的關係可以這樣理解：

1. 文字需要 Token 與 Embedding。
2. 文字編碼器需要理解句子語意。
3. 影像也可以透過 Vision Transformer（視覺轉換器）切成 Patch 後編碼。
4. 圖片與文字最後會被放到共同向量空間比較。

因此，學會 Transformer 的基礎後，CLIP 的「圖文對齊」會更容易理解。

## 11. 本週最小理解版本

如果只能記住幾句話，請記住：

- Token 是文字的基本單位。
- Embedding 是 Token 的向量表示。
- Attention 讓模型知道該看哪些上下文。
- Self-Attention 讓同一段輸入內部彼此參考。
- Encoder 偏向理解，Decoder 偏向生成。
- VLM 需要 Transformer 來連接影像、文字與語意。
- CLIP 是理解圖文對齊的下一步。

## 12. AGENTS v2 五層學習補強

本節保留前面原有說明，並依照 Learning Content Standard（學習內容標準）補齊每個核心概念的五層學習架構。閱讀時建議依照每個概念後的 Demo（示範程式）提示立即執行，不要把所有 Demo 集中到最後。

### 12.1 Token（詞元）

#### Level 1：直覺理解

Token（詞元）可以想成模型閱讀文字時的「最小閱讀單位」。人看到一句話時，可以直接理解整句意思；模型則需要先把句子拆成一小段一小段，再把這些片段轉成數字。

生活化例子：你要把「請帶我去實驗室」交給機器人理解時，模型不會一次吃下整句話，而是先拆成「請」、「帶」、「我」、「去」、「實驗室」等片段。

#### Level 2：技術原理

Tokenizer（分詞器）會把文字切成 Token，接著把每個 Token 對應到 vocabulary（詞彙表）中的 Token ID（詞元編號）。模型真正接收的是 Token ID，而不是原始文字。

簡化資料流：

```text
原始文字 -> Tokenizer（分詞器） -> Token（詞元） -> Token ID（詞元編號）
```

不同模型的 Tokenizer 規則不同，因此同一句話在不同模型中可能被切成不同 Token。

#### Level 3：實作驗證

建議讀完 Token（詞元）後立即執行：

Demo 名稱：`demo_tokenizer.py`

執行指令：

```powershell
python demo\demo_tokenizer.py
```

觀察重點：

- 原始文字如何被切成 Token。
- Token 如何被轉成 Token ID。
- Token 列表與 Token ID 列表是否一一對應。

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
3. 為什麼模型不能直接使用原始文字？

#### Level 4：VLM/VLA 關聯

在 Vision-Language Model（視覺語言模型）中，文字指令、圖片描述與問題都需要先被切成 Token。CLIP（對比式圖文預訓練）的文字編碼器需要 Token；LLaVA（大型語言與視覺助手）需要把使用者問題切成 Token 後再生成回答；OpenVLA（開源視覺語言動作模型）也需要理解語言指令中的動作、物件與目標位置。

對機器人來說，「拿起紅色杯子」這類指令必須先被切成可處理的語言單位，後續才有機會連結到視覺場景與動作規劃。

#### Level 5：驗收問題

請用自己的話回答：

1. Token（詞元）是什麼？
2. Token 和 Token ID 有什麼不同？
3. 如果輸入是「go to the red door」，你會如何直覺切分？
4. 為什麼 VLM/VLA 必須先處理語言 Token？

### 12.2 Embedding（嵌入向量）

#### Level 1：直覺理解

Embedding（嵌入向量）是把 Token 轉成一串數字，讓模型可以計算語意關係。可以把它想成每個詞在模型世界中的「座標」。

生活化例子：「實驗室」和「研究室」在語意上接近，它們的向量位置可能也比較接近；「實驗室」和「香蕉」的語意較遠，向量位置可能較遠。

#### Level 2：技術原理

模型會透過 Embedding Table（嵌入表）把 Token ID 查成向量。每個 Token ID 都對應一個固定長度的向量，這些向量會在訓練過程中被更新，使模型學到語意與上下文關係。

簡化資料流：

```text
Token ID（詞元編號） -> Embedding Table（嵌入表） -> Embedding Vector（嵌入向量）
```

Embedding 的 shape（形狀）通常可理解成：

```text
batch_size x token_count x embedding_dim
```

#### Level 3：實作驗證

建議讀完 Embedding（嵌入向量）後立即執行：

Demo 名稱：`demo_embedding.py`

執行指令：

```powershell
python demo\demo_embedding.py
```

若尚未安裝套件，先執行：

```powershell
pip install transformers torch
```

注意：此 Demo 會載入 Hugging Face Transformers（模型工具套件）的 `distilbert-base-uncased`，第一次執行時可能需要下載模型與 tokenizer 檔案。

觀察重點：

- Token 數量是多少。
- Embedding 維度是多少。
- 每個 Token 是否都有對應向量表示。

預期輸出：

```text
Token（詞元）列表：
[...]

Embedding Shape（嵌入向量形狀）：
(batch_size, token_count, embedding_dim)
```

執行後應回答問題：

1. Embedding Shape 中三個數字分別代表什麼？
2. 為什麼每個 Token 都需要向量？
3. Embedding 和 Token ID 有什麼不同？

#### Level 4：VLM/VLA 關聯

CLIP 會把文字與影像都轉成可比較的向量表示；Embedding 是理解文字向量化的第一步。LLaVA 會把文字 Token 與影像特徵接到語言模型中，讓模型根據圖片回答問題。OpenVLA 則需要把語言指令、視覺觀察與可能動作放進可計算的表示空間。

在室內語意導覽中，「紅色門」、「實驗室」、「前方」等語意若能被轉成向量，模型才有機會把語言描述對應到影像中的區域。

#### Level 5：驗收問題

請用自己的話回答：

1. Embedding（嵌入向量）解決了什麼問題？
2. Token ID 和 Embedding Vector（嵌入向量）哪一個更接近模型可計算的語意表示？
3. 為什麼語意相近的詞在向量空間中可能比較接近？
4. Embedding 如何幫助 VLM 連接文字和圖片？

### 12.3 Attention（注意力機制）

#### Level 1：直覺理解

Attention（注意力機制）是模型決定「現在應該關注哪些資訊」的方法。理解一句話時，不是每個字都同等重要；模型會替不同位置分配不同重要性。

生活化例子：在「請帶我去紅色門旁邊的實驗室」中，理解目的地時，「紅色門」、「旁邊」、「實驗室」比「請」更重要。

#### Level 2：技術原理

Attention 常用 Query（查詢）、Key（鍵）、Value（值）來理解：

- Query（查詢）：目前這個位置想找什麼資訊。
- Key（鍵）：每個位置提供給別人比對的特徵。
- Value（值）：真正被取用、加權整合的內容。

模型會用 Query 和 Key 計算 Attention Score（注意力分數），再用分數加權 Value，得到新的上下文表示。

簡化資料流：

```text
Query 與 Key 比對 -> Attention Score（注意力分數） -> 加權 Value -> 上下文表示
```

#### Level 3：實作驗證

建議讀完 Attention（注意力機制）後立即執行：

Demo 名稱：`demo_attention.py`

執行指令：

```powershell
python demo\demo_attention.py
```

觀察重點：

- 每個 Token 的 Attention Score 是否不同。
- 分數最高的 Token 是哪一個。
- 分數如何影響模型目前關注的資訊。

預期輸出：

```text
Token（詞元）與 Attention Score（注意力分數）：
...
最重要的 Token（詞元）：
laboratory
```

執行後應回答問題：

1. Attention Score 代表什麼？
2. 為什麼不是所有 Token 都一樣重要？
3. 在導航指令中，哪些 Token 可能應該得到較高注意力？

#### Level 4：VLM/VLA 關聯

在 CLIP 中，Attention 幫助文字或影像編碼器建立更好的表示。在 LLaVA 中，語言模型需要根據圖片特徵與問題文字決定要關注哪些資訊。在 OpenVLA 中，模型可能需要關注影像中的目標物、語言中的動作詞，以及機器人目前狀態。

例如桌面操作機器人聽到「把紅色杯子放到盤子旁邊」時，Attention 可以協助模型關注「紅色杯子」、「放到」、「盤子旁邊」這些對行動最重要的資訊。

#### Level 5：驗收問題

請用自己的話回答：

1. Attention（注意力機制）是什麼？
2. Query、Key、Value 分別可以怎麼理解？
3. Attention Score 高代表什麼？
4. Attention 如何幫助機器人理解語言指令與視覺場景？

### 12.4 Self-Attention（自注意力）

#### Level 1：直覺理解

Self-Attention（自注意力）是同一段輸入內部彼此互相參考。每個 Token 都可以看同一句話中的其他 Token，判斷哪些字對理解自己最重要。

生活化例子：在「紅色門旁邊的實驗室」中，理解「實驗室」時需要參考「紅色門」與「旁邊」；理解「旁邊」時也需要知道它描述的是哪個物件。

#### Level 2：技術原理

Self-Attention 會讓同一序列中的每個位置都產生自己的 Query、Key、Value，並和同一序列中的其他位置計算注意力。結果是每個 Token 的表示都會融合上下文資訊。

簡化資料流：

```text
同一句話中的每個 Token -> 互相比對注意力 -> 產生上下文化 Token 表示
```

Self-Attention 不只適用於文字，也可用於影像 Patch（影像切塊），讓不同影像區域彼此交換資訊。

#### Level 3：實作驗證

建議讀完 Self-Attention（自注意力）後立即執行：

Demo 名稱：`demo_self_attention.py`

執行指令：

```powershell
python demo\demo_self_attention.py
```

觀察重點：

- 每個 Token 都有自己的注意力分布。
- 不同 Token 會關注不同上下文。
- Self-Attention 是「序列內部互相參考」，不是只看單一目標 Token。

預期輸出：

```text
Query token: laboratory
attends to: red, door, laboratory
```

執行後應回答問題：

1. Self-Attention 和 Attention 有什麼關係？
2. 為什麼每個 Token 都需要看其他 Token？
3. 影像 Patch 之間為什麼也可以使用 Self-Attention？

#### Level 4：VLM/VLA 關聯

Vision Transformer（視覺轉換器）會把圖片切成 Patch，再用 Self-Attention 學習不同區域之間的關係。CLIP 的影像編碼器若使用 Vision Transformer，就會利用這種機制理解影像內容。OpenVLA 面對機器人視覺輸入時，也需要理解不同物件、目標與環境區域的關係。

在災害巡檢或室內導覽中，模型需要同時理解門、走廊、障礙物與文字指令，Self-Attention 是建立這些上下文關係的基礎。

#### Level 5：驗收問題

請用自己的話回答：

1. Self-Attention（自注意力）是什麼？
2. 為什麼 Self-Attention 適合處理一句話？
3. 為什麼圖片切成 Patch 後也能使用 Self-Attention？
4. Self-Attention 對 VLM/VLA 的場景理解有什麼幫助？

### 12.5 Encoder（編碼器）

#### Level 1：直覺理解

Encoder（編碼器）的工作是「理解輸入」。它把文字、圖片或特徵序列讀完後，整理成模型可以拿來分類、比對或檢索的表示。

生活化例子：Encoder 像是閱讀理解的人，先把文章讀懂並整理重點，但不一定負責寫出下一句回答。

#### Level 2：技術原理

Transformer Encoder（轉換器編碼器）通常由多層 Self-Attention、Feed Forward Network（前饋網路）、Residual Connection（殘差連接）與 Layer Normalization（層正規化）組成。輸入序列經過 Encoder 後，每個位置都會得到包含上下文的表示。

簡化資料流：

```text
Token/影像特徵序列 -> 多層 Encoder -> 上下文化表示 -> 分類、檢索或相似度比對
```

#### Level 3：實作驗證

建議讀完 Encoder（編碼器）後立即執行：

Demo 名稱：`demo_encoder_decoder_flow.py`

執行指令：

```powershell
python demo\demo_encoder_decoder_flow.py
```

觀察重點：

- Encoder 的輸入是完整指令或完整特徵。
- Encoder 的輸出偏向「表示」或「理解結果」。
- Encoder 適合用在分類、檢索與圖文相似度。

預期輸出：

```text
Encoder mode:
input instruction -> contextual representation -> retrieval/classification
```

執行後應回答問題：

1. Encoder 的主要任務是什麼？
2. Encoder 為什麼適合 CLIP 的圖片與文字編碼？
3. Encoder 的輸出通常拿來做什麼？

#### Level 4：VLM/VLA 關聯

CLIP 需要 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）把圖片和文字轉成共同向量空間中的表示。這是圖文檢索、零樣本分類與語意比對的基礎。VLA 系統也可能使用 Encoder 理解目前影像、語言指令與機器人狀態。

在室內語意導覽中，Encoder 可以把「走廊影像」與「實驗室門口」等語意表示出來，讓系統比較哪個視覺區域最符合文字目標。

#### Level 5：驗收問題

請用自己的話回答：

1. Encoder（編碼器）偏向理解還是生成？
2. Encoder 的輸出為什麼適合做相似度比較？
3. CLIP 為什麼需要 Image Encoder 與 Text Encoder？
4. Encoder 如何支援機器人的語意導覽？

### 12.6 Decoder（解碼器）

#### Level 1：直覺理解

Decoder（解碼器）的工作是「產生輸出」。它會根據已知上下文，一步一步產生文字、答案或任務描述。

生活化例子：Decoder 像是正在回答問題的人，會根據已經讀到的資訊和已經說出的字，繼續決定下一個字要說什麼。

#### Level 2：技術原理

Transformer Decoder（轉換器解碼器）通常使用 Masked Self-Attention（遮罩自注意力），讓模型產生文字時只能看已經產生的 Token，不能偷看未來答案。若是 Encoder-Decoder 架構，Decoder 還可以透過 Cross-Attention（交叉注意力）參考 Encoder 的輸出。

簡化資料流：

```text
已產生 Token + 上下文表示 -> Decoder -> 下一個 Token -> 持續生成
```

#### Level 3：實作驗證

建議讀完 Decoder（解碼器）後立即執行：

Demo 名稱：`demo_encoder_decoder_flow.py`

執行指令：

```powershell
python demo\demo_encoder_decoder_flow.py
```

觀察重點：

- Decoder 的輸出偏向逐步產生。
- Decoder 會根據上下文與已產生內容決定下一步。
- Decoder 適合問答、影像描述、對話與動作文字規劃。

預期輸出：

```text
Decoder mode:
context + generated tokens -> next token/action description
```

執行後應回答問題：

1. Decoder 的主要任務是什麼？
2. 為什麼 Decoder 產生文字時需要一步一步生成？
3. LLaVA 為什麼需要 Decoder 類語言模型？
4. Decoder 如何支援機器人動作文字規劃？

#### Level 4：VLM/VLA 關聯

LLaVA 類模型常使用 Decoder 類大型語言模型，根據圖片特徵與文字問題生成回答。OpenVLA 則需要把視覺與語言理解轉成可執行或可描述的動作，例如「移動到桌前」、「抓取杯子」、「放到盤子旁邊」。

對桌面操作機器人而言，Decoder 可以把視覺場景與語言需求轉成下一步動作描述，成為後續控制模組的輸入。

#### Level 5：驗收問題

請用自己的話回答：

1. Decoder（解碼器）偏向理解還是生成？
2. Masked Self-Attention（遮罩自注意力）的用途是什麼？
3. Decoder 和 Encoder 的差異是什麼？
4. Decoder 如何連接 VLM 的回答生成與 VLA 的動作規劃？

## 13. 本週已掌握內容

完成本週後，應能掌握：

- Token（詞元）如何把文字切成模型可處理的單位。
- Token ID（詞元編號）如何作為查表與模型輸入的中介。
- Embedding（嵌入向量）如何把 Token 轉成可計算的向量表示。
- Attention（注意力機制）如何用重要性分數關注上下文。
- Self-Attention（自注意力）如何讓同一段序列內部互相參考。
- Encoder（編碼器）如何產生適合理解、檢索與比對的表示。
- Decoder（解碼器）如何根據上下文逐步產生文字或動作描述。
- Transformer（轉換器架構）如何支援 CLIP、LLaVA、OpenVLA 與機器人語意任務。

## 14. 本週尚未涵蓋內容

本週尚未深入涵蓋：

- Positional Encoding（位置編碼）：模型如何知道 Token 或 Patch 的順序與位置。
- Multi-Head Attention（多頭注意力）：模型如何從多個角度同時關注資訊。
- Layer Normalization（層正規化）：Transformer 如何穩定訓練。
- Feed Forward Network（前饋網路）：Attention 之後如何進一步轉換表示。
- Cross-Attention（交叉注意力）：文字和影像之間如何互相參考。
- Vision Transformer（視覺轉換器）：圖片如何切成 Patch 後進入 Transformer。
- CLIP 的 contrastive learning（對比式學習）訓練目標。
- OpenVLA 如何把視覺、語言與動作資料整合成機器人策略。

## 15. 下一週預告

下一週將銜接 CLIP（對比式圖文預訓練）與圖文對齊，重點包括：

- 圖片如何被 Image Encoder（影像編碼器）轉成向量。
- 文字如何被 Text Encoder（文字編碼器）轉成向量。
- 圖片向量與文字向量如何進入共同向量空間。
- Similarity（相似度）如何用於圖文檢索與零樣本分類。
- CLIP 如何成為後續 LLaVA 與 OpenVLA 的基礎概念。
