# Week07 Demo Guide

| Demo | 目的 | 指令 | 觀察 | 問題 |
| --- | --- | --- | --- | --- |
| Queue | 非同步 latest-frame policy | `python demo/demo_01_realtime_queue.py` | replaced／processed | 為何不能無限排隊？ |
| Interface | Structured result + freshness | `python demo/demo_02_semantic_interface.py` | publish／reject | JSON 合法為何仍可能錯？ |

皆為標準函式庫 CPU Demo，不需 ROS2；真實 publisher／subscriber 留給具 ROS2 環境的後續實驗。
