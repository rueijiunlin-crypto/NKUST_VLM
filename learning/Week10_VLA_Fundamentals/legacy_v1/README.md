# Week10 VLM + ROS2 Topic

## 本週定位

本週把 Week08 的結構化 VLM 結果與 Week09 的相機觀測接入 ROS2 Humble。最小版本使用 `std_msgs/msg/String` 傳送 JSON，建立 publisher（發布者）、subscriber（訂閱者）、Topic 契約與分層診斷流程。

## 文件導覽

- [weekly_plan.md](./weekly_plan.md)：任務、執行順序及驗收條件。
- [notes.md](./notes.md)：ROS2 通訊、訊息契約、QoS 與除錯方法。
- [demo/demo_README.md](./demo/demo_README.md)：契約、發布、訂閱與診斷 Demo。
- [practice/README.md](./practice/README.md)：觀念與 Implementation Practice Mode 練習。
- [study_log.md](./study_log.md)：ROS2 環境、Topic 輸出及問題紀錄。

## 建議使用方式

先在任意 Python 環境執行 contract 與 `--dry-run`，確認 JSON 不依賴 ROS2。真正通訊則切換至 Ubuntu 22.04 + ROS2 Humble 終端機，source 環境後分別啟動 subscriber 與 publisher，再用 ROS2 CLI 獨立觀察 Topic。

## 與碩士研究的關聯

ROS2 Topic 將感知結果從模型實作中解耦，讓導覽、巡檢或操作模組只依賴公開介面。保留觀測識別碼與時間戳後，語意結果也能與原始影像、機器人狀態及實驗紀錄對齊。
