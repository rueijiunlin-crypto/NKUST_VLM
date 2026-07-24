# Week14 Notes：Isaac Sim Robot Learning

## 1. USD Scene 與 Robot Asset

USD 描述場景、階層、材質與資產。Robot asset 還需 articulation、joint limits、collision 與 controller 設定；載入模型不等於可做有效實驗。

## 2. Sensors 與 Ground Truth

RGB／Depth 是模擬感測觀察；semantic labels、instance IDs、真值 pose 可作 ground truth。訓練輸入與評估真值必須分開，避免把 simulator-only 資訊洩漏給部署 Policy。

## 3. Robot State 與 Task

Task Setup 定義初始狀態、目標、成功／失敗條件、timeout 與 reset。Robot State、action space 與 control rate 必須一致。

## 4. Synthetic Data

合成資料可控制場景與標註，但仍有 rendering、physics 與資產偏差。需保存 seed、scene revision、simulator version 與生成參數。

## 5. Domain Randomization

在合理範圍改變 lighting、texture、camera pose、object pose、noise 與 dynamics。範圍太窄無法泛化，太寬可能破壞任務語意。

## 6. Controlled Experiment

一次只改研究變因，固定 seed set、task cases、Policy checkpoint 與 metric。Demo 成功不等於研究結論。
