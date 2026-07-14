# Week05 VLM Architecture 架構與資料流

## 本週定位

Week05 延續 Week04 LLaVA（大型語言與視覺助手），把單一模型的推論流程抽象成 Vision-Language Model（視覺語言模型，VLM）的共通架構問題。

本週重點不是背模型名稱，而是能回答：

- 圖片與文字分別如何被編碼。
- Connector（連接器）如何處理 modality gap（模態差距）。
- Dual Encoder（雙編碼器）、Projector-based（投影器式）、Query-based（查詢式）與 Cross-Attention（交叉注意力式）架構有何差異。
- 圖片解析度、圖片數量與 connector 如何影響 token budget（詞元預算）。
- Camera（相機）輸入如何經過驗證後形成 Answer（回答）。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 本週學習順序、Demo、Practice 任務與驗收條件。 |
| `notes.md` | VLM 架構家族、connector、融合策略、token budget 與系統限制。 |
| `study_log.md` | 學生實際執行結果、架構比較與未解問題。 |
| `demo/` | 快速展示架構家族、Camera-to-Answer、connector 與 token budget。 |
| `practice/` | Concept Practice 與 Guided Code Reading Mode（引導式程式閱讀模式）。 |

## 建議使用方式

1. 閱讀 `weekly_plan.md` 與 `notes.md` 第 1–3 節。
2. 依序執行四個 Demo，建立各架構的 What（做什麼）與主要差異。
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
```

## 與 VLM/VLA 碩士研究的關聯

研究系統必須能說明每個模組的輸入、輸出、可訓練參數、資源成本與失敗方式。這些架構觀念會直接影響後續 Camera、ROS2（機器人作業系統第二版）、navigation（導航）、NVIDIA Isaac Sim 6.0（NVIDIA 機器人模擬器）與 Vision-Language-Action Model（視覺語言動作模型，VLA）的系統設計。

## 本週完成後應具備的能力

- 能畫出至少三種 VLM 架構並指出輸出差異。
- 能解釋 Vision Encoder、Connector 與 Language Model 的介面。
- 能比較直接投影、查詢壓縮與 cross-attention 融合。
- 能估算 image tokens 對多模態序列的影響。
- 能說明 Camera-to-Answer 各階段的驗證點與風險。
