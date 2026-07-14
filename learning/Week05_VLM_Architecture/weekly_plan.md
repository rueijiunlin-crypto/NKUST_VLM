# Week05 Weekly Plan：VLM Architecture 架構與資料流

## 本週目標

- 理解 VLM（視覺語言模型）共通元件與主要架構家族。
- 能區分 representation output（表示輸出）與 generative output（生成輸出）。
- 能說明 Vision Encoder（視覺編碼器）、Connector（連接器）與 Language Model（語言模型）的分工。
- 能追蹤 Camera-to-Answer 資料流與 shape。
- 能比較 connector 的資訊保留、序列成本與研究取捨。

## 必學概念

- Dual Encoder、Projector-based、Query-based 與 Cross-Attention 架構。
- Vision features、text embeddings（文字嵌入向量）與 modality alignment（模態對齊）。
- Linear／MLP Projector、query tokens（查詢詞元）與 cross-attention。
- Early／late／interleaved fusion（早期／晚期／交錯融合）。
- Token budget、context length（上下文長度）與計算成本。
- Camera-to-Answer 的驗證與安全邊界。

## 建議學習順序

1. 閱讀 `README.md` 與 `notes.md` 第 1–2 節。
2. 執行 Demo 01，比較架構家族與輸出型態。
3. 執行 Demo 02，畫出 Camera-to-Answer 資料流。
4. 閱讀 `notes.md` 第 3–4 節，理解 connector 與融合策略。
5. 執行 Demo 03 與 Guided Demo 01–03。
6. 閱讀 `notes.md` 第 5–6 節，理解 token budget 與系統驗證。
7. 執行 Demo 04 與 Guided Demo 04。
8. 完成 Concept Practice、Coding Practice 與 `study_log.md`。

## Demo 執行順序

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_architecture_families.py
python demo/demo_02_camera_to_answer_flow.py
python demo/demo_03_connector_comparison.py
python demo/demo_04_token_budget.py
python demo/demo_04_token_budget.py --images 2 --query-tokens 32
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
- [ ] 執行四個 Demo 並保存輸出。
- [ ] 畫出 Dual Encoder 與生成式 VLM 的差異圖。
- [ ] 執行四個 Guided Demo 並完成觀察欄位。
- [ ] 完成 Concept Practice。
- [ ] 比較 Projector 與 Query Connector 的取捨。
- [ ] 記錄一組不同圖片數量或 query tokens 的 token budget 結果。
- [ ] 在 `study_log.md` 記錄理解與未解問題。
- [ ] 更新 Notion 學習狀態並進行 ChatGPT 驗收。

## 驗收條件

- [ ] 能畫出 Camera → Preprocess → Vision Encoder → Connector → LLM → Validator → Answer。
- [ ] 能區分 CLIP 類相似度輸出與 LLaVA 類生成輸出。
- [ ] 能解釋 Projector 與 Query Connector 的 token 數量差異。
- [ ] 能說明 cross-attention 的 Query、Key、Value 來自何處。
- [ ] 能估算圖片數量與解析度對 token budget 的影響。
- [ ] 能指出至少三個架構失敗點。
- [ ] `study_log.md` 已由學生填入實際觀察。

## 銜接 Week06 Paper Reading

Week06 將使用本週的架構詞彙閱讀 CLIP 與 LLaVA 論文，從架構圖、方法與實驗證據判斷作者的研究主張。
