# Week07 教材筆記：Prompt Engineering

## 1. Prompt Engineering 是實驗設計

Prompt Engineering（提示工程）不是尋找一組永遠有效的魔法句子，而是控制模型輸入、輸出與失敗處置的實驗設計。

一個可研究的 Prompt 需要：

- Version（版本）。
- Intended task（預期任務）。
- Input assumptions（輸入假設）。
- Output contract（輸出契約）。
- Test cases（測試案例）。
- Metrics／failure taxonomy（指標／失敗分類）。
- Change reason（修改原因）。

只比較「回答看起來比較好」不足以形成可重現實驗。

## 2. Prompt Anatomy

適合機器人 VLM（視覺語言模型）的 Prompt 可拆成：

```text
Role
Task
Observation scope
Evidence boundary
Output contract
Unknown policy
Safety boundary
```

### Role

限定模型角色，例如「分析單張室內相機畫面」。角色不應賦予不存在的感測能力。

### Task

使用可驗證動詞，例如 identify、describe、compare、locate。避免「理解整個環境」這類不可測試描述。

### Evidence Boundary

要求只使用可見影像證據，不推測遮擋物、房間外狀態、路徑安全或未提供的感測資訊。

### Output Contract

明確列出欄位、型別、允許值與不允許的額外文字。

### Unknown Policy

影像模糊、遮擋或證據不足時允許輸出 `unknown`。如果 Prompt 只允許 found／not found，模型容易在資訊不足時被迫猜測。

### Safety Boundary

禁止輸出直接速度、轉向或「路徑安全」等超出單張圖片證據的控制結論。

### 對應 Demo

- `python demo/demo_01_prompt_anatomy.py`
- 執行後應能回答：Evidence boundary 與 safety boundary 有何不同？

## 3. Chat Template 與 Prompt Content

Chat template（對話模板）處理模型需要的角色 token 與訊息格式；Prompt content（提示內容）描述任務本身。兩者不可混為一談。

多模態對話概念資料：

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "..."},
            {"type": "text", "text": "Identify the visible target."},
        ],
    }
]
```

不同 checkpoint 使用不同 control tokens（控制詞元）。應使用 Processor 的 `apply_chat_template()` 或模型官方格式，而不是把 LLaVA 1.5 的 `USER: <image>` 格式套到所有模型。

官方參考：[Hugging Face Multimodal Chat Templates](https://huggingface.co/docs/transformers/en/chat_templating_multimodal)

## 4. Structured Output Contract

### 範例 JSON

```json
{
  "status": "found",
  "target": "exit",
  "evidence": ["visible exit sign"],
  "uncertainty": "low"
}
```

### 建議限制

- `status`：`found`、`not_found`、`unknown`。
- `target`：字串或 `null`。
- `evidence`：可見證據字串陣列。
- `uncertainty`：有限列舉值。
- 禁止未定義欄位，避免模型夾帶直接控制命令。

JSON Schema（JSON 結構規格）可用 `type`、`required`、`properties` 與 `additionalProperties` 描述機器可驗證的契約。Schema 只能驗證結構與部分值限制，不能自動判斷證據是否真的出現在圖片。

官方參考：[JSON Schema Object Reference](https://json-schema.org/understanding-json-schema/reference/object)

### 對應 Demo

- `python demo/demo_02_structured_output_validation.py`
- 執行後應能回答：為什麼合法 JSON 仍可能是幻覺？

## 5. Validation Layers

建議依序驗證：

```text
1. Parse／Syntax
2. Schema／Types／Enums
3. Cross-field Semantics
4. Grounding
5. Freshness／System State
6. Safety Policy
```

### Syntax

能否解析為 JSON。Markdown code fence、前後解釋文字或缺少引號都可能失敗。

### Schema

欄位是否齊全、型別是否正確、status 是否在允許集合、是否有額外欄位。

### Cross-field Semantics

例如 `status=found` 時 evidence 不可為空；`status=unknown` 時不應輸出確定目標位置。

### Grounding

Evidence 是否由圖片支持。這通常需要人工標註、額外模型、幾何資訊或多感測器交叉確認。

### Freshness

相機 frame 是否過期、是否對應目前機器人位置。語意正確但時間過期仍不可用。

### Safety

結果是否越過系統允許的語意範圍，或包含直接控制與未驗證路徑。

## 6. Retry、Reject 與 Unknown

不同失敗需要不同處置：

| Failure | 建議處置 |
| --- | --- |
| JSON syntax error | 提供格式錯誤後有限次重試 |
| Missing required field | 指出缺少欄位後有限次重試 |
| Unknown due to image | 要求新觀察，不靠文字強迫改答案 |
| Unsupported claim | 拒絕主張並記錄 |
| Safety violation | 拒絕並記錄安全事件 |
| Repeated failure | 停止重試，交由 fallback／人工處理 |

重試應有最大次數與停止原因。無限重試會增加延遲，也可能讓模型為了滿足格式而捏造內容。

### 對應 Demo

- `python demo/demo_04_retry_policy.py`
- 執行後應能回答：為什麼 unknown 不應重試成 found？

## 7. Prompt Version Comparison

每次只改少量變因：

- V1：模糊任務。
- V2：加入 evidence boundary。
- V3：加入 JSON contract。
- V4：加入 unknown 與 safety policy。

固定：模型、revision、圖片、生成參數與評估規則。記錄：

- Format pass rate（格式通過率）。
- Required field pass rate（必要欄位通過率）。
- Grounded claim rate（有依據主張比例）。
- Unknown handling accuracy（未知處理正確率）。
- Safety violation count（安全違規次數）。
- Latency 與 retry count（延遲與重試次數）。

### 對應 Demo

- `python demo/demo_03_prompt_version_comparison.py`
- 靜態檢查只能確認契約是否寫出，不能替代真實模型與標註資料測試。

## 8. Robot Semantic Safety Gate

VLM output（視覺語言模型輸出）應先成為「候選語意結果」，而不是直接 action（動作）：

```text
VLM Raw Output
↓ schema validation
Structured Semantic Result
↓ grounding + uncertainty + freshness
Verified Semantic Candidate
↓ navigation feasibility + map + obstacle checks
Navigation Goal
↓ controller safety
Robot Action
```

即使 status=found、有 evidence 且 uncertainty=low，也只能進入下游驗證。單張 RGB 圖片不足以證明路徑無障礙或目標可安全到達。

### 對應 Demo

- `python demo/demo_05_robot_safety_gate.py`
- 執行後應能回答：通過 semantic gate 後還需要哪些 navigation 檢查？

## 9. Test Matrix 與錯誤分類

至少包含：

- Normal：清楚可見目標。
- Not found：確定畫面中沒有目標。
- Unknown：模糊、遮擋、過暗或視角不足。
- False premise：問題假設不存在物件。
- Format stress：要求嚴格 JSON。
- Conflicting instruction：使用者要求繞過安全規則。
- Stale observation：正確但過期的 frame。

錯誤分類需在測試前定義，避免看到結果後才調整標準。

## 本週尚未涵蓋

- Prompt automatic optimization（提示自動最佳化）。
- Function calling／tool use（函式呼叫／工具使用）。
- 完整 JSON Schema validator 套件整合。
- ROS2 message、navigation action 與真實控制程式。
- 對大型測試集的統計顯著性分析。
