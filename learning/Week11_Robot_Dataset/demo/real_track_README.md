# Week11 Real LeRobot Dataset Track

- Status：Not validated yet（不自動下載 dataset）。
- Entry：`python demo/demo_03_real_lerobot_sample.py --dataset-id lerobot/aloha_sim_insertion_human --episode 0`
- Requirements：安裝與所選模型相容的官方 `lerobot` release、`torch`、`datasets`、`pyarrow`、影片解碼依賴。
- Download：只限制單一 episode；大小與 license 以 dataset card 為準，cache 不提交 Git。
- 驗證：repo/revision、tasks、fps、feature schema、image/state/action shape、timestamp、license。
- Troubleshooting：影片 codec、Parquet schema 或 revision 不符時，保存 stack trace 與套件版本。

## 執行契約

- Required：官方 LeRobot API 讀取 metadata、episode、sample 是必修路線。
- Official source：[LeRobot dataset loading example](https://github.com/huggingface/lerobot/blob/main/examples/dataset/load_lerobot_dataset.py)。
- Dataset：預設 `lerobot/aloha_sim_insertion_human`；必須 pin `--revision`，記錄 dataset card URL、license、tasks、episodes、frames、fps。
- Download：單一 episode 仍可能包含影片／Parquet；大小依 dataset card，先查檔案清單。公開資料通常不需登入，受限資料則標 Model/Data access blocked。
- Target：Python 3.10/3.11、官方相容 LeRobot/PyTorch/codec；CPU 可讀取，GPU 非必要，RAM/磁碟依 episode。
- Cache：Hugging Face datasets/cache；不得提交 dataset。
- Target versions — verify before execution：官方 LeRobot release/commit、PyTorch 2.2+、datasets/pyarrow 與相容 video backend；本機未安裝 LeRobot。
- VRAM / System RAM / CUDA / dtype / quantization：GPU/CUDA/quantization 非必要；RAM/磁碟依 episode，sample dtype 由程式列印。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_lerobot_sample.py --dataset-id lerobot/aloha_sim_insertion_human --revision <commit> --episode 0
```

保存 LeRobot version/commit、repo/revision、metadata、sample keys、image/state/action shape、dtype、timestamp、task、codec 與 elapsed time。schema／codec／revision 錯誤須保存 stack trace；能讀取一筆資料不代表資料品質或 task coverage 已驗證。
