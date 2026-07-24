# Week16 Coding Observation Key

> 請先執行 `guided_demos/guided_evidence_chain.py`，並用自己的研究題目重寫一次 evidence chain，再查看本說明。

## 觀察方向

- research question 必須能對應到比較條件與可量測 metric。
- baseline、proposed method 與 controlled variables 共同決定結論是否可歸因。
- task success 之外仍需報告 latency、failure case 與 safety-related metric。
- 原始輸出、聚合結果與主張之間應可追溯，不能只留下漂亮圖表。

## 常見誤解

- 只描述系統功能，卻沒有可否證的研究問題。
- 只挑成功案例，沒有固定 cases 或 failure taxonomy。
- baseline 使用不同硬體或資料，導致比較失去公平性。
