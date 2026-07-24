# Week07 Real ROS2 Track

- Status：Node source added；Not validated yet on a ROS2 camera host。
- Entry：`python demo/demo_03_real_ros2_semantic_node.py --ros-args -p image_topic:=/camera/image_raw`
- Environment：Ubuntu + ROS2 Humble/Jazzy、`rclpy`、`sensor_msgs`、`cv_bridge`、OpenCV；ROS 套件由系統安裝，不列入 pip requirements。
- Pipeline：camera→capacity-1 latest-frame buffer→worker→real Qwen2.5-VL adapter→validated semantic JSON topic。
- Hardware：相機可先由 rosbag 取代；確認 image encoding、QoS、timestamp 與 p95 latency。
- Safety：只發布語意 topic，不發布 motor command。

## 模型、版本與執行證據

- Required：必修學習路線；若 ROS／相機／模型環境缺失，保留 Environment 或 Hardware blocked 證據。
- Model：`Qwen/Qwen2.5-VL-3B-Instruct`；[官方 model card](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)，執行時以 ROS parameter `model_revision` pin commit。
- Download / License / Auth：權重約數 GB 級，實際依 revision；依 model card 條款，公開權重通常不需登入。
- Target：ROS2 Humble/Jazzy、Python/ABI 與 `cv_bridge` 必須一致；ML 環境見 `requirements_real.txt`。建議 CUDA GPU 與 12 GB 以上 VRAM。
- Cache：Hugging Face cache；不得提交權重或 access token。
- Target versions — verify before execution：ROS2 Humble/Jazzy、PyTorch 2.2+、Transformers 4.49+；需在同一 ABI 組合實機確認。
- System RAM / CUDA / dtype / quantization：建議 16–32 GB RAM、相容 CUDA、float16/bfloat16；預設不量化，任何量化須另存設定。

```bash
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_ros2_semantic_node.py --ros-args \
  -p image_topic:=/camera/image_raw -p model_revision:=<commit>
```

保存 ROS distro、camera/rosbag、topic/QoS、model/revision、GPU/driver/CUDA、dtype、image age、queue replacement count、load/inference/publish latency、JSON parse/schema result、peak VRAM 與 failure log。常見問題依序檢查 encoding、QoS、timestamp、ROS/ML ABI、OOM 與模型存取；structured semantic result 不得接 motor controller。
