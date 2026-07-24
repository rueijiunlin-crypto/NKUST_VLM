# Week05 VLM Architecture for Robotics

## 本週定位

Week05 延續 Week04 LLaVA（大型語言與視覺助手）與 Grounded Visual Reasoning（具有視覺依據的多模態推理），把單一模型流程抽象成 VLM Architecture for Robotics（機器人視覺語言模型架構與資料流）。一般 VLM 架構基礎仍完整保留。

本週重點不是背模型名稱，而是能回答：

- 圖片與文字分別如何被編碼。
- Connector（連接器）如何處理 modality gap（模態差距）。
- Dual Encoder（雙編碼器）、Projector-based（投影器式）、Query-based（查詢式）與 Cross-Attention（交叉注意力式）架構有何差異。
- 圖片解析度、圖片／影格數量與 connector 如何共同影響 token budget（詞元預算）與 Latency（延遲）壓力。
- Camera（相機）、語言與 Robot State（機器人狀態）如何形成 Structured Output（結構化輸出），再交給 Planner（任務規劃器）與 Controller（控制器）。
- Semantic Location（語意位置）、2D／3D Grounding（定位）與 Robot Coordinate（機器人座標）為什麼是不同資料層級。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 本週學習順序、Demo、Practice 任務與驗收條件。 |
| `notes.md` | VLM 架構家族、connector、融合策略、token budget 與系統限制。 |
| `study_log.md` | 學生實際執行結果、架構比較與未解問題。 |
| `demo/` | 快速展示架構家族、Camera-to-Structured-Perception、connector、token／latency budget 與 Robot VLM 系統邊界。 |
| `practice/` | Concept Practice 與 Guided Code Reading Mode（引導式程式閱讀模式）。 |

## 建議使用方式

1. 閱讀 `weekly_plan.md` 與 `notes.md` 第 1–3 節。
2. 依序執行五個 Demo，建立各架構與機器人系統邊界的 What（做什麼）。
3. 閱讀 `notes.md` 第 4–6 節，理解融合、序列成本與系統邊界。
4. 執行四個 Guided Demo，追蹤 shape、中間值與失敗位置。
5. 完成 Concept Practice 與 Coding Practice。
6. 將自己的架構圖、比較表與疑問寫入 `study_log.md`。

## Demo 主線

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_architecture_families.py
python demo/demo_02_camera_to_answer_flow.py
python demo/demo_03_connector_comparison.py
python demo/demo_04_token_budget.py
python demo/demo_05_robot_vlm_system_flow.py
```

## 與 VLM/VLA 碩士研究的關聯

研究系統必須能說明每個模組的輸入、輸出、資源成本、證據來源與失敗方式。本週只建立 Robot VLM 系統架構，不提前實作 ROS2、深度相機 SDK、Isaac Sim 或 VLA 訓練；這些概念會成為後續實作選擇的共同語言。

## 本週完成後應具備的能力

- 能畫出至少四種 VLM 架構並指出 representation、generative 與未來 action output 的差異。
- 能解釋 Vision Encoder、Connector 與 Language Model 的介面。
- 能比較直接投影、查詢壓縮與 cross-attention 融合。
- 能估算 single-frame（單影格）與 multi-frame（多影格）token／latency budget。
- 能說明 Robot State、Spatial Grounding（空間語意定位）與 Structured Output。
- 能畫出 VLM／語意系統 → Planner → Controller，並解釋 VLM 為何不能直接控制馬達。
