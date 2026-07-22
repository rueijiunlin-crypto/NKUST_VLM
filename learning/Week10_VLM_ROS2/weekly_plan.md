# Week10 Weekly Plan

## 本週目標

- 理解 ROS2 Node、publisher、subscriber 與 Topic 的資料流。
- 以固定 Topic 名稱和 JSON schema 發布 Week08 VLM 結果。
- 在 subscriber 解析並驗證訊息，而非盲目信任字串。
- 使用 ROS2 CLI 分層檢查環境、節點、Topic、型別、內容與頻率。

## 必學概念

- `rclpy`、`std_msgs/msg/String` 與 callback（回呼函式）。
- Topic 名稱、訊息型別與 schema 是不同層次的契約。
- QoS depth（佇列深度）與語意結果新鮮度。
- Node 清理、`rclpy.shutdown()` 與例外處理。

## 建議學習順序

1. 閱讀 README.md 與 notes.md。
2. 執行 Topic 契約、publisher dry-run、subscriber dry-run 與診斷清單。
3. 在 ROS2 Humble 環境 source `/opt/ros/humble/setup.bash`。
4. 分別啟動 subscriber、publisher 與 `ros2 topic echo`。
5. 注入不合法 JSON，觀察 subscriber 如何拒絕。
6. 完成 Implementation Practice Mode 並保存終端機證據。

## Demo 執行順序

1. `python3 demo/demo_01_topic_contract.py`
2. `python3 demo/demo_02_semantic_publisher.py --dry-run`
3. `python3 demo/demo_03_semantic_subscriber.py --dry-run`
4. `python3 demo/demo_04_topic_diagnostics.py`
5. `python3 demo/demo_03_semantic_subscriber.py`（ROS2 終端機 A）
6. `python3 demo/demo_02_semantic_publisher.py`（ROS2 終端機 B）

完整環境與觀察方式見 [demo/demo_README.md](./demo/demo_README.md)。

## Practice 順序

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)（Implementation Practice Mode）

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)
- [Coding Answer Key](./practice/coding/coding_answer_key.md)
- [Coding Solutions](./practice/coding/solutions/)

## 任務清單

* [ ] 閱讀本週文件
* [ ] 執行四個不需 ROS2 通訊的契約／dry-run Demo
* [ ] 在 ROS2 Humble 執行 publisher 與 subscriber
* [ ] 使用 `ros2 topic info`、`echo` 與 `hz` 保存證據
* [ ] 完成 Concept Practice
* [ ] 完成 Coding Practice 中的 TODO
* [ ] 在 study_log.md 記錄實際結果與錯誤
* [ ] 更新 Notion 並進行 ChatGPT 驗收

## 驗收條件

* [ ] 能畫出 publisher → Topic → subscriber 資料流
* [ ] `/vlm/semantic_description` 型別為 `std_msgs/msg/String`
* [ ] subscriber 能接收合法訊息並拒絕不合法 JSON/schema
* [ ] CLI 可觀察 Topic 型別、內容與發布頻率
* [ ] 能說明 depth 10 並不保證處理到每一筆舊語意結果
* [ ] study_log.md 含 ROS_DISTRO、節點清單、Topic 證據及問題修正
* [ ] ChatGPT 驗收 Pass

