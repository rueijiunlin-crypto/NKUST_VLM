# Multi-Head Attention Demo

## 對應概念

Multi-Head Attention（多頭注意力）。

## 執行指令

```powershell
python demo\multi_head_attention\demo_multi_head_attention.py
```

## 預期輸出

- 多個 head（頭）的注意力分數
- 每個 head 的主要關注 Token

## 觀察重點

- 不同 head 可關注不同語意線索。
- 多視角關注能補足單一 Attention 的限制。

## 執行後應回答的問題

1. 為什麼需要多個 head？
2. 不同 head 可以學到哪些不同關係？
3. Multi-Head Attention 如何銜接 Encoder（編碼器）？
