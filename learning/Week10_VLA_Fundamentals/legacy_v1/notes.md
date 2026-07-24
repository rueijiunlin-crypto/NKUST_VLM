# Week10 Notes：VLM + ROS2 Topic

## 1. 為什麼使用 Topic

ROS2 Topic 適合持續、非同步傳遞資料。VLM Node 負責產生語意結果，下游導覽或紀錄 Node 負責消費結果，雙方不必知道彼此內部模型或程式：

```text
Week09 camera observation
          ↓
Week08 VLM inference
          ↓
publisher node
          ↓ /vlm/semantic_description
subscriber node
          ↓
navigation / logging / inspection
```

Topic 適合資料流；若工作需要明確請求與單次回應，可評估 service（服務）；若工作長時間執行且需回饋與取消，可評估 action（動作）。

## 2. 三層通訊契約

本週先固定：

1. Topic name：`/vlm/semantic_description`
2. ROS message type：`std_msgs/msg/String`
3. JSON schema：沿用 Week08 九個必要欄位

`String` 便於學習與快速檢查，但編譯期無法驗證 JSON 欄位。因此 subscriber 必須解析 JSON、檢查必填欄位與跨欄位規則。正式研究介面穩定後，可建立 custom interface（自訂介面）以提供型別安全。

對應 Demo：`demo/demo_01_topic_contract.py`。執行後應能回答：Topic 型別正確是否代表 JSON 內容也正確？

## 3. `rclpy` publisher

Publisher Node 以 `create_publisher(String, topic, 10)` 建立發布端，用 timer（計時器）定期觸發 callback。callback 產生 Week08 結果、序列化成 JSON，放入 `String.data` 再發布。

`demo/demo_02_semantic_publisher.py --dry-run` 只驗證 payload，不匯入 ROS2；移除 `--dry-run` 才會進入真正的 ROS2 executor（執行器）。這個邊界讓 schema 可在非 ROS 環境測試。

## 4. subscriber 與防禦性驗證

Subscriber callback 收到 `String` 後依序：

1. `json.loads()`。
2. 確認最外層是 object。
3. 檢查必要欄位。
4. 驗證 `task`、`status` 與跨欄位規則。
5. 合法才交給下游使用。

對應 Demo：`demo/demo_03_semantic_subscriber.py`。

- 預期：dry-run 印出合法結果；不合法內容應回報解析或 schema 錯誤。
- 問題：為何不能讓導覽 Node 直接相信 `answer` 字串？

## 5. QoS 與新鮮度

範例中的 `10` 是 history queue depth（歷史佇列深度）的簡寫設定之一，不是「一定保存十筆到永遠」，也不保證慢速 subscriber 應逐一處理所有舊結果。機器人語意感知通常重視最新狀態；進入正式設計時應依可靠度、耐久性與新鮮度需求選擇 QoS profile。

若下游只需最新語意，還應比較訊息 `timestamp_utc` 或序號，避免把過時結果用於現在的機器人決策。

## 6. 分層診斷

`demo/demo_04_topic_diagnostics.py` 列出建議順序：

1. 確認 `ROS_DISTRO`。
2. 確認 Node discovery（節點探索）。
3. 確認 Topic discovery。
4. 確認 Topic 型別與端點資訊。
5. `echo` 檢查內容。
6. `hz` 檢查頻率。

如果 Topic 看不到，先檢查環境與 discovery，而不是先修改 JSON schema。官方入門教材與 `rclpy` 介面可參考：

- [ROS2 Humble Beginner client libraries](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)
- [ROS2 Humble rclpy documentation](https://docs.ros.org/en/humble/p/rclpy/index.html)

## 7. 環境邊界

本專案目標環境為 Ubuntu 22.04、ROS2 Humble。`rclpy` 與 `std_msgs` 應由 ROS2 系統環境提供，而不是寫入一般 pip requirements。每個新終端機先執行：

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
```

避免用與 ROS2 binary 不相容的獨立 Python 環境。若後續改成正式 ROS2 package，還需加入 `package.xml`、setup metadata 與 colcon 工作區；本週先用獨立腳本聚焦通訊概念。

## 本週尚未涵蓋

- ROS2 custom message 與 interface package。
- `sensor_msgs/Image`、`cv_bridge` 與影像 Topic。
- 跨主機 DDS（資料分散服務）設定、安全性及正式 QoS 實驗。

