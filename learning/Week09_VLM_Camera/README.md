# Week09 VLM + Camera

## 本週定位

本週把 Week08 的本機影像輸入改成 OpenCV（開源電腦視覺函式庫）相機影格，建立「擷取、驗證、保存、交接」的可追蹤資料流。實體相機是正式驗收路徑；合成影像只用於無硬體時的程式測試。

## 文件導覽

- [weekly_plan.md](./weekly_plan.md)：學習任務與驗收條件。
- [notes.md](./notes.md)：影格格式、顏色空間、相機生命週期與取樣策略。
- [demo/demo_README.md](./demo/demo_README.md)：四個相機資料流 Demo。
- [practice/README.md](./practice/README.md)：觀念與實作練習入口。
- [study_log.md](./study_log.md)：實際相機資訊、輸出與問題紀錄。

## 建議使用方式

先以 `--synthetic` 驗證環境與檔案輸出，再接上實體相機完成硬體驗收。保存一張 snapshot（快照）後，產生與 Week08 相容的 handoff（交接）JSON，最後才交給 VLM 推論，避免把相機錯誤誤判為模型錯誤。

## 與碩士研究的關聯

相機是室內語意導覽、災害巡檢及桌面操作的主要觀測來源。本週加入時間戳、影格尺寸、顏色空間與來源路徑，使視覺結果可與後續 ROS2 訊息及機器人狀態對齊。
