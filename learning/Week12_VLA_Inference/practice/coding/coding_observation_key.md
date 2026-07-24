# Week12 Coding Observation Key

> 請先執行 `guided_demos/guided_policy_adapter.py` 並完成自己的 shape 與風險紀錄，再查看本說明。

## 觀察方向

- processor 將原始影像、語言與 robot state 轉成 checkpoint 預期的 observation schema。
- normalization statistics 必須與訓練 checkpoint 相符，不能任意從單次輸入重新估計。
- policy output 可能是單一步驟或 action chunk；shape 與 action dimension 必須由 model／dataset contract 決定。
- unnormalization 後仍須通過 range、freshness 與 safety validation。
- mock policy 只能驗證介面與資料流，不能當成 SmolVLA／OpenVLA 的能力或 latency 證據。

## 常見誤解

- 模型成功載入不代表 observation schema 正確。
- action 數值落在範圍內不代表適合目前 robot embodiment。
- 只記錄平均 latency 會掩蓋 warm-up 與 tail latency。
