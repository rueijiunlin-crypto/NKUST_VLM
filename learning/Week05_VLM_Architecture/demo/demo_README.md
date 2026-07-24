# Week05 Demo README

`demo/` 快速展示 VLM（視覺語言模型）與 Robot VLM 系統架構的主要現象，回答 What。逐步 shape、中間值與融合機制放在 `../practice/coding/guided_demos/`。

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
- Common errors：缺少 NumPy、參數非正整數、圖片尺寸無法被 patch size 整除、query tokens 無效

## Demo 檔案清單

| Demo | 對應概念 | 指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_architecture_families.py` | CLIP／LLaVA／BLIP-2／Flamingo | `python demo/demo_01_architecture_families.py --include-action-context` | 元件、representation／generative／action output | 輸出型態不能互相直接替代。 |
| `demo_02_camera_to_answer_flow.py` | Camera-to-Structured-Perception | `python demo/demo_02_camera_to_answer_flow.py` | 處理階段與結構化感知 JSON | 不虛構深度、robot coordinate 或 reachability。 |
| `demo_03_connector_comparison.py` | Connector | `python demo/demo_03_connector_comparison.py` | Projector／Query shape | Hidden size 與 token count 是不同軸。 |
| `demo_04_token_budget.py` | Token + Latency Budget | `python demo/demo_04_token_budget.py --frames 4` | Raw／compressed／total positions 與 relative cost | 影格數、壓縮、記憶體與延遲壓力。 |
| `demo_05_robot_vlm_system_flow.py` | Robot VLM system boundary | `python demo/demo_05_robot_vlm_system_flow.py` | 模組責任與缺少資訊 | VLM 語意不等於低階控制。 |

## Demo 01：Architecture Families

執行後應回答：representation output、generative output 與未來 action output 的介面為何不同？

## Demo 02：Camera-to-Structured-Perception

```powershell
python demo/demo_02_camera_to_answer_flow.py --frames 2 --image-tokens 32
```

預期輸出包含 detected semantic objects、relative relations、uncertainty 與 missing information。執行後應回答：

- 哪三個階段的錯誤可能被誤認為 LLM 幻覺？
- 為什麼 JSON 合法不代表內容具有視覺依據？
- 為什麼結果不包含假造的真實深度與 robot coordinate？

## Demo 03：Connector Comparison

```powershell
python demo/demo_03_connector_comparison.py --vision-tokens 576 --query-tokens 32
```

執行後應回答：位置壓縮 18 倍為什麼不代表資訊完整保留？Small object（小物件）、spatial detail（空間細節）與 manipulation-relevant feature（操作相關特徵）可能如何遺失？

## Demo 04：Token and Latency Budget

```powershell
python demo/demo_04_token_budget.py
python demo/demo_04_token_budget.py --frames 4 --query-tokens 32
python demo/demo_04_token_budget.py --frames 16 --query-tokens 32
```

預期輸出包含 patch tokens per frame、total raw visual tokens、compressed visual tokens、text tokens、total positions 與 relative cost indicator。執行後應回答：

- 影格數增加時，visual positions 與 total positions 如何變化？
- 為什麼 relative cost 不是實際 GPU benchmark？
- 為什麼不能把 30 FPS Camera 每一幀完整送入大型 VLM？

## Demo 05：Robot VLM System Flow

```powershell
python demo/demo_05_robot_vlm_system_flow.py
python demo/demo_05_robot_vlm_system_flow.py --depth-m 0.8 --robot-pose-known
```

預期輸出分開列出：

- VLM 可提供：semantic object、relation、task understanding。
- 其他模組提供：metric geometry、Robot State、safety constraint、low-level control。

觀察重點是加入深度或 Robot State 後，哪些缺失欄位改變，哪些安全責任仍不屬於 VLM。執行後應回答：Why should a VLM not directly control the motor?

## 與研究主線的關係

這些 Demo 是架構比較工具，不代表真實 checkpoint 的精確設定。研究使用時應從模型 config、原始論文與實際 Processor 輸出確認數值。
