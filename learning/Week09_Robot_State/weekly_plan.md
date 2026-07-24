# Week09 Weekly Plan：Robot State + Multimodal Observation

## 本週目標

- 解釋 proprioception（本體感覺）與 observation space。
- 組合 joint position／velocity、end-effector、gripper、base／camera pose。
- 處理 multi-camera、timestamp synchronization、missing／stale state。

## 必學概念

Robot State、Observation Space、Proprioception、Multi-camera、Timestamp Synchronization、Missing／Stale State、Observation Contract。

## 建議學習順序

1. 閱讀 `notes.md` 並區分 image、state 與 command。
2. 執行 Robot State 與同步 Demo。
3. 執行 Guided Demo，計算各來源 age 與 freshness。
4. 完成 observation builder Implementation Practice。

## Demo 執行順序

```powershell
python demo/demo_01_robot_state.py
python demo/demo_02_observation_sync.py
python practice/coding/guided_demos/guided_observation_alignment.py
python practice/coding/solutions/observation_builder_solution.py
```

## 任務清單

- [ ] 閱讀本週文件並畫出 multimodal observation schema。
- [ ] 執行兩個 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `observation_builder_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 missing、stale 或 misaligned case。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

模式：Guided + Implementation。

## 驗收條件

- [ ] 能畫出 Vision + Language + Robot State。
- [ ] 能辨識 missing、stale、misaligned observation。
- [ ] 能說明 image 不是完整機器人狀態。

## 銜接 Week10

Week10 將 observation 輸入 Policy 並定義 action space。
