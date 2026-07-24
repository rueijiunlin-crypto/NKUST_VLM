# Week16 Integrated Evaluation Track

- Entry：`python demo/demo_03_integrated_evaluation.py --events results.jsonl`
- Input schema：每行至少含 `latency_ms`，並建議含 `valid`、`success`、`safety_rejected`、case/revision。
- Output：樣本數、valid/success/safety rejection rate、latency p50/p95/p99。
- Boundary：只分析 recorded events，不呼叫模型或 controller。
- Artifact：連同 raw JSONL、config、Git/model/data revision、hardware 與 failure cases 保存。

## 執行契約與可重現性

- Required：整合評估與 My Method vs Paper Method matrix 為必修。
- Model / Framework：評估器無模型依賴；被評估 pipeline 的 model/framework/revision 必須由 event manifest 提供。
- Data：使用已授權的 recorded JSONL；記錄 schema version、case split、source、license 與 immutable hash/revision。
- Download / Auth：評估器無下載或登入；上游模型／資料沿用各週條款。
- Hardware：CPU/RAM 即可；上游 runtime hardware 仍需逐 run 記錄。
- Cache / Artifact：保存 raw JSONL、config、Git commit、model/data revision、environment lock、metrics 與 failure samples。
- Target versions — verify before execution：Python 3.10/3.11、標準函式庫；上游 framework 版本由 manifest pin。
- VRAM / System RAM / CUDA / dtype / quantization：評估器不需要 GPU/CUDA/quantization，一般 RAM 即可；上游 runtime metadata 不得省略。

```powershell
python demo/demo_03_integrated_evaluation.py --events results.jsonl
```

預期輸出 sample count、valid/success/safety rejection rate、latency p50/p95/p99。缺欄位、混合 revision 或無 case ID 時不得形成研究結論。此腳本只分析 log，不呼叫模型／controller；最終比較表需明確列出 My Method、Paper Method、差異、證據與尚未重現項目。
