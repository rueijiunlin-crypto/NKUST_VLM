# Week05 Coding Observation Key

> 請先完成 `coding_practice.md`，再查看本觀察方向。

## 1. Vision Encoder Flow

預設 RGB `4 × 4` 圖片使用 `2 × 2` patch，形成四個位置；每個 patch vector 包含 `3 × 2 × 2 = 12` 個值。Patch size 改成 1 時會形成 16 個位置，每個位置只有 3 個 channel 值。Patch vector 尚未經 Transformer 上下文化，不能當成完整物件表示。

## 2. Projector Alignment

範例由 `[1,3,4]` 經 hidden `[1,3,5]` 轉成 `[1,3,6]`。Batch 與 token axes 保留，最後 hidden axis 改變。Seed 改變數值但不改架構 shape，說明介面正確不等於權重或語意正確。

## 3. Fusion Strategies

串接保留所有位置；query compression 用少量查詢加權摘要視覺位置；cross-attention 讓 text states 作 Query、image states 作 Key／Value。三者輸出 shape 可能相容，但資訊互動與計算成本不同。

## 4. End-to-End Flow

回答錯誤可能源自影像品質、色彩格式、視覺 domain shift、connector 壓縮、LLM 幻覺或 validator 過弱。診斷時應檢查第一個偏離預期的中間輸出，不應直接把所有錯誤歸因於最後模型。

## 常見誤解修正

- Patch 不等於物件。
- Hidden size 對齊不等於語意已對齊。
- Token 越少不必然越好。
- 最終 JSON 合法不代表視覺內容正確。
