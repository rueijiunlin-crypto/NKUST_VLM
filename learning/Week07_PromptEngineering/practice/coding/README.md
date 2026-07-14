# Week07 Coding Practice README

## 結構說明

| 程式 | 用途 |
| --- | --- |
| `guided_01_prompt_contract_flow.py` | 組裝 Prompt 六段契約。 |
| `guided_02_schema_validation_flow.py` | Syntax、欄位、型別與跨欄位規則。 |
| `guided_03_retry_flow.py` | 失敗類型到 retry／reject 決策。 |
| `guided_04_safety_gate_flow.py` | Schema 到 freshness 的逐層 safety gate。 |

## 安裝與執行

```powershell
python -m pip install -r practice/coding/requirements.txt
python practice/coding/guided_demos/guided_01_prompt_contract_flow.py
python practice/coding/guided_demos/guided_02_schema_validation_flow.py
python practice/coding/guided_demos/guided_03_retry_flow.py
python practice/coding/guided_demos/guided_04_safety_gate_flow.py
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：無
- Source：小型 Prompt 與 JSON 案例
- Download size：無
- Requires login：否
- CPU supported：是
- GPU recommended：否
- Expected runtime：數秒
- Common errors：把示範規則當成完整 production safety policy（正式系統安全政策）

## 觀察重點

- 每個 Prompt 段落控制的風險。
- JSON syntax、schema 與 semantic rule 的差異。
- Retry 是否針對可修正錯誤且有上限。
- Safety gate 失敗後是否停止下游 handoff（交接）。
