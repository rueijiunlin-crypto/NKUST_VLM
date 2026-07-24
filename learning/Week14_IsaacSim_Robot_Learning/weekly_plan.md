# Week14 Weekly Plan：Isaac Sim Robot Learning

## 本週目標

- 建立 Isaac Sim robot learning experiment 的系統組成與責任邊界。
- 設計可控制變因、可重現的 simulation evaluation。

## 必學概念

USD、Robot Asset、RGB／Depth Camera、Semantic Label、Ground Truth、Robot State、Task Setup、Synthetic Data、Domain Randomization、Controlled Experiment。

## 建議學習順序

1. 閱讀 `notes.md` 並畫出 simulation-to-evaluation flow。
2. 執行 experiment config 與 domain randomization Demo。
3. 完成 experiment validator Implementation Practice。
4. 記錄 simulator ground truth 與 policy observation 的差異。

## Demo 執行順序

```powershell
python demo/demo_01_sim_experiment_config.py
python demo/demo_02_domain_randomization.py
python practice/coding/solutions/experiment_validator_solution.py
```

模式：Implementation Practice。

## Practice

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行兩個 Basic Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `experiment_validator_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 controlled variables、seed 與 ground truth。

## 驗收條件

- [ ] 能畫出 simulation-to-evaluation flow。
- [ ] 能區分 sensor observation 與 simulator ground truth。
- [ ] 能設計 controlled variable 與 domain randomization range。
- [ ] 能說明 simulation action 仍需 Policy／Controller／Safety 邊界。

## 銜接 Week15

Week15 將比較模擬設定與真實部署差距。
