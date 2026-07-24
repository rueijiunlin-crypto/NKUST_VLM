# Week12 SmolVLA / OpenVLA Inference

## LeRobot Compatibility

- Target LeRobot version：`>=0.6,<0.7`（穩定目標為 `0.6.0`）。
- Python：`>=3.12`。
- Dataset format：LeRobotDataset v3.x。
- Official documentation source：[LeRobot 0.6.0 release](https://github.com/huggingface/lerobot/releases/tag/v0.6.0)、[SmolVLA v0.6.0 source](https://github.com/huggingface/lerobot/tree/v0.6.0/src/lerobot/policies/smolvla)。
- API status：已稽核 `make_pre_post_processors` 與 `SmolVLAPolicy` 的穩定明確匯入路徑；本機真實模型推論仍為 Environment blocked。
- Reproducibility：正式實驗必須同時固定 model revision 與 dataset revision 的 commit SHA。

## 本週定位

本週第一次建立預訓練 VLA 推論介面觀念：

```text
Image + Robot State + Instruction → Processor / Policy → Action Prediction
```

SmolVLA 作主要學習模型，OpenVLA 作規模與架構比較。Basic Demo 使用可控 mock policy 驗證 observation、normalization、action chunk 與 latency；SmolVLA 真實模型是 Required Real Model Track。若無法實際推論，仍須完成環境、revision、資料與 blocker 證據。

## 與前週銜接、本週目標與資料流

Week11 提供真實 offline dataset observation；本週使用官方 `make_pre_post_processors`：

```text
dataset sample → preprocess → SmolVLA.select_action
→ postprocess → finite action log
```

完成後應能辨識 raw／processed shape、action chunk、dtype、warm-up／inference latency、VRAM 與 pre/postprocessor 的必要性。

## 文件、Demo、Practice 與 Paper

依序使用 `weekly_plan.md`、`notes.md`、`demo/demo_README.md`、`practice/README.md`。Basic Demo 回答 What；Guided Reading 拆解 How；Demo 03 使用官方介面且只列印 action。論文驗收需對應 architecture、training objective、benchmark、action ablation 與 reproduction gap。

## Hardware Requirements / Environment / Download / Troubleshooting

Real Track 需要相容的 LeRobot、PyTorch、Transformers、模型與 dataset revision；建議 CUDA GPU，CPU 僅作資源足夠時的慢速診斷。模型與資料使用 Hugging Face cache。OOM 時降低 batch／影像設定或改用受支援 dtype；schema／processor 不符時記錄 LeRobot commit、完整 feature keys 與 stack trace。

## 安全邊界、論文與下週

輸出是 log-only，未經 action range、collision、workspace、timeout 與 hardware interlock 驗證前不得接 controller。這些 latency／shape／failure evidence 可作論文 baseline runtime 表；Week13 才進入短步數 fine-tuning 與 checkpoint reload。
