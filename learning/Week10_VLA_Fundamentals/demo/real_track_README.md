# Week10 Real VLA Inspection Track

- Status：config-only；執行時只下載 `lerobot/smolvla_base` 的 `config.json`。
- Entry：`python demo/demo_03_real_vla_inspection.py --revision <immutable-revision>`
- Requirement：`huggingface-hub>=0.28`。
- Model：SmolVLA 約 450M；model card 與 code 分別受其聲明授權約束。
- 驗證：config、processor/interface、camera/state/action features、chunk size、revision、cache。
- Troubleshooting：若 config key 隨 LeRobot 版本改名，保留完整 config 並標記差異，不猜測缺失欄位。

## 執行契約與資源

- Required：真實 checkpoint interface inspection 必修；不等同權重推論。
- Official sources：[SmolVLA model card](https://huggingface.co/lerobot/smolvla_base) 與 [LeRobot](https://github.com/huggingface/lerobot)。
- Revision：必須傳 immutable model commit，並記錄 LeRobot package/commit。
- Download：config/metadata 為 KB/MB 級，不下載約 450M 參數權重；License/Auth 依 model card 與 LeRobot repository。
- Hardware：CPU、低 RAM、無 CUDA 要求；cache 使用 Hugging Face 預設位置。
- Target versions — verify before execution：huggingface-hub 0.28+；LeRobot/config schema 以 pinned commit 為準。
- VRAM / System RAM / dtype / quantization：VRAM/CUDA/quantization 不適用，低 RAM 即可；config inspection 不載入 tensor dtype。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_vla_inspection.py --revision <commit>
```

保存 model/revision、resolved file、feature keys、camera/state/action shapes、chunk size、normalization／processor interface 與套件版本。404／schema drift 時標 Network／Model access／Environment blocked 並保存原始 config；不得宣稱已驗證 inference latency 或 action quality。
