# Research Paper Reading Framework

本文件由舊 Week06 Paper Reading 教材遷移而來，作為所有主題共用的 Research Paper Reading Framework（研究論文閱讀框架）。原始教材、Demo、Practice 與學生紀錄完整保存在對應 Week 的 `legacy_v1/`。

> 每週原則上至少指定一篇 Core Paper（核心必讀論文）。Paper Reading 是正式學習流程，不是只供延伸閱讀的附錄。

## Reading Levels

- **Core Reading**：本週必讀，目標是連結 Theory、Demo、Practice 與研究證據。
- **Deep Reading**：針對架構轉折、主要模型、方法細節或論文題目高度相關研究，追蹤公式、圖表、ablation（消融實驗）與重現條件。
- **Optional Reading**：補充替代方法、近期進展或背景知識，不列入必要完成條件。

## Paper Selection

來源優先使用 original paper、official technical report、正式 conference／journal、arXiv、official project page、official code 與 model card。每篇 Core Paper 必須保存 Title、Authors、Year、Venue、DOI、arXiv、Project Page、Code 與 Model Page；無資料時標示 `N/A`。

選擇文獻時同時判斷：

- 是否直接回答本週核心 research problem。
- 是否有可讀取的 method、experiment、metric 與 limitation。
- 是否為原始工作，而不是二手解說。
- 快速發展領域是否仍具有代表性，並搭配近期 Optional Reading。
- 經典基礎論文是否仍是理解後續架構的必要前提。

## Reading Depth

### Core Reading

至少閱讀 Abstract、Introduction、核心 Method／Architecture、最重要 Figure、主要 Experiment／Table 與 Limitation／Discussion。

### Deep Reading

除 Core 範圍外，需追蹤：

- 公式與變數如何映射到程式、tensor shape 或資料結構。
- 訓練資料、split、model revision 與 hardware。
- baseline 是否公平、metric 是否足以支持 claim。
- ablation 是否真正隔離方法貢獻。
- 目前 Repository 的 Demo 能重現哪一段，不能重現哪一段。

### Optional Reading

先讀 Abstract、Figure 1、Conclusion；只有與研究題目直接相關時才深入 Method 與 Experiment。

## 三階段閱讀

1. **Orientation（方向定位）**：確認研究問題、輸入輸出、核心圖表、主要貢獻與限制。
2. **Evidence（證據閱讀）**：把作者的 claim（主張）對應到 experiment、table、figure、metric 與 baseline。
3. **Reproduction（重現評估）**：確認資料、split、模型版本、訓練／推論設定、硬體與缺失資訊。

## Evidence Extraction

不要只抄摘要。每個重要 claim 都應建立：

```text
Claim
↓
Method
↓
Evidence
↓
Boundary
↓
Limitation
```

| Claim | Method | Evidence | Dataset / Split | Metric Context | Boundary / Limitation |
| --- | --- | --- | --- | --- | --- |
| 作者聲稱改善什麼？ | 哪個機制帶來改善？ | 哪個表格或實驗支持？ | 在什麼資料與切分？ | 指標方向、尺度與基準？ | 證據不能支持什麼？ |

沒有證據對應的句子只能視為動機、推論或待驗證假設。單一 benchmark 改善也不能自動外推到真實機器人、安全性或其他 domain。

## Metric Context

記錄 metric（評估指標）時必須同時保存：

- 指標定義與越高／越低越好。
- dataset、split、sample count 與 filtering。
- baseline 是否使用相同資料、模型規模與計算量。
- 平均值、變異、重複次數與統計不確定性。
- latency、throughput、memory 與硬體條件。

## Reproducibility Check

- Paper／code／model／dataset 是否提供官方 revision 或 commit。
- 環境、套件、CUDA、dtype、quantization 與 seed 是否可確認。
- 資料授權、下載方式、preprocessing 與 normalization 是否完整。
- checkpoint 與 processor 是否成對。
- 訓練步數、batch size、learning rate、evaluation protocol 是否足以重建。
- 未公開的資料、硬體或人工選擇是否限制重現。

無法確認的項目寫 `Not reported`，不得自行補值。

## Comparison Matrix

| Paper | Problem | Input | Architecture | Output | Training Data | Metric | Cost | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

比較必須在相同條件下進行；若設定不同，表格應明確標記 `not directly comparable`。

## Paper Reading Record

- Citation：
- Reading Level：
- Research question：
- Baseline：
- Proposed method：
- Input / Output：
- Dataset / split：
- Main metric：
- Strongest evidence：
- Failure cases：
- Limitation：
- Reproducibility gaps：
- 對 Robot VLM / VLA 研究的可用啟示：

## Thesis Literature Review Usage

每讀完一篇 Core／Deep Paper，將結果整理成可供 thesis literature review（論文文獻回顧）使用的單位：

1. 以 research problem 分群，不以模型名稱流水帳排列。
2. 說明方法如何處理前一類方法的限制。
3. 使用 Comparison Matrix 對齊 input、output、data、metric、cost 與 boundary。
4. 區分作者 claim、paper evidence 與自己的 inference。
5. 記錄 My Method 與 Paper Method 可直接比較及不可直接比較之處。
6. 將 reproducibility gap 與 limitation 轉為可能的研究問題或實驗控制變因。

## 跨週使用原則

各週累積的 Paper Reading Record 應沿著 Foundation、VLM、Video／Streaming、Spatial Grounding、VLA、Robot Dataset、Simulation、Sim-to-Real 與 Research Evaluation 形成一條可追蹤的文獻鏈。Optional Reading 可以更新，但 Core Paper 的更換必須說明原因與來源。
