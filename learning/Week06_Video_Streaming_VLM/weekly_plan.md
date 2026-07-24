# Week06 Weekly Plan：Video and Streaming VLM

## 本週目標

- 區分 single-image、multi-frame、video 與 streaming inference。
- 解釋 Temporal Context（時間上下文）、Temporal Memory（時間記憶）與 Sliding Window（滑動視窗）。
- 估算 Visual Token Growth（視覺詞元成長）、latency 與 throughput。
- 說明 `Camera FPS ≠ VLM Inference FPS`。

## 必學概念

Frame Sampling、online／offline understanding、KV Cache 概念、長影片 context 問題、stale result。

## 建議學習順序

1. 閱讀 `notes.md`。
2. 執行兩個 Demo。
3. 執行 Guided Demo 並完成 Practice。
4. 使用共用 Paper Reading Framework 閱讀一篇 Video／Streaming VLM 論文。

## Demo 執行順序

```powershell
python demo/demo_01_frame_sampling.py
python demo/demo_02_stream_budget.py --camera-fps 30 --inference-fps 2
python practice/coding/guided_demos/guided_sliding_window.py
```

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Observation Key](./practice/coding/coding_observation_key.md)

本週採 Guided Code Reading Mode。

## 任務清單

- [ ] 閱讀 `README.md` 與 `notes.md`。
- [ ] 依序執行 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice 與 Coding Practice 的個人觀察欄位。
- [ ] 使用共用 Paper Reading Framework 閱讀一篇相關論文。
- [ ] 在 `study_log.md` 記錄實際輸出、理解與疑問。

## 驗收條件

- [ ] 能畫出 Camera → Sampling → Temporal Context → VLM。
- [ ] 能估算不同 frames 的 visual token 數量。
- [ ] 能解釋 online 與 offline 的 latency 取捨。
- [ ] 能說明為何相機 30 FPS 不代表模型可 30 FPS 推論。
- [ ] 實際結果由學生記錄於 `study_log.md`。

## 銜接 Week07

Week07 將把取樣與非同步推論放入 ROS2 Camera realtime pipeline。
