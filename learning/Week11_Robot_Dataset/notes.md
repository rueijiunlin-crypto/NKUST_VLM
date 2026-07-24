# Week11 Notes：Robot Dataset and Demonstrations

## Why 與 Problem

VLA 的能力上限深受 demonstration 品質與 schema 一致性限制。Robot dataset 不是影像資料夾，而是同步的 observation-action trajectories；少一個 timestamp、錯一個 joint order 或洩漏相鄰 frame，就可能得到看似很高但不可用的指標。

## Dataset Unit 與 Schema

```text
Dataset
└─ Episode
   ├─ task / language instruction
   ├─ observation.images.{camera} [T,C,H,W]
   ├─ observation.state [T,S]
   ├─ action [T,A]
   ├─ timestamp [T]
   └─ metadata: robot, fps, units, frames, calibration, license
```

LeRobotDataset v3 以 Parquet 保存 tabular data、以 MP4 保存影像，metadata 記錄 features、episodes、tasks 與 statistics。使用 sample 前先 pin repository revision，閱讀 dataset card 與 license，避免不受控地下載完整資料。

## Alignment 與 Data Flow

```text
raw sensors / teleoperation
→ timestamp normalization
→ observation-action alignment
→ schema validation
→ episode segmentation
→ statistics / normalization
→ split by episode/task/environment
→ dataloader batch [B,T,...]
```

Action 的語意需明確：它是與 `o_t` 同時量測、由 `o_t` 導出的 `a_t`，或下一步執行後的狀態差？必須寫入 dataset card。Dropped frame 不可悄悄 forward-fill。

## Split、Leakage 與 Metric

不能把同一 episode 的相鄰 frame 分散到 train 與 validation。依研究問題以 episode、task、environment、robot 或 operator 分割。保存 split manifest 與 seed。Data quality 指標包含 missing rate、timestamp monotonicity、action finite/range、task distribution、episode length 與 failed demonstration ratio。

## Real LeRobot Sample Track

載入官方小型 sample／公開 dataset subset，列印 repo ID、revision、episode/task 數、feature schema、image/state/action shape、fps 與 cache path。只讀一小段，不預設下載全資料。若套件或網路未就緒，必須標記 `Not validated yet`，不得偽造 frame 或統計。

## Example

一個 batch 可為 image `[8,2,3,480,640]`、state `[8,8]`、action `[8,7]`、timestamp `[8]`。Dataset statistics 的 shape 應與 state/action feature 對應；同為 `[7]` 不代表 joint order 相同。

## Failure、Limitation 與 Ethics

- observation/action shift 一格。
- episode 邊界錯誤。
- failed demo 未標示。
- normalization statistics 由 validation 計算造成 leakage。
- private scene、operator 影像或受限資料未處理。
- dataset license 與模型再散布條款不相容。

## Demo 與 Paper Mapping

- Basic Demo：小型 episode schema 與 validation。
- Real Track：官方 LeRobot sample dataset。
- Core Paper：Open X-Embodiment，對應跨 embodiment standardization 與 RT-X mixture。

## 本週尚未涵蓋

不進行 policy training；Week12 先驗證 inference contract。
