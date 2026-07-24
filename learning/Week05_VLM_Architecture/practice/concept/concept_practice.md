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

把 576 個視覺位置壓成 32 個 query tokens 有什麼優點與風險？對 robot manipulation（機器人操作）而言，可能遺失哪些 small object、spatial detail 或操作相關特徵？

### 學生作答區



### 自我檢查

- [ ] 我有討論計算成本與資訊遺失。

## 5. Cross-Attention

當語言 states 讀取視覺 features 時，Query、Key、Value 各來自哪裡？與串接後 self-attention 有何概念差異？

### 學生作答區



### 自我檢查

- [ ] 我有指出模態來源與互動方向。

## 6. Token Budget

一張圖片提供 576 個位置，文字使用 128 個位置。兩張圖片時概念總位置是多少？若每張圖片壓成 32 個 query positions 又是多少？忽略特殊 token。若輸入是 16 個未壓縮影格，為什麼會產生 token explosion（詞元爆增）與延遲壓力？

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

## 9. Spatial Grounding 層級

Semantic Grounding（語意定位）、2D Grounding（二維定位）與 3D Grounding（三維定位）差在哪？`"The cup is left of the box."` 為什麼不等於 `cup = [0.42, 0.16, 0.81] m`？

### 學生作答區



### 自我檢查

- [ ] 我有區分語意關係、像素區域與公尺座標。

## 10. Camera Coordinate 與 Robot Coordinate

兩者的原點與方向由什麼決定？從 camera coordinate 轉成 robot coordinate 還需要什麼？

### 學生作答區



### 自我檢查

- [ ] 我有提到外部標定／座標轉換與時間一致性。

## 11. Robot State

列出至少六種典型 Robot State（機器人狀態），並說明為什麼 Image 不是決策需要的全部資訊。

### 學生作答區



### 自我檢查

- [ ] 我有涵蓋 pose、joint、gripper、camera 或 navigation state。

## 12. Structured Output

為什麼 JSON／structured schema 通常比自由文字更適合作為機器人系統介面？合法 JSON 是否代表內容正確？

### 學生作答區



### 自我檢查

- [ ] 我有同時說明可驗證性與 Grounding 限制。

## 13. Streaming Camera

Single-frame、multi-frame 與 Streaming VLM（串流視覺語言模型）有何差異？為什麼 30 FPS Camera 不應逐幀完整送入大型 VLM？

### 學生作答區



### 自我檢查

- [ ] 我有提到 Frame Sampling、時間上下文、token、記憶體與 Latency。

## 14. VLM Output 與 VLA Action Output

VLM Answer／Structured Perception 與 VLA action output 的根本差異是什麼？

### 學生作答區



### 自我檢查

- [ ] 我沒有把文字動詞直接當成已定義的動作表示。

## 15. Safety Boundary

為什麼 Low-Level Motor Control、Collision Avoidance、Safety Interlock 與 Emergency Stop 不能只依賴 VLM？

### 學生作答區



### 自我檢查

- [ ] 我有比較生成模型與即時、安全關鍵模組的需求。
