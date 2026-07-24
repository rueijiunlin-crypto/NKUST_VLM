# Week09 Multimodal Tensor Track

- Status：程式可離線建立實際 tensor；tokenizer 首次執行會下載。
- Entry：`python demo/demo_03_multimodal_tensors.py --image <path> --device cpu`
- Requirements：`torch>=2.2`、`transformers>=4.49`、`pillow>=10`。
- Model/Data：僅使用 `bert-base-uncased` tokenizer 示範 token IDs，授權以官方 model card 為準。
- 驗證：記錄 image/state/language/timestamp 的 shape、dtype、device、unit、joint order 與 freshness。

## 執行契約與資源

- Required：multimodal tensor contract 必修；tokenizer runtime 可因 Network blocked 而延期。
- Official source：[BERT base uncased model card](https://huggingface.co/google-bert/bert-base-uncased)；以 `--revision` pin commit。
- Download：tokenizer 約 MB 級；無 BERT 權重。License/Auth 依 model card，通常不需登入。
- Target：Python 3.10/3.11、CPU 可執行、GPU 非必要、RAM 需求低；dtype 由腳本輸出。
- Cache：Hugging Face cache，不提交下載內容。
- Target versions — verify before execution：PyTorch 2.2+、Transformers 4.49+、Pillow 10+；本機未下載 tokenizer 驗證。
- VRAM / System RAM / CUDA / dtype / quantization：CPU/一般 RAM 即可，CUDA 非必要；記錄 tensor dtype，無模型量化。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_multimodal_tensors.py --image <path> --device cpu --revision <commit>
```

保存 model/revision、套件版本、source timestamp、image/state/token shape、dtype/device、unit、joint order、freshness 與 validation result。常見 blocker 是圖片路徑、網路、revision、batch dimension 與 stale timestamps；此 tensor 僅是 observation，不是 action。
