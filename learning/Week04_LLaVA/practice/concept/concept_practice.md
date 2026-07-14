# Week04 Concept Practice（觀念練習）

> 請先依自己的理解作答。學生作答區刻意保留空白，不要先查看 `concept_answer_key.md`。

## Q1 CLIP 與 LLaVA 的輸出差異

請比較 CLIP（對比式圖文預訓練）的相似度輸出與 LLaVA（大型語言與視覺助手）的生成式輸出。

提示：候選 labels、自回歸生成、輸出 shape。

### 學生作答區



### 自我檢查

- [ ] 我有說明兩者回答的問題不同。
- [ ] 我沒有把 LLaVA 描述成只會選 top-1 label。

## Q2 Vision Encoder 的角色

Vision Encoder（視覺編碼器）如何把 RGB 圖片轉成可供後續模組使用的特徵？Patch token 是否必然對應一個完整物件？

提示：patch、feature vector（特徵向量）、contextualization（上下文化）。

### 學生作答區



### 自我檢查

- [ ] 我有描述圖片到多個向量的流程。
- [ ] 我有解釋 patch 與物件不是一對一關係。

## Q3 Projector 為什麼必要

若 Vision Encoder 輸出 `[1, 576, 1024]`，LLM token embedding 需要最後一維 `4096`，Projector 前後的概念 shape 應如何變化？它會直接輸出句子嗎？

提示：保留 token 數量、改變 hidden size。

### 學生作答區



### 自我檢查

- [ ] 我有寫出 Projector 前後的 shape。
- [ ] 我有區分連續向量與文字答案。

## Q4 `<image>` Placeholder

為什麼 prompt 中的一個 `<image>` 字串，不代表模型只使用一個 image token？

提示：Processor（前處理器）、替換／展開、image embeddings（影像嵌入向量）。

### 學生作答區



### 自我檢查

- [ ] 我有區分文字占位符與影像向量序列。

## Q5 Chat Template

手動把同一種 prompt 格式套到所有 LLaVA checkpoint，可能產生哪些問題？至少列出兩項。

提示：角色標記、特殊 token、圖片位置、對話結束符號。

### 學生作答區



### 自我檢查

- [ ] 我有說明格式是模型輸入契約的一部分。
- [ ] 我有提出使用 checkpoint processor／template 的做法。

## Q6 自回歸生成

請用自己的話說明 LLM 如何逐 token 產生回答，以及 `max_new_tokens` 控制什麼。

提示：logits、選擇下一個 token、接回序列、停止條件。

### 學生作答區



### 自我檢查

- [ ] 我沒有把 `max_new_tokens` 解釋成字數。

## Q7 Hallucination 與視覺依據

模型回答「桌上有一個紅色急救箱」，但圖片中的物件模糊且顏色無法確認。研究紀錄應如何分析？機器人系統是否能直接依此回答行動？

提示：可見證據、不確定性、交叉確認、安全邊界。

### 學生作答區



### 自我檢查

- [ ] 我有區分語言流暢度與事實正確性。
- [ ] 我有提出安全處置方式。

## Q8 可重現 VLM 實驗

除了保存圖片與回答，至少還要記錄哪些五項資訊，才能合理重現一次 LLaVA 推論？

提示：模型、環境、prompt、生成參數、原始輸出。

### 學生作答區



### 自我檢查

- [ ] 我列出的資訊能幫助另一個人重做相同實驗。
