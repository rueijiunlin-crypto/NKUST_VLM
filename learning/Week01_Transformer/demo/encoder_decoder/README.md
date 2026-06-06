# Encoder Decoder Demo

## 對應概念

Encoder（編碼器）與 Decoder（解碼器）。

## 執行指令

```powershell
python demo\encoder_decoder\demo_encoder_decoder_flow.py
```

## 預期輸出

- Encoder mode：輸入指令轉成上下文表示
- Decoder mode：上下文與已生成 Token 產生下一步描述

## 觀察重點

- Encoder 偏向理解輸入。
- Decoder 偏向逐步生成輸出。
- 兩者如何對應 VLM/VLA 任務。

## 執行後應回答的問題

1. Encoder 和 Decoder 的主要差異是什麼？
2. Encoder 的輸出適合做什麼？
3. Decoder 如何支援回答生成或動作描述？
