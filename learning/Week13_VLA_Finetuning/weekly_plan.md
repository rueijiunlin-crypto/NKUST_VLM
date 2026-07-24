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

## Paper Reading（論文閱讀）

### Core Reading

- Title: Octo: An Open-Source Generalist Robot Policy
- Authors: Octo Model Team et al.
- Year / Venue: 2024 / Robotics: Science and Systems
- DOI: N/A
- arXiv: 2405.12213
- Link: https://arxiv.org/abs/2405.12213
- Code / Project: https://github.com/octo-models/octo
- Required Reading：Abstract、architecture、pretraining data、fine-tuning、evaluation。
- Skim Reading：完整 optimizer 與集群設定。
- Skip for Now：大規模預訓練重現。
- Optional Reading：SmolVLA training guide；LoRA。

### Reading Questions

1. Generalist policy fine-tuning 要解決什麼轉移問題？
2. 預訓練 checkpoint 與新資料的介面為何？
3. Observation、task、action 如何 tokenize？
4. Batch、window、action chunk shape 如何設定？
5. 哪些參數被更新或凍結？
6. Normalization 與 dataset statistics 如何影響結果？
7. Overfitting 要如何由 train／validation curve 判斷？
8. 使用哪些 fine-tuning 任務與指標？
9. 哪項結果支持預訓練遷移？
10. 小資料、硬體與 seed 的限制是什麼？
11. SmolVLA 小型實驗要保存哪些 artifact？
12. 哪個 failure case 最值得轉成研究問題？

### Deep Reading

比較 full fine-tuning、parameter-efficient tuning 與從零訓練；本週實驗不得把尚未執行的結果寫成完成。

## 驗收條件

- [ ] 能區分 pretraining、fine-tuning 與 inference。
- [ ] 能解釋 train／validation split。
- [ ] 能辨識 overfitting 與 distribution shift。
- [ ] 能保存可重現 checkpoint metadata。

## 銜接 Week14

Week14 以 Isaac Sim 建立受控資料與 policy evaluation 環境。
