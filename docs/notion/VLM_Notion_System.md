# VLM/VLA 碩士研究管理系統

本文件用於規劃 Notion（筆記與資料庫管理工具）中的研究管理系統，核心聚焦 Vision-Language Model（視覺語言模型）、Vision-Language-Action Model（視覺語言動作模型）、ROS2（機器人作業系統第二版）與 Isaac Sim（NVIDIA 機器人模擬器）。

## 1. Dashboard

用途：

- 每週學習目標
- 本月進度
- 目前研究方向
- 待完成任務
- Codex 任務追蹤
- GitHub 連結

區塊：

- 本週目標
- 本月目標
- 目前進度
- 目前論文方向
- 最近實驗
- 待閱讀論文
- 待詢問 ChatGPT 的問題

建議呈現方式：

- 最上方放置本週目標與目前論文方向。
- 中間放置 Learning Roadmap Database（學習路線資料庫）與 Experiment Log Database（實驗紀錄資料庫）的 linked view（連結視圖）。
- 下方放置 Paper Database（論文資料庫）、Codex 任務追蹤與 GitHub（版本控制平台）連結。

## 2. Learning Roadmap Database

欄位：

- Week
- Topic
- Status
- Priority
- Start Date
- End Date
- GitHub Folder
- Related Papers
- Notes
- Output

預設 Week01 到 Week16：

| Week | Topic | GitHub 對應資料夾 |
| --- | --- | --- |
| Week01 | Transformer 基礎 | `learning/Week01_Transformer/` |
| Week02 | CLIP | `learning/Week02_CLIP/` |
| Week03 | Hugging Face | `learning/Week03_HuggingFace/` |
| Week04 | LLaVA | `learning/Week04_LLaVA/` |
| Week05 | VLM Architecture | `learning/Week05_VLM_Architecture/` |
| Week06 | Video and Streaming VLM | `learning/Week06_Video_Streaming_VLM/` |
| Week07 | ROS2 + Camera + Realtime VLM | `learning/Week07_Realtime_VLM_ROS2/` |
| Week08 | Spatial Reasoning and Grounding | `learning/Week08_Spatial_Grounding/` |
| Week09 | Robot State + Multimodal Observation | `learning/Week09_Robot_State/` |
| Week10 | Embodied AI + VLA Fundamentals | `learning/Week10_VLA_Fundamentals/` |
| Week11 | Robot Dataset and Demonstrations | `learning/Week11_Robot_Dataset/` |
| Week12 | SmolVLA / OpenVLA Inference | `learning/Week12_VLA_Inference/` |
| Week13 | VLA Fine-tuning | `learning/Week13_VLA_Finetuning/` |
| Week14 | Isaac Sim Robot Learning | `learning/Week14_IsaacSim_Robot_Learning/` |
| Week15 | Sim-to-Real / Real Robot Deployment | `learning/Week15_Sim2Real/` |
| Week16 | Research Prototype and Evaluation | `learning/Week16_Research_Prototype/` |

每一週頁面都要包含：

- 學習目標
- 必懂概念
- 實作任務
- 驗收標準
- GitHub 對應資料夾
- Notion 紀錄項目

### Week01 Transformer 基礎

- 學習目標：理解 Token（詞元）、Embedding（嵌入向量）與 Attention（注意力機制）。
- 必懂概念：Transformer Encoder（轉換器編碼器）、Transformer Decoder（轉換器解碼器）。
- 實作任務：整理資料流圖與概念筆記。
- 驗收標準：能說明為什麼 VLM 需要 Transformer。
- GitHub 對應資料夾：`learning/Week01_Transformer/`
- Notion 紀錄項目：概念筆記、資料流圖、下週 CLIP 問題。

### Week02 CLIP

