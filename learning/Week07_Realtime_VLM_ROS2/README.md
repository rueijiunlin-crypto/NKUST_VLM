# Week07 ROS2 + Camera + Realtime VLM

## 本週定位

建立 Camera → ROS2 Image Stream → Sampling／Trigger → VLM Inference → Structured Semantic Result → ROS2 Semantic Topic 的即時感知管線。舊 Prompt Engineering 教材完整保存在 `legacy_v1/`，其中 schema、validator、Unknown／Retry Policy 重新整合為本週資料契約。

## 導覽與使用

依序閱讀 `weekly_plan.md`、`notes.md`，執行 `demo/`，再完成 Guided + Implementation 混合 Practice。CPU Demo 使用模擬 timestamp 與 queue，不要求 ROS2 安裝。

## 研究關聯

真正的 realtime VLM 需要區分 Camera FPS、perception rate、result freshness 與安全邊界；structured semantic topic 不是 Motor Command。
