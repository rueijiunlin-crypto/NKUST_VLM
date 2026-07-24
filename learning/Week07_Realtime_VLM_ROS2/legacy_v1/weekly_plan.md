# Week07 Weekly Plan：Prompt Engineering

## 本週目標

- 將 Prompt（提示）設計成明確、可測試的輸入契約。
- 能使用結構化欄位表示 target、evidence、uncertainty 與 status。
- 能分層驗證 JSON syntax（語法）、schema、semantic（語意）、grounding（視覺依據）與 safety（安全）。
- 能設計 retry（重試）、request new observation（要求新觀察）與 reject（拒絕）政策。
- 能為語意導覽與物體辨識建立 Prompt 測試矩陣。

## 必學概念

- Role、task、context、evidence boundary（證據邊界）與 output contract（輸出契約）。
- Multimodal chat template（多模態對話模板）。
- JSON object、required fields、enum（列舉值）與 additional fields（額外欄位）。
- Unknown／not found／found 狀態差異。
- Format retry、grounding rejection 與 bounded retries（有限重試）。
- VLM semantic output 與 ROS2／navigation 控制邊界。

## 建議學習順序

1. 閱讀 `README.md` 與 `notes.md` 第 1–2 節。
2. 執行 Demo 01、03，比較模糊與有契約的 Prompt。
3. 閱讀第 3–4 節，執行 Demo 02 與 Guided Demo 01、02。
4. 閱讀第 5 節，執行 Demo 04 與 Guided Demo 03。
5. 閱讀第 6 節，執行 Demo 05 與 Guided Demo 04。
6. 建立三個 Prompt 版本與至少六個測試案例。
7. 完成 Concept Practice、Coding Practice 與 `study_log.md`。

## Demo 執行順序

```powershell
python demo/demo_01_prompt_anatomy.py
python demo/demo_02_structured_output_validation.py
python demo/demo_03_prompt_version_comparison.py
python demo/demo_04_retry_policy.py
python demo/demo_05_robot_safety_gate.py
```

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

本週採 Guided Code Reading Mode。程式完整提供，學生需觀察 Prompt contract、validation layers（驗證層）、retry decision 與 safety handoff，不使用 TODO 補空題。

## 任務清單

- [ ] 閱讀本週入口、計畫與教材。
- [ ] 執行五個 Demo。
- [ ] 定義一份室內語意目標 JSON contract。
- [ ] 設計至少三個 Prompt 版本。
- [ ] 設計正常、模糊、缺少目標、錯誤前提、格式錯誤與安全違規案例。
- [ ] 執行四個 Guided Demo 並填寫觀察。
- [ ] 完成 Concept Practice。
- [ ] 在 `study_log.md` 記錄 Prompt 版本、結果與失敗分類。
- [ ] 更新 Notion 並進行 ChatGPT 驗收。

## 驗收條件

- [ ] Prompt 明確包含任務、證據邊界、輸出契約與 unknown policy。
- [ ] Validator 能拒絕非法 JSON、缺少欄位與不允許值。
- [ ] 能說明 JSON 合法為何不代表視覺事實正確。
- [ ] Retry 有明確原因與最大次數。
- [ ] Unknown 不會被文字重試強迫改成 found。
- [ ] 語意輸出不包含直接速度或轉向控制。
- [ ] `study_log.md` 已由學生填入實際測試結果。

## 銜接 Week08 Mini Project

Week08 將把本週 Prompt contract、structured output（結構化輸出）與 validation flow（驗證流程）放入 Image Caption（影像描述）與 Visual QA（視覺問答）最小系統。
