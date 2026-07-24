# Week08 Spatial Reasoning and Grounding

## 本週定位

本週建立 Semantic Object → 2D Grounding → Pixel／Box／Mask → Depth → 3D Camera Coordinate → Robot Coordinate。使用 NumPy／標準函式庫 mock data，不強迫依賴 RealSense。舊 Mini Project 與 observation contract 保存在 `legacy_v1/`，其 `observation_id`、timestamp、structured result 與 validator 概念整合為 Spatial Observation schema。

依序使用 `weekly_plan.md`、`notes.md`、`demo/` 與混合模式 `practice/`。

## 與前週銜接、目標與資料流

Week07 的 semantic JSON 只能回答「看見什麼」；本週補上「在影像哪裡、對應相機與機器人座標何處」。完成後應能檢查 intrinsics（內參）、depth scale、extrinsics（外參）、單位、座標方向與重投影誤差。

## 文件、Demo、Practice 與 Paper

先讀 `notes.md`，再執行 `demo/demo_README.md` 列出的 2D grounding 與 pixel-to-3D Basic Demo，最後完成 `practice/README.md` 的 Guided／Implementation 任務。論文驗收須說明 grounding 表示、幾何假設、評估指標與至少一項 calibration／depth ablation。

## Hardware Requirements / Environment / Download / Troubleshooting

必修主線只需 NumPy mock data，無下載與 GPU；真實相機延伸需保存相機型號、intrinsics/extrinsics revision、depth scale、對齊設定與資料授權。常見錯誤是 mm/m 混用、`T_camera_robot` 方向顛倒、無效深度、像素 row/column 混淆。

## 能力邊界、論文與下週

幾何投影不會自動解決遮擋、可達性或語意錯認。可將 calibration residual 與 3D error 納入論文 reproducibility（可重現性）證據；Week09 會把視覺／語言結果與 robot state、timestamp 對齊成 embodied observation。
