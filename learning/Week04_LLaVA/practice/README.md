# Week04 Practice Overview

`practice/` 是 Week04 所有練習內容的唯一入口。本週練習分成 Concept Practice（觀念練習）與 Coding Practice（程式閱讀練習）。

## 練習檔案

| 路徑 | 用途 |
| --- | --- |
| `concept/concept_practice.md` | 學生觀念作答檔，包含 LLaVA 基礎、Grounding 與 Robot VLM 能力邊界。 |
| `concept/concept_answer_key.md` | 觀念參考答案，請完成練習後再查看。 |
| `coding/README.md` | Coding Practice 執行方式、環境需求與模型需求。 |
| `coding/coding_practice.md` | Guided Code Reading、robot-oriented prompt 比較與主張分類紀錄表。 |
| `coding/coding_observation_key.md` | 觀察方向與理解說明，請完成紀錄後再查看。 |
| `coding/guided_demos/` | 完整可執行的引導式程式閱讀檔。 |
| `coding/requirements.txt` | 程式練習依賴。 |

## 建議順序

1. 先執行 `../demo/` 的 Demo 01、02，建立輸入與架構的整體印象。
2. 完成 `concept/concept_practice.md`，不要先看答案。
3. 閱讀 `coding/README.md`，依序執行 `coding/guided_demos/`。
4. 在 `coding/coding_practice.md` 記錄 Processor shape、Projector、多模態序列與生成觀察。
5. 完成後再查看 `concept/concept_answer_key.md` 與 `coding/coding_observation_key.md`。
6. 進入 Required Real Track 的 Demo 03；若 runtime 受阻，記錄標準 blocker。Demo 04 用於進階比較。將回答分類為 Supported／Uncertain／Contradicted／Requires Additional Sensor or Robot State，再整理到 `../study_log.md`。

## 本週 Coding Practice 模式

本週採 Guided Code Reading Mode（引導式程式閱讀模式）。原因是 Week04 的主要目標是理解 LLaVA（大型語言與視覺助手）推論資料流，而不是從零實作大型模型。程式提供完整可執行版本，學生需要觀察 shape、中間值、image token 位置、逐 token 生成與問題改寫效果。
