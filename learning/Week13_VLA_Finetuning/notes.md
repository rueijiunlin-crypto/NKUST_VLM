# Week13 Notes：VLA Fine-tuning

## 1. Task Adaptation

Fine-tuning 從 pretrained parameters 開始，用目標 robot dataset 更新權重；不等於從零訓練，也不保證跨 robot／camera 泛化。

## 2. Training Step

Batch 提供 observations 與 target actions。模型預測、計算 loss、反向傳播、optimizer update。Learning rate 太大可能破壞預訓練能力，太小可能無法適應。

## 3. Epoch、Checkpoint、Validation

Epoch 是資料遍歷；checkpoint 應保存 model、optimizer、step、config、normalization 與 dataset revision。Validation 不參與更新，用於選模型與發現 overfitting。

## 4. Overfitting

Train loss 降而 validation loss 上升是警訊。需檢查 task variation、split leakage、augmentation、regularization 與 early stopping，而非只增加 epoch。

## 5. Distribution Shift

Camera、lighting、robot dynamics、instruction 或 action scale 改變都會造成 shift。評估 split 要覆蓋預期部署條件。

## 6. Research Boundary

Toy linear model只驗證 optimization 機制；不能作為大型 VLA fine-tuning 成效證據。
