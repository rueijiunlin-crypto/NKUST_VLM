# Week13 Weekly Plan：VLA Fine-tuning

## 本週目標

- 理解 VLA task adaptation 的訓練與驗證資料流。
- 建立小型可重現 training step 與 checkpoint 紀錄。

## 必學概念

Pretrained Model、Task Adaptation、Batch、Training Step、Epoch、Learning Rate、Checkpoint、Validation、Overfitting、Distribution Shift 與 Evaluation Split。

## 建議學習順序

1. 閱讀 `notes.md` 並畫出 dataset-to-checkpoint flow。
2. 執行 tiny fine-tune 與 validation curve Demo。
3. 完成 training step Implementation Practice。
4. 比較 train／validation 指標並記錄重現條件。

## Demo 執行順序

```powershell
python demo/demo_01_tiny_finetune.py
python demo/demo_02_validation_curve.py
python practice/coding/solutions/training_step_solution.py
```

## 任務清單

- [ ] 閱讀本週文件。
- [ ] 執行兩個 Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `training_step_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 seed、split、learning rate 與 failure case。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)

模式：Implementation Practice。

## 驗收條件

- [ ] 能區分 pretraining、fine-tuning 與 inference。
- [ ] 能解釋 train／validation split。
- [ ] 能辨識 overfitting 與 distribution shift。
- [ ] 能保存可重現 checkpoint metadata。

## 銜接 Week14

Week14 以 Isaac Sim 建立受控資料與 policy evaluation 環境。
