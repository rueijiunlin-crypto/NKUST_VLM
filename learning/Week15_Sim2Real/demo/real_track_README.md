# Week15 Camera vs Simulation Track

- Entry：`python demo/demo_03_camera_sim_comparison.py --real <image> --sim <image> --output metrics.json`
- Requirements：`numpy>=1.24,<3`、`opencv-python>=4.9`。
- Input：同一 scene/test case 的 real camera 或錄影 frame，以及 Isaac Sim RGB frame。
- Output：shape、RGB mean/std、brightness、noise proxy、elapsed time；不可把這些 proxy 單獨解讀成 task success。
- Reproducibility：保存 camera/Isaac revision、calibration、prompt/model revision 與 paired-case ID。

## 執行契約與資料治理

- Required：Simulation Observation 與 Real Observation 成對比較必修；缺真實硬體可標 Hardware blocked，但需完成採集 schema。
- Model / Framework：無模型下載；NumPy/OpenCV 版本 pin 於 requirements。
- Source / Revision：保存 Isaac/scene/asset revision、camera/firmware/calibration revision、paired case ID、capture timestamp。
- Download / License / Auth：輸入影像由使用者合法取得；無模型登入。受限 real data 不提交 Git。
- Hardware：分析 CPU 可執行；real capture 需要已安全架設 camera/robot，GPU 非必要。
- Cache：輸出 `metrics.json` 與 raw artifact manifest；圖片位置需符合資料治理規範。
- Target versions — verify before execution：NumPy 1.24–2.x、OpenCV 4.9+；camera SDK 另 pin，本機未做 real capture。
- VRAM / System RAM / CUDA / dtype / quantization：GPU/CUDA/quantization 非必要；一般 RAM，影像 dtype/color order 由程式與 artifact 記錄。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_camera_sim_comparison.py --real <real.png> --sim <sim.png> --output metrics.json
```

保存 shape/color order、mean/std/brightness/noise proxy、elapsed、normalization、calibration 與 failure。proxy 差異不是 task success；任何 hardware action 都不在此腳本範圍。
