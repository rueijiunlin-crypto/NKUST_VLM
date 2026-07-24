# Week11 Robot Dataset and Demonstrations

## 本週定位

本週學習 VLA 的資料來源：Episode → Observation + Action + Language + Timestamp + Metadata。Implementation Practice 為主，使用小型 JSONL mock dataset，不需真實機器人。

舊占位 README 保存在 `legacy_v1/`。

## 與前週銜接、本週目標與資料流

Week10 定義 policy interface；本週檢查能否由 dataset 提供一致的 Image + State + Action + Language + Timestamp。完成後應能用官方 `LeRobotDatasetMetadata` 與 `LeRobotDataset` 讀取 metadata、episode 與 sample，說明 fps、feature schema、camera keys、action/state shape 及資料授權。

## 文件、Demo、Practice 與 Paper

依序讀 `weekly_plan.md`、`notes.md`，先執行 JSONL Basic Demo，再執行 `demo_03_real_lerobot_sample.py` Required Real Track，最後完成 `practice/README.md`。論文驗收需說明 dataset composition、split、quality control、metric 與 data ablation／bias。

## Hardware Requirements / Environment / Download / Cache / Troubleshooting

Basic Track 無大型下載；Real Track 需要相容的官方 LeRobot、PyTorch、datasets／pyarrow 與影片 codec。先限制單一 episode，pin dataset revision，保存 cache 路徑但不提交資料。若失敗，記錄套件版本、stack trace、Parquet schema、codec 與 dataset card 的存取／授權條件。

## 邊界、論文與下週

sample 能讀取不代表資料品質、時間同步或 task coverage 足夠；不得以單筆資料推論模型能力。Week12 將使用相同 offline observation 經官方 preprocess → policy → postprocess 進行 log-only 推論。
