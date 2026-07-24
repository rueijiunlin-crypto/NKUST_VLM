# Week13 VLA Fine-tuning

## LeRobot Compatibility

- Target LeRobot version：`>=0.6,<0.7`（穩定目標為 `0.6.0`）。
- Python：`>=3.12`。
- Dataset format：LeRobotDataset v3.x。
- Official documentation source：[LeRobot 0.6.0 release](https://github.com/huggingface/lerobot/releases/tag/v0.6.0)、[`lerobot-train` v0.6.0 source](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/scripts/lerobot_train.py)。
- API status：已依穩定 CLI schema 稽核 dataset revision、policy revision、`policy.optimizer_lr`、checkpoint 與 reload 流程；GPU 訓練仍為 Environment blocked。
- Reproducibility：正式實驗必須固定 LeRobot 版本、model/dataset commit SHA、seed、訓練參數與 checkpoint。

## 本週定位

本週以小型 NumPy Policy 說明 pretrained model + robot dataset → fine-tuning → task-specific policy，並以官方 `lerobot-train` 執行 Required Real Model Track。重點是 training step、validation、overfitting、checkpoint 與可重新載入，不從零訓練大型 VLA。舊占位內容在 `legacy_v1/`。

## 與前週銜接、本週目標與資料流

Week12 驗證 pretrained inference；本週固定 model/data revision、learning rate、seed、20／50／100 steps，先 dry-run 檢查命令，再 `--execute` 訓練並用 Demo 04 reload checkpoint 推論。完成後應能區分 smoke test、正式實驗與過擬合證據。

## 文件、Demo、Practice 與 Paper

依 `weekly_plan.md` 的 dry-run → execute → reload 順序進行，並搭配 `notes.md`、`demo/demo_README.md`、`practice/README.md`。論文驗收需列 training objective、optimizer、dataset split、baseline、metric、seed、checkpoint selection 與至少一個 step／learning-rate ablation。

## Hardware Requirements / Environment / Download / Troubleshooting

Real Track 需要官方相容 LeRobot、CUDA PyTorch、SmolVLA 與 dataset，模型／資料寫入 Hugging Face cache，checkpoint 寫入指定 output directory。先執行 20-step smoke test；OOM 時降低 batch，resume／reload 失敗時核對 checkpoint 目錄、config、revision 與套件版本。下載、授權與資源估計見 `demo/real_track_README.md`。

## 邊界、論文與下週

短步數 loss 下降不代表 task success；必須保存命令、環境、seed、metric、checkpoint 與 failure log。未經 offline evaluation 與 safety gate 不得部署。Week14 將在 Isaac Sim 建立可控觀察與 ground truth，為 policy evaluation 做準備。
