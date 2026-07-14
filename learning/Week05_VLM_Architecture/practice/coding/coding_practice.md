# Week05 Coding Practice：Guided Code Reading Mode

> 請先執行與填寫觀察，再查看 `coding_observation_key.md`。

## 練習清單與執行方式

```powershell
python practice/coding/guided_demos/guided_01_vision_encoder_flow.py
python practice/coding/guided_demos/guided_02_projector_alignment.py
python practice/coding/guided_demos/guided_03_fusion_strategies.py
python practice/coding/guided_demos/guided_04_end_to_end_flow.py
```

## 1. Vision Encoder Flow

| 項目 | 學生觀察 |
| --- | --- |
| Image shape |  |
| Patch grid |  |
| Patch vector shape |  |
| Patch vector 是否等於 contextualized feature |  |

將 `--patch-size 2` 改為 `--patch-size 1`，記錄 token 數量與每個 token 維度的變化：



## 2. Projector Alignment

| 項目 | 學生觀察 |
| --- | --- |
| Vision features shape |  |
| Hidden shape |  |
| Projected shape |  |
| 保持不變的 axes |  |
| 改變的 axis |  |

修改 `--seed` 後，哪些數值改變、哪些 shape 不變？



## 3. Fusion Strategies

| 策略 | 輸入位置 | 輸出位置 | 中間值／權重 | 可能取捨 |
| --- | --- | --- | --- | --- |
| Concatenation |  |  |  |  |
| Query compression |  |  |  |  |
| Cross-attention |  |  |  |  |

Cross-attention 中的 Query、Key、Value 分別對應什麼？



## 4. End-to-End Flow

| 階段 | 輸入 | 輸出 | 可能錯誤 | 驗證方法 |
| --- | --- | --- | --- | --- |
| Camera |  |  |  |  |
| Preprocess |  |  |  |  |
| Vision Encoder |  |  |  |  |
| Connector |  |  |  |  |
| Language Model |  |  |  |  |
| Validator |  |  |  |  |

## 錯誤紀錄欄位

| 日期 | 程式 | 修改參數 | 錯誤／現象 | 修正方式 | 未解問題 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 自我檢查項目

- [ ] 我能由圖片與 patch size 計算 patch positions。
- [ ] 我能區分 token axis 與 hidden axis。
- [ ] 我能說明三種融合策略的資料流。
- [ ] 我能指出 Camera-to-Answer 的至少三個驗證點。
- [ ] 我已將實際觀察整理到 `study_log.md`。
