# Week07 Notes：ROS2 + Camera + Realtime VLM

## 1. Realtime Pipeline

Camera 持續發布帶 timestamp 的 frames；sampling／trigger 選擇要推論的觀察；VLM 結果再經 schema、grounding、freshness 與 safety boundary 驗證後發布 semantic topic。

## 2. ROS2 通訊概念

Publisher 發布 message，Subscriber 接收；Topic 是具型別的命名資料流。QoS（服務品質）描述 reliability、history、depth 與 durability。感知影格通常重視新鮮度，不能因可靠排隊而處理大量過期資料。

## 3. Asynchronous Inference

Camera callback 不應被慢速模型長時間阻塞。可將最新 frame 交給 worker；若 worker 忙碌，取代尚未處理的舊 frame，而不是無限堆積。

## 4. Structured Semantic Interface

建議欄位：`observation_id`、`source_timestamp`、`result_timestamp`、`objects`、`relations`、`unknown`、`model_id`、`valid`。Validator 要檢查 syntax、schema、跨欄位語意、grounding 與 freshness。

## 5. Prompt 高價值內容遷移

Prompt Contract 定義任務與輸出；Unknown Policy 防止猜測；Retry Policy 必須有上限；Safety Gate 拒絕把未驗證語意轉成動作。Robot instruction design 與更完整安全界線在 Week10 延伸。

## 6. 系統邊界

ROS2 只負責通訊，不自動保證語意正確或安全。Semantic result 必須與 Planning、Policy、Control、Safety 分離。
