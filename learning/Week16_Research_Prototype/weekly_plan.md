# Week16 Weekly Plan：Research Prototype and Evaluation

## 本週目標

- 將機器人 VLM／VLA 系統收斂成可驗證的 research prototype。
- 建立從 research question 到 conclusion 的可追溯 evidence chain。

## 必學概念

Research question、hypothesis、baseline、controlled variables、metric、ground truth、test／failure cases、latency、reproducibility、ablation concept、limitation。

## 建議學習順序

1. 閱讀 `notes.md` 並定義 research question 與 hypothesis。
2. 執行 evaluation matrix 與 metric summary Demo。
3. 執行 Guided evidence chain，再完成 result validator。
4. 填寫 evaluation plan、failure record 與 limitation。

## Demo 執行順序

```powershell
python demo/demo_01_evaluation_matrix.py
python demo/demo_02_metric_summary.py
python practice/coding/guided_demos/guided_evidence_chain.py
python practice/coding/solutions/result_validator_solution.py
```

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行兩個 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `result_validator_practice.py` 後再比較 solution。
- [ ] 在 `coding_practice.md` 與 `study_log.md` 記錄 evidence、failure 與 limitation。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

模式：Research / Guided Code Reading / Implementation mixed mode。

## 驗收條件

- [ ] 研究問題可被實驗回答。
- [ ] 有合理 baseline 與 controlled variables。
- [ ] Metric 有定義、ground truth 與 test cases。
- [ ] 保存 failure cases、latency、環境與 seed。
- [ ] Conclusion 不超出 evidence。
- [ ] 明確列出 limitation 與未完成驗證。
