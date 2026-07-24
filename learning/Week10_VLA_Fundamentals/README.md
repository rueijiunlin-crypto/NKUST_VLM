# Week10 Embodied AI + VLA Fundamentals

## 本週定位

本週第一次正式學習 Vision-Language-Action Model（視覺語言動作模型，VLA），比較 VLM 的 semantic／text output 與 VLA 的明確 action representation。以架構理解為主，不訓練大型模型。

舊 ROS2 semantic interface、QoS 與防禦性 subscriber 教材完整保存在 `legacy_v1/`，未來仍可作為 Policy 與系統通訊介面參考。

## 與前週銜接、本週目標與資料流

Week09 定義 embodied observation；本週理解 VLA 如何將 Vision + Language + State 映射成 action chunk（動作區塊）。目標是能比較 VLM text／semantic output、VLA continuous/discrete action、chunk size、normalization 與控制頻率。

## 文件、Demo、Practice 與 Paper

依 `weekly_plan.md` → `notes.md` → `demo/demo_README.md` → `practice/README.md` 學習。Basic Demo 說明 What；SmolVLA config inspection 讀取真實 checkpoint 介面但不推論。論文驗收需畫出 architecture、列出 action representation、training objective、experiment 與至少一個 action/state ablation。

## Hardware Requirements / Environment / Download / Troubleshooting

Basic Track 可離線執行；Real Inspection Track 需要 `huggingface_hub`，只抓取 pinned revision 的 config／metadata，下載量遠小於權重。若 config schema 隨 LeRobot 版本變動，保存原始 config 與套件版本，不猜測缺失欄位；授權與 cache 詳見 `demo/real_track_README.md`。

## 能力邊界、論文與下週

讀懂 config 不等於完成 runtime validation，也不能把 action 直接送到硬體。這一週形成 model-interface audit，可支援論文 baseline 描述；Week11 接著檢查訓練與評估所需的真實 robot dataset schema。
