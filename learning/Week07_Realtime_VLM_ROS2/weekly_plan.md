# Week07 Weekly Plan：ROS2 + Camera + Realtime VLM

## 本週目標

- 理解 ROS2 Image、Publisher／Subscriber、Topic 與 QoS 概念。
- 比較 Camera FPS、inference rate、queue 與 stale frame。
- 設計含 timestamp、observation ID、unknown 與 validator 狀態的 semantic result。

## 必學概念

Frame sampling、asynchronous inference（非同步推論）、latest-frame policy、QoS、structured semantic interface、Retry／Unknown Policy。

## 建議學習順序

1. 閱讀 `notes.md`，先建立 realtime pipeline 與 system boundary。
2. 執行快速 Demo，觀察 queue 與 semantic interface。
3. 執行 Guided Demo，再完成 freshness Implementation Practice。
4. 將實際觀察與問題記錄到 `study_log.md`。

## Demo 執行順序

```powershell
python demo/demo_01_realtime_queue.py
python demo/demo_02_semantic_interface.py
python practice/coding/guided_demos/guided_async_flow.py
python practice/coding/solutions/realtime_policy_solution.py
```

## 任務清單

- [ ] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [ ] 依序執行 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `realtime_policy_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 queue、latency 與 stale frame 觀察。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

本週採 Guided Code Reading + Implementation Practice。

## Paper Reading（論文閱讀）

### Core Reading

- Title: RT-1: Robotics Transformer for Real-World Control at Scale
- Authors: Anthony Brohan et al.
- Year / Venue: 2022 / arXiv
- DOI: N/A
- arXiv: 2212.06817
- Link: https://arxiv.org/abs/2212.06817
- Code / Project: https://robotics-transformer1.github.io/
- Required Reading：Abstract、architecture、tokenization、real-time execution、evaluation。
- Skim Reading：機器人資料收集細節。
- Skip for Now：完整訓練基礎設施重現。
- Optional Reading：ROS 2 executor 官方文件；RT-2。

### Reading Questions

1. RT-1 要解決什麼真實機器人規模問題？
2. Image、instruction、action 的輸入輸出為何？
3. TokenLearner 與 Transformer 的資料流為何？
4. 時間、影像與 action token shape 如何變化？
5. Action discretization 有什麼代價？
6. 即時迴圈的頻率與模型延遲如何協調？
7. 資料多樣性如何影響 generalization？
8. 使用哪些真實機器人評估？
9. 哪項結果支持多任務資料的價值？
10. 失敗、延遲與安全限制是什麼？
11. ROS2 camera→VLM→topic 可借用哪些邊界？
12. 哪些輸出只能是語意事件、不能直接當控制命令？

## 驗收條件

- [ ] 能解釋 QoS 與 freshness。
- [ ] 能處理 queue overflow 與 stale result。
- [ ] 能驗證 semantic schema。
- [ ] 能說明 ROS2 semantic topic 為何不是控制命令。

## 銜接 Week08

Week08 將把語意物件進一步定位到 2D、深度與座標系。
