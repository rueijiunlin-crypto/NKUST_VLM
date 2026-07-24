# Week06 Video and Streaming VLM

## 本週定位

從 single-image VLM（單張影像視覺語言模型）進入 Multi-frame VLM（多影格視覺語言模型）、Video VLM（影片視覺語言模型）與 Streaming VLM（串流視覺語言模型），理解時間感知、token 成本與即時限制。

## 文件導覽

- `weekly_plan.md`：任務、順序與驗收。
- `notes.md`：Temporal Context、Frame Sampling、KV Cache 與 latency／throughput。
- `demo/`：影格取樣與 token／推論率示範。
- `practice/`：Guided Code Reading Mode。
- `legacy_v1/`：重構前 Paper Reading 教材與學生資料。
- [共用論文閱讀框架](../../docs/papers/paper_reading_framework.md)

## 核心資料流

```text
Camera / Video → Frames → Frame Sampling → Vision Encoder
→ Temporal / Multiframe Context → VLM → Semantic Result
```

CPU Basic Demo 使用合成時間戳與 token 計算；Qwen2.5-VL 真實影片推論是本週 Required Real Model Track（必要真實模型學習路線）。若受硬體、網路或環境阻塞，仍須完成安裝規劃、指令、問題設計與 blocker 證據。

## 與前週的銜接與本週目標

Week05 建立 Image → Encoder → Projector → LLM；本週把單張影像擴展成依時間取樣的影格序列。完成後應能解釋 FPS（每秒影格數）、固定影格數、影片 token 成本、首幀延遲、吞吐量與 freshness（新鮮度）的差異。

## 建議學習與 Demo 層級

1. 先讀 `notes.md`，執行 `demo_01_frame_sampling.py` 與 `demo_02_streaming_budget.py`（Basic／What）。
2. 讀 `practice/coding/guided_demos/`（Guided／How），追蹤取樣與佇列資料流。
3. 執行 `demo_03_real_video_vlm.py`，分別比較 `--fps 1|2|4` 或 `--frames 2|4|8|16`。
4. 以 temporal question（時間問題）檢查事件先後、狀態變化與動作持續性，不以單幀猜測冒充影片理解。

## Practice、Paper 與驗收

`practice/README.md` 是練習入口；論文閱讀依[共用框架](../../docs/papers/paper_reading_framework.md)記錄 Problem、Method、Experiment、Limitation 與本週資料流的對應。驗收以 `weekly_plan.md` 為準，Required Real Track 可記錄 Executed 或明確 blocker，不得只寫「程式可編譯」。

## 硬體、環境、下載與快取

Basic Track 可在 CPU 執行。Real Track 需要 PyTorch、Transformers、Qwen VL utilities、影片解碼器與模型／影片資料；建議 CUDA GPU。權重使用 Hugging Face cache，不提交 Git；執行前閱讀 `demo/real_track_README.md` 的版本、授權、下載與 VRAM 說明。

## Troubleshooting 與能力邊界

OOM 時先降低解析度、影格數或輸出 token；影片無法解碼時記錄 codec、OpenCV／decord 版本與原始 FPS。Video VLM 產生的是語意描述，不保證幾何定位、控制頻率或安全動作。這些 runtime evidence 將銜接 Week07 的 ROS2 即時管線，並可成為論文的 sampling ablation（取樣消融實驗）。
