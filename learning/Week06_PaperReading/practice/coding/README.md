# Week06 Coding Practice README

## 結構說明

| 程式 | 用途 |
| --- | --- |
| `guided_01_research_question_flow.py` | Topic 到可驗證研究問題。 |
| `guided_02_method_experiment_mapping.py` | 方法元件到實驗證據。 |
| `guided_03_claim_evidence_validator.py` | Claim record 完整性檢查。 |
| `guided_04_comparison_matrix.py` | 固定欄位論文比較。 |

## 安裝與執行

```powershell
python -m pip install -r practice/coding/requirements.txt
python practice/coding/guided_demos/guided_01_research_question_flow.py
python practice/coding/guided_demos/guided_02_method_experiment_mapping.py
python practice/coding/guided_demos/guided_03_claim_evidence_validator.py
python practice/coding/guided_demos/guided_04_comparison_matrix.py
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：無
- Source：小型教學 metadata（中繼資料）
- Download size：無
- Requires login：否
- CPU supported：是
- GPU recommended：否
- Expected runtime：數秒
- Common errors：把範例 claim 當成已核對的論文證據；實際紀錄仍需回到原始來源

## 觀察重點

- Topic、gap、question、variables 與 evidence 的連續性。
- 核心方法元件是否有對應控制實驗。
- Claim 是否具有來源位置、範圍與限制。
- 比較矩陣的欄位是否對兩篇論文一致。
