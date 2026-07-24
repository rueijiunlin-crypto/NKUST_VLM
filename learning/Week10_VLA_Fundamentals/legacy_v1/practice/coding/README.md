# Week10 Coding Practice

## 模式與目標

本週採 Implementation Practice Mode。請完成 `exercises/semantic_topic_practice.py` 的 payload 建構、驗證、publisher 與 subscriber 四個 TODO。

## 環境

程式需求由 ROS2 Humble 安裝提供，`requirements.txt` 不列 pip 套件。Ubuntu 22.04 終端機應先：

```bash
source /opt/ros/humble/setup.bash
```

不需模型、資料下載或 GPU。系統限制與常見錯誤見 [Demo Guide](../../demo/demo_README.md)。

## 執行

完成前兩個 TODO 後先 dry-run：

```bash
python3 practice/coding/exercises/semantic_topic_practice.py --mode publisher --dry-run
```

完成全部 TODO 後在兩個 ROS2 終端機執行：

```bash
python3 practice/coding/exercises/semantic_topic_practice.py --mode subscriber
python3 practice/coding/exercises/semantic_topic_practice.py --mode publisher --interval 2
```

詳細任務與紀錄欄位見 [coding_practice.md](./coding_practice.md)。

