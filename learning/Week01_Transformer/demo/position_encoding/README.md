# Position Encoding Demo

## 對應概念

Position Encoding（位置編碼）。

## 執行指令

```powershell
python demo\position_encoding\demo_position_encoding.py
```

## 預期輸出

- 不同 position（位置）的 encoding（編碼）數值
- Token 與位置編碼的對應

## 觀察重點

- 不同位置會產生不同位置訊號。
- Transformer（轉換器架構）需要額外位置資訊。
- 順序改變會影響語意。

## 執行後應回答的問題

1. Transformer 為什麼不知道 Token 順序？
2. Position Encoding 解決了什麼問題？
3. 影像 Patch（影像切塊）為什麼也需要位置資訊？
