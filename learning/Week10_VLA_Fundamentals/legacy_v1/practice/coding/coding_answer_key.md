# Week10 Coding Answer Key

> 請先完成 `exercises/` 中的練習檔案，再查看本程式練習參考說明。

## TODO 1：payload

沿用 Week08 九個欄位，UUID 與 UTC 時間每次發布重新產生。`String.data` 只能放字串，因此最後需 `json.dumps()`；不要直接把 Python dictionary 指派給它。

## TODO 2：驗證

先找缺少欄位，再限制 `task` 與 `status`，最後檢查 VQA 問題及成功結果答案等跨欄位規則。Token ID 與 embedding（嵌入向量）不應出現在這個語意 Topic；這裡傳遞的是已解碼結果與追蹤 metadata。

## TODO 3：publisher

在函式內匯入 ROS2，建立 Node、`String` publisher 與 timer。Callback 建 payload、驗證、序列化再發布。主迴圈以 `try/finally` 保證 `destroy_node()` 與 `shutdown()`。

## TODO 4：subscriber

Callback 先 `json.loads()` 並確認最外層是 dictionary，再呼叫共同驗證器。捕捉解析及規則錯誤並記錄，但不要讓一筆壞訊息終止整個 Node。

## 常見錯誤

- 忘記 source ROS2，誤以為應使用 pip 安裝 `rclpy`。
- Publisher 和 subscriber Topic 名稱或型別不同。
- 將 JSON 字串雙重編碼，subscriber 解析後仍得到字串。
- 只檢查欄位存在，未檢查 VQA 問題、`status` 與答案關係。
- Callback 執行重型 VLM 推論，阻塞 executor；正式系統應拆分 Node 或使用適合的 executor 設計。

