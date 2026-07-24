# Week15 Camera vs Simulation Track

- Entry：`python demo/demo_03_camera_sim_comparison.py --real <image> --sim <image> --output metrics.json`
- Requirements：`numpy>=1.24,<3`、`opencv-python>=4.9`。
- Input：同一 scene/test case 的 real camera 或錄影 frame，以及 Isaac Sim RGB frame。
- Output：shape、RGB mean/std、brightness、noise proxy、elapsed time；不可把這些 proxy 單獨解讀成 task success。
- Reproducibility：保存 camera/Isaac revision、calibration、prompt/model revision 與 paired-case ID。
