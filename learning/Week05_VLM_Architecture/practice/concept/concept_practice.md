# Week05 Concept Practice

> 請先自行作答，不要先查看 `concept_answer_key.md`。

## 1. Dual Encoder 與生成式 VLM

兩者的資料流與輸出有何不同？各舉一個適合任務。

提示：embedding、similarity、generated tokens。

### 學生作答區



### 自我檢查

- [ ] 我有同時比較輸入、互動方式與輸出。

## 2. Vision Encoder

為什麼 patch vector 不能直接等同物件？圖片寬高加倍、patch size 不變時，patch 數量如何變化？

### 學生作答區



### 自我檢查

- [ ] 我有解釋上下文化與二維網格。

## 3. Projector

Projector 將 `[1,576,1024]` 轉成 `[1,576,4096]` 時，各維度代表什麼？它是否已完成語意對齊？

### 學生作答區



### 自我檢查

- [ ] 我沒有把 shape 相容等同語意正確。

## 4. Query Connector

把 576 個視覺位置壓成 32 個 query tokens 有什麼優點與風險？

### 學生作答區



### 自我檢查

- [ ] 我有討論計算成本與資訊遺失。

## 5. Cross-Attention

當語言 states 讀取視覺 features 時，Query、Key、Value 各來自哪裡？與串接後 self-attention 有何概念差異？

### 學生作答區



### 自我檢查

- [ ] 我有指出模態來源與互動方向。

## 6. Token Budget

一張圖片提供 576 個位置，文字使用 128 個位置。兩張圖片時概念總位置是多少？若每張圖片壓成 32 個 query positions 又是多少？忽略特殊 token。

### 學生作答區



### 自我檢查

- [ ] 我有分別計算視覺與文字位置。

## 7. Camera-to-Answer 診斷

回答把藍色物件說成紅色。列出至少三個可能失敗階段及對應檢查。

### 學生作答區



### 自我檢查

- [ ] 我沒有只寫「LLM 幻覺」。

## 8. 架構選擇

若研究任務分別是「大規模圖文檢索」與「室內場景問答」，你會優先選哪類架構？說明理由與限制。

### 學生作答區



### 自我檢查

- [ ] 我的選擇由任務與輸出需求支持。
