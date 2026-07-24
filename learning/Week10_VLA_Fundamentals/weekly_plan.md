# Week10 Weekly Plan：Embodied AI + VLA Fundamentals

## 本週目標

- 區分 VLM 的語意輸出與 VLA 的動作輸出。
- 建立 Observation → Policy → Action → Robot → Observation 閉迴路。

## 必學概念

Embodied AI、Policy、Observation、Action Space／Representation、Joint／Cartesian／End-Effector／Gripper Action、Action Chunk、open-loop、closed-loop、Imitation Learning、Foundation Policy 與 Safety Boundary。

## 建議學習順序

1. 閱讀 `notes.md` 並比較 VLM 與 VLA。
2. 執行快速 Demo，觀察 action representation 與 action chunk。
3. 執行 Guided policy loop。
4. 完成小型 action validator Implementation Practice。

## Demo 執行順序

```powershell
python demo/demo_01_vlm_vs_vla.py
python demo/demo_02_action_chunk.py
python practice/coding/guided_demos/guided_policy_loop.py
python practice/coding/solutions/action_validator_solution.py
```

## 任務清單

- [ ] 閱讀本週文件並畫出 VLA closed-loop。
- [ ] 執行兩個 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `action_validator_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 safety boundary 與 failure case。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

模式：Guided 為主、少量 Implementation。

## 驗收條件

- [ ] 能區分 VLM output 與 VLA action。
- [ ] 能比較 joint／Cartesian action。
- [ ] 能解釋 action chunk、open／closed-loop。
- [ ] 能畫出 Observation → Policy → Action → Robot → Observation。
- [ ] 能說明 Safety Gate 不能只靠生成模型。

## 銜接 Week11

Week11 將說明 imitation policy 所需的 demonstrations 與 dataset schema。
