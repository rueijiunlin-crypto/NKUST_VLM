# Week01 Transformer Demo README

## Demo（示範程式）目標

本資料夾用小型 Python（程式語言）Demo 觀察 Transformer（轉換器架構）的基本資料流。每個子資料夾對應一個核心概念，請先閱讀子資料夾的 `README.md`，再執行 `demo_*.py`。

## 建議執行順序

請在 `learning/Week01_Transformer/` 目錄下依序執行：

```powershell
python demo/token/demo_tokenizer.py
python demo/embedding/demo_embedding.py
python demo/qkv/demo_qkv.py
python demo/attention/demo_attention.py
python demo/attention/demo_attention_matrix.py
python demo/self_attention/demo_self_attention.py
python demo/position_encoding/demo_position_encoding.py
python demo/multi_head_attention/demo_multi_head_attention.py
python demo/encoder_decoder/demo_encoder_decoder_flow.py
```

## Demo 與概念對應

| 概念 | Demo | 類型 |
|---|---|---|
| Token（詞元）/ Token ID（詞元編號） | `demo/token/demo_tokenizer.py` | Concept Demo（概念示範） |
| Embedding（嵌入向量） | `demo/embedding/demo_embedding.py` | Real Model Demo（真實模型示範） |
| Query（查詢）/ Key（鍵）/ Value（值） | `demo/qkv/demo_qkv.py` | Mechanism Demo（機制示範） |
| Attention（注意力機制） | `demo/attention/demo_attention.py` | Concept Demo（概念示範） |
| Attention Matrix（注意力矩陣） | `demo/attention/demo_attention_matrix.py` | Mechanism Demo（機制示範） |
| Self-Attention（自注意力） | `demo/self_attention/demo_self_attention.py` | Mechanism Demo（機制示範） |
| Position Encoding（位置編碼） | `demo/position_encoding/demo_position_encoding.py` | Mechanism Demo（機制示範） |
| Multi-Head Attention（多頭注意力） | `demo/multi_head_attention/demo_multi_head_attention.py` | Concept Demo（概念示範） |
| Transformer Encoder（轉換器編碼器）/ Transformer Decoder（轉換器解碼器） | `demo/encoder_decoder/demo_encoder_decoder_flow.py` | Concept Demo（概念示範） |

## 依賴提醒

`demo/embedding/demo_embedding.py` 可能需要額外套件：

```powershell
pip install transformers torch
```

若本機尚未安裝相關套件，請先記錄錯誤訊息，不要把 Demo（示範程式）標記為已完成。

## 完成標準

- 執行 Demo（示範程式）。
- 保存或摘要輸出。
- 在 `study_log.md` 寫下觀察。
- 回答對應子資料夾 `README.md` 的問題。
