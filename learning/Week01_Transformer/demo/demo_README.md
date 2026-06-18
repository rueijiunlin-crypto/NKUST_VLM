# Week01 Transformer Demo README

## Demo 目標

Week01 採用 Flat Integrated Demo（扁平整合式 Demo）。這些程式快速回答「Transformer 的概念在做什麼（What）」；完整 shape tracing、中間值與內部機制拆解請使用 [`../practice/coding/guided_demos/`](../practice/coding/guided_demos/)。

所有 Demo 僅使用 Python 標準函式庫，不需額外安裝套件。

## Demo 清單

| Demo 名稱 | 對應概念 | 執行指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| Token 與 Embedding | Token、Token ID、Embedding | `python demo/demo_01_token_embedding.py` | Token、ID 與簡化向量 | 文字會先變成索引，再變成可計算向量 |
| Attention Overview | QKV 角色、Attention、Self-Attention | `python demo/demo_02_attention_overview.py` | 不同 Query 的注意力分布與重點 | Attention 會依目前位置改變參考對象 |
| Position 與 Multi-Head | Position Encoding、Multi-Head Attention | `python demo/demo_03_position_multihead.py` | 位置標記與兩個 head 的關注重點 | 模型需要順序，也可同時觀察不同關係 |
| Transformer Flow | Encoder、Decoder、VLM 關聯 | `python demo/demo_04_transformer_flow.py` | 輸入理解、上下文與逐步輸出流程 | Encoder 偏向理解，Decoder 偏向生成 |

## 建議執行順序

```powershell
python demo/demo_01_token_embedding.py
python demo/demo_02_attention_overview.py
python demo/demo_03_position_multihead.py
python demo/demo_04_transformer_flow.py
```

## Demo 與 Guided Code Reading 的分工

```text
demo = What
practice/coding/guided_demos = How
```

Demo 保持精簡，不逐步拆解 QKV、不做完整 shape tracing，也不印出大量矩陣。若想理解計算如何完成，請接著執行 Guided Code Reading。

## 完成標準

* 成功執行 Demo。
* 在 `study_log.md` 摘要實際輸出與觀察。
* 能指出每個 Demo 對應的核心概念。
