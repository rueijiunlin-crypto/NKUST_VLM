# Week06 Notes：Video and Streaming VLM

## 1. 從單張到時間上下文

單張影像描述一個時間點；多影格提供順序，Video VLM 進一步建模動作、狀態改變與事件。Streaming VLM 還必須持續接收新資料、限制記憶並及時輸出。

## 2. Frame Sampling

Camera FPS 是感測器產生影格的速率；inference FPS 是模型完成推論的速率。若相機 30 FPS、模型 2 FPS，逐幀排隊會累積 stale frame（過期影格）。可用固定間隔、事件觸發、最新影格優先或 adaptive sampling（自適應取樣）。

## 3. Visual Token Growth

若每個 frame 產生 `V` 個 visual tokens，`F` 個影格的原始量約為 `F × V`。更多 token 增加 memory、attention cost 與 latency；壓縮雖省成本，可能遺失短暫事件與小物件。

## 4. Temporal Context 與 Memory

- Sliding Window：只保留最近 `W` 個影格，成本有界但會遺忘較早事件。
- Temporal Memory：保存摘要或狀態，不等於保存所有原始 token。
- Long-video Context：事件跨越視窗時可能失去因果關係。
- KV Cache：重用已處理 token 的 key／value 表示，可減少重算，但仍占記憶體且需淘汰策略。

## 5. Online vs Offline

Offline Video Understanding 可讀完整影片，重視整體正確性；online／streaming 必須在未看到未來影格時輸出，重視 latency、throughput、freshness 與可更新性。

## 6. Robot System Boundary

時間語意結果仍不是 Motor Command。模型輸出需要 timestamp、confidence／unknown、來源影格與 validator，後續 Planner、Policy、Control、Safety 各自負責其邊界。

## 本週尚未涵蓋

不實作大型 Video VLM 訓練、真實 Camera 或 ROS2；即時管線於 Week07 處理。
