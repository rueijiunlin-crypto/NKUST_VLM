# Week10 Coding Practice Record

## 練習清單

| 練習 | 模式 | 對應檔案 | 目標 |
|---|---|---|---|
| Semantic Topic | Implementation Practice Mode | `exercises/semantic_topic_practice.py` | 完成可驗證 ROS2 語意通訊 |

## TODO

1. `build_payload`：建立 Week08 相容結果，包含 UUID 與 UTC 時間。
2. `validate_payload`：檢查必要欄位、enum（列舉值）與跨欄位規則。
3. `run_publisher`：建立 timer、序列化 JSON、發布 `String` 並安全清理。
4. `run_subscriber`：解析、驗證、記錄合法與不合法訊息並安全清理。

## 學生觀察

| 測試 | 是否執行 | 結果／頻率 | 觀察 |
|---|---|---|---|
| publisher dry-run |  |  |  |
| publisher + subscriber |  |  |  |
| topic echo |  |  |  |
| invalid JSON/schema |  |  |  |

## 錯誤紀錄

| 錯誤 | 診斷層 | 修正方式 |
|---|---|---|
|  |  |  |

## 自我檢查

* [ ] ROS2 import 放在實際 ROS 執行路徑，dry-run 可獨立驗證 schema
* [ ] Publisher 每次建立可追蹤 payload
* [ ] Subscriber 不信任未驗證字串
* [ ] `KeyboardInterrupt` 後 Node 與 rclpy 正確清理
* [ ] 我使用 CLI 獨立驗證 Topic 型別、內容與頻率
* [ ] 我沒有把 dry-run 記為 ROS2 通訊完成

