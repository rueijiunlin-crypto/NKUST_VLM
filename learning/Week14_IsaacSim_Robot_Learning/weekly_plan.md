# Week14 Weekly Plan：Isaac Sim Robot Learning

## 本週目標

- 建立 Isaac Sim robot learning experiment 的系統組成與責任邊界。
- 設計可控制變因、可重現的 simulation evaluation。

## 必學概念

USD、Robot Asset、RGB／Depth Camera、Semantic Label、Ground Truth、Robot State、Task Setup、Synthetic Data、Domain Randomization、Controlled Experiment。

## 建議學習順序

1. 閱讀 `notes.md` 並畫出 simulation-to-evaluation flow。
2. 執行 experiment config 與 domain randomization Demo。
3. 以 Isaac Sim launcher 執行 Required Real default scene，或留下 Environment blocker。
4. 完成 experiment validator Implementation Practice。
5. 記錄 simulator ground truth 與 policy observation 的差異。

## Demo 執行順序

```powershell
python demo/demo_01_sim_experiment_config.py
python demo/demo_02_domain_randomization.py
<isaac-sim-root>\python.bat demo\demo_03_real_isaac_observation.py --headless
python practice/coding/solutions/experiment_validator_solution.py
```

## Required Real Isaac Sim Track

本軌是 Required Learning Track。未提供 `--stage` 時必須建立 Ground Plane、Franka、RGB Camera、Target Object 與 Lighting；提供 `--stage` 時檢查指定 prim。需記錄 RGB/depth shape、camera pose、joint shape、simulation timestep、render rate，以及 Sensor Observation 與 Simulator Ground Truth 的差異。無 Isaac Sim 時記錄 `Environment blocked`。

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

## Paper Reading（論文閱讀）

### Core Reading

- Title: Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning
- Authors: Mayank Mittal et al.
- Year / Venue: 2025 / arXiv
- DOI: N/A
- arXiv: 2511.04831
- Link: https://arxiv.org/abs/2511.04831
- Code / Project: https://github.com/isaac-sim/IsaacLab / https://isaac-sim.github.io/IsaacLab/
- Required Reading：Abstract、framework architecture、sensor／environment interface、benchmarks、limitations。
- Skim Reading：所有 benchmark 超參數。
- Skip for Now：大型 GPU 叢集重現。
- Optional Reading：Isaac Sim official tutorials；Replicator documentation。

### Reading Questions

1. Isaac Lab 要解決什麼模擬研究工程問題？
2. Scene、robot、sensor、action 的介面為何？
3. OpenUSD、physics、rendering 的資料流為何？
4. Environment、camera、state tensor shape 如何批次化？
5. Simulation timestep 與 control timestep 如何區分？
6. Randomization 在 pipeline 哪裡套用？
7. ROS2 bridge 與原生 tensor path 有何差異？
8. 使用哪些 benchmark 與效能指標？
9. 哪項證據支持 GPU parallelism？
10. 版本、資產與感測器 fidelity 限制是什麼？
11. 本週真實 Isaac 軌需記錄哪些環境資訊？
12. 哪些模擬輸出可供 VLM/VLA，哪些不能等同真實資料？

### Deep Reading

深讀 simulation boundary、sensor fidelity、timing 與 reproducibility，並把官方 API 對應到本週 observation pipeline。

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Architecture、Experiment 與 simulation flow。
- [ ] 能指出至少一項 Claim、Evidence 與 Ablation。
- [ ] 能說明 Limitation、Boundary 與 Reproducibility 條件。
- [ ] 能區分 Sensor Observation 與 Simulator Ground Truth。

## 驗收條件

- [ ] 能畫出 simulation-to-evaluation flow。
- [ ] 能區分 sensor observation 與 simulator ground truth。
- [ ] 能設計 controlled variable 與 domain randomization range。
- [ ] 能說明 simulation action 仍需 Policy／Controller／Safety 邊界。

## 銜接 Week15

Week15 將比較模擬設定與真實部署差距。
