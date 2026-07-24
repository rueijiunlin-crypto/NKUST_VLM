# Research Paper Reading Framework

本文件由舊 Week06 Paper Reading 教材遷移而來，作為所有主題共用的 Research Paper Reading Framework（研究論文閱讀框架）。原始教材、Demo、Practice 與學生紀錄完整保存在對應 Week 的 `legacy_v1/`。

## 三階段閱讀

1. **Orientation（方向定位）**：確認研究問題、輸入輸出、核心圖表、主要貢獻與限制。
2. **Evidence（證據閱讀）**：把作者的 claim（主張）對應到 experiment、table、figure、metric 與 baseline。
3. **Reproduction（重現評估）**：確認資料、split、模型版本、訓練／推論設定、硬體與缺失資訊。

## Claim-to-Evidence

| Claim | Evidence | Dataset / Split | Metric Context | Boundary |
| --- | --- | --- | --- | --- |
| 作者聲稱改善什麼？ | 哪個表格或實驗支持？ | 在什麼資料與切分？ | 指標方向、尺度與基準？ | 證據不能支持什麼？ |

沒有證據對應的句子只能視為動機、推論或待驗證假設。單一 benchmark 改善也不能自動外推到真實機器人、安全性或其他 domain。

## Metric Context

記錄 metric（評估指標）時必須同時保存：

- 指標定義與越高／越低越好。
- dataset、split、sample count 與 filtering。
- baseline 是否使用相同資料、模型規模與計算量。
- 平均值、變異、重複次數與統計不確定性。
- latency、throughput、memory 與硬體條件。

## Comparison Matrix

| Paper | Problem | Input | Architecture | Output | Training Data | Metric | Cost | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

比較必須在相同條件下進行；若設定不同，表格應明確標記 `not directly comparable`。

## Paper Reading Record

- Citation：
- Research question：
- Baseline：
- Proposed method：
- Dataset / split：
- Main metric：
- Strongest evidence：
- Failure cases：
- Reproducibility gaps：
- 對 Robot VLM / VLA 研究的可用啟示：

## 跨週使用原則

每週可推薦一篇核心原始論文，不要求大量下載。建議沿著 Transformer、CLIP、LLaVA、VLM Architecture、Video／Streaming VLM、Spatial Grounding、VLA、Robot Dataset、Simulation 與 Sim-to-Real 主題逐步累積比較矩陣。
