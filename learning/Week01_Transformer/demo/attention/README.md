# Attention Demo

## 對應概念

Attention（注意力機制）與 Attention Matrix（注意力矩陣）。

## 執行指令

```powershell
python demo\attention\demo_attention.py
python demo\attention\demo_attention_matrix.py
```

## 預期輸出

- 每個 Token（詞元）的 Attention Score（注意力分數）
- 最重要的 Token
- Attention Matrix（注意力矩陣）

## 觀察重點

- Attention Score 如何表達重要性。
- Attention Matrix 每一列如何表示一個 Query Token 的注意力分布。
- 每一列加總是否為 1。

## 執行後應回答的問題

1. Attention Score 代表什麼？
2. 為什麼要用 Q x K 產生分數？
3. Attention Matrix 的列與欄分別代表什麼？
