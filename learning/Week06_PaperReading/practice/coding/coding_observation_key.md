# Week06 Coding Observation Key

> 請先完成實際論文閱讀與 `coding_practice.md`，再查看本指引。

## 1. Research Question Flow

Topic 只描述領域；research question 必須指出可操控或比較條件、可觀察結果與證據。若 gap 只寫「很少人做」，通常還不足以形成研究問題。

## 2. Method-to-Experiment Mapping

方法新增的核心元件應有 ablation、matched baseline（匹配基準）或其他控制證據。只有整體分數改善，通常無法單獨證明改善由某一元件造成。

## 3. Claim-to-Evidence Validation

「模型更好」缺少 task、metric、baseline 與 setting，屬不可驗證主張。可追溯紀錄還需限制範圍，避免把局部結果推廣到所有任務。

## 4. Comparison Matrix

固定欄位能避免只摘錄每篇論文最亮眼的結果。缺失資訊應標記 Unknown／Not reported，不應自行推測填滿。

## 常見誤解修正

- Abstract 是作者摘要，不是完整證據。
- Higher score 不必然代表可直接比較。
- Parameter 少不必然代表 latency 低。
- Qualitative case 不代表整體可靠性。
- 引用來源不代表自己的推論已被來源直接證明。
