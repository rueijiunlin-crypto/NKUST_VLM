# Week10 Real VLA Inspection Track

- Status：config-only；執行時只下載 `lerobot/smolvla_base` 的 `config.json`。
- Entry：`python demo/demo_03_real_vla_inspection.py --revision <immutable-revision>`
- Requirement：`huggingface-hub>=0.28`。
- Model：SmolVLA 約 450M；model card 與 code 分別受其聲明授權約束。
- 驗證：config、processor/interface、camera/state/action features、chunk size、revision、cache。
- Troubleshooting：若 config key 隨 LeRobot 版本改名，保留完整 config 並標記差異，不猜測缺失欄位。
