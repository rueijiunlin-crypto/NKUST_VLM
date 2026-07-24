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

## Paper Reading（論文閱讀）

### Core Reading

- Title: OpenVLA: An Open-Source Vision-Language-Action Model
- Authors: Moo Jin Kim et al.
- Year / Venue: 2024 / CoRL
- DOI: N/A
- arXiv: 2406.09246
- Link: https://arxiv.org/abs/2406.09246
- Code / Project / Model: https://github.com/openvla/openvla / https://openvla.github.io/
- Required Reading：Abstract、architecture、training data、evaluation、limitations。
- Skim Reading：完整訓練基礎設施與附錄。
- Skip for Now：7B 模型從零預訓練。
- Optional Reading：依最後題目選 1–3 篇最接近的 baseline／evaluation 論文。

### Reading Questions

1. OpenVLA 的研究主張與適用邊界是什麼？
2. Prototype 的 perception、state、policy、evaluation 介面為何？
3. 模型內外部資料流如何連接？
4. 每個模組的 tensor／message shape 如何驗證？
5. Action representation 如何影響部署？
6. Baseline 為何足以回答研究問題？
7. Metric、threshold 與 safety gate 如何設定？
8. 論文使用哪些資料集、任務與指標？
9. 哪項結果最能支持其主要 claim？
10. License、硬體、資料與 validity 限制是什麼？
11. 本課程原型與論文系統有哪些可比／不可比處？
12. 哪三項 evidence 能形成論文 proposal 的論證鏈？

### Deep Reading

完成 Evidence Table、Comparison Matrix、Reproducibility Check 與 Thesis Literature Review Usage；若研究題目已收斂，另選一篇直接 baseline 取代泛讀材料。

## 驗收條件

- [ ] 研究問題可被實驗回答。
- [ ] 有合理 baseline 與 controlled variables。
- [ ] Metric 有定義、ground truth 與 test cases。
- [ ] 保存 failure cases、latency、環境與 seed。
- [ ] Conclusion 不超出 evidence。
- [ ] 明確列出 limitation 與未完成驗證。
