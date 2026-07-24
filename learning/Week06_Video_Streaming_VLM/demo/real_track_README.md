# Week06 Real Video VLM Track

- Status：Not validated yet（未自動下載模型）。
- Entry：`python demo/demo_03_real_video_vlm.py --video <path> --device auto`
- Model：`Qwen/Qwen2.5-VL-3B-Instruct`；請 pin `--revision`，授權以官方 model card 為準。
- Requirements：`torch>=2.2`、`transformers>=4.49`、`accelerate>=0.28`、`qwen-vl-utils>=0.0.8`、`decord>=0.6`。
- Hardware：建議 CUDA GPU；CPU 可嘗試但生成時間長，VRAM 依影片 token 與 dtype 變化。
- Cache：使用 Hugging Face 預設 cache；不要把權重提交到 Git。
- Troubleshooting：OOM 時降低影片解析度／frame 數／`max-new-tokens`；記錄 model、revision、device、dtype、shape、time、memory。
