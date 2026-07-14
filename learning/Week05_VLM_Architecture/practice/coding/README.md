# Week05 Coding Practice README

本週以完整可執行的小型程式拆解 Vision Encoder（視覺編碼器）、Projector（投影器）、fusion（融合）與 Camera-to-Answer 資料流。

## 結構說明

| 程式 | 觀察重點 |
| --- | --- |
| `guided_01_vision_encoder_flow.py` | RGB → patch vectors 的 shape。 |
| `guided_02_projector_alignment.py` | Projector 前後 hidden dimension。 |
| `guided_03_fusion_strategies.py` | 串接、query compression 與 cross-attention。 |
| `guided_04_end_to_end_flow.py` | 每個系統階段的輸入、輸出與風險。 |

## 安裝與執行

```powershell
python -m pip install -r practice/coding/requirements.txt
python practice/coding/guided_demos/guided_01_vision_encoder_flow.py
python practice/coding/guided_demos/guided_02_projector_alignment.py
python practice/coding/guided_demos/guided_03_fusion_strategies.py
python practice/coding/guided_demos/guided_04_end_to_end_flow.py
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：無
- Source：小型合成矩陣與架構 metadata（中繼資料）
- Download size：無模型下載
- Requires login：否
- License / Terms：無額外資料授權
- CPU supported：是
- GPU recommended：否
- Expected runtime：數秒
- Common errors：缺少 NumPy、patch 參數無法整除、從錯誤目錄執行

## 觀察重點

- Shape 正確與語意正確的差異。
- Token axis 與 hidden axis 的差異。
- Query compression 的資訊取捨。
- Cross-attention 的 Query、Key、Value 來源。
- 系統錯誤應由第一個失敗階段開始定位。
