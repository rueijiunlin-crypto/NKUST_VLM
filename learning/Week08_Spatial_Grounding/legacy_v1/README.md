# Week08 Mini VLM Project

## 本週定位

本週把前七週的模型、推論與提示設計知識整合成一個可操作的 Mini Project（迷你專案）：輸入本機影像，執行 Image Captioning（影像描述）或 Visual Question Answering（視覺問答），並輸出結構一致、可驗證的 JSON 結果。

## 文件導覽

- [weekly_plan.md](./weekly_plan.md)：學習順序、任務與驗收條件。
- [notes.md](./notes.md)：系統邊界、BLIP（Bootstrapping Language-Image Pre-training，語言影像預訓練）與資料契約。
- [demo/demo_README.md](./demo/demo_README.md)：四個快速展示用 Demo。
- [practice/README.md](./practice/README.md)：觀念與程式練習入口。
- [study_log.md](./study_log.md)：由學習者記錄實際輸出、問題與理解。

## 建議使用方式

1. 依 [weekly_plan.md](./weekly_plan.md) 閱讀必要概念。
2. 先執行不需下載模型的資料契約與驗證 Demo。
3. 準備自有圖片，再依環境能力執行 BLIP Caption 與 VQA Demo。
4. 完成 [practice/README.md](./practice/README.md) 中的 Implementation Practice Mode（實作練習模式）。
5. 將真實執行結果與尚未解決的問題寫入 [study_log.md](./study_log.md)。

## 與碩士研究的關聯

本週建立的 `observation_id`、時間戳、任務、狀態與答案欄位，會成為 Week09 相機輸入及 Week10 ROS2（機器人作業系統第二版）Topic 整合的共同介面。研究原型若先固定資料契約，之後更換模型或感測器時較容易重現實驗並定位錯誤。
