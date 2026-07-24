# Week15 Notes：Sim-to-Real / Real Robot Deployment

## 1. Domain Shift

Simulation 與真實世界在 lighting、texture、background、camera response、noise、object physics 與 robot dynamics 上不同。Sim success 不可直接外推 real success。

## 2. Calibration 與 Sensor Error

Intrinsics、extrinsics、time sync 與 coordinate convention 的小誤差會累積到 action。部署前需 calibration version、residual error 與 validity check。

## 3. Latency Budget

End-to-end latency 包含 capture、transport、preprocess、inference、validation、planning、control。平均 latency 不足以描述安全性，還需 percentile、jitter、timeout 與 stale policy。

## 4. Action Error 與 Recovery

比較 predicted／commanded／executed action。失敗恢復需 safe stop、retry limit、re-observation、operator takeover 與 error log。

## 5. Deployment Safety

Checklist 應含 workspace、joint／velocity limits、collision、E-stop、watchdog、communication loss、model uncertainty 與 rollback。

## 6. Hardware-ready Alternative

無實機時仍可驗證介面 schema、timing、mock controller、fault injection、record/replay、calibration contract 與 deployment checklist；必須標示未做 real-world validation。
