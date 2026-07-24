# Week12 SmolVLA / OpenVLA Inference

本週第一次建立預訓練 VLA 推論介面觀念：

```text
Image + Robot State + Instruction → Processor / Policy → Action Prediction
```

SmolVLA 作主要學習模型，OpenVLA 作規模與架構比較。Basic Demo 使用可控 mock policy 驗證 observation、normalization、action chunk 與 latency；真實模型屬 optional／advanced，需依最新官方 Model Card 安裝與下載。
