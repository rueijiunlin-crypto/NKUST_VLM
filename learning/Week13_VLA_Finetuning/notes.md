# Week13 Notes：VLA Fine-tuning

## Why 與 Problem

Pretrained VLA 未必認得本地 camera、robot geometry、task wording 與 action convention。Fine-tuning（微調）以少量目標資料調整 policy，但小資料也最容易 overfit、split leakage 與忘記預訓練能力。

## Input、Output 與 Training Objective

Batch 含 observation、instruction 與 target action chunk：

- image `[B,T,Ncam,C,H,W]`
- state `[B,T,S]`
- token IDs `[B,L]`
- target action `[B,H,A]`

SmolVLA flow-matching training 對 action path 加 noise，模型預測 velocity／denoising direction，loss 對有效 action 與 mask 聚合。Dataset statistics、feature keys、chunk size 必須與 config 一致。

## Training Data Flow

```text
pinned dataset revision
→ episode-level split
→ train-only statistics
→ processor / augmentation
→ batch + mask
→ policy forward
→ loss
→ backward / optimizer / scheduler
→ checkpoint + validation
→ fixed offline evaluation
```

Checkpoint 至少保存 model、optimizer、scheduler、global step、config、model/dataset revision、normalization、seed 與 environment lock。

## Fine-tuning Strategies

- Full fine-tuning：彈性最高，VRAM 與 forgetting 風險較大。
- Frozen backbone / action head：資源低但 adaptation 能力有限。
- LoRA／adapter：參數效率高，但可插入模組與部署工具需驗證。
- From scratch：只適合研究對照，不是小資料的預設。

## Real SmolVLA Small Experiment

使用官方 LeRobot CLI 與小型 dataset，先以 `--steps 20` smoke test 驗證資料與 checkpoint，再進行受控小實驗。官方指南的完整訓練時間與資料建議只作資源估計，不能當成本機結果。CLI wrapper 應支援 `--dry-run`，輸出確切命令與 metadata；未在相容 GPU 執行時標記 `Not validated yet`。

至少比較 pretrained baseline 與 fine-tuned checkpoint，固定 validation episodes、seed、processor、replan 方式與 metric。不要只報最後 train loss。

## Metric、Failure 與 Limitation

- Train loss 降、validation loss 升：overfitting。
- Camera/background 記憶造成環境 leakage。
- Action normalization 錯誤使 loss 看似正常但動作尺度錯。
- Resume 時 optimizer／scheduler 不一致。
- 只挑成功 episode 評估。
- 小型 offline metric 不等同 real-robot task success。

記錄 GPU、VRAM、dtype、batch size、gradient accumulation、steps、wall time、peak memory、checkpoint hash 與 failure logs。

## Demo 與 Paper Mapping

- Basic Demo：toy optimization 只解釋 gradient 與 overfitting。
- Real Track：SmolVLA small fine-tuning CLI + fixed evaluation。
- Core Paper：Octo，對應 generalist policy transfer；Deep Reading 比較 full、PEFT 與 scratch。

## 本週尚未涵蓋

不在沒有安全審查下把 fine-tuned checkpoint 接到實體機器人。
