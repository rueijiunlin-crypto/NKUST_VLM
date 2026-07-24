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

## Paper Reading（論文閱讀）

### Core Reading

- Title: SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics
- Authors: Mustafa Shukor et al.
- Year / Venue: 2025 / arXiv
- DOI: N/A
- arXiv: 2506.01844
- Link: https://arxiv.org/abs/2506.01844
- Code / Model: https://github.com/huggingface/lerobot / https://huggingface.co/lerobot/smolvla_base
- Required Reading：Abstract、architecture、flow matching、asynchronous inference、experiments。
- Skim Reading：完整訓練超參數與附錄。
- Skip for Now：多 GPU 大規模重現。
- Optional Reading：OpenVLA；Diffusion Policy。

### Reading Questions

1. SmolVLA 要解決什麼可負擔部署問題？
2. 多視角影像、state、language、action 的介面為何？
3. VLM backbone 與 action expert 如何互動？
4. Batch、camera、time、state、action shape 如何變化？
5. Flow matching 如何產生連續 action？
6. Action chunking 與 asynchronous inference 如何降延遲？
7. Processor 與 normalization metadata 為何不可省略？
8. 使用哪些真實機器人基準與指標？
9. 哪個 ablation 支持模型設計？
10. OOD、硬體與安全限制是什麼？
11. 真實 inference 必須記錄哪些版本與耗時？
12. 模型輸出為何不能未經 safety gate 直接控制硬體？

### Deep Reading

深讀 architecture、inference data flow、action representation、latency 與評估；真實模型軌若未執行，狀態必須標為 `Not validated yet`。

## 驗收條件

- [ ] 能建立 observation contract。
- [ ] 能說明 normalization 必須配合 checkpoint。
- [ ] 能解讀 action shape／chunk。
- [ ] 能記錄 device、dtype、latency 與 model revision。

## 銜接 Week13

Week13 將由 inference 進入小規模 task adaptation。
