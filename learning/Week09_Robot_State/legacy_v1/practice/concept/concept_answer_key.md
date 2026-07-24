# Week09 Concept Answer Key

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

## 題目 1

OpenCV 彩色影格一般為 HWC、BGR、`uint8`；模型張量常為 BCHW、RGB、浮點數，並完成縮放或正規化。Processor 可能處理維度與數值轉換，但呼叫者仍需確認它期望 RGB 或 BGR。常見誤解是 shape 正確就代表語意也正確。

## 題目 2

先用 `isOpened()` 確認裝置，接著檢查 `read()` 的布林值與 frame，再檢查 shape/dtype，保存時檢查 `imwrite()`，重新解碼快照後才交給 VLM。如此每一層都有獨立證據，不會把裝置故障誤記為模型錯誤。

## 題目 3

模型處理速度只有 0.5 FPS，若把 30 FPS 全部排隊，延遲會持續增長。可固定每兩秒取一幀，或讓擷取端持續覆蓋單一 latest-frame buffer（最新影格緩衝），推論端有空時只取最新值。

