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

## Paper Reading（論文閱讀）

### Core Reading

- Title: PaLM-E: An Embodied Multimodal Language Model
- Authors: Danny Driess et al.
- Year / Venue: 2023 / ICML
- DOI: N/A
- arXiv: 2303.03378
- Link: https://proceedings.mlr.press/v202/driess23a.html
- Code / Project: https://palm-e.github.io/
- Required Reading：Abstract、architecture、multimodal sentences、robot experiments、limitations。
- Skim Reading：完整 scaling 與語言 benchmark。
- Skip for Now：不可取得模型的訓練重現。
- Optional Reading：Gato；RoboCat。

### Reading Questions

1. PaLM-E 如何定義 embodied multimodal input？
2. Image、state、text 的輸入輸出是什麼？
3. Sensor embeddings 如何插入 language sequence？
4. Batch、time、state 與 token shape 如何對齊？
5. Continuous state 如何映射到 embedding？
6. Timestamp 與同步誤差會造成什麼問題？
7. 不同 embodiment 如何共享模型？
8. 主要機器人任務與指標是什麼？
9. 哪項結果支持 positive transfer？
10. Closed model 與資料限制如何影響重現？
11. 本週 observation schema 如何保存 provenance？
12. 哪個 evidence 可支持多模態狀態融合設計？

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Core Method 與主要資料流。
- [ ] 能指出至少一項 Claim 與對應 Evidence。
- [ ] 能說明至少一項 Limitation／Boundary。
- [ ] 能說明本論文與本週及後續研究的關聯。

## 驗收條件

- [ ] 能畫出 Vision + Language + Robot State。
- [ ] 能辨識 missing、stale、misaligned observation。
- [ ] 能說明 image 不是完整機器人狀態。

## 銜接 Week10

Week10 將 observation 輸入 Policy 並定義 action space。
