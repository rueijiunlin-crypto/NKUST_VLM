# QKV Demo（查詢鍵值示範程式）

## 對應概念

Query（查詢）、Key（鍵）、Value（值）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/qkv/demo_qkv.py
```

## 預期輸出

- Query token。
- Query 向量。
- 每個 Token 的 Q x K 分數。
- 分數最高的 Token。

## 觀察重點

- Query 表示目前要找的資訊。
- Key 用來被 Query 比對。
- Value 是最後被加權取用的內容。
- Q x K 分數越高，代表越值得被目前 Query 關注。

## 執行後應回答的問題

1. Q、K、V 分別扮演什麼角色？
2. 為什麼 Attention（注意力機制）要先計算 Q x K？
3. 分數最高的 Key 是否符合你的直覺？為什麼？
