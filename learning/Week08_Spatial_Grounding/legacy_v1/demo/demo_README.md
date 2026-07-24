# Week08 Demo Guide

## Demo 清單

| Demo | 對應概念 | 依賴 | 觀察重點 |
|---|---|---|---|
| `demo_01_input_output_contract.py` | 請求與結果契約 | Python 標準函式庫 | 任務差異與共同欄位 |
| `demo_02_blip_caption.py` | 影像描述 | Torch、Transformers、Pillow | 影像張量形狀與描述文字 |
| `demo_03_blip_visual_qa.py` | 視覺問答 | Torch、Transformers、Pillow | 問題如何限制回答範圍 |
| `demo_04_result_validation.py` | Schema 與跨欄位驗證 | Python 標準函式庫 | 合法與不合法結果 |

Demo 回答「這個功能在做什麼」；內部功能補寫放在 `practice/coding/`，兩者不互相取代。

## 安裝

建議使用獨立虛擬環境：

```bash
python -m pip install -r demo/requirements.txt
```

## 執行順序

```bash
python demo/demo_01_input_output_contract.py
python demo/demo_04_result_validation.py
python demo/demo_02_blip_caption.py --image <IMAGE_PATH>
python demo/demo_03_blip_visual_qa.py --image <IMAGE_PATH> --question "What is in the image?"
```

前兩項不下載模型。後兩項第一次執行會連線下載權重，應先確認網路、磁碟與模型條款。

## 預期輸出與問題

### Demo 01

- 預期：列出 Caption、VQA 請求與共同結果 JSON。
- 問題：哪些欄位適合成為 Week09 與 Week10 的穩定介面？

### Demo 02

- 預期：顯示裝置、`pixel_values` shape、推論時間與 Caption。
- 問題：CPU 與 GPU 的推論時間差距為何？

### Demo 03

- 預期：顯示問題、張量 shape、推論時間與回答。
- 問題：改變問題但保持影像不變時，回答如何改變？

### Demo 04

- 預期：合法案例通過，缺少 VQA 問題的案例列出錯誤。
- 問題：為什麼只檢查欄位存在仍不夠？

## Model / Data Requirement（模型與資料需求）

### Caption

- Model / Dataset：`Salesforce/blip-image-captioning-base`；測試影像由學習者提供。
- Source：[官方 Hugging Face 模型卡](https://huggingface.co/Salesforce/blip-image-captioning-base)
- Download size：模型快取約 GB 等級，實際大小依框架與版本而異。
- Requires login：公開模型通常不需要登入；仍以模型頁面當下規則為準。
- License / Terms：BSD-3-Clause；執行前查看模型卡。
- CPU supported：支援，但可能較慢。
- GPU recommended：建議但非必要；CUDA 可用時程式會自動選用。
- Expected runtime：首次包含下載；後續單張推論依硬體而異。
- Common errors：網路中斷、磁碟不足、Torch/CUDA 版本不符。

### VQA

- Model / Dataset：`Salesforce/blip-vqa-base`；測試影像與問題由學習者提供。
- Source：[官方 Hugging Face 模型卡](https://huggingface.co/Salesforce/blip-vqa-base)
- Download size：模型快取約 GB 等級，實際大小依框架與版本而異。
- Requires login：公開模型通常不需要登入；仍以模型頁面當下規則為準。
- License / Terms：BSD-3-Clause；執行前查看模型卡。
- CPU supported：支援，但可能較慢。
- GPU recommended：建議但非必要。
- Expected runtime：首次包含下載；後續單張推論依硬體而異。
- Common errors：模型類別選錯、問題為空、裝置不一致。

## 與 VLM/VLA 研究的關係

Caption 可提供場景語意摘要，VQA 可提供任務導向查詢；共同結果契約讓後續相機、ROS2 與行動決策模組不必依賴特定模型實作。
