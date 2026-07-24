# Week07 Concept Answer Key

> 請先完成 `concept_practice.md`，再查看本參考答案。

## 1. Prompt Anatomy

Role 限定能力語境；Task 定義工作；Evidence boundary 限制可用資訊；Output contract 定義機器介面；Unknown policy 允許資訊不足；Safety boundary 防止越權控制。它們分別影響可測試性、幻覺與系統風險。

## 2. Chat Template

Chat template 將 role／content 轉成 checkpoint 預期的 control tokens；Prompt content 是實際任務文字。不同模型訓練格式不同，錯誤 control tokens 會降低表現或破壞圖片位置。

## 3. Structured Output

合理例子：`status` enum、`target` string／null、`evidence` string array、`uncertainty` enum。也可加入 image timestamp 或 observation ID，但需明確定義來源，不能要求模型捏造。

## 4. Validation Layers

Syntax 檢查可解析性；schema 檢查欄位與型別；semantic 檢查欄位關係；grounding 檢查圖片支持；freshness 檢查時間與系統狀態；safety 檢查是否越過允許行為。

## 5. Retry Policy

格式與缺少欄位可有限重試；影像不清楚需新觀察；無依據主張與安全違規應拒絕。重試有上限，且不能用語言壓力改變不可觀察事實。

## 6. Prompt Comparison

固定模型／revision、圖片與標註、chat template、生成參數、random seed（如有）、硬體或推論後端與評估規則。記錄 raw output、失敗類型、重試數與延遲。

## 7. Robot Safety

語意辨識只提供候選目標，仍需時間同步、座標轉換、地圖對應、可達性、障礙物、定位、速度限制與控制器安全檢查。單張圖像回答不足以授權動作。

## 8. Test Matrix

正常案例預期 found；模糊／遮擋預期 unknown；錯誤前提應 not_found 或 unknown；格式錯誤在 syntax／schema 層有限重試；安全覆寫要求應在 safety 層拒絕並記錄。
