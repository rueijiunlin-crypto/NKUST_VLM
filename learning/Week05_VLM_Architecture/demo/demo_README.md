# Week05 Demo README

`demo/` 快速展示 VLM（視覺語言模型）架構的主要現象，回答 What。逐步 shape、中間值與融合機制放在 `../practice/coding/guided_demos/`。

## 安裝方式

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：不使用外部模型或資料集
- Source：程式使用小型教學參數與 NumPy（數值運算函式庫）
- Download size：只有 Python 套件，無模型權重
- Requires login：否
- License / Terms：依 NumPy 套件授權；無額外資料授權
- CPU supported：是
- GPU recommended：否
- Expected runtime：各 Demo 通常在數秒內完成
- Common errors：缺少 NumPy、參數非正整數、圖片尺寸無法被 patch size 整除

## Demo 檔案清單

| Demo | 對應概念 | 指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_architecture_families.py` | 四種架構家族 | `python demo/demo_01_architecture_families.py` | 元件、輸出與代表模型 | 架構分類依資料流與輸出，不只看名稱。 |
| `demo_02_camera_to_answer_flow.py` | 系統資料流 | `python demo/demo_02_camera_to_answer_flow.py` | 八個處理與驗證階段 | 模型前後也需要驗證。 |
| `demo_03_connector_comparison.py` | Connector | `python demo/demo_03_connector_comparison.py` | Projector／Query shape | Hidden size 與 token count 是不同軸。 |
| `demo_04_token_budget.py` | Token budget | `python demo/demo_04_token_budget.py` | Visual、text 與 total positions | 圖片數量與壓縮策略的成本。 |

## Demo 01：Architecture Families

執行後應回答：Dual Encoder 與生成式 VLM 的輸出介面為何不同？

## Demo 02：Camera-to-Answer

```powershell
python demo/demo_02_camera_to_answer_flow.py --frames 2 --image-tokens 32
```

執行後應回答：哪三個階段的錯誤可能被誤認為 LLM 幻覺？

## Demo 03：Connector Comparison

```powershell
python demo/demo_03_connector_comparison.py --vision-tokens 576 --query-tokens 32
```

執行後應回答：位置壓縮 18 倍為什麼不代表資訊完整保留？

## Demo 04：Token Budget

```powershell
python demo/demo_04_token_budget.py
python demo/demo_04_token_budget.py --images 2 --query-tokens 32
```

執行後應回答：加入第二張圖片時，visual positions 與 total positions 如何變化？

## 與研究主線的關係

這些 Demo 是架構比較工具，不代表真實 checkpoint 的精確設定。研究使用時應從模型 config、原始論文與實際 Processor 輸出確認數值。
