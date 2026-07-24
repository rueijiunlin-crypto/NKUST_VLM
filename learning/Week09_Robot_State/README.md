# Week09 Robot State + Multimodal Observation

本週正式進入 Embodied Observation（具身觀察）：

```text
Vision + Language + Robot State → Embodied Observation
```

使用 mock robot state，不需真實機械手。舊 Camera lifecycle、snapshot、timestamp 與 VLM handoff 教材完整保存在 `legacy_v1/`，並整合為 observation 的 sensor lifecycle 與時間同步基礎。
