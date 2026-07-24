# Week12 Real SmolVLA Inference Track

- Status：Not validated yet；只允許 offline dataset observation，輸出為 log-only。
- Entry：`python demo/demo_03_real_smolvla_inference.py --device cuda --dtype bfloat16`
- Requirements：官方相容版 `lerobot`、`torch`、`transformers`、`accelerate`。
- Model：`lerobot/smolvla_base`，權重約 907 MB；dataset 另計，授權見官方 model/dataset card。
- Hardware：建議 CUDA GPU；記錄 GPU/driver/CUDA、VRAM、warm-up、p50/p95。
- Cache：Hugging Face 預設 cache；pin model/dataset revision。
- Safety：action 只列印，未接 validator/controller 前不得驅動硬體。
