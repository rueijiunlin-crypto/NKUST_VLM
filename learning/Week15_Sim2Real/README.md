# Week15 Sim-to-Real / Real Robot Deployment

## 本週定位

本週比較 Simulation 與 Real World 的 domain shift、感測／標定／延遲／action error、安全與 failure recovery。沒有實體 Robot 時，以 hardware-ready pipeline 或 Sim-to-Real analysis 驗收。舊占位內容在 `legacy_v1/`。

## 與前週銜接、本週目標與資料流

Week14 產生 sim RGB/depth、state 與 ground truth；本週必須把 Simulation Observation 與 Real Observation 分欄保存，而不是只比較兩張未標來源圖片。完成後應能描述 visual、sensor、dynamics、latency 與 calibration gap，以及哪些 proxy metric 不能代表 task success。

## 文件、Demo、Practice 與 Paper

依 `weekly_plan.md` → `notes.md` → `demo/demo_README.md` → `practice/README.md` 執行。Demo 03 計算 paired case 的 image statistics，學生另記 camera/Isaac revision、calibration、timestamp、model/prompt revision。論文驗收需列 domain gap 假設、adaptation method、real-world metric、safety protocol 與 sim-only vs sim+real ablation。

## Hardware Requirements / Environment / Download / Cache / Troubleshooting

分析程式需要 NumPy/OpenCV，不需 GPU；輸入需由合法來源取得並保存 case ID，不提交受限資料。shape、color order、exposure 或裁切不一致時先完成 normalization，再比較。沒有真實硬體可標為 Hardware blocked，但仍須完成 real observation schema、採集計畫與風險清單。

## 安全邊界、論文與下週

亮度／noise proxy 不能證明 policy transfer 成功；任何 real robot test 都需 workspace、速度、急停、observer 與 rollback。Week16 將把這些限制放入 My Method vs Paper Method 與最終 evaluation matrix。
