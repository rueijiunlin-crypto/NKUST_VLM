# Self-Attention Demo

## 對應概念

Self-Attention（自注意力）。

## 執行指令

```powershell
python demo\self_attention\demo_self_attention.py
```

## 預期輸出

- 不同 Query token 的注意力分布
- 每個 Token 對其他 Token 的關注分數

## 觀察重點

- 每個 Token 都可以是 Query（查詢）。
- 不同 Token 會看到不同資訊。
- Self-Attention 是序列內部互相參考。

## 執行後應回答的問題

1. 為什麼每個 Token 都可以是 Query？
2. Self-Attention 和一般 Attention 有什麼關係？
3. 為什麼不同 Token 會關注不同資訊？
