# Week01 Transformer Demo 說明

本資料夾提供三個 Demo（示範程式），用來理解 Transformer（轉換器架構）中的基礎流程：文字如何變成 Token（詞元）、Token 如何變成 Embedding（嵌入向量），以及 Attention（注意力機制）如何決定要關注哪些資訊。

## 檔案列表

- `demo_tokenizer.py`：示範文字如何切成 Token（詞元）與 Token ID（詞元編號）。
- `demo_embedding.py`：使用 Hugging Face Transformers（模型工具套件）取得 Embedding Shape（嵌入向量形狀）。
- `demo_attention.py`：用簡化分數展示 Attention（注意力機制）的直覺。

## 如何執行

請先切換到 Week01 的 `demo/` 資料夾：

```powershell
cd D:\NKUST_VLM\learning\Week01_Transformer\demo
```

執行 Tokenizer（分詞器）示範：

```powershell
python demo_tokenizer.py
```

執行 Embedding（嵌入向量）示範：

```powershell
python demo_embedding.py
```

如果尚未安裝套件，請先安裝 Hugging Face Transformers（模型工具套件）與 PyTorch（深度學習框架）：

```powershell
pip install transformers torch
```

執行 Attention（注意力機制）示範：

```powershell
python demo_attention.py
```

也可以從 Week01 根目錄執行：

```powershell
python demo\demo_tokenizer.py
python demo\demo_embedding.py
python demo\demo_attention.py
```

## 預期結果

### demo_tokenizer.py

你會看到輸入文字：

```text
take me to the laboratory
```

程式會輸出：

- Token（詞元）列表
- Token ID（詞元編號）列表
- 文字如何先被切分，再轉成數字 ID 的說明

### demo_embedding.py

你會看到：

- Token（詞元）列表
- Embedding Shape（嵌入向量形狀）
- Token 數量
- Embedding 維度

Embedding Shape 通常會長得像：

```text
(batch_size, token_count, embedding_dim)
```

其中 batch_size（批次大小）代表一次輸入幾筆資料，token_count（詞元數量）代表本句被切成幾個 Token，embedding_dim（嵌入維度）代表每個 Token 的向量長度。

### demo_attention.py

你會看到：

- 每個 Token（詞元）的 Attention Score（注意力分數）
- 最重要的 Token
- Attention 如何決定關注哪些資訊的說明

## 如何觀察

觀察 `demo_tokenizer.py` 時，請注意原始文字並不是直接進入模型，而是先變成 Token 與 ID。

觀察 `demo_embedding.py` 時，請注意每個 Token 都會對應到一個向量。這些向量不是給人閱讀，而是給模型計算語意與上下文關係。

觀察 `demo_attention.py` 時，請注意分數最高的 Token 代表目前任務中最需要關注的資訊。在導航語句中，目的地通常會是很重要的線索。

## 與 Transformer 的關係

Transformer（轉換器架構）的基本流程可以簡化成：

```text
文字輸入 → Token（詞元） → Token ID（詞元編號） → Embedding（嵌入向量） → Attention（注意力機制） → 上下文表示
```

這三個 Demo 分別對應流程中的三個重要部分：

1. `demo_tokenizer.py`：理解文字如何變成 Token。
2. `demo_embedding.py`：理解 Token 如何變成向量。
3. `demo_attention.py`：理解模型如何判斷哪些 Token 比較重要。

理解這三件事後，下一週學習 CLIP（對比式圖文預訓練）時，就能更容易理解圖片與文字如何被轉成向量並進行相似度比較。

## AGENTS v2 Demo 補強

### 新增 Demo 檔案

- `demo_self_attention.py`：展示 Self-Attention（自注意力）中，不同 Token（詞元）如何在同一序列內互相參考。
- `demo_encoder_decoder_flow.py`：比較 Encoder（編碼器）與 Decoder（解碼器）在理解、檢索、生成與動作描述中的角色差異。

### 模型下載提醒

`demo_embedding.py` 會使用 Hugging Face Transformers（模型工具套件）載入 `distilbert-base-uncased`。第一次執行時，可能需要下載 tokenizer（分詞器）與模型權重；若環境無網路，請先在可連網環境準備模型快取，或暫時只閱讀程式與預期輸出。

### 補強後建議執行順序

請從 Week01 根目錄依序執行：

```powershell
python demo\demo_tokenizer.py
python demo\demo_embedding.py
python demo\demo_attention.py
python demo\demo_self_attention.py
python demo\demo_encoder_decoder_flow.py
```

### 與 VLM/VLA 研究的關係

- `demo_tokenizer.py`：對應 VLM/VLA 對語言指令的第一步處理，例如把「拿起紅色杯子」切成可處理的 Token。
- `demo_embedding.py`：對應文字向量化，協助理解 CLIP（對比式圖文預訓練）如何把文字放進共同向量空間。
- `demo_attention.py`：對應模型如何關注任務中最重要的語意線索，例如導航目標、物件屬性或空間關係。
- `demo_self_attention.py`：對應文字 Token 或影像 Patch（影像切塊）之間的上下文關係，是 Vision Transformer（視覺轉換器）與多模態理解的基礎。
- `demo_encoder_decoder_flow.py`：對應 CLIP 的 Encoder（編碼器）式圖文表示，以及 LLaVA（大型語言與視覺助手）和 OpenVLA（開源視覺語言動作模型）中 Decoder（解碼器）式回答生成或動作描述。

### 每個 Demo 對應的學習概念

| Demo | 對應概念 | 執行後應能回答 |
|---|---|---|
| `demo_tokenizer.py` | Token（詞元） | Token 和原始文字有什麼差異？ |
| `demo_embedding.py` | Embedding（嵌入向量） | Embedding Shape 代表什麼？ |
| `demo_attention.py` | Attention（注意力機制） | Attention Score 代表什麼？ |
| `demo_self_attention.py` | Self-Attention（自注意力） | 為什麼同一句話內的 Token 需要互相參考？ |
| `demo_encoder_decoder_flow.py` | Encoder（編碼器）、Decoder（解碼器） | Encoder 偏理解、Decoder 偏生成，差異是什麼？ |

