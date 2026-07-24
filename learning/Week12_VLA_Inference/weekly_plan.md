# Week12 Weekly Plan：SmolVLA / OpenVLA Inference

## 本週目標

- 理解 pretrained VLA、processor、observation input、normalization、policy inference 與 action output。
- 解讀 action chunk、hardware requirement 與 inference latency。
- 區分 Basic interface test 與真實權重推論。

## 必學概念

Pretrained VLA、Processor、Observation Input、Normalization、Policy Inference、Action Output／Chunk、Hardware Requirement、Inference Latency 與 Model Revision。

## 建議學習順序

1. 閱讀 `notes.md`，先理解 processor-to-action interface。
2. 執行 CPU Basic Demo 與 runtime planner。
3. 執行 Guided policy adapter 並追蹤 shape。
4. 依硬體與模型條件決定是否進行 optional real-model experiment。

## Demo 執行順序

```powershell
python demo/demo_01_basic_vla_inference.py --device cpu
python demo/demo_02_runtime_planner.py
python practice/coding/guided_demos/guided_policy_adapter.py
```

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行 Basic VLA Inference Demo 與 runtime planner。
- [ ] 執行 Guided Demo 並完成 Concept／Coding Practice 紀錄。
- [ ] 記錄 device、dtype、latency、model ID 與 revision。
- [ ] 未執行真實模型時，明確記錄 hardware／model requirement。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

模式：Guided + Real Model Demo planning。真實模型需獨立環境時不得阻塞 Basic 學習。

## 驗收條件

- [ ] 能建立 observation contract。
- [ ] 能說明 normalization 必須配合 checkpoint。
- [ ] 能解讀 action shape／chunk。
- [ ] 能記錄 device、dtype、latency 與 model revision。

## 銜接 Week13

Week13 將由 inference 進入小規模 task adaptation。
