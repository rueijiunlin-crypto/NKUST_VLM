# Week06 VLM Paper Reading 論文閱讀與證據整理

## 本週定位

Week06 將 Week01–05 的 Transformer、CLIP、LLaVA 與 VLM Architecture（視覺語言模型架構）知識轉成研究閱讀能力。本週以 CLIP 與 LLaVA 原始論文為核心，不只摘要內容，而是建立 claim-to-evidence（主張到證據）與可重現比較流程。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 閱讀順序、Demo、Practice 與驗收條件。 |
| `notes.md` | 三階段閱讀、架構圖、方法、實驗、限制與引用規範。 |
| `study_log.md` | 學生實際閱讀位置、證據與未解問題。 |
| `demo/` | 快速展示閱讀 passes、主張證據、metric context 與論文比較。 |
| `practice/` | Concept Practice 與 Guided Code Reading Mode（引導式程式閱讀模式）。 |

## 建議使用方式

1. 閱讀 `weekly_plan.md` 與 `notes.md` 第 1–3 節。
2. 執行 Demo 01，完成 CLIP 論文 Pass 1。
3. 執行 Demo 02、03，建立 claim-evidence 與 metric context 表。
4. 對 LLaVA 重複相同步驟。
5. 執行 Demo 04 與四個 Guided Demo，完成比較矩陣。
6. 完成 Practice，將自己的證據位置寫入 `study_log.md`。

## Demo 主線

```powershell
python demo/demo_01_reading_passes.py
python demo/demo_02_claim_evidence_map.py
python demo/demo_03_metric_context.py
python demo/demo_04_clip_llava_comparison.py
```

## 與 VLM/VLA 碩士研究的關聯

論文題目收斂需要區分作者主張、實驗證據與自己的推論。固定閱讀模板能協助後續比較模型、設計 baseline（基準方法）、建立實驗指標並避免把論文宣傳語句直接當成研究事實。

## 本週完成後應具備的能力

- 能用一句話寫出研究問題與核心貢獻。
- 能由架構圖還原輸入、元件、輸出與訓練目標。
- 能把主張連到具體圖、表、段落或附錄。
- 能判斷兩個分數是否具有可比較條件。
- 能用固定欄位比較 CLIP 與 LLaVA。
- 能列出限制、未報告資訊與自己的未解問題。
