# Week01 Transformer Demo 總覽

本資料夾依照 AGENTS_v2.md 採用概念子資料夾結構。每個子資料夾都有自己的 `README.md`，說明對應概念、執行指令、預期輸出、觀察重點與驗收問題。

## Demo 結構

```text
demo/
├─ demo_README.md
├─ token/
│  ├─ README.md
│  └─ demo_tokenizer.py
├─ embedding/
│  ├─ README.md
│  └─ demo_embedding.py
├─ qkv/
│  ├─ README.md
│  └─ demo_qkv.py
├─ attention/
│  ├─ README.md
│  ├─ demo_attention.py
│  └─ demo_attention_matrix.py
├─ self_attention/
│  ├─ README.md
│  └─ demo_self_attention.py
├─ position_encoding/
│  ├─ README.md
│  └─ demo_position_encoding.py
├─ multi_head_attention/
│  ├─ README.md
│  └─ demo_multi_head_attention.py
└─ encoder_decoder/
   ├─ README.md
   └─ demo_encoder_decoder_flow.py
```

## 建議執行順序

請從 `learning/Week01_Transformer/` 根目錄執行：

```powershell
python demo\token\demo_tokenizer.py
python demo\embedding\demo_embedding.py
python demo\qkv\demo_qkv.py
python demo\attention\demo_attention.py
python demo\attention\demo_attention_matrix.py
python demo\self_attention\demo_self_attention.py
python demo\position_encoding\demo_position_encoding.py
python demo\multi_head_attention\demo_multi_head_attention.py
python demo\encoder_decoder\demo_encoder_decoder_flow.py
```

## 外部套件與模型下載

大部分 Demo 只使用 Python 標準函式庫。

`demo/embedding/demo_embedding.py` 需要：

```powershell
pip install transformers torch
```

第一次執行可能需要下載 Hugging Face Transformers（模型工具套件）的 `distilbert-base-uncased` tokenizer（分詞器）與模型權重。

## Demo 與概念對照

| 概念 | Demo | Demo 類型 |
|---|---|---|
| Token（詞元）/ Token ID（詞元編號） | `demo/token/demo_tokenizer.py` | Concept Demo（概念示範） |
| Embedding（嵌入向量） | `demo/embedding/demo_embedding.py` | Real Model Demo（真實模型示範） |
| Query（查詢）、Key（鍵）、Value（值） | `demo/qkv/demo_qkv.py` | Mechanism Demo（機制示範） |
| Attention（注意力機制） | `demo/attention/demo_attention.py` | Concept Demo（概念示範） |
| Attention Matrix（注意力矩陣） | `demo/attention/demo_attention_matrix.py` | Mechanism Demo（機制示範） |
| Self-Attention（自注意力） | `demo/self_attention/demo_self_attention.py` | Mechanism Demo（機制示範） |
| Position Encoding（位置編碼） | `demo/position_encoding/demo_position_encoding.py` | Mechanism Demo（機制示範） |
| Multi-Head Attention（多頭注意力） | `demo/multi_head_attention/demo_multi_head_attention.py` | Concept Demo（概念示範） |
| Encoder（編碼器）/ Decoder（解碼器） | `demo/encoder_decoder/demo_encoder_decoder_flow.py` | Concept Demo（概念示範） |

## Demo 完成條件

依照 AGENTS_v2.md，Demo 不以成功執行為完成條件。學生需完成：

1. 成功執行 Demo。
2. 保存輸出結果。
3. 在 `study_log.md` 記錄觀察。
4. 回答對應子資料夾 `README.md` 中的問題。

## 與本週主題的關係

這些 Demo 對應 Week01 Transformer（轉換器架構）的資料流：

```text
Token -> Token ID -> Embedding -> QKV -> Attention -> Self-Attention
-> Position Encoding -> Multi-Head Attention -> Encoder / Decoder
```

## 與 VLM/VLA 研究的關係

- VLM（視覺語言模型）需要把文字與影像都轉成可計算的表示。
- VLA（視覺語言動作模型）需要把文字指令、視覺場景與動作描述連接起來。
- Transformer 的 Attention、Self-Attention、Encoder、Decoder 是理解 CLIP、LLaVA、OpenVLA 的基礎。
