# Week04 Concept Answer Key（觀念參考答案）

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

## Q1 CLIP 與 LLaVA 的輸出差異

CLIP 常把圖片與預先提供的候選文字各自編碼，輸出 `[num_images, num_texts]` 的相似度，再於候選集合中排序。LLaVA 則把圖片特徵與問題組成多模態上下文，由 LLM 逐 token 生成開放式文字。常見誤解是把 LLaVA 想成「候選 labels 更多的 CLIP」；兩者的輸出機制與研究風險並不相同。

## Q2 Vision Encoder 的角色

圖片先被調整尺寸、正規化並切成 patches，每個 patch 轉成向量，再經視覺 Transformer 交換全域資訊。輸出是多個 contextualized visual features（上下文化視覺特徵）。Patch 是固定影像區塊，不一定等於一個物件；一個物件可能跨越多個 patches，一個 patch 也可能包含背景與多個局部特徵。

## Q3 Projector 為什麼必要

概念 shape 可由 `[1, 576, 1024]` 轉為 `[1, 576, 4096]`。第二維的 576 個位置可保留，最後一維改成 LLM 的表示維度。Projector 輸出連續向量，不直接輸出句子；句子由 LLM 自回歸生成。

## Q4 `<image>` Placeholder

`<image>` 是提示文字中的插入位置。Processor 會按照 checkpoint 規則，把圖片產生的許多 image embeddings 對應到該位置。因此字串表面的一個標記，可能對應模型序列中的數百個影像向量位置。

## Q5 Chat Template

錯誤格式可能讓角色邊界、圖片位置、特殊 token 或停止條件不符模型訓練方式，造成圖片未正確對齊、prompt 重複、回答品質下降或 shape mismatch。應使用 checkpoint 隨附的 processor 與 chat template，並保存實際送入模型的格式。

## Q6 自回歸生成

LLM 對目前上下文計算下一 token 的 logits，依 greedy 或 sampling 規則選 token，再接回上下文重複計算，直到停止 token 或長度上限。`max_new_tokens` 限制新增 token 數量，不是人類語言的字數或單字數。

## Q7 Hallucination 與視覺依據

應把「有急救箱」「紅色」「在桌上」拆成可檢查主張，逐一標記是否能由圖片支持；模糊與顏色不明應記為不確定，而不是正確。機器人不應直接行動，可要求更清晰影像、從其他角度確認、結合物件偵測或地圖資料，並限制可執行動作與保留人工停止機制。

## Q8 可重現 VLM 實驗

合理答案包含：Model ID／revision、套件版本、硬體與 dtype、完整 prompt／conversation、圖片來源、生成參數、random seed、原始回答、執行時間與錯誤訊息。核心推理原則是讓另一位研究者能重建輸入、環境與生成設定，而不是只看到挑選過的成功結果。

## Q9 物體辨識與 Robot Coordinate

物體辨識提供的是語意類別；Robot Coordinate 是相對機器人基座的度量位置。後者通常需要深度或多視角幾何、相機內外參、camera-to-robot 座標轉換與有效時間戳。常見誤解是把語意定位或影像中的像素位置當成三維機器人座標。

## Q10 單張 RGB 與精確 3D

同一個二維投影可能對應不同尺寸與深度的三維場景，單張 RGB 因此存在尺度與深度歧義。模型可根據經驗猜測，但猜測不等於量測。可靠系統需加入深度、立體／多視角資訊、相機標定或其他幾何約束。

## Q11 相對位置與公尺座標

「左側」是相對的 semantic spatial relation（語意空間關係），可能只依影像平面判斷；`x = 0.32 m` 是特定座標系、單位與原點下的度量值。若未說明座標系與量測來源，數字本身不可直接用於機器人。

## Q12 VLM Answer 與 Motor Command

自然語言回答可能幻覺、歧義、延遲或缺少即時狀態，也沒有自動滿足關節限制、碰撞檢查、速度限制與緊急停止條件。它最多能成為高階語意候選，仍需結構驗證、Planner（任務規劃器）、Controller（控制器）與獨立安全層處理。

## Q13 Robot Reachability

至少需要 robot pose、關節狀態與限制、工作空間、目標三維位置、相機與機器人座標關係，以及障礙物／碰撞資訊。只有 RGB 時應標為 `Uncertain` 或 `Requires Additional Sensor / Robot State`，不能因回答語氣肯定就標為 Supported。
