# Week04 Required Real LLaVA Track

## Purpose、Status 與必要性

- Purpose：用真實 LLaVA 權重回答三個固定問題，建立 visual evidence 與 hallucination audit。
- Required：學習路線必修；runtime 可因可證明的限制而 blocked。
- Status：Not validated yet。只有保存真實輸出後才能改為 Executed。

## Model / Data Requirement（模型與資料需求）

- Model：`llava-hf/llava-1.5-7b-hf`
- Official source：[Hugging Face model card](https://huggingface.co/llava-hf/llava-1.5-7b-hf)
- Revision：執行時必須以 `--revision` pin immutable commit。
- Image：`../Week02_CLIP/demo/000000039769.jpg` 或記錄來源／授權的自備圖片。
- Download size：約 14 GB 級別，實際以 pinned revision 檔案清單為準。
- Requires login：公開權重通常不需登入；若服務政策改變，記錄 Model access blocked。
- License / Terms：執行與再散布前依 model card、上游 LLaVA／Vicuna／CLIP 條款逐項確認。

## Target Environment 與硬體

- Python 3.10/3.11、PyTorch 2.2+、Transformers 4.49+、Accelerate、Pillow。
- 建議 NVIDIA CUDA GPU；float16 約需 16 GB 級 VRAM，實際隨裝置映射與生成長度變動。
- CPU 可嘗試但載入與生成可能非常慢；記錄 RAM、GPU、driver、CUDA、dtype。
- Cache：Hugging Face 預設 cache；不得提交權重、Token 或受限圖片。
- Target versions — verify before execution：PyTorch 2.2+、Transformers 4.49+、Accelerate 0.28+；本機未實測，不得標成 Tested。
- System RAM：建議 32 GB 以上並依 device mapping 留意 CPU offload。
- CUDA / dtype：依 PyTorch 相容矩陣；建議 float16，bfloat16 需硬體支援。
- Quantization：預設關閉；若使用 4/8-bit，另記 backend、版本與回答差異。

## Install / Run

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg --revision <commit> --question "<必要問題>"
python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

三個必要問題與逐項命令列在 `weekly_plan.md`，不得用單一泛化問題取代。

## Expected Output 與 Runtime Evidence

保存 model/revision、device/GPU、dtype、peak VRAM、load/inference seconds、input/output token、完整回答，以及每個主張的 Supported／Uncertain／Contradicted／Requires Additional Sensor or Robot State 標記。

## Troubleshooting 與安全邊界

- OOM：降低 `max_new_tokens`、採官方支援 dtype／device mapping，並如實標 Hardware blocked。
- 下載／403：檢查 revision、網路、登入與條款，分別標 Network 或 Model access blocked。
- processor/model mismatch：保存 Transformers 版本與完整 stack trace。
- LLaVA 回答不是 metric pose、reachability 或 motor command；不得直接送入控制器。
