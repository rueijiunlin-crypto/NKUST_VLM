# Week16 Research Prototype and Evaluation

## 本週定位

最終週不是只完成 Final Demo，而是建立：

```text
Research Question → Baseline → Proposed Method → Dataset
→ Experiment → Metric → Result → Failure Analysis
→ Limitation → Conclusion
```

Research／Implementation mixed mode。舊占位內容保存在 `legacy_v1/`。

## 與前週銜接、本週目標與資料流

Week15 產生 sim-to-real gap 與安全限制；本週將 Week01–15 的模型、資料、runtime evidence 與 failure cases 整合成可答辯的研究原型。目標不是堆疊功能，而是讓每個主張可追溯到 baseline、metric、raw result 與 limitation。

## 文件、Demo、Practice 與 Paper

依 `weekly_plan.md` 定義 Research Question、Baseline、My Method、Dataset、Metric 與 acceptance threshold，再執行 `demo/demo_README.md` 的 integrated evaluation，完成 `practice/README.md`。Paper Reading 必須填寫 My Method vs Paper Method matrix：problem、input/output、architecture、data、training、metric、hardware、result、failure、limitation 與 reproduction gap。

## Hardware Requirements / Environment / Download / Run / Troubleshooting

評估程式只讀 JSONL recorded events，不下載模型也不控制硬體；原型所依賴的模型／資料／Isaac／ROS2 環境則沿用各週 pinned metadata。若 event schema、case ID、revision 或 metric 缺失，應拒絕形成結論並回到來源週補證據。

## 邊界、論文與下一步

aggregate metric 不得掩蓋 invalid samples、safety rejection 或 tail latency；必須保存 p50/p95/p99、failure taxonomy 與 raw artifacts。完成後的下一步是收斂 thesis proposal、重跑可重現實驗與安排真實硬體安全驗證，不把課程完成狀態等同於研究結論成立。
