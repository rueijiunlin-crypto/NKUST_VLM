# Week14 Notes：Isaac Sim Robot Learning

## Why 與 Problem

真實機器人資料昂貴且有風險。Isaac Sim 以 OpenUSD（通用場景描述）、物理模擬、RTX 感測器與 ROS2／Python 介面建立可重現環境；但 simulator ground truth、rendering 與 dynamics 仍是近似，不能直接等同真實世界。

## Input、Output 與 Scene Contract

- Scene：USD stage、asset revision、units、physics timestep。
- Robot：articulation、joint limits、controller、initial state。
- Sensor：RGB `[H,W,4]`、depth `[H,W]`、camera intrinsics/extrinsics。
- Output：observation、robot state、action/result、simulation timestamp 與 seed。

## Mechanism 與 Data Flow

```text
SimulationApp
→ open/create USD stage
→ load robot + environment assets
→ configure physics / renderer
→ attach camera / sensors
→ reset with fixed seed
→ step physics
→ render / read observation
→ VLM/VLA or baseline policy
→ validated action
→ articulation controller
→ metric + failure recorder
```

Physics timestep 與 control timestep 必須區分。例如 physics 120 Hz、control 20 Hz，則每次 action 維持 6 physics steps；camera 可能只有 10 Hz。所有訊號需保存 simulation time，不能以 wall-clock 代替。

## Real Isaac Sim Track

使用官方 Isaac Sim Python 環境執行，參數包含 `--headless`、`--renderer`、`--stage`、`--robot-prim`、`--camera-prim`、`--steps`、`--seed` 與 output directory。程式印出 Isaac Sim、driver、GPU、renderer、stage units、sensor shape、step/render time 與 peak GPU memory。

先完成 camera + robot state observation，不直接執行 learned action。若本機未安裝相容 Isaac Sim、driver 或 GPU，保留可讀腳本與 README，狀態標記 `Not validated yet`。

## Synthetic Data 與 Domain Randomization

可隨機化 lighting、texture、camera pose、object pose、sensor noise、mass 與 friction；每個變因需有範圍、分布與 seed。隨機化太寬可能破壞任務語意，太窄則無法涵蓋 reality gap。Replicator metadata 應保存生成設定與 asset provenance。

## Metric、Failure 與 Limitation

- USD asset scale 或 joint axis 錯誤。
- Camera prim path、render product 或 sensor initialization 失敗。
- Headless 與 GUI renderer 結果／效能不同。
- Physics instability、穿透、reset 不完整。
- Simulator ground truth 被誤當成 real sensor output。
- Isaac Sim／Isaac Lab API 版本變動。

量測 simulation steps/s、render latency、sensor freshness、task success、collision、timeout 與 seed variance。

## Demo 與 Paper Mapping

- Basic Demo：mock scene/task schema。
- Real Track：官方環境載入 scene、robot、RGB sensor 與 state。
- Core Paper：Isaac Lab，對應 GPU parallel simulation、sensor/task interface 與 reproducibility。

## 本週尚未涵蓋

不宣稱 sim policy 可直接部署；Week15 才以 paired evidence 量測 sim-to-real gap。
