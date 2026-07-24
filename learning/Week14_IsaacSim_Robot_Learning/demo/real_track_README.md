# Week14 Real Isaac Sim Track

- Status：Not validated yet；必須在官方 Isaac Sim Python 環境執行。
- Entry：使用 Isaac Sim launcher 執行 `demo/demo_03_real_isaac_observation.py --headless`；`--stage` 為可選自訂場景。
- Environment：腳本 target Isaac Sim 5.1.0 Camera API；NVIDIA driver、GPU、renderer 與 Python 必須依官方 compatibility 文件成套安裝。
- Asset：預設由官方 assets root 載入 Franka 並建立 ground/camera/target/light；自訂 stage 需含指定 articulation 與 camera prim。
- Output：RGB/depth、joint state、camera/target pose、physics/render dt、steps/s；不執行 learned action。
- Troubleshooting：prim path、API namespace、driver/renderer、headless sensor 初始化是首要檢查點。

## 版本、授權與執行證據

- Required：完整 default scene 與 observation/ground-truth 對照為必修；未安裝可標 Environment blocked。
- Official sources：[Isaac Sim quickstart](https://docs.isaacsim.omniverse.nvidia.com/latest/introduction/quickstart_isaacsim_robot.html)、[Isaac Sim 5.1 Camera API](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/sensors/isaacsim_sensors_camera.html)。
- Download：Isaac Sim 與 assets 為多 GB；依 NVIDIA 安裝方式與 asset cache 實際值記錄。
- License / Auth：依 NVIDIA Omniverse/Isaac Sim 與各 USD asset 條款；assets/Nucleus 可能需要網路或帳號。
- Hardware：NVIDIA RTX GPU、相容 driver 與足夠 VRAM/RAM/disk；不提供不實最低值，依官方 compatibility 文件記錄實機。
- Target versions — verify before execution：Isaac Sim 5.1.0；本機未安裝。GPU driver/VRAM/System RAM/CUDA 依 5.1 compatibility 文件與實際 renderer 記錄。
- dtype / Quantization / Cache：模型 dtype/quantization 不適用；使用 Isaac asset/cache，記錄資產來源與 cache blocker。
- Migration：Isaac Sim 6.0 camera API 已遷移到 experimental RTX namespace，不把 5.1 執行結果直接套用到 6.0。

```powershell
<ISAAC_SIM>\python.bat demo/demo_03_real_isaac_observation.py --headless
<ISAAC_SIM>\python.bat demo/demo_03_real_isaac_observation.py --stage <usd> --headless
```

保存 Isaac/Kit version、GPU/driver、renderer、headless、asset/stage revision、seed、RGB/depth/state shape、poses、dt、steps/s 與 error log。此路線只觀察、不控制。
