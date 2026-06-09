# Attention Demo（注意力示範程式）

## 對應概念

Attention（注意力機制）與 Attention Matrix（注意力矩陣）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下依序執行：

```powershell
python demo/attention/demo_attention.py
python demo/attention/demo_attention_matrix.py
```

## 預期輸出

- 每個 Token 的 Attention Score（注意力分數）。
- 分數最高或權重最高的 Token。
- Attention Matrix。
- 每一列的權重分布。

## 觀察重點

- Attention Score 如何表示目前 Token 對其他 Token 的關注程度。
- Softmax（柔性最大化函數）後的權重如何加總為 1。
- Attention Matrix 的 row（列）與 column（欄）分別代表什麼。

## 執行後應回答的問題

1. Attention 是找單一最大值，還是加權融合資訊？
2. Attention Matrix 的每一列代表什麼？
3. 為什麼矩陣能幫助觀察 Self-Attention（自注意力）？
