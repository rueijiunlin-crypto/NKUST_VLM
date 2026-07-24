# Week11 Real LeRobot Dataset Track

- Status：Not validated yet（不自動下載 dataset）。
- Entry：`python demo/demo_03_real_lerobot_sample.py --dataset-id lerobot/aloha_sim_insertion_human --episode 0`
- Requirements：安裝與所選模型相容的官方 `lerobot` release、`torch`、`datasets`、`pyarrow`、影片解碼依賴。
- Download：只限制單一 episode；大小與 license 以 dataset card 為準，cache 不提交 Git。
- 驗證：repo/revision、tasks、fps、feature schema、image/state/action shape、timestamp、license。
- Troubleshooting：影片 codec、Parquet schema 或 revision 不符時，保存 stack trace 與套件版本。
