# Week11 Real LeRobot Dataset Track

## LeRobot Compatibility

- LeRobot：`>=0.6,<0.7`（stable target `0.6.0`）；Python：`>=3.12`；Dataset：LeRobotDataset v3.x。
- API source：[v0.6.0 dataset source](https://github.com/huggingface/lerobot/tree/v0.6.0/src/lerobot/datasets)。
- Status：source-audited；本機未安裝相依環境，runtime 為 Environment blocked。

- Status：Not validated yet（不自動下載 dataset）。
- Entry：`python demo/demo_03_real_lerobot_sample.py --dataset-id lerobot/aloha_sim_insertion_human --episode 0`
- Requirements：安裝與所選模型相容的官方 `lerobot` release、`torch`、`datasets`、`pyarrow`、影片解碼依賴。
- Download：只限制單一 episode；大小與 license 以 dataset card 為準，cache 不提交 Git。
- 驗證：repo/revision、tasks、fps、feature schema、image/state/action shape、timestamp、license。
- Troubleshooting：影片 codec、Parquet schema 或 revision 不符時，保存 stack trace 與套件版本。

## 執行契約

- Required：官方 LeRobot API 讀取 metadata、episode、sample 是必修路線。
- Official source：[LeRobot v0.6.0 dataset implementation](https://github.com/huggingface/lerobot/blob/v0.6.0/src/lerobot/datasets/lerobot_dataset.py)。
- Dataset：預設 `lerobot/aloha_sim_insertion_human`；必須 pin `--dataset-revision`，記錄 dataset card URL、license、tasks、episodes、frames、fps。
- Download：單一 episode 仍可能包含影片／Parquet；大小依 dataset card，先查檔案清單。公開資料通常不需登入，受限資料則標 Model/Data access blocked。
- Target：Python 3.12+、LeRobot `>=0.6,<0.7` 與 Dataset v3 相容 codec；CPU 可讀取，GPU 非必要，RAM/磁碟依 episode。
- Cache：Hugging Face datasets/cache；不得提交 dataset。
- Target versions — verify before execution：LeRobot 0.6.x 的 `dataset` extra 與其鎖定的 PyTorch、datasets/pyarrow、video backend；本機未安裝 LeRobot。
- VRAM / System RAM / CUDA / dtype / quantization：GPU/CUDA/quantization 非必要；RAM/磁碟依 episode，sample dtype 由程式列印。

```powershell
python -m pip install -r demo/requirements_real.txt
python demo/demo_03_real_lerobot_sample.py --dataset-id lerobot/aloha_sim_insertion_human --dataset-revision <commit> --episode 0
```

保存 LeRobot version/commit、repo/revision、metadata、sample keys、image/state/action shape、dtype、timestamp、task、codec 與 elapsed time。schema／codec／revision 錯誤須保存 stack trace；能讀取一筆資料不代表資料品質或 task coverage 已驗證。
