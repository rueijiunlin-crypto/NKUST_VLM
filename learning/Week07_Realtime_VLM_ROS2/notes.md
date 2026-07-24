# Week07 Notes：ROS2 + Camera + Realtime VLM

## Why 與 Problem

真實系統不是把相機圖片直接丟進模型就完成。Camera FPS、模型 inference FPS、網路傳輸、queue 與 consumer 都可能不同速；若 callback 被大型模型阻塞，ROS2 會累積過期 frame。目標是建立可觀察、可丟棄 stale data、可回報 unknown 的 camera→VLM→semantic topic pipeline。

## Input、Output 與 Message Contract

- Input：`sensor_msgs/Image`、camera info、source timestamp。
- Model input：RGB tensor `[B,C,H,W]` 與 prompt tokens `[B,L]`。
- Output：結構化 JSON 或自訂 message，至少含 `observation_id`、時間戳、objects、relations、unknown、model revision、valid。

Semantic Topic（語意主題）只表達感知結果；不得發布 joint velocity、pose command 或其他控制命令。

## Mechanism 與 Data Flow

```text
camera publisher
→ ROS2 image topic
→ lightweight callback
→ latest-frame buffer (capacity=1)
→ worker preprocess
→ VLM inference
→ schema / freshness validator
→ semantic result topic
→ planner or logger
```

Callback 只複製必要 metadata 並更新 latest frame。Worker 忙碌時以新 frame 取代舊 frame，可控制延遲而非追求處理每一張。`age = publish_time - source_time` 超過門檻時，輸出 `valid=false`。

## QoS、Rate 與 Latency

Camera 通常使用 sensor-data QoS、best effort 與小 queue；需要可靠傳輸的低頻結果 topic 可選 reliable。選擇必須由網路、資料率與失敗容忍度決定。端到端延遲為：

`L_total = L_capture + L_transport + L_queue + L_preprocess + L_model + L_validate + L_publish`

除平均值外要保存 p50、p95、p99、drop rate 與 stale rate。模型吞吐量高不代表單筆延遲足夠低。

## Prompt 與 Validator

Prompt Contract（提示契約）限定允許欄位、座標語意與 unknown policy。Validator 檢查 JSON syntax、schema、有限數值、時間新鮮度與必要 grounding。Retry 必須有限次，且不能讓舊 frame 重新進入控制時序。

## Example 與 Shape

相機送出 `[480,640,3] uint8`，經 bridge 轉 RGB、resize 與 batch 後為 `[1,3,336,336] float16`。模型文字結果經 JSON parser 變成固定 schema；這個 schema shape 穩定，但 object list 長度可變，consumer 必須處理空集合。

## Failure、Limitation 與 Robot Boundary

- Callback 內推論造成 executor starvation。
- 無上限 queue 導致結果雖正確但已過期。
- QoS 不相容導致 topic 看得到名稱卻收不到資料。
- Camera encoding BGR/RGB 顛倒。
- 模型回傳自然語言而非合法 schema。
- GPU OOM 或首次 warm-up 造成 latency spike。

Safety Gate、planner、controller 與 E-stop 必須位於 VLM 之外。Real ROS2 Track 應先用 recorded bag 或靜態影像 dry-run，再接真實相機。

## Demo 與 Paper Mapping

- Demo：觀察 bounded queue 與 freshness。
- Implementation Practice：完成 ROS2 node、parameters 與 structured publisher。
- Core Paper：RT-1，對應即時 perception-to-action 系統的 token、rate 與邊界；本週只實作 perception-to-semantic topic。

## 本週尚未涵蓋

不做 robot action generation；座標 grounding 於 Week08，VLA policy 於 Week10–13。
