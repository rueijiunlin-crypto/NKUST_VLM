# Week12 Real SmolVLA Inference Track

## LeRobot Compatibility

- LeRobot：`>=0.6,<0.7`（stable target `0.6.0`）；Python：`>=3.12`；Dataset：LeRobotDataset v3.x。
- API source：[v0.6.0 policy factory](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/policies/factory.py)、[v0.6.0 SmolVLA source](https://github.com/huggingface/lerobot/tree/v0.6.0/src/lerobot/policies/smolvla)。
- Status：source-audited；本機未安裝相依環境，runtime 為 Environment blocked。

- Status：Not validated yet；只允許 offline dataset observation，輸出為 log-only。
- Entry：`python demo/demo_03_real_smolvla_inference.py --device cuda --dtype bfloat16`
- Requirements：官方相容版 `lerobot`、`torch`、`transformers`、`accelerate`。
- Model：`lerobot/smolvla_base`，權重約 907 MB；dataset 另計，授權見官方 model/dataset card。
- Hardware：建議 CUDA GPU；記錄 GPU/driver/CUDA、VRAM、warm-up、p50/p95。
- Cache：Hugging Face 預設 cache；pin model/dataset revision。
- Safety：action 只列印，未接 validator/controller 前不得驅動硬體。

## 官方介面與執行契約

- Required：`make_pre_post_processors → preprocess → select_action → postprocess` 必修。
- Official sources：[SmolVLA v0.6.0 source](https://github.com/huggingface/lerobot/tree/v0.6.0/src/lerobot/policies/smolvla)、[model card](https://huggingface.co/lerobot/smolvla_base)。
- Revision：model 與 dataset 都必須 pin immutable commit；另記錄 LeRobot package/commit。
- Dataset：預設 `lerobot/svla_so100_pickplace` 單一 episode；授權與下載依 dataset card。
- Auth：公開資源通常不需登入；若條款／gated access 改變，標 Model access blocked。
- Target：Python 3.12+、LeRobot `>=0.6,<0.7`；建議 CUDA、bfloat16 與約 8–12 GB 以上 VRAM，實際依 observation 與模型 revision。
- Quantization：預設不量化；若自行使用，另存設定與 accuracy/runtime 差異。
- Target versions — verify before execution：LeRobot 0.6.x 的 `dataset,smolvla` extras 與其相容 PyTorch / Transformers / Accelerate；本機未安裝 LeRobot。
- System RAM / CUDA：建議 16–32 GB RAM 與 LeRobot/PyTorch 支援的 CUDA；不得把未實測組合標為 Tested。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_smolvla_inference.py --model-revision <commit> --dataset-revision <commit> --device cuda --dtype bfloat16
```

保存 resolved model、dataset、raw/processed keys/shapes、parameter count、chunk size、action shape/finite、load/warm-up/inference seconds、peak VRAM、GPU/driver/CUDA 與 stack trace。OOM、feature mismatch 或 processor drift 時標對應 blocker；輸出永遠 log-only。
