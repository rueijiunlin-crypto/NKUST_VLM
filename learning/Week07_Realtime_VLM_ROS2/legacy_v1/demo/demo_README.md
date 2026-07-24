# Week07 Demo README

本週 Demo 快速展示 Prompt contract（提示契約）、structured output（結構化輸出）、retry（重試）與 safety gate（安全閘門）。所有程式使用 Python 標準函式庫，不呼叫外部模型；真實模型實驗可沿用 Week04 的 LLaVA Demo 與本週測試表。

## 安裝方式

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：無
- Source：小型 Prompt 與 JSON 教學案例
- Download size：無
- Requires login：否
- License / Terms：無額外模型或資料授權
- CPU supported：是
- GPU recommended：否
- Expected runtime：各 Demo 數秒
- Common errors：把靜態 Prompt 檢查誤當模型效果；把 JSON 合法誤當視覺事實正確

## Demo 檔案清單

| Demo | 概念 | 指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_prompt_anatomy.py` | Prompt 組成 | `python demo/demo_01_prompt_anatomy.py` | 六個契約段落 | 每段控制不同風險。 |
| `demo_02_structured_output_validation.py` | JSON validation | `python demo/demo_02_structured_output_validation.py` | PASS／FAIL 與錯誤 | Syntax、欄位與 enum。 |
| `demo_03_prompt_version_comparison.py` | Prompt 版本 | `python demo/demo_03_prompt_version_comparison.py` | 靜態契約分數 | 靜態檢查不是模型評估。 |
| `demo_04_retry_policy.py` | Retry policy | `python demo/demo_04_retry_policy.py` | retry／request／reject／accept | 失敗類型決定處置。 |
| `demo_05_robot_safety_gate.py` | Semantic safety | `python demo/demo_05_robot_safety_gate.py` | allowed 與原因 | 語意通過仍不是控制許可。 |

## 執行後應回答

- Prompt 哪些段落限制可用證據與輸出格式？
- JSON 合法後還需要哪些驗證？
- 哪些錯誤可重試，哪些應要求新觀察或拒絕？
- Semantic gate 與 navigation safety 的責任有何不同？

## 真實模型銜接

可將本週 Prompt 送入 Week04 `demo_03_llava_visual_qa.py` 或 `demo_04_question_comparison.py`，但必須固定模型、圖片與生成參數，並將 raw output（原始輸出）保存在本週 `study_log.md`。大型模型仍屬選做／進階。
