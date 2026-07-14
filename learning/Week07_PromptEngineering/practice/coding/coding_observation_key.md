# Week07 Coding Observation Key

> 請先完成 `coding_practice.md`，再查看本指引。

## 1. Prompt Contract Flow

Role 限定模型能力語境；Task 定義要完成的工作；Evidence boundary 限制可使用資訊；Output contract 定義機器介面；Unknown policy 防止被迫猜測；Safety boundary 防止越權控制。各段責任不同，不能只靠「請準確回答」取代。

## 2. Schema Validation Flow

範例 JSON 可成功解析、欄位齊全、型別正確，但 `status=found` 且 evidence 空白，違反跨欄位語意。即使補上 evidence 字串，仍需檢查它是否真的由圖片支持。

## 3. Retry Flow

Syntax 與缺少欄位屬可能透過格式回饋修正的錯誤；影像資訊不足應取得新觀察；無依據主張與安全違規應拒絕。所有重試都應有上限與紀錄。

## 4. Safety Gate Flow

範例在 freshness（新鮮度）失敗後停止 navigation handoff。這避免使用過期但內容看似正確的影像。每一層只負責自己的判定，不能因上游通過就跳過下游安全檢查。

## 常見誤解修正

- Prompt 越長不必然越好。
- JSON 合法不代表圖片證據正確。
- Low uncertainty 字串不等於校準後信心。
- Retry 不應改寫事實。
- Semantic target 不等於 navigation goal。
