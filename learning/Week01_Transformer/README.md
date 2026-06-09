# Week01 Transformer 基礎

## 學習定位

Week01 的任務是建立 Transformer（轉換器架構）的基礎概念，讓後續學習 CLIP（對比式圖文預訓練）、LLaVA（大型語言與視覺助手）、Vision-Language Model（視覺語言模型，VLM）與 Vision-Language-Action Model（視覺語言動作模型，VLA）時，有清楚的資料流直覺。

本週不追求完整論文推導，而是先理解文字如何被切成 Token（詞元）、轉成 Embedding（嵌入向量），再透過 Query（查詢）、Key（鍵）、Value（值）與 Attention（注意力機制）建立上下文表示。

## 檔案說明

- `README.md`：Week01 導覽、學習定位與閱讀順序。
- `weekly_plan.md`：本週學習目標、7 天安排、練習、驗收清單與 Notion（筆記與資料庫管理工具）紀錄項目。
- `notes.md`：正式教材，依 Level 1 至 Level 5 說明每個核心概念。
- `study_log.md`：學生個人學習紀錄與 Demo 執行紀錄。
- `demo/`：每個概念的可執行示範程式與對應說明。
- `practice/`：本週練習總入口，包含觀念練習、程式練習、參考答案與練習用程式。

## 建議閱讀順序

1. 先讀 `README.md`，確認本週定位。
2. 讀 `weekly_plan.md`，了解學習安排、練習與驗收方式。
3. 依序閱讀 `notes.md` 的核心概念。
4. 依 `weekly_plan.md` 的 Demo 執行順序跑 `demo/`。
5. 依 `weekly_plan.md` 的 Practice 順序完成 [`practice/`](./practice/README.md)。
6. 將真實執行結果、Practice 結果與觀察寫入 `study_log.md`。

## 與 VLM/VLA 主線的關聯

Transformer 是理解多模態模型的共同基礎。文字可以被切成 Token，影像可以被切成 Patch（影像切塊），兩者都能轉成向量序列；Attention 讓模型學會序列內與序列間的關係。Week02 會接續到 CLIP，理解影像與文字如何被放到共同向量空間中比較。
