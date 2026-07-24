# Week07 ROS2 + Camera + Realtime VLM

## 本週定位

建立 Camera → ROS2 Image Stream → Sampling／Trigger → VLM Inference → Structured Semantic Result → ROS2 Semantic Topic 的即時感知管線。舊 Prompt Engineering 教材完整保存在 `legacy_v1/`，其中 schema、validator、Unknown／Retry Policy 重新整合為本週資料契約。

## 導覽與使用

依序閱讀 `weekly_plan.md`、`notes.md`，執行 `demo/`，再完成 Guided + Implementation 混合 Practice。CPU Demo 使用模擬 timestamp 與 queue，不要求 ROS2 安裝。

## 研究關聯

真正的 realtime VLM 需要區分 Camera FPS、perception rate、result freshness 與安全邊界；structured semantic topic 不是 Motor Command。

## 與前週的銜接、本週目標與資料流

Week06 處理影片取樣；本週把相同限制放入持續到達的 ROS2 Camera Stream（相機串流）：

```text
Image Topic → capacity-1 latest frame → worker → real VLM adapter
→ validated semantic JSON → semantic topic
```

完成後應能解釋 callback 與模型 worker 為何分離、為何只保留最新影格、如何計算 age／latency，以及 schema validation 為何不能由自由文字取代。

## Files / Demo Tracks / Practice Mode / Paper Reading

依序使用 `weekly_plan.md`、`notes.md`、`demo/demo_README.md`、`practice/README.md`。Demo 01–02 是可離線的 What；Demo 03 是 ROS2 + Qwen2.5-VL Required Real Track；Guided Reading 解釋 How，Implementation Practice 才要求學生補功能。論文驗收須連結 realtime perception、queue policy 或 semantic interface 的方法與實驗。

## Hardware Requirements / Environment / Download / Troubleshooting

Real Track 需要 Ubuntu、ROS2 Humble/Jazzy、camera topic 或 rosbag、`cv_bridge`，以及獨立 Python ML 依賴；兩套環境若 ABI 衝突，應分程序部署而非混裝。模型使用 Hugging Face cache。先驗證 image encoding、QoS、timestamp，再查模型載入、JSON parse、OOM 與 freshness rejection；完整命令見 `demo/real_track_README.md`。

## 邊界、論文與下週

本週只發布 semantic result，不接 motor controller；timeout、unknown 與 schema error 必須可見。這個 ROS2 observation contract 可成為論文的系統介面與 latency 評估基礎，Week08 再加入 pixel／depth／座標系的幾何 grounding（定位）。
