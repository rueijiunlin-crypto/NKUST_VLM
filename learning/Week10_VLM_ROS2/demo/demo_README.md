# Week10 Demo Guide

## 環境

- Target OS：Ubuntu 22.04。
- ROS2 distribution：Humble。
- Python packages：`rclpy`、`std_msgs` 由 ROS2 安裝提供，不以 pip 安裝。
- Model / data download：無；範例使用固定語意結果。
- GPU：不需要。

每個 ROS2 終端機先執行：

```bash
source /opt/ros/humble/setup.bash
printenv ROS_DISTRO
```

預期 `ROS_DISTRO` 為 `humble`。若使用 overlay workspace（疊加工作區），再 source 該工作區的 `install/setup.bash`。

## Demo 清單

| Demo | 對應概念 | 執行方式 | 觀察重點 |
|---|---|---|---|
| `demo_01_topic_contract.py` | Topic 與 JSON 契約 | `python3 demo/demo_01_topic_contract.py` | 名稱、型別、depth、必要欄位 |
| `demo_02_semantic_publisher.py` | publisher/timer | `python3 demo/demo_02_semantic_publisher.py --dry-run` | 序列化結果 |
| `demo_03_semantic_subscriber.py` | subscriber/validation | `python3 demo/demo_03_semantic_subscriber.py --dry-run` | 解析與跨欄位檢查 |
| `demo_04_topic_diagnostics.py` | 分層除錯 | `python3 demo/demo_04_topic_diagnostics.py` | CLI 檢查順序 |

前三個 local/dry-run 可在非 ROS 環境驗證，但不能算 ROS2 通訊完成。

## 真正 ROS2 通訊

終端機 A：

```bash
source /opt/ros/humble/setup.bash
python3 demo/demo_03_semantic_subscriber.py
```

終端機 B：

```bash
source /opt/ros/humble/setup.bash
python3 demo/demo_02_semantic_publisher.py --interval 2
```

終端機 C：

```bash
source /opt/ros/humble/setup.bash
ros2 topic info /vlm/semantic_description -v
ros2 topic echo /vlm/semantic_description
ros2 topic hz /vlm/semantic_description
```

## 預期輸出與問題

- Publisher：每兩秒記錄一個新的 `observation_id`。
- Subscriber：記錄通過驗證的識別碼與答案。
- `topic info`：型別應為 `std_msgs/msg/String`，且能看到 publisher/subscriber endpoint（端點）。
- `topic hz`：頻率應接近 0.5 Hz，受排程影響可能略有差異。

執行後應回答：

1. 為何每次發布要產生新 observation ID？
2. Topic 型別吻合時，subscriber 還需驗證哪些 JSON 規則？
3. 若 node list 有節點但 topic echo 無資料，下一步檢查什麼？

## 常見錯誤

- `ModuleNotFoundError: rclpy`：未 source ROS2，或使用了不相容 Python。
- Topic 看不到：兩端環境、Domain ID 或 discovery 設定不一致。
- 型別不符：Topic 名稱相同但訊息型別不同。
- JSON parse error：publisher 發布了非 JSON 字串或截斷內容。
- 頻率不符：timer interval、CPU 負載或 executor 阻塞。

## 與 VLM/VLA 研究的關係

Topic 契約使 VLM 感知、相機、導覽與紀錄模組能獨立演進。下游以 observation ID 和時間戳確認結果來源與新鮮度，降低使用錯誤語意決策的風險。

