# Week16 Notes：Research Prototype and Evaluation

## 1. Research Question 與 Hypothesis

問題需指定系統、輸入、輸出、比較對象與可觀察結果。Hypothesis 必須可被 evidence 支持或反駁，不能只是「完成一個系統」。

## 2. Baseline 與 Proposed Method

Baseline 應代表合理現有方法；比較需固定 dataset、split、hardware、prompt／checkpoint、action convention 與其他 controlled variables。

## 3. Metric 與 Ground Truth

Metric 可含 task success、grounding accuracy、action error、latency、throughput、memory 與 safety violations。每個 metric 需定義單位、方向、聚合方式與 ground truth 來源。

## 4. Test Cases 與 Failure Cases

Test matrix 應涵蓋正常、邊界、missing／stale、domain shift 與 safety rejection。Failure 不是刪除對象，而是定位 perception、state、policy、control 或 safety 的證據。

## 5. Reproducibility

保存 code revision、environment、model／dataset revision、seed、config、raw result、metric script 與 hardware。只保存最佳截圖不可重現。

## 6. Ablation

Ablation 一次移除或改變一個元件，回答該元件是否真正貢獻結果；它不等於任意多跑幾組參數。

## 7. Limitation 與 Conclusion

Conclusion 必須受 evidence 邊界限制。未測真實機器人、樣本過少、模型下載受限或硬體不足都應明確列為 limitation。
