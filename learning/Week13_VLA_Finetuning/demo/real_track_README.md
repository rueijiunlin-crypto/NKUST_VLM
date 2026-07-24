# Week13 Real SmolVLA Fine-tuning Track

- Status：預設 dry-run，Not validated yet。
- Entry：`python demo/demo_03_real_smolvla_finetune.py --dataset-id <repo>`；確認後才加 `--execute`。
- Requirements：官方相容版 `lerobot`、CUDA PyTorch；完整版本以 LeRobot lockfile/安裝指南為準。
- Hardware：先做 20-step smoke test；正式時間與 VRAM 依 batch、image、dataset、dtype 變化。
- Artifact：保存 config、model/data revision、seed、environment、train/validation metric、checkpoint 與 failure log。
- License：確認 dataset、SmolVLA 與輸出 checkpoint 的再散布條款。
