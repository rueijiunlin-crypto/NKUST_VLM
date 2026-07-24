# Week15 Weekly Plan：Sim-to-Real / Real Robot Deployment

## 本週目標

- 系統化辨識 simulation-to-real 的 perception、timing 與 action gap。
- 建立 deployment gate 與 hardware-ready 驗證證據。

## 必學概念

Lighting、texture、camera noise、calibration error、sensor／inference latency、action error、safety、failure recovery、deployment checklist。

## 建議學習順序

1. 閱讀 `notes.md` 並建立 sim／real comparison matrix。
2. 執行 domain gap 與 latency budget Demo。
3. 完成 deployment gate Implementation Practice。
4. 設計無實體機器人時仍可驗證的 hardware-ready evidence。

## Demo 執行順序

```powershell
python demo/demo_01_domain_gap.py
python demo/demo_02_latency_budget.py
python practice/coding/solutions/deployment_gate_solution.py
```

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

## 驗收條件

- [ ] 能建立 sim／real comparison matrix。
- [ ] 能計算 end-to-end latency budget。
- [ ] 能設計 calibration、freshness、action-limit 與 emergency-stop checks。
- [ ] 能提出無實體機器人時的 hardware-ready 證據。

## 銜接 Week16

Week16 將部署差異轉成研究問題、baseline、metric 與 failure analysis。
