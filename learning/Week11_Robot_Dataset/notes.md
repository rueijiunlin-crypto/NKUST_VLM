# Week11 Notes：Robot Dataset and Demonstrations

## 1. Dataset Unit

Episode 是一次任務嘗試；trajectory 是隨時間排列的 observation-action sequence；demonstration 可由 teleoperation 或其他示範策略產生。

```text
Episode
├─ Camera Observation
├─ Robot State
├─ Action
├─ Language Instruction
├─ Timestamp
└─ Metadata
```

## 2. Alignment

每個 action 必須對應正確時間的 observation。延遲、不同頻率與 dropped frame 會造成 label shift；資料管線需記錄原始 timestamp 與 alignment policy。

## 3. Schema 與 LeRobot

Schema 應定義 shape、dtype、unit、frame、rate、normalization 與 task metadata。可用 LeRobot Dataset 作格式案例，但本週 Basic Demo 不下載資料。

## 4. Split 與 Leakage

不可把同一 episode 的相鄰 frames 隨機分到 train／validation，否則場景幾乎相同造成 leakage。應依 episode、task、environment 或 robot 分組切分。

## 5. Data Quality

檢查 missing field、non-finite action、timestamp order、stale observation、task imbalance 與 failed demonstrations。失敗資料可用於 failure analysis，不應無記錄刪除。

## 6. Research Boundary

資料量不等於資料品質；必須記錄 collection policy、operator、版本、license、privacy 與 known bias。