- 學習目標：理解 CLIP（對比式圖文預訓練）的圖文對齊概念。
- 必懂概念：Image Encoder（影像編碼器）、Text Encoder（文字編碼器）、Similarity（相似度）。
- 實作任務：以圖片與多個文字標籤進行相似度測試。
- 驗收標準：能說明共同向量空間如何支援分類與檢索。
- GitHub 對應資料夾：`learning/Week02_CLIP/`
- Notion 紀錄項目：測試圖片、候選文字、相似度結果。

### Week03 Hugging Face

- 學習目標：能使用 Hugging Face（模型平台）與 PyTorch（深度學習框架）執行模型推論。
- 必懂概念：Processor（處理器）、Model（模型）、CUDA（GPU 運算平台）。
- 實作任務：下載模型並完成一次推論。
- 驗收標準：能記錄環境、模型與輸出結果。
- GitHub 對應資料夾：`learning/Week03_HuggingFace/`
- Notion 紀錄項目：模型名稱、硬體環境、執行結果。

### Week04 LLaVA

- 學習目標：理解 LLaVA（大型語言與視覺助手）的影像問答流程。
- 必懂概念：Vision Encoder、Projector、Large Language Model（大型語言模型）。
- 實作任務：對圖片提出問題並取得文字回答。
- 驗收標準：能分析回答是否符合影像內容。
- GitHub 對應資料夾：`learning/Week04_LLaVA/`
- Notion 紀錄項目：圖片、問題、回答、錯誤案例。

### Week05 VLM Architecture

- 學習目標：能畫出典型 VLM 架構。
- 必懂概念：影像特徵、文字特徵、跨模態對齊。
- 實作任務：整理 LLaVA 類模型流程圖。
- 驗收標準：能說明 Camera（相機）到 Answer（回答）的資料流。
- GitHub 對應資料夾：`learning/Week05_VLM_Architecture/`
- Notion 紀錄項目：架構圖、輸入輸出、限制。

### Week06 Video and Streaming VLM

- 學習目標：建立 multi-frame、video 與 streaming temporal perception。
- 必懂概念：Frame Sampling、Temporal Context、KV Cache、latency／throughput。
- 實作任務：比較 Camera FPS 與 inference FPS，分析 sliding window。
- 驗收標準：能說明即時串流的 token、memory 與 freshness 取捨。
- GitHub 對應資料夾：`learning/Week06_Video_Streaming_VLM/`
- Notion 紀錄項目：取樣設定、token budget、延遲與論文閱讀條目。

### Week07 ROS2 + Camera + Realtime VLM

- 學習目標：建立 Camera、ROS2、非同步推論與 semantic topic 管線。
- 必懂概念：FPS、timestamp、Topic、QoS、queue、stale frame、structured result。
- 實作任務：用 mock queue 驗證 latest-frame 與 freshness policy。
- 驗收標準：能設計可驗證且不等同控制命令的 semantic interface。
- GitHub 對應資料夾：`learning/Week07_Realtime_VLM_ROS2/`
- Notion 紀錄項目：rate、QoS、schema、unknown／retry 與錯誤結果。

### Week08 Spatial Reasoning and Grounding

- 學習目標：建立 semantic → 2D → depth → 3D → robot frame 資料鏈。
- 必懂概念：Box／Mask、intrinsics、extrinsics、coordinate transform。
- 實作任務：以 mock depth 完成 pixel-to-3D 與 frame transform。
- 驗收標準：能區分語意位置、像素、相機座標與機器人座標。
- GitHub 對應資料夾：`learning/Week08_Spatial_Grounding/`
- Notion 紀錄項目：Spatial Observation schema、標定與不確定性。

### Week09 Robot State + Multimodal Observation

- 學習目標：整合 Vision、Language 與 Robot State。
- 必懂概念：proprioception、joint／end-effector／gripper／camera pose、sync。
- 實作任務：建立 mock embodied observation 並檢查 missing／stale state。
- 驗收標準：能定義 observation space 與 sensor alignment。
- GitHub 對應資料夾：`learning/Week09_Robot_State/`
- Notion 紀錄項目：state schema、timestamp delta、missing policy。

