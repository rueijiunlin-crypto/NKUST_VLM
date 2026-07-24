# Week04 Coding Practice README

Week04 Coding Practice 採 Guided Code Reading Mode（引導式程式閱讀模式）。請透過完整可執行程式理解 LLaVA（大型語言與視覺助手）的 Processor（前處理器）、Projector（投影器）、多模態序列與自回歸生成，而不是從零補 TODO。

## 結構說明

| 路徑 | 用途 |
| --- | --- |
| `guided_demos/guided_01_multimodal_processor_flow.py` | 觀察真實 `AutoProcessor` 的文字、圖片 tensor 與 token IDs。 |
| `guided_demos/guided_02_projector_flow.py` | 觀察 Vision features（視覺特徵）如何投影到語言 hidden size（隱藏維度）。 |
| `guided_demos/guided_03_multimodal_sequence.py` | 觀察一個 `<image>` 如何對應多個 image positions（影像位置）。 |
| `guided_demos/guided_04_generation_flow.py` | 觀察 next-token logits（下一詞元分數）、greedy decoding（貪婪解碼）與停止條件。 |
| `coding_practice.md` | 學生 shape、參數修改與問題實驗紀錄表。 |
| `coding_observation_key.md` | 觀察方向與理解說明。 |
| `requirements.txt` | 本練習需要的 Python 套件。 |

## 安裝方式

請從 `learning/Week04_LLaVA` 執行：

```powershell
python -m pip install -r practice/coding/requirements.txt
```

Guided 01 使用真實 `AutoProcessor`，首次需要下載 Processor 相關檔案；不會載入完整 7B 模型。Guided 02–04 使用 NumPy（數值運算函式庫）或 Python 標準函式庫，可在 CPU 上快速完成。

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：Guided 01 使用 `llava-hf/llava-1.5-7b-hf` 的 Processor；Guided 02–04 使用小型教學資料
- Source：[Hugging Face LLaVA Model Card](https://huggingface.co/llava-hf/llava-1.5-7b-hf)
- Download size：Guided 01 只下載 Processor／tokenizer（詞元化器）設定，不下載完整 7B 權重
- Requires login：通常不需要；以模型頁面最新狀態為準
- License / Terms：以模型頁面最新授權條款為準
- CPU supported：支援
- GPU recommended：不需要
- Expected runtime：Guided 02–04 通常數秒內完成；Guided 01 首次下載時間依網路而定
- Common errors：網路下載失敗、圖片路徑錯誤、缺少套件、patch 或 shape 參數不相容

## 執行指令

```powershell
python practice/coding/guided_demos/guided_01_multimodal_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_projector_flow.py
python practice/coding/guided_demos/guided_03_multimodal_sequence.py
python practice/coding/guided_demos/guided_04_generation_flow.py
```

若 Week02 圖片不存在，請改用自己的圖片：

```powershell
python practice/coding/guided_demos/guided_01_multimodal_processor_flow.py --image demo/my_image.jpg
```

## 觀察重點

- `input_ids.shape`、`attention_mask.shape` 與 `pixel_values.shape`
- Prompt token IDs 與解碼後特殊 token
- Projector 前後的 batch、image token 與 hidden dimensions（隱藏維度）
- `<image>` 文字占位符與多個 image positions 的差異
- `max_new_tokens`、`<eos>` 與回答完整性的關係
- Shape 正確、語句流暢與視覺事實正確是三種不同檢查
- Robot-oriented prompt 是否把語意候選誇大成精確幾何、可達性或安全動作
- 回答主張需要 RGB、額外感測、Robot State 或其他系統模組中的哪一層證據

請把觀察記錄到 `coding_practice.md`，再整理到 `../../study_log.md`。
