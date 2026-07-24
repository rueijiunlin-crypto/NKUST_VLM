# Week07 Coding Observation Key

> 請先執行 `guided_demos/guided_async_flow.py` 並完成自己的觀察紀錄，再查看本說明。

## 觀察方向

- producer 與 consumer 的頻率不同時，queue 會累積舊 frame。
- `max_queue` 限制的是等待處理的資料量；它不能單獨保證輸出新鮮。
- 即時機器人流程應同時記錄 capture、inference 與 publish timestamp，才能分辨延遲來源。
- 當最新觀測比舊觀測更有決策價值時，丟棄過期 frame 通常比逐張補算更合理。

## 常見誤解

- 「平均 FPS 足夠」不等於每次輸出都符合 latency budget（延遲預算）。
- queue 沒有爆滿不代表資料沒有過期。
- ROS2 message timestamp 應描述資料取得時間，不應一律以 publish 時間取代。
