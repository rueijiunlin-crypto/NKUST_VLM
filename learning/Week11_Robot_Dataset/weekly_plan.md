# Week11 Weekly Plan：Robot Dataset and Demonstrations

## 本週目標

- 建立可重現的 robot episode 與 demonstration 資料結構。
- 能檢查時間對齊、資料品質、split 與 leakage。

## 必學概念

Episode、Trajectory、Demonstration、Teleoperation、observation-action alignment、dataset schema、split、variation、failed demonstration、data quality 與 leakage。

## 建議學習順序

1. 閱讀 `notes.md` 並畫出 episode schema。
2. 執行 schema 與 dataset audit Demo。
3. 完成 dataset validator Implementation Practice。
4. 將資料品質與 failed demonstration 觀察記錄到 `study_log.md`。

## Demo 執行順序

```powershell
python demo/demo_01_episode_schema.py
python demo/demo_02_dataset_audit.py
python practice/coding/solutions/dataset_validator_solution.py
```

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行兩個 Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `dataset_validator_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 alignment、leakage 與 failure case。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)

模式：Implementation Practice。

## 驗收條件

- [ ] 能畫出 episode schema。
- [ ] 能檢查 observation-action timestamp alignment。
- [ ] 能設計 train／validation split，避免 episode leakage。
- [ ] 能記錄 failed demonstrations 而非任意刪除。

## 銜接 Week12

Week12 將把同一 observation schema 送入預訓練 VLA。
