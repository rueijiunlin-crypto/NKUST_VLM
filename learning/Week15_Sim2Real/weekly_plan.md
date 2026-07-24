# Week15 Weekly Plan：Sim-to-Real / Real Robot Deployment

## 本週目標

- 系統化辨識 simulation-to-real 的 perception、timing 與 action gap。
- 建立 deployment gate 與 hardware-ready 驗證證據。

## 必學概念

Lighting、texture、camera noise、calibration error、sensor／inference latency、action error、safety、failure recovery、deployment checklist。

## 建議學習順序

1. 閱讀 `notes.md` 並建立 sim／real comparison matrix。
2. 執行 domain gap 與 latency budget Demo。
3. 執行 Required Sim Observation vs Real Observation comparison；缺 real source 時記錄 Hardware blocker 與採集計畫。
4. 完成 deployment gate Implementation Practice。
5. 設計無實體機器人時仍可驗證的 hardware-ready evidence。

## Demo 執行順序

```powershell
python demo/demo_01_domain_gap.py
python demo/demo_02_latency_budget.py
python demo/demo_03_camera_sim_comparison.py --real <real-image> --sim <sim-image>
python practice/coding/solutions/deployment_gate_solution.py
```

## Required Sim / Real Observation Track

本軌是 Required Learning Track。比較 `Sim Observation vs Real Observation`，真實來源可為 webcam、RealSense 或事先錄製影像，不要求直接控制 robot。需固定 preprocessing，保存 source/calibration/revision、shape、latency、domain-gap metric 與 failure。

模式：Implementation Practice。

## Practice

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行兩個 Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `deployment_gate_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 domain gap、latency 與 recovery case。

## Paper Reading（論文閱讀）

### Core Reading

- Title: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World
- Authors: Josh Tobin et al.
- Year / Venue: 2017 / IROS
- DOI: 10.1109/IROS.2017.8202133
- arXiv: 1703.06907
- Link: https://arxiv.org/abs/1703.06907
- Code / Project: N/A
- Required Reading：Abstract、randomization method、sim-to-real hypothesis、experiments、limitations。
- Skim Reading：網路訓練細節。
- Skip for Now：舊版模擬環境重建。
- Optional Reading：SimOpt；Dynamics Randomization。

### Reading Questions

1. Reality gap（現實落差）如何被定義？
2. 模擬與真實影像的輸入輸出差異是什麼？
3. 哪些視覺參數被 randomize？
4. Resolution、color、noise tensor 如何比較？
5. 為何增加模擬變異可能改善真實表現？
6. 哪些變異會破壞任務語意？
7. Calibration 與 adaptation 如何分工？
8. 論文使用哪些真實評估與指標？
9. 哪項結果支持 domain randomization？
10. 實驗規模與泛化限制是什麼？
11. Camera vs simulation comparison 要保存哪些 evidence？
12. 哪個 gap 最可能成為論文變因？

### Deep Reading

以 real/sim paired evidence、randomization assumption、evaluation leakage 與 failure analysis 為深讀重點。

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Architecture、Experiment 與 domain randomization。
- [ ] 能指出至少一項 Claim、Evidence 與 Ablation。
- [ ] 能說明 Limitation、Boundary 與 Reproducibility 條件。
- [ ] 能把論文假設對應到 Sim／Real comparison。

## 驗收條件

- [ ] 能建立 sim／real comparison matrix。
- [ ] 能計算 end-to-end latency budget。
- [ ] 能設計 calibration、freshness、action-limit 與 emergency-stop checks。
- [ ] 能提出無實體機器人時的 hardware-ready 證據。

## 銜接 Week16

Week16 將部署差異轉成研究問題、baseline、metric 與 failure analysis。
