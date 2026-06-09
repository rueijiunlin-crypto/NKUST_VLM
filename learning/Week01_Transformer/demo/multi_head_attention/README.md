# Multi-Head Attention Demo（多頭注意力示範程式）

## 對應概念

Multi-Head Attention（多頭注意力）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/multi_head_attention/demo_multi_head_attention.py
```

## 預期輸出

- 多個 head（頭）的關注目標。
- 各 head 的注意力分布摘要。
- 合併多個 head 後的輸出示意。

## 觀察重點

- 不同 head 可以從不同視角觀察同一段輸入。
- 單一 Attention 較難同時捕捉多種關係。
- 多個 head 的輸出會被串接與投影。

## 執行後應回答的問題

1. 為什麼多個 head 比單一 Attention 更有彈性？
2. 不同 head 可能分別關注哪些資訊？
3. Multi-Head Attention 如何幫助 VLM（視覺語言模型）處理圖文線索？
