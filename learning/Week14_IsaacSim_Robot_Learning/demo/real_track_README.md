# Week14 Real Isaac Sim Track

- Status：Not validated yet；必須在官方 Isaac Sim Python 環境執行。
- Entry：`python demo/demo_03_real_isaac_observation.py --stage <usd> --robot-prim /World/Robot --camera-prim /World/Camera --headless`
- Environment：Isaac Sim 版本、NVIDIA driver、GPU、renderer 與 Python 必須依官方 compatibility 文件成套安裝。
- Asset：stage 必須含指定 articulation 與 camera prim；保存 USD/asset revision 與 license。
- Output：camera RGBA shape、joint-state shape、steps/s；不執行 learned action。
- Troubleshooting：prim path、API namespace、driver/renderer、headless sensor 初始化是首要檢查點。
