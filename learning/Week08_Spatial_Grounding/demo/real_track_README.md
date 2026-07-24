# Week08 Geometry Track

- Entry：`python demo/demo_02_pixel_to_3d.py`
- Requirement：`numpy>=1.24,<3`。
- 驗證：以已知 `K`、depth、`T_robot_camera` 逐步檢查 pixel→camera→robot，保存矩陣 shape、單位與重投影誤差。
- 真實相機：需另存 intrinsics/extrinsics revision、depth scale、RGB-depth alignment 與 calibration residual。
- Failure：毫米／公尺、矩陣方向、row/column vector、無效 depth。

## Required Track Metadata

- Status：Basic geometry 可離線執行；真實相機 runtime 為 `Not validated yet`。
- Required：幾何驗證是必修；真實相機若缺硬體可標 Hardware blocked，但需完成 calibration 計畫。
- Model / Framework：無大型模型；NumPy pin 於 `requirements.txt`。
- Source / Revision：真實資料需記錄 camera SDK、firmware、intrinsics/extrinsics 與 dataset revision。
- Download / License / Auth：mock data 無下載；相機錄影或 dataset 依原始來源條款，通常不需模型登入。
- Hardware：CPU/RAM 即可；真實 track 需要 RGB-D camera 或已授權錄影。
- Cache：不需要模型 cache；校正檔與測試素材需以可追蹤但不洩漏資料的方式保存。
- Target versions — verify before execution：Python 3.10/3.11、NumPy 1.24–2.x；真實 camera SDK 依硬體另 pin。
- VRAM / System RAM / CUDA / dtype / quantization：GPU/CUDA/quantization 不適用；一般 RAM 即可，幾何運算 dtype 與 unit 必須記錄。

預期證據包含 input pixel/depth、`K`、`T_robot_camera`、shape、dtype、unit、camera/robot XYZ 與 reprojection error。invalid depth、scale 或 transform 方向不明時必須拒絕輸出，不得以語意描述代替幾何量測。
