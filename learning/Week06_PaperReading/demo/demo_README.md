# Week06 Demo README

本週 Demo 用小型 Python 程式展示論文閱讀的 What，不下載 PDF 或模型，也不宣稱自動完成論文理解。

## 安裝方式

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：無
- Source：CLIP 與 LLaVA 原始論文的結構化教學摘要
- Download size：無
- Requires login：否
- License / Terms：閱讀與引用原始論文時遵守來源授權與引用規範
- CPU supported：是
- GPU recommended：否
- Expected runtime：各程式數秒
- Common errors：無額外套件；主要風險是把教學範例誤當論文實際證據

## Demo 檔案清單

| Demo | 概念 | 指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_reading_passes.py` | 三階段閱讀 | `python demo/demo_01_reading_passes.py` | 每階段閱讀位置與產物 | Pass 1 不等於完成證據驗證。 |
| `demo_02_claim_evidence_map.py` | 主張到證據 | `python demo/demo_02_claim_evidence_map.py` | Claim、required evidence、threat | 主張的範圍與替代解釋。 |
| `demo_03_metric_context.py` | 指標比較條件 | `python demo/demo_03_metric_context.py` | 不可直接比較的欄位 | 分數需連同 context 解讀。 |
| `demo_04_clip_llava_comparison.py` | 固定欄位比較 | `python demo/demo_04_clip_llava_comparison.py` | CLIP／LLaVA 比較 | 不同研究問題需要不同證據。 |

## 執行後應回答

- 三個 reading passes 各產生什麼？
- 什麼資訊能讓主張可追溯？
- 哪四個 metric context 欄位不一致時不可直接比較？
- CLIP 與 LLaVA 的研究問題、輸出與證據焦點有何不同？

## 原始來源

- [CLIP](https://arxiv.org/abs/2103.00020)
- [LLaVA](https://arxiv.org/abs/2304.08485)
