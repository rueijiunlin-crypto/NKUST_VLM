# Week06 Real Video VLM Track

- Status：Not validated yet（未自動下載模型）。
- Entry：`python demo/demo_03_real_video_vlm.py --video <path> --device auto`
- Model：`Qwen/Qwen2.5-VL-3B-Instruct`；請 pin `--revision`，授權以官方 model card 為準。
- Requirements：`torch>=2.2`、`transformers>=4.49`、`accelerate>=0.28`、`qwen-vl-utils>=0.0.8`、`decord>=0.6`。
- Hardware：建議 CUDA GPU；CPU 可嘗試但生成時間長，VRAM 依影片 token 與 dtype 變化。
- Cache：使用 Hugging Face 預設 cache；不要把權重提交到 Git。
- Troubleshooting：OOM 時降低影片解析度／frame 數／`max-new-tokens`；記錄 model、revision、device、dtype、shape、time、memory。

## 執行契約

- Required：本週學習路線必修；目前 `Not validated yet`，blocker 不等於免修。
- Official source：[Qwen2.5-VL model card](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)。
- Data：自備短影片；須記錄來源、授權、duration、codec、source FPS 與 frame count。
- Download size：模型約數 GB 級，影片另計；以 pinned revision 檔案清單為準。
- License / Auth：依官方 model card；公開模型通常不需登入，存取政策改變時記錄 Model access blocked。
- Target：Python 3.10/3.11、CUDA-capable PyTorch；建議 12 GB 以上 VRAM，實際依 frames/resolution/dtype。
- Quantization：本腳本不自行啟用；若另行量化，必須保存方法與輸出差異。
- Target versions — verify before execution：PyTorch 2.2+、Transformers 4.49+、Accelerate 0.28+、qwen-vl-utils 0.0.8+、OpenCV 4.9+；未在本機模型 runtime 實測。
- System RAM / CUDA / dtype：建議 16–32 GB RAM、相容 CUDA；auto/float16/bfloat16/float32 皆須記錄實際 resolved dtype。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_video_vlm.py --video <path> --revision <commit> --fps 1
python demo/demo_03_real_video_vlm.py --video <path> --revision <commit> --frames 8
```

`--fps` 與 `--frames` 互斥。至少比較 `1/2/4 fps` 或 `2/4/8/16 frames`，保存 sampled frame count、input shape、load/inference seconds、tokens、peak VRAM、回答與 temporal error。解碼失敗先查 codec／OpenCV／decord；OOM 降低 frame、resolution 或 generation length。輸出只供語意分析，不是控制命令。
