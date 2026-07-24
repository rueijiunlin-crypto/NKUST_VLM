# Week12 Notes：SmolVLA / OpenVLA Inference

## LeRobotDataset v3 → SmolVLA

LeRobot 0.6.x 的官方 preprocessor 會替單一 Dataset v3 sample 加上 batch 維度，再執行 device transfer、文字處理與正規化。因此流程起點應是 `dataset[index]`，不應先用 `DataLoader(batch_size=1)` 批次化後再交給同一個 preprocessor。

```text
dataset[index]（raw、未批次化）
→ 挑選 observation / task 欄位
→ preprocessor（add batch + normalize + tokenize + device）
→ SmolVLAPolicy.select_action
→ raw model-space action
→ postprocessor（unnormalize + CPU）
→ final action
```

`raw sample != normalized model input`，而且 `raw policy output != final postprocessed action`。教材與實驗紀錄應同時保存 raw/processed shapes、所用 statistics、action shape 與 finite 檢查，避免把模型空間中的數值誤認為機器人可直接使用的控制量。

## Why 與 Problem

能載入 checkpoint 不等於 inference 正確。Observation keys、image order、state normalization、action unnormalization、chunk length 與 device/dtype 必須與訓練 metadata 相符。本週以 SmolVLA 為可執行真實軌，OpenVLA 作架構與資源比較。

## SmolVLA Input / Output

SmolVLA 約 450M parameters，接收多視角 image、proprioceptive state 與 language instruction，透過 VLM backbone 與 action expert 產生 continuous action chunk。

- images：依 dataset feature keys 組成 `[B,Ncam,C,H,W]`。
- state：`[B,S]`，依 training statistics normalization。
- language：token IDs／mask `[B,L]`。
- action：`[B,H,A]` 或 policy API 回傳的當前 action `[B,A]`。

## Mechanism 與 Data Flow

```text
LeRobot episode / live observation
→ feature mapping
→ preprocessor + normalization
→ device / dtype transfer
→ SmolVLA policy forward
→ flow-matching action generation
→ action chunk
→ postprocessor + unnormalization
→ validator
→ log only / controller boundary
```

Flow matching 從 noise path 逐步求得 continuous action。推論步數、chunk size 與 replan 頻率共同影響 latency、smoothness 與 closed-loop correction。

## Reproducible Real Inference

CLI 必須可設定 `--model-id`、`--model-revision`、`--dataset-id`、`--dataset-revision`、`--episode`、`--index`、`--device`、`--dtype`、`--seed` 與 cache。程式需印出 model、revision、parameter count、device、dtype、observation/action shape、warm-up 與單步時間、peak memory。

執行順序：

1. 只讀 model/dataset card、license 與 config。
2. 限制 sample 與 step 數下載。
3. 以 dataset observation 離線推論，不接硬體。
4. 檢查 finite、shape、range 與 metadata。
5. 保存環境與 raw output，狀態由 `Not validated yet` 更新為實際結果。

## OpenVLA Comparison

OpenVLA 是 7B VLA，使用視覺 encoder、projector 與 Llama-family language backbone，將 action 離散化成 token。其計算需求與 Llama 2 衍生 license 必須另行評估；不應把 SmolVLA 的 processor 或 normalization 套到 OpenVLA。

## Failure、Limitation 與 Safety

- feature key 或 camera order 不符。
- dataset statistics 缺失或 revision 不一致。
- CPU 不支援選定 dtype/operator。
- GPU VRAM 不足、首次編譯或 warm-up 被算入穩態 latency。
- action shape 合法但 unit/frame 錯誤。
- benchmark 使用 teacher observation，不代表 live deployment。

所有真實 inference 預設只寫 log；未經 validator、workspace limit、collision check、watchdog 與 operator approval，不得控制 robot。

## Demo 與 Paper Mapping

- Basic Demo：mock action contract，快速回答 What。
- Real Track：SmolVLA + LeRobot observation，回答實際 processor／policy 如何串接。
- Core Paper：SmolVLA；對照 OpenVLA 的規模與 action representation。

## 本週尚未涵蓋

不宣稱 real-robot success；Week13 才處理 fine-tuning。
