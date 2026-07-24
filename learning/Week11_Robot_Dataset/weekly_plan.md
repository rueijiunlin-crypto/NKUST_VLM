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

## Paper Reading（論文閱讀）

### Core Reading

- Title: Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- Authors: Open X-Embodiment Collaboration
- Year / Venue: 2024 / ICRA
- DOI: N/A
- arXiv: 2310.08864
- Link: https://arxiv.org/abs/2310.08864
- Code / Project: https://github.com/google-deepmind/open_x_embodiment
- Required Reading：Abstract、dataset mixture、standardization、RT-X experiments、limitations。
- Skim Reading：各資料集逐項統計。
- Skip for Now：完整跨機器人訓練重現。
- Optional Reading：LeRobotDataset v3 documentation；DROID。

### Reading Questions

1. 跨 embodiment 資料整合的核心問題是什麼？
2. Episode、observation、action、task 的輸入輸出為何？
3. 不同資料集如何標準化？
4. Image、state、action、timestamp 的 shape 如何記錄？
5. Task vocabulary 如何對齊？
6. Sampling mixture 如何影響模型？
7. 資料 provenance 與 license 為何重要？
8. 使用哪些跨機器人評估？
9. 哪項結果支持資料共訓練？
10. Action space 與硬體差異造成哪些限制？
11. LeRobot sample 的 schema 如何對應論文概念？
12. 哪些資料品質證據必須寫入 dataset card？

## 驗收條件

- [ ] 能畫出 episode schema。
- [ ] 能檢查 observation-action timestamp alignment。
- [ ] 能設計 train／validation split，避免 episode leakage。
- [ ] 能記錄 failed demonstrations 而非任意刪除。

## 銜接 Week12

Week12 將把同一 observation schema 送入預訓練 VLA。
