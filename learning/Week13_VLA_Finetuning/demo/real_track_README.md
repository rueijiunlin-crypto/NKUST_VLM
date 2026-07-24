# Week13 Real SmolVLA Fine-tuning Track

## LeRobot Compatibility

- LeRobot：`>=0.6,<0.7`（stable target `0.6.0`）；Python：`>=3.12`；Dataset：LeRobotDataset v3.x。
- API source：[v0.6.0 training entrypoint](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/scripts/lerobot_train.py)、[v0.6.0 training config](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/configs/train.py)。
- Status：CLI/source-audited and dry-run only；CUDA training runtime 為 Environment blocked。

- Status：預設 dry-run，Not validated yet。
- Entry：`python demo/demo_03_real_smolvla_finetune.py --dataset-id <repo>`；確認後才加 `--execute`。
- Requirements：官方相容版 `lerobot`、CUDA PyTorch；完整版本以 LeRobot lockfile/安裝指南為準。
- Hardware：先做 20-step smoke test；正式時間與 VRAM 依 batch、image、dataset、dtype 變化。
- Artifact：保存 config、model/data revision、seed、environment、train/validation metric、checkpoint 與 failure log。
- License：確認 dataset、SmolVLA 與輸出 checkpoint 的再散布條款。

## 官方命令、版本與資源

- Required：dry-run、20/50/100-step smoke training、checkpoint discover/reload 是必修路線；runtime 可被硬體／環境阻塞。
- Official source：[LeRobot v0.6.0 training entrypoint](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/scripts/lerobot_train.py)。
- Model / Dataset：`lerobot/smolvla_base` 與使用者指定 LeRobot dataset；兩者 pin revision，另存 LeRobot commit。
- Download：模型約 907 MB 級，dataset/checkpoint 另計；以實際 revision 檔案清單與 output directory 為準。
- License / Auth：依 model/dataset card；公開資源通常不需登入。
- Target：CUDA GPU 強烈建議；官方完整訓練可能需 A100 級資源與數小時，本週只做 20/50/100-step smoke test。保存 GPU、VRAM、driver、CUDA、dtype、RAM/disk。
- Cache：Hugging Face cache；checkpoint 不納入 Git。
- Target versions — verify before execution：LeRobot 0.6.x 的 `training,smolvla` extras 與其 CUDA/PyTorch 相容範圍；本機未安裝 `lerobot-train`。
- System RAM / CUDA / dtype / quantization：建議 32 GB 以上 RAM、相容 CUDA；dtype 由 checkpoint/config 決定，smoke script 不自行量化。

```powershell
python demo/demo_03_real_smolvla_finetune.py --dataset-id <repo> --model-revision <commit> --dataset-revision <commit> --steps 20 --learning-rate 0.0001 --seed 7
python demo/demo_03_real_smolvla_finetune.py --dataset-id <repo> --model-revision <commit> --dataset-revision <commit> --steps 20 --learning-rate 0.0001 --seed 7 --execute
python demo/demo_04_reload_finetuned_checkpoint.py --checkpoint <path> --dataset-id <repo> --dataset-revision <commit>
```

保存完整 `lerobot-train` 命令、LR/seed/steps/batch、loss、elapsed、peak VRAM、checkpoint path/files、reload action shape/finite 與 failure log。CLI schema drift、OOM、dataset features 或 checkpoint 缺檔時標 Environment／Hardware blocked；短步數 loss 不代表 task success。
