# Week07 Prompt Engineering 結構化輸出與安全語意

## 本週定位

Week07 延續 Week04 的 LLaVA（大型語言與視覺助手）問題比較與 Week06 的證據閱讀，將 Prompt Engineering（提示工程）視為可版本控制、可測試的輸入契約。

本週不追求「神奇關鍵字」，而是設計：任務、影像證據邊界、輸出 schema（結構規格）、unknown（未知）政策、錯誤回覆與機器人安全邊界。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 學習順序、Demo、Practice、任務與驗收。 |
| `notes.md` | Prompt 組成、chat template、JSON 契約、驗證、重試與安全。 |
| `study_log.md` | Prompt 版本、測試案例、結果與錯誤紀錄。 |
| `demo/` | 快速展示 Prompt anatomy、結構驗證、版本比較、重試與 safety gate。 |
| `practice/` | Concept Practice 與 Guided Code Reading Mode（引導式程式閱讀模式）。 |

## 建議使用方式

1. 閱讀 `notes.md` 第 1–3 節並執行 Demo 01、03。
2. 閱讀第 4–5 節並執行 Demo 02、04。
3. 閱讀第 6 節並執行 Demo 05。
4. 執行四個 Guided Demo，理解驗證與安全資料流。
5. 設計至少三個 Prompt 版本與正常／邊界／失敗測試。
6. 完成 Practice 並把實際結果寫入 `study_log.md`。

## Demo 主線

```powershell
python demo/demo_01_prompt_anatomy.py
python demo/demo_02_structured_output_validation.py
python demo/demo_03_prompt_version_comparison.py
python demo/demo_04_retry_policy.py
python demo/demo_05_robot_safety_gate.py
```

## 與 VLM/VLA 碩士研究的關聯

機器人系統需要穩定的 semantic interface（語意介面），不能直接解析任意自然語言。Prompt、schema、validator（驗證器）、unknown policy 與 safety gate（安全閘門）將成為 Week08 Mini Project、Camera、ROS2 與 navigation 的共用設計基礎。

## 本週完成後應具備的能力

- 能把 Prompt 拆成角色、任務、證據、輸出、未知與安全段落。
- 能設計固定 JSON 欄位與允許值。
- 能區分 syntax、schema、semantic、grounding 與 safety 驗證。
- 能針對可修正錯誤重試，對未知或不安全結果拒絕。
- 能建立 Prompt version、test case 與結果比較表。
