# Encoder / Decoder Demo（編碼器與解碼器示範程式）

## 對應概念

Transformer Encoder（轉換器編碼器）與 Transformer Decoder（轉換器解碼器）。

## 執行指令

請在 `learning/Week01_Transformer/` 目錄下執行：

```powershell
python demo/encoder_decoder/demo_encoder_decoder_flow.py
```

## 預期輸出

- Encoder mode 的資料流。
- Decoder mode 的資料流。
- Encoder 與 Decoder 的用途比較。

## 觀察重點

- Encoder 偏向理解輸入並產生表示。
- Decoder 偏向根據上下文逐步產生輸出。
- CLIP（對比式圖文預訓練）較重視 Encoder 產生可比較向量；LLaVA（大型語言與視覺助手）等生成式模型會更需要 Decoder 概念。

## 執行後應回答的問題

1. Encoder 和 Decoder 的主要差異是什麼？
2. CLIP 為什麼需要 Image Encoder（影像編碼器）與 Text Encoder（文字編碼器）？
3. 為什麼生成回答或動作描述時會需要 Decoder？
