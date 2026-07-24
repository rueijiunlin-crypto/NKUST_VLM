# Week07 Real ROS2 Track

- Status：Node source added；Not validated yet on a ROS2 camera host。
- Entry：`python demo/demo_03_real_ros2_semantic_node.py --ros-args -p image_topic:=/camera/image_raw`
- Environment：Ubuntu + ROS2 Humble/Jazzy、`rclpy`、`sensor_msgs`、`cv_bridge`、OpenCV；ROS 套件由系統安裝，不列入 pip requirements。
- Pipeline：camera→capacity-1 subscription→RGB conversion→semantic JSON topic；範例 adapter 預設回報 `unknown`，不偽造模型結果。
- Hardware：相機可先由 rosbag 取代；確認 image encoding、QoS、timestamp 與 p95 latency。
- Safety：只發布語意 topic，不發布 motor command。