### Week10 Embodied AI + VLA Fundamentals

- 學習目標：區分 VLM semantic output 與 VLA action policy。
- 必懂概念：Policy、Observation、Action Space、Action Chunk、open／closed-loop。
- 實作任務：追蹤 policy loop 並實作 action validator。
- 驗收標準：能說明 VLA 與 Control／Safety 邊界。
- GitHub 對應資料夾：`learning/Week10_VLA_Fundamentals/`
- Notion 紀錄項目：action schema、loop、safety rejection。

### Week11 Robot Dataset and Demonstrations

- 學習目標：理解 demonstrations 與 episode dataset。
- 必懂概念：trajectory、teleoperation、alignment、split、quality、leakage。
- 實作任務：建立並驗證最小 episode schema。
- 驗收標準：能檢查 observation-action alignment 與 split。
- GitHub 對應資料夾：`learning/Week11_Robot_Dataset/`
- Notion 紀錄項目：dataset revision、schema、quality audit。

### Week12 SmolVLA / OpenVLA Inference

- 學習目標：理解預訓練 VLA 的 observation-to-action 推論介面。
- 必懂概念：processor、normalization、action chunk、device、latency。
- 實作任務：先驗證 Basic Policy Adapter，再依硬體選做真實模型。
- 驗收標準：能解讀 observation／action shape 與 checkpoint metadata。
- GitHub 對應資料夾：`learning/Week12_VLA_Inference/`
- Notion 紀錄項目：model revision、硬體、latency、skipped reason。

### Week13 VLA Fine-tuning

- 學習目標：由 pretrained VLA 進入 task adaptation。
- 必懂概念：batch、training step、LR、checkpoint、validation、overfitting、shift。
- 實作任務：以 tiny policy 實作 training step 與 validation curve。
- 驗收標準：能保存可重現 checkpoint 與分析 train／validation gap。
- GitHub 對應資料夾：`learning/Week13_VLA_Finetuning/`
- Notion 紀錄項目：dataset／model revision、曲線、checkpoint、限制。

### Week14 Isaac Sim Robot Learning

- 學習目標：建立 Scene、Robot、Sensors、Task、Policy、Evaluation。
- 必懂概念：USD、RGB／Depth、ground truth、synthetic data、randomization。
- 實作任務：建立受控 experiment config 與 randomization。
- 驗收標準：能區分 observation、ground truth 與 controlled variable。
- GitHub 對應資料夾：`learning/Week14_IsaacSim_Robot_Learning/`
- Notion 紀錄項目：scene／asset revision、seed、task、metric。

### Week15 Sim-to-Real / Real Robot Deployment

- 學習目標：分析 simulation／real domain gap 與部署安全。
- 必懂概念：noise、calibration、latency、action error、recovery、checklist。
- 實作任務：建立 latency budget、fault injection 與 deployment gate。
- 驗收標準：能提出 hardware-ready 或 real-robot validation evidence。
- GitHub 對應資料夾：`learning/Week15_Sim2Real/`
- Notion 紀錄項目：domain gap、fault、recovery、未驗證限制。

### Week16 Research Prototype and Evaluation

- 學習目標：完成可評估、可重現的 Robot VLM/VLA Research Prototype。
- 必懂概念：question、baseline、metric、ground truth、failure、ablation、limitation。
- 實作任務：建立 evaluation matrix、result schema 與 failure analysis。
- 驗收標準：結論有 evidence，且不把 Demo 成功等同研究完成。
- GitHub 對應資料夾：`learning/Week16_Research_Prototype/`
- Notion 紀錄項目：研究問題、baseline、raw result、metric、failure、limitation。

## 3. Paper Database

欄位：

- Paper Title
- Year
- Category
- Status
- Importance
- Link
- Code
- Related Week
- Summary
- Possible Thesis Usage

