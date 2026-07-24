# Week09 Robot State + Multimodal Observation

## 本週定位

本週正式進入 Embodied Observation（具身觀察）：

```text
Vision + Language + Robot State → Embodied Observation
```

使用 mock robot state，不需真實機械手。舊 Camera lifecycle、snapshot、timestamp 與 VLM handoff 教材完整保存在 `legacy_v1/`，並整合為 observation 的 sensor lifecycle 與時間同步基礎。

## 與前週銜接、本週目標與完整資料流

Week08 產生相機／機器人座標；本週加入 joint state（關節狀態）、instruction token、timestamp、unit 與 feature order。完成後應能建立可驗證的 multimodal tensor contract，並拒絕 stale、shape 不符或欄位缺失的 observation。

## 文件、Demo、Practice 與 Paper

依序閱讀 `weekly_plan.md`、`notes.md`，執行 `demo/demo_README.md` 的 mock observation 與真實 tensor track，再進入 `practice/README.md`。論文驗收需對應 state representation、時間同步、normalization 與至少一個 modality ablation。

## Hardware Requirements / Environment / Download / Troubleshooting

Basic Track 只需 NumPy；Real Tensor Track 需要 PyTorch、Transformers、Pillow，tokenizer 首次使用會下載並寫入 Hugging Face cache。記錄版本、revision、image/state/language shape、dtype、device、單位與 joint order。常見問題是 batch 維度、token ID／embedding 混淆與不同時間戳被錯誤拼接。

## 能力邊界、論文與下週

tensor 對齊只建立模型輸入，不代表 policy 已學會安全控制。此 observation schema 是論文資料欄位與 failure analysis 的基礎；Week10 會將它映射到 VLA action representation 與 policy interface。
