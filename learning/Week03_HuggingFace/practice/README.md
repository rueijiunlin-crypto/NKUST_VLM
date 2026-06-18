# Week03 Practice Overview

`practice/` 是 Week03 所有練習內容的唯一入口。本週練習分成 Concept Practice（觀念練習）與 Coding Practice（程式閱讀練習）。

## 練習檔案

| 路徑 | 用途 |
| --- | --- |
| `concept/concept_practice.md` | 學生觀念作答檔，包含 token、shape、softmax、top-k 與候選 labels 題目。 |
| `concept/concept_answer_key.md` | 觀念參考答案，請完成練習後再查看。 |
| `coding/README.md` | Coding Practice 執行方式與環境需求。 |
| `coding/coding_practice.md` | Guided Code Reading 任務與 prompt 實驗紀錄表。 |
| `coding/coding_observation_key.md` | 觀察方向與理解說明，請完成紀錄後再查看。 |
| `coding/guided_demos/` | 可執行的引導式程式閱讀檔。 |
| `coding/requirements.txt` | 程式練習依賴。 |

## 建議順序

1. 先執行 `../demo/` 的三個 demo，建立整體印象。
2. 完成 `concept/concept_practice.md`，不要先看答案。
3. 閱讀 `coding/README.md`，執行 `coding/guided_demos/`。
4. 在 `coding/coding_practice.md` 記錄 tensor shape、softmax/top-k 與 prompt 實驗結果。
5. 完成後再查看 `concept/concept_answer_key.md` 與 `coding/coding_observation_key.md`。
6. 將重要觀察與疑問整理到 `../study_log.md`。

## 本週 Coding Practice 模式

本週採用 Guided Code Reading Mode（引導式程式閱讀模式）。原因是 Week03 的主要目標是理解 Hugging Face CLIP 推論資料流，而不是從零實作模型。程式已提供完整可執行版本，學生需要觀察 shape、中間值、top-k 索引與 prompt 改寫效果。
