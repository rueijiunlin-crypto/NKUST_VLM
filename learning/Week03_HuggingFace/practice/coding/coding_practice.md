# Week03 Coding Practice（程式練習）：Guided Code Reading（引導式程式閱讀）

本週 Coding Practice 採 Guided Code Reading Mode（引導式程式閱讀模式）。請從 `learning/Week03_HuggingFace` 目錄執行 `practice/coding/guided_demos/` 中的程式，閱讀程式註解與輸出，重點是理解 Hugging Face Transformers（模型載入與推論工具庫）如何把 Week02 的 CLIP（對比式圖文預訓練）概念落到真實推論流程。

> 本週不是 TODO 填空題，請不要修改 guided demos（引導式示範程式）當作作答；請把觀察結果記錄在本檔與 `../../study_log.md`。

## 練習清單

### Processor 輸出觀察

- 模式：Guided Code Reading（引導式程式閱讀）。
- 對應檔案：`guided_demos/guided_01_processor_flow.py`
- 學習目標：觀察 `input_ids`、`attention_mask`、`pixel_values` 的 keys（欄位）與 shape（形狀）。

### Zero-shot 推論觀察

- 模式：Guided Code Reading。
- 對應檔案：`guided_demos/guided_02_logits_topk_flow.py`
- 學習目標：觀察 labels（候選標籤）數量如何影響 `logits_per_image` shape 與 probability（機率分布）。

### Prompt 比較觀察

- 模式：Guided Code Reading。
- 對應檔案：`guided_demos/guided_03_prompt_effect_flow.py`
- 學習目標：比較 prompt（提示詞）改寫後 top-1（第一名預測）與 probability 的變化。

## 執行方式

請先安裝依賴：

```powershell
python -m pip install -r demo/requirements.txt
```

若 Week02 範例圖片存在，可使用：

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_logits_topk_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_03_prompt_effect_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若圖片不存在，請改用自己的本地圖片路徑，例如：

```powershell
python practice/coding/guided_demos/guided_02_logits_topk_flow.py --image demo/my_image.jpg --labels "a photo of a cat" "a photo of a robot" "a photo of a classroom"
```

第一次執行可能會下載 `openai/clip-vit-base-patch32` 權重與 processor（前處理器）檔案，請確認網路與 Hugging Face（模型平台）連線狀態。

## 學生觀察欄位

### 1. Processor keys 與 tensor shape（張量形狀）

| Key | Shape | 來源是圖片或文字？ | 我的理解 |
| --- | --- | --- | --- |
| `input_ids` | | | |
| `attention_mask` | | | |
| `pixel_values` | | | |

### 2. Labels 數量與 `logits_per_image` shape

請使用不同數量的 `--labels` 重跑 `guided_02_logits_topk_flow.py`，觀察 shape 如何改變。

| 圖片數量 | Labels 數量 | `logits_per_image` shape | 我的觀察 |
| --- | --- | --- | --- |
| 1 | | | |
| 1 | | | |

### 3. Probability 與 top-k 排序

| Top-k 設定 | Top-1 label | Top-1 probability | 我如何判斷排序來自 probability？ |
| --- | --- | --- | --- |
| 1 | | | |
| 3 | | | |

### 4. Prompt 改寫觀察

| Prompt set | Top-1 label | 最明顯變化 | 可能原因 |
| --- | --- | --- | --- |
| `object_only` | | | |
| `photo_template` | | | |
| `scene_aware` | | | |

## 錯誤紀錄欄位

| 錯誤訊息 | 發生在哪個 Demo | 我嘗試的修正 | 是否解決 |
| --- | --- | --- | --- |
| | | | |

## 自我檢查項目

- [ ] 我能說出 processor 輸出的 keys 與每個 tensor 的用途。
- [ ] 我能解釋 labels 數量為什麼會改變 `logits_per_image` 的第二個維度。
- [ ] 我能說明 top-k 是從 softmax probability 排序取得，而不是人工指定答案。
- [ ] 我能舉例說明 prompt 改寫如何影響 CLIP zero-shot classification（零樣本分類）。
- [ ] 我能把 Week03 的 Hugging Face 推論流程連到 Week04 LLaVA（大型語言與視覺助手）的模型載入與前處理流程。
