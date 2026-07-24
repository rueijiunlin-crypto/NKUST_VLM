# Week05 Weekly Plan：VLM Architecture for Robotics

## 本週目標

- 理解 VLM（視覺語言模型）共通元件與主要架構家族。
- 能區分 representation output（表示輸出）與 generative output（生成輸出）。
- 能說明 Vision Encoder（視覺編碼器）、Connector（連接器）與 Language Model（語言模型）的分工。
- 能追蹤 Camera-to-Structured-Perception 與 Robot VLM 系統資料流。
- 能比較 connector 的資訊保留、序列成本與研究取捨。
- 能區分語意、2D、3D、相機座標、機器人座標與 Robot State。
- 能解釋 single-frame、multi-frame 與 Streaming VLM（串流視覺語言模型）的 token／latency 取捨。

## 必學概念

- Dual Encoder、Projector-based、Query-based 與 Cross-Attention 架構。
- Vision features、text embeddings（文字嵌入向量）與 modality alignment（模態對齊）。
- Linear／MLP Projector、query tokens（查詢詞元）與 cross-attention。
- Early／late／interleaved fusion（早期／晚期／交錯融合）。
- Token budget、context length（上下文長度）、Frame Sampling（影格取樣）與 Latency。
- Robot VLM system boundary、Robot State、Spatial Grounding 與 Structured Output。
- VLM Answer、VLA action output、Planner 與 Controller 的責任差異。

## 建議學習順序

1. 閱讀 `README.md` 與 `notes.md` 第 1–2 節。
2. 執行 Demo 01，比較架構家族與輸出型態。
3. 執行 Demo 02，畫出 Camera-to-Structured-Perception 資料流。
4. 閱讀 `notes.md` 第 3–4 節，理解 connector 與融合策略。
5. 執行 Demo 03 與 Guided Demo 01–03。
6. 閱讀 `notes.md` 第 5–10 節，理解 Spatial Grounding、Robot State、時間輸入、結構化輸出與系統邊界。
7. 執行 Demo 04、Demo 05 與 Guided Demo 04。
8. 完成 Concept Practice、Coding Practice 與 `study_log.md`。

## Demo 執行順序

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_architecture_families.py
python demo/demo_02_camera_to_answer_flow.py
python demo/demo_03_connector_comparison.py
python demo/demo_04_token_budget.py
python demo/demo_04_token_budget.py --frames 4 --query-tokens 32
python demo/demo_05_robot_vlm_system_flow.py
```

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

本週採 Guided Code Reading Mode。完整程式用於追蹤 shape、融合中間值與失敗位置，不使用 TODO 補空題。

## 任務清單

- [ ] 閱讀本週入口、計畫與正式教材。
- [ ] 執行五個 Demo 並保存輸出。
- [ ] 畫出 Dual Encoder 與生成式 VLM 的差異圖。
- [ ] 執行四個 Guided Demo 並完成觀察欄位。
- [ ] 完成 Concept Practice。
- [ ] 比較 Projector 與 Query Connector 的取捨。
- [ ] 記錄一組不同圖片數量或 query tokens 的 token budget 結果。
- [ ] 記錄 frame count 對 token、relative cost 與 latency implication 的影響。
- [ ] 畫出 semantic → geometric → robot-system pipeline，標示缺少資訊。
- [ ] 在 `study_log.md` 記錄理解與未解問題。
- [ ] 更新 Notion 學習狀態並進行 ChatGPT 驗收。

## Paper Reading（論文閱讀）

### Core Reading

- Title: BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
- Authors: Junnan Li, Dongxu Li, Silvio Savarese, Steven Hoi
- Year / Venue: 2023 / ICML
- DOI: N/A
- arXiv: 2301.12597
- Link: https://proceedings.mlr.press/v202/li23q.html
- Code / Project: https://github.com/salesforce/LAVIS/tree/main/projects/blip2
- Required Reading：Abstract、Figure 1、Q-Former、兩階段預訓練、主要結果。
- Skim Reading：完整資料清理與超參數。
- Skip for Now：所有 benchmark 的逐表重現。
- Optional Reading：Flamingo；InstructBLIP。

### Reading Questions

1. BLIP-2 要解決什麼成本與對齊問題？
2. Frozen vision encoder、Q-Former、LLM 如何分工？
3. Query tokens 如何壓縮視覺資訊？
4. 各模組介面 shape 如何對齊？
5. 兩階段目標各自建立什麼能力？
6. 為何凍結大型模型仍能有效學習？
7. Architecture choice 如何影響 latency 與 token budget？
8. 主要基準與比較對象是什麼？
9. 哪個 ablation 最能支持 Q-Former？
10. 架構限制與資料偏差是什麼？
11. 哪些介面可映射到機器人 VLM 系統？
12. BLIP-2 應放在本路線哪個知識節點，為什麼？

## 驗收條件

- [ ] 能畫出 Camera → Preprocess → Vision Encoder → Connector → LLM → Validator → Structured Perception。
- [ ] 能區分 CLIP 類相似度輸出與 LLaVA 類生成輸出。
- [ ] 能解釋 Projector 與 Query Connector 的 token 數量差異。
- [ ] 能說明 cross-attention 的 Query、Key、Value 來自何處。
- [ ] 能估算圖片數量與解析度對 token budget 的影響。
- [ ] 能解釋 single-frame、multi-frame、Streaming VLM 與 Frame Sampling。
- [ ] 能列出 Robot Pose、Joint Position／Velocity、Gripper／Camera Pose 與 Navigation State。
- [ ] 能區分 semantic／2D／3D／camera coordinate／robot coordinate。
- [ ] 能畫出 Camera + Language + Robot State → VLM／Semantic System → Planner → Controller。
- [ ] 能說明 VLM Answer 與 VLA action output 的差異，以及 VLM 為何不能直接控制馬達。
- [ ] 能指出至少三個架構失敗點。
- [ ] `study_log.md` 已由學生填入實際觀察。

## 銜接 Week06 Video and Streaming VLM

Week06 將從 Single Image → Multi-frame → Video → Streaming 開始處理 Temporal Perception（時間感知），延伸本週的 multi-frame、token／latency 與系統邊界概念。論文閱讀方法則改由 Repository 共用的 Research Paper Reading Framework 支援。
