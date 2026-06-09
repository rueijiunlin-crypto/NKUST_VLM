# Position Encoding Demo（位置編碼示範程式）

## 對應概念

Position Encoding（位置編碼）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/position_encoding/demo_position_encoding.py
```

## 預期輸出

- 不同位置的 Position Encoding 向量。
- 相同維度在不同位置的數值變化。
- Token Embedding 加上位置資訊後的示意。

## 觀察重點

- Transformer（轉換器架構）本身不天然知道順序。
- 不同位置需要有不同的位置表示。
- 文字 Token 與影像 Patch（影像切塊）都需要位置資訊。

## 執行後應回答的問題

1. 為什麼 Transformer 需要 Position Encoding？
2. Position Encoding 如何補足順序資訊？
3. 影像 Patch 的位置資訊和文字 Token 的位置資訊有什麼相似之處？
