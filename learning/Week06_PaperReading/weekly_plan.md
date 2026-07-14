# Week06 Weekly Plan：VLM Paper Reading

## 本週目標

- 建立三階段 VLM 論文閱讀流程。
- 能區分 research problem（研究問題）、method（方法）、experiment（實驗）、claim（主張）與 evidence（證據）。
- 能閱讀架構圖、表格、metric（評估指標）、ablation（消融實驗）與 limitation（限制）。
- 完成 CLIP 與 LLaVA 的固定欄位比較。
- 建立可同步到 Notion Paper Database（論文資料庫）的紀錄。

## 必學概念

- Pass 1 Orientation、Pass 2 Evidence、Pass 3 Reproduction。
- Claim-to-evidence mapping（主張到證據映射）。
- Dataset、split、metric、baseline 與 evaluation setting（評估設定）。
- Ablation、controlled comparison（控制比較）與 threat to validity（效度威脅）。
- 直接引用、改寫、自己的推論與未報告資訊。

## 建議學習順序

1. 閱讀 `notes.md` 第 1–2 節並執行 Demo 01。
2. 對 CLIP 做 Pass 1，記錄問題、方法、輸出與核心證據。
3. 閱讀第 3–5 節並執行 Demo 02、03。
4. 對 LLaVA 做 Pass 1 與 Pass 2。
5. 閱讀第 6–7 節，執行 Demo 04 與 Guided Demo 01–04。
6. 完成 Concept Practice、Coding Practice 與比較矩陣。
7. 在 `study_log.md` 保存來源位置、限制與未解問題。

## Demo 執行順序

```powershell
python demo/demo_01_reading_passes.py
python demo/demo_02_claim_evidence_map.py
python demo/demo_03_metric_context.py
python demo/demo_04_clip_llava_comparison.py
```

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

本週 Coding Practice 採 Guided Code Reading Mode。程式協助建立結構化閱讀與證據檢查流程，不代表自動讀完論文，也不會代填學生的 Paper Database。

## 任務清單

- [ ] 閱讀 CLIP 與 LLaVA 原始論文摘要、架構圖與結論。
- [ ] 執行四個 Demo。
- [ ] 為兩篇論文各建立至少三筆 claim-evidence 紀錄。
- [ ] 記錄 dataset、split、metric 與 evaluation setting。
- [ ] 執行四個 Guided Demo。
- [ ] 完成 Concept Practice 與比較矩陣。
- [ ] 記錄至少兩項限制或未報告資訊。
- [ ] 更新 `study_log.md`、Notion 與 ChatGPT 驗收。

## 驗收條件

- [ ] 能用自己的話說明兩篇論文的研究問題。
- [ ] 每個核心主張都有可定位來源與證據。
- [ ] 不把不同 dataset、split 或 setting 的分數直接比較。
- [ ] 能說明架構元件與實驗證據的對應。
- [ ] 能區分論文事實、自己的推論與未知資訊。
- [ ] `study_log.md` 已由學生填入實際閱讀結果。

## 銜接 Week07 Prompt Engineering

Week07 會把論文中的 instruction（指令）、prompt（提示）與輸出限制轉成可測試的機器人語境 Prompt 實驗。
