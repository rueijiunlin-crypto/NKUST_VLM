# Self-Attention Demo（自注意力示範程式）

## 對應概念

Self-Attention（自注意力）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/self_attention/demo_self_attention.py
```

## 預期輸出

- 每個 Query token。
- 該 Query token 關注的其他 Token。
- 權重或分數摘要。

## 觀察重點

- 同一段輸入中的每個 Token 都能扮演 Query。
- 每個 Token 會依照自己的 Query 關注不同 Key。
- 輸出表示會包含上下文資訊。

## 執行後應回答的問題

1. Self-Attention 與一般 Attention 的差異是什麼？
2. 為什麼每個 Token 需要看其他 Token？
3. 經過 Self-Attention 後，Token 表示如何改變？
