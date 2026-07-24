# Week07 Coding Practice：Guided Code Reading Mode

> 請先執行與填寫，再查看 `coding_observation_key.md`。

## 執行方式

```powershell
python practice/coding/guided_demos/guided_01_prompt_contract_flow.py
python practice/coding/guided_demos/guided_02_schema_validation_flow.py
python practice/coding/guided_demos/guided_03_retry_flow.py
python practice/coding/guided_demos/guided_04_safety_gate_flow.py
```

## 1. Prompt Contract Flow

請為「尋找出口」或另一個室內語意目標填寫：

| Section | 學生設計 | 要控制的風險 |
| --- | --- | --- |
| Role |  |  |
| Task |  |  |
| Evidence boundary |  |  |
| Output contract |  |  |
| Unknown policy |  |  |
| Safety boundary |  |  |

移除其中一段時，哪一種失敗更可能發生？



## 2. Schema Validation Flow

| Validation layer | Sample 是否通過 | 原因 | 修正方式 |
| --- | --- | --- | --- |
| JSON syntax |  |  |  |
| Required fields |  |  |  |
| Types／enums |  |  |  |
| Cross-field semantics |  |  |  |
| Grounding |  |  |  |

自行設計一個「JSON 合法但語意失敗」的輸出：



## 3. Retry Flow

| Failure | Retry／new observation／reject | 最大次數 | 停止原因 |
| --- | --- | --- | --- |
| Invalid JSON |  |  |  |
| Missing field |  |  |  |
| Image unclear |  |  |  |
| Unsupported claim |  |  |  |
| Direct motor command |  |  |  |

為什麼影像不清楚時不應只修改文字要求模型「一定回答」？



## 4. Safety Gate Flow

| Gate | Input | Pass rule | Failure action | 學生觀察 |
| --- | --- | --- | --- | --- |
| Schema |  |  |  |  |
| Grounding |  |  |  |  |
| Uncertainty |  |  |  |  |
| Freshness |  |  |  |  |
| Navigation |  |  |  |  |

## 5. Prompt Test Matrix

| Case | Prompt version | Expected status | Expected validation | 實際結果／待測 |
| --- | --- | --- | --- | --- |
| Clear target |  |  |  |  |
| Target absent |  |  |  |  |
| Image blurred |  |  |  |  |
| False premise |  |  |  |  |
| Invalid format |  |  |  |  |
| Safety override request |  |  |  |  |

## 錯誤紀錄欄位

| 日期 | Prompt／程式 | Failure layer | 錯誤內容 | 處置 | 尚未解決 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 自我檢查項目

- [ ] Prompt 包含證據、未知與安全邊界。
- [ ] 我能區分五種 validation layers。
- [ ] Retry 有明確理由與上限。
- [ ] Unknown 不會被強制轉成 found。
- [ ] 通過 semantic gate 不等於允許機器人行動。
- [ ] 我已把實際測試或待測原因記錄到 `study_log.md`。