預設分類：

- VLM
- VLA
- Robot Learning
- Embodied AI
- ROS2 Integration
- Isaac Sim

預設論文條目：

| Paper Title | Category | Related Week | Possible Thesis Usage |
| --- | --- | --- | --- |
| CLIP | VLM | Week02 | 圖文對齊與語意標籤比對 |
| Attention Is All You Need | Foundation | Week01 | Transformer 與 attention 共同骨架 |
| LLaVA | VLM | Week04 | 影像問答與機器人場景理解 |
| BLIP | VLM | Week05 | 影像描述與視覺語言預訓練架構比較 |
| BLIP-2 | VLM | Week05 | Q-Former 與凍結模型介面 |
| MovieChat | Video VLM | Week06 | 長影片 sparse memory 與時間理解 |
| RT-1 | VLA | Week07 | 即時機器人資料流、token 與系統邊界 |
| 3D-LLM | Spatial Grounding | Week08 | 3D-language alignment 與空間推理 |
| PaLM-E | Embodied AI | Week09 | 影像、語言與 robot state 融合 |
| RT-2 | VLA | Week10 | VLA action token 與知識轉移 |
| Open X-Embodiment | Robot Dataset | Week11 | 跨 embodiment 資料標準化 |
| SmolVLA | VLA | Week12 | 可負擔 VLA inference 與 flow matching |
| Octo | Robot Learning | Week13 | Generalist policy fine-tuning |
| Isaac Lab | Isaac Sim | Week14 | GPU 模擬、感測器與任務介面 |
| Domain Randomization | Sim-to-Real | Week15 | 模擬到真實的變異假設 |
| OpenVLA | VLA | Week16 | 開源研究原型與 evaluation 比較 |

每篇論文模板需包含：

- 研究問題
- 方法
- 架構
- Dataset
- Experiment
- 優點
- 缺點
- 與我的研究關聯
- 是否值得深入閱讀

## 4. Experiment Log Database

欄位：

- Date
- Experiment Name
- Category
- Status
- Environment
- GPU
- Repository Folder
- Result
- Problem
- Next Step

模板：

- 實驗目的
- 實驗環境
- 使用模型
- 使用資料
- 執行步驟
- 結果
- 錯誤紀錄
- 修正方式
- 結論
- 下一步

## 5. Isaac Sim & ROS2 Page

注意：這裡不得包含本專案排除項目的主題內容。

主題只包含：

- Isaac Sim 基礎
- Camera Sensor
- ROS2 Bridge
- Topic
- Service
- Action
- TF
- Navigation
- VLM Integration
- Robot Simulation
- Reinforcement Learning

建立子頁面規劃：

- Isaac Sim Notes
- ROS2 Notes
- Camera Integration
- VLM to ROS2 Pipeline
- Navigation Notes
- Simulation Experiment Log

## 6. Thesis Research Database

欄位：

- Topic
- Status
- Feasibility
- Novelty
- Difficulty
- Required Skills
- Related Papers
- Related Experiments
- Risk
- Next Action

預設題目：

- VLM 室內語意導覽機器人
- VLM 災害巡檢機器人
- VLM 桌面操作機器人
- VLM + ROS2 語意導航系統
- Isaac Sim 中的 VLM 機器人模擬平台

每個題目模板：

- 研究動機
- 問題定義
- 系統架構
- 創新點
- 技術難點
- 需要閱讀的論文
- 需要完成的實驗
- 可行性分析
- 預期成果

## 建置順序建議

1. 建立 Dashboard。
2. 建立 Learning Roadmap Database，先填 Week01 到 Week16。
3. 建立 Paper Database，先填入預設論文條目。
4. 建立 Experiment Log Database，作為每次實作紀錄入口。
5. 建立 Isaac Sim & ROS2 Page，整理模擬與機器人中介軟體筆記。
6. 建立 Thesis Research Database，持續比較論文題目。

