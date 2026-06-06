# QKV Demo

## 對應概念

Query（查詢）、Key（鍵）、Value（值）。

## 執行指令

```powershell
python demo\qkv\demo_qkv.py
```

## 預期輸出

- Query token
- Q vector
- 每個 Token 的 Q x K 分數
- 分數最高的 Token

## 觀察重點

- Q 和 K 越相似，分數越高。
- Value 是後續被加權整合的內容。
- QKV 是 Attention（注意力機制）的準備步驟。

## 執行後應回答的問題

1. Query、Key、Value 各自的角色是什麼？
2. 為什麼不能只用 Embedding（嵌入向量）？
3. 圖書館類比中 Q、K、V 分別對應什麼？
