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

本週不要求大型 Video VLM；CPU Demo 使用合成時間戳與 token 計算。
