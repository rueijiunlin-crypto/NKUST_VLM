# Week09 Coding Observation Key

> 請先執行 `guided_demos/guided_observation_alignment.py` 並寫下各訊號的 age 與 freshness 判斷，再查看本說明。

## 觀察方向

- robot observation（機器人觀測）不是一張影像，而是多來源、帶 timestamp 的結構化狀態。
- 不同訊號可有不同 freshness budget；高頻控制狀態通常比慢速語意資訊更嚴格。
- 「最近收到」不必然等於「最接近決策時間」，更不代表 frame 與 unit 正確。
- observation contract 應明確定義必填欄位、型別、shape、frame、unit、timestamp 與缺值策略。

## 常見誤解

- 只檢查欄位存在，卻不檢查資料是否過期。
- 把 command 當成已成功執行後的 state。
- 以陣列位置猜測關節意義，而沒有 joint name 對應。
