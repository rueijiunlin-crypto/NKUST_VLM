# Week06 Demo Guide

## Demo 清單

| Demo | 目的 | 執行 | 預期輸出 | 問題 |
| --- | --- | --- | --- | --- |
| `demo_01_frame_sampling.py` | 觀察 stride sampling | `python demo/demo_01_frame_sampling.py` | 原始與選取 index | 哪些事件可能遺失？ |
| `demo_02_stream_budget.py` | 比較 Camera／Inference FPS | `python demo/demo_02_stream_budget.py` | captured、processed、tokens | 為何不能無限排隊？ |

兩者僅使用標準函式庫、CPU 數秒內完成，無模型或資料下載。
