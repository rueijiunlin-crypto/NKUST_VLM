# Week14 Isaac Sim Robot Learning

本週把 Isaac Sim 定位為受控 Robot Learning Simulation（機器人學習模擬）：

```text
Isaac Sim → Scene → Robot → RGB / Depth → Robot State
→ Task → Policy → Evaluation
```

Basic Demo 驗證 experiment config 與 synthetic ground truth，不要求本機已安裝 Isaac Sim。舊占位內容在 `legacy_v1/`。

## 與前週銜接、本週目標與資料流

Week13 產生可重新載入的 policy checkpoint；本週先建立可重現的 simulator observation，不執行 learned action。Required Real Track 預設建立 ground、Franka、RGB/depth camera、target 與 light，也保留 `--stage` 自訂 USD。

## 文件、Demo、Practice 與 Paper

依序使用 `weekly_plan.md`、`notes.md`、Basic Demo、`demo_03_real_isaac_observation.py` 與 `practice/README.md`。需分別記錄 Sensor Observation（RGB/depth/joint state）與 Simulator Ground Truth（camera/target pose、simulation timestep）。論文驗收需說明 simulator setup、asset revision、randomization、metric、seed 與至少一個 scene/domain ablation。

## Hardware Requirements / Environment / Download / Assets / Run

本教材的實際腳本鎖定 Isaac Sim 5.1.0 穩定 Camera API；需 NVIDIA GPU、相容 driver、Isaac Sim Python launcher 與可用官方 assets root。Windows 用 Isaac Sim 的 `python.bat`，Linux 用 `./python.sh`，不是一般 venv Python。Isaac Sim 6.0 將 camera namespace 遷移到 experimental RTX API，升級時必須另做 migration validation。

## Troubleshooting / Research Boundary

優先檢查 launcher、driver／renderer、assets/Nucleus 存取、prim path、headless sensor initialization 與相機是否產生有效 depth。此 Demo 只觀察、不控制；simulation ground truth 也不等於 real-world truth。Week15 會將這組 sim observation 與真實 camera observation 成對比較，支援 sim-to-real 論文分析。
