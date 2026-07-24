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
2. 執行兩個 Basic Demo。
3. 執行 Required Real Video VLM 的 FPS／frames temporal experiment；受阻時記錄 blocker。
4. 執行 Guided Demo 並完成 Practice。
5. 使用共用 Paper Reading Framework 閱讀一篇 Video／Streaming VLM 論文。

## Demo 執行順序

```powershell
python demo/demo_01_frame_sampling.py
python demo/demo_02_stream_budget.py --camera-fps 30 --inference-fps 2
python demo/demo_03_real_video_vlm.py --revision <commit> --video <video.mp4> --fps 1
python demo/demo_03_real_video_vlm.py --revision <commit> --video <video.mp4> --fps 2
python demo/demo_03_real_video_vlm.py --revision <commit> --video <video.mp4> --frames 8
python practice/coding/guided_demos/guided_sliding_window.py
```

## Required Real Video VLM Track

本軌是 Required Learning Track。依序比較 1、2、4 FPS，或 2、4、8、16 frames；至少回答 `What happened first?` 與 `What happened after the object was picked up?`。需記錄 model/revision、video duration、sampling FPS、sampled frames、resolution、input shape、peak VRAM、latency、generated tokens 與 answer。無法執行時須記錄 blocker。

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

## Paper Reading（論文閱讀）

### Core Reading

- Title: MovieChat: From Dense Token to Sparse Memory for Long Video Understanding
- Authors: Enxin Song et al.
- Year / Venue: 2024 / CVPR
- DOI: N/A
- arXiv: 2307.16449
- Link: https://openaccess.thecvf.com/content/CVPR2024/html/Song_MovieChat_From_Dense_Token_to_Sparse_Memory_for_Long_Video_Understanding_CVPR_2024_paper.html
- Code / Project: https://github.com/rese1f/MovieChat
- Required Reading：Abstract、architecture figure、short/long-term memory、experiments、limitations。
- Skim Reading：完整資料集統計與附錄案例。
- Skip for Now：大規模訓練重現。
- Optional Reading：Video-LLaVA；StreamingLLM。

### Reading Questions

1. 長影片理解的主要瓶頸是什麼？
2. Frame、clip、memory 的輸入輸出為何？
3. Dense tokens 如何轉為 sparse memory？
4. 時間與 token 維度如何變化？
5. Short-term 與 long-term memory 如何互動？
6. Sampling rate 對語意保留有何影響？
7. Streaming 情境如何控制延遲與記憶？
8. 使用哪些影片基準與指標？
9. 哪個 ablation 支持記憶設計？
10. 遺漏事件與時間混淆如何發生？
11. 這些失敗如何影響機器人即時決策？
12. 真實影片 VLM 軌應記錄哪些效能證據？

### Deep Reading

以 Architecture、Data Flow、Memory Compression 與 Evaluation 為本週深讀重點，完成共用 Paper Reading Record。

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Architecture、Experiment 與主要資料流。
- [ ] 能指出至少一項 Claim、Evidence 與 Ablation。
- [ ] 能說明 Limitation、Boundary 與 Reproducibility 條件。
- [ ] 能說明本論文與 Video VLM 研究的關聯。

## 驗收條件

- [ ] 能畫出 Camera → Sampling → Temporal Context → VLM。
- [ ] 能估算不同 frames 的 visual token 數量。
- [ ] 能解釋 online 與 offline 的 latency 取捨。
- [ ] 能說明為何相機 30 FPS 不代表模型可 30 FPS 推論。
- [ ] 實際結果由學生記錄於 `study_log.md`。

## 銜接 Week07

Week07 將把取樣與非同步推論放入 ROS2 Camera realtime pipeline。
