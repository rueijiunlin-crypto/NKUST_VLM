# Week05 Concept Answer Key

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

## 1. Dual Encoder 與生成式 VLM

Dual Encoder 分別編碼圖片與文字，再比較向量，適合檢索或零樣本分類。生成式 VLM 讓視覺資訊進入語言模型上下文，逐 token 產生回答，適合描述與問答。前者通常容易預先索引，後者表達彈性較高但有生成成本與幻覺風險。

## 2. Vision Encoder

Patch 是固定像素區塊，不必然對應物件；經多層 attention 後才形成上下文化表示。寬高各加倍會使網格兩軸各加倍，總位置約四倍。

## 3. Projector

1 是 batch、576 是 image token positions、1024／4096 是前後 hidden size。線性或 MLP 轉換讓介面尺寸相容；真正語意對齊仍依賴訓練資料與目標，不能由 shape 單獨證明。

## 4. Query Connector

32 個 queries 可降低送入 LLM 的序列長度與計算，但固定壓縮可能遺失小物件、計數或空間細節。優劣需由目標任務實驗驗證。

## 5. Cross-Attention

語言 states 通常作 Query，視覺 features 作 Key／Value，代表語言位置主動讀取視覺資訊。串接 self-attention 則把兩種 tokens 放在共同序列中依 attention mask 互動。

## 6. Token Budget

保留所有位置時為 `2 × 576 + 128 = 1280`。每張壓成 32 個 query positions 時為 `2 × 32 + 128 = 192`。兩者仍未計特殊 token 與輸出 token。

## 7. Camera-to-Answer 診斷

可能包含 Camera 白平衡或曝光、BGR／RGB 前處理錯誤、Vision Encoder domain shift、connector 資訊損失、LLM 幻覺或 validator 未檢查顏色。應保存各階段中間結果並定位第一個錯誤。

## 8. 架構選擇

大規模檢索可優先 Dual Encoder，因向量可預先建立索引；場景問答可優先生成式 VLM，因需依問題產生文字。仍需考慮資料、延遲、硬體、正確性與輸出驗證，不能只由模型類別決定。
