# Week16 Integrated Evaluation Track

- Entry：`python demo/demo_03_integrated_evaluation.py --events results.jsonl`
- Input schema：每行至少含 `latency_ms`，並建議含 `valid`、`success`、`safety_rejected`、case/revision。
- Output：樣本數、valid/success/safety rejection rate、latency p50/p95/p99。
- Boundary：只分析 recorded events，不呼叫模型或 controller。
- Artifact：連同 raw JSONL、config、Git/model/data revision、hardware 與 failure cases 保存。
