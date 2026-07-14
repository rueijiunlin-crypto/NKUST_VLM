# Week04 Coding Practice：Guided Code Reading Mode

> 請先執行程式並填寫自己的觀察，再查看 `coding_observation_key.md`。本檔不放完整答案。

## 練習清單

| 順序 | Guided Demo | 學習目標 |
| --- | --- | --- |
| 1 | `guided_01_multimodal_processor_flow.py` | 追蹤真實 Processor 的圖片、文字 tensor 與 token IDs。 |
| 2 | `guided_02_projector_flow.py` | 追蹤 vision hidden size 到 language hidden size。 |
| 3 | `guided_03_multimodal_sequence.py` | 觀察 image tokens 與 text tokens 的插入位置。 |
| 4 | `guided_04_generation_flow.py` | 觀察逐 token 生成與停止條件。 |

本週使用 Guided Code Reading Mode（引導式程式閱讀模式）。程式已完整提供；工作重點是閱讀 step-by-step comments（逐步註解）、執行、觀察輸出、修改小參數並解釋變化。

## 執行方式

```powershell
python -m pip install -r practice/coding/requirements.txt
python practice/coding/guided_demos/guided_01_multimodal_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_projector_flow.py
python practice/coding/guided_demos/guided_03_multimodal_sequence.py
python practice/coding/guided_demos/guided_04_generation_flow.py
```

## 1. Multimodal Processor Shape 觀察

| 項目 | 學生觀察 |
| --- | --- |
| Processor class |  |
| `input_ids.shape` |  |
| `attention_mask.shape` |  |
| `pixel_values.shape` |  |
| `pixel_values.dtype` |  |
| 前 20 個 Token IDs |  |
| 解碼後的 Prompt 片段 |  |

將問題改長後重新執行：

```powershell
python practice/coding/guided_demos/guided_01_multimodal_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg --question "Describe the visible objects, colors, and spatial relationships."
```

- 哪一個文字 tensor 維度可能改變？
- `pixel_values.shape` 是否因問題變長而改變？
- Processor 是否已經產生自然語言回答？

學生觀察：



## 2. Projector Flow 觀察

| 項目 | 學生觀察 |
| --- | --- |
| Vision features shape |  |
| Hidden layer shape |  |
| Projected features shape |  |
| 哪一個維度保持不變 |  |
| 哪一個維度被轉換 |  |

修改 `--seed` 後，shape 與數值分別如何變化？這說明 shape tracing（張量形狀追蹤）與數值正確性有何不同？

學生觀察：



## 3. Multimodal Sequence 觀察

```powershell
python practice/coding/guided_demos/guided_03_multimodal_sequence.py --image-tokens 4 --question "find the door"
python practice/coding/guided_demos/guided_03_multimodal_sequence.py --image-tokens 8 --question "find the door"
```

| 項目 | 4 image tokens | 8 image tokens |
| --- | --- | --- |
| 文字中的 `<image>` 數量 |  |  |
| 模型序列中的 image positions |  |  |
| 總序列長度 |  |  |

為什麼 prompt 中仍只有一個 `<image>`，序列長度卻改變？

學生觀察：



## 4. Generation Flow 觀察

```powershell
python practice/coding/guided_demos/guided_04_generation_flow.py
python practice/coding/guided_demos/guided_04_generation_flow.py --max-new-tokens 2
```

| 項目 | 預設 | 限制為 2 tokens |
| --- | --- | --- |
| 產生的 token |  |  |
| 停止原因 |  |  |
| 是否形成完整句意 |  |  |

Toy logits（玩具分數）為何只能解釋生成機制，不能證明回答有視覺依據？

學生觀察：



## 5. 自訂 Question／Prompt 實驗設計

請為同一張圖片設計至少三種問題。若硬體不足，不必執行完整 7B 模型，但仍需寫出問題目的與預期檢查方式。

| 問題 | 問題類型 | 想驗證的圖片資訊 | 可能誘發的錯誤 |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

若已執行 Demo 04，記錄結果：

| 問題 | 回答摘要 | Supported | Uncertain | Contradicted |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 錯誤紀錄欄位

| 日期 | 檔案 | 修改參數 | 錯誤訊息 | 修正方式 | 尚未解決 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 自我檢查項目

- [ ] 我能區分 `input_ids`、`attention_mask` 與 `pixel_values`。
- [ ] 我能指出 Projector 前後哪個 shape 維度改變。
- [ ] 我能區分 `<image>` 文字占位符與多個 image embeddings。
- [ ] 我能說明 `max_new_tokens` 造成的停止與語意完整性是兩件事。
- [ ] 我能設計問題來檢查圖片支持、不確定與錯誤主張。
- [ ] 我有將實際觀察與未解問題記錄到 `study_log.md`。
