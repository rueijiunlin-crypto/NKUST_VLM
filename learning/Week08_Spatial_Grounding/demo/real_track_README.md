# Week08 Geometry Track

- Entry：`python demo/demo_02_pixel_to_3d.py`
- Requirement：`numpy>=1.24,<3`。
- 驗證：以已知 `K`、depth、`T_robot_camera` 逐步檢查 pixel→camera→robot，保存矩陣 shape、單位與重投影誤差。
- 真實相機：需另存 intrinsics/extrinsics revision、depth scale、RGB-depth alignment 與 calibration residual。
- Failure：毫米／公尺、矩陣方向、row/column vector、無效 depth。
