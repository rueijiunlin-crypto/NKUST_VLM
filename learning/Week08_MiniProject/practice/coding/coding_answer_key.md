# Week08 Coding Answer Key

> 請先完成 `exercises/` 中的練習檔案，再查看本程式練習參考說明。

## TODO 1：`validate_request`

先確認 `task` 在允許集合中，再處理跨欄位規則：VQA 的 `question` 必須是非空字串，Caption 則不需要問題。非 dry-run 還要確認影像是實際檔案。驗證應先於模型載入，避免用昂貴推論回報可預先發現的錯誤。

## TODO 2：`run_model`

Caption 使用 `BlipForConditionalGeneration`，VQA 使用 `BlipForQuestionAnswering`。`BlipProcessor` 會產生 batched tensor；將每個 tensor 移至與模型相同的 `device`，再呼叫 `generate()` 與 `decode()`。常見錯誤包括模型類別用錯、CPU/GPU 混用，以及把 Token ID 當成可直接閱讀的答案。

## TODO 3：`build_result`

用 UUID 建立唯一觀測識別碼，用含時區的 UTC 時間建立 `timestamp_utc`，再填入固定 schema 欄位。Caption 的 `question` 應為 `None`，序列化後會成為 JSON `null`。

## Shape 與除錯重點

- `pixel_values` 通常為 `[batch, channels, height, width]`，不要誤認成 OpenCV 的 `[height, width, channels]`。
- VQA 另有 `input_ids` 與 `attention_mask`，長度會隨問題而變。
- 若看到裝置不一致錯誤，檢查模型及所有 processor 輸出，而不只 `pixel_values`。
- 若下載失敗，先確認連線、模型快取與磁碟容量，不要把環境錯誤記為模型回答 `unknown`。

