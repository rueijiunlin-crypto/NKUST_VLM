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
|---|---|---|
| Week01 | Transformer 基礎 | `learning/Week01_Transformer/` |
| Week02 | CLIP | `learning/Week02_CLIP/` |
| Week03 | Hugging Face | `learning/Week03_HuggingFace/` |
| Week04 | LLaVA | `learning/Week04_LLaVA/` |
| Week05 | VLM Architecture | `learning/Week05_VLM_Architecture/` |
| Week06 | VLM Paper Reading | `learning/Week06_PaperReading/` |
| Week07 | Prompt Engineering | `learning/Week07_PromptEngineering/` |
| Week08 | Mini Project：Image Caption + Visual QA | `learning/Week08_MiniProject/` |
| Week09 | VLM + Camera | `learning/Week09_VLM_Camera/` |
| Week10 | VLM + ROS2 Topic | `learning/Week10_VLM_ROS2/` |
| Week11 | VLM + Navigation Concept | `learning/Week11_VLM_Navigation/` |
| Week12 | VLM Robot System Prototype | `learning/Week12_Robot_Prototype/` |
| Week13 | Isaac Sim Environment | `learning/Week13_IsaacSim_Environment/` |
| Week14 | Isaac Sim Camera | `learning/Week14_IsaacSim_Camera/` |
| Week15 | Isaac Sim + VLM | `learning/Week15_IsaacSim_VLM/` |
| Week16 | Final Mini Project | `learning/Week16_FinalProject/` |

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

### Week06 VLM Paper Reading

- 學習目標：建立論文閱讀流程。
- 必懂概念：研究問題、方法、資料集、實驗與貢獻。
- 實作任務：閱讀 CLIP 與 LLaVA 摘要與架構。
- 驗收標準：能用固定模板摘要論文。
- GitHub 對應資料夾：`learning/Week06_PaperReading/`
- Notion 紀錄項目：Paper Database 條目。

### Week07 Prompt Engineering

- 學習目標：設計適合機器人語境的 Prompt（提示）。
- 必懂概念：任務提示、輸出格式限制、錯誤回覆處理。
- 實作任務：設計語意導覽與物體辨識提示。
- 驗收標準：輸出能穩定轉成結構化結果。
- GitHub 對應資料夾：`learning/Week07_PromptEngineering/`
- Notion 紀錄項目：提示版本與測試結果。

### Week08 Mini Project：Image Caption + Visual QA

- 學習目標：完成 Image Caption（影像描述）與 Visual QA（視覺問答）小系統。
- 必懂概念：圖片輸入、文字問題、模型輸出。
- 實作任務：建立最小可執行範例。
- 驗收標準：能展示三組圖片問答結果。
- GitHub 對應資料夾：`learning/Week08_MiniProject/`
- Notion 紀錄項目：截圖、問題、回答、心得。

### Week09 VLM + Camera

- 學習目標：串接 Camera（相機）影像與 VLM 推論。
- 必懂概念：OpenCV、影像擷取、單張推論。
- 實作任務：從相機取得影像並輸入模型。
- 驗收標準：能得到場景描述。
- GitHub 對應資料夾：`learning/Week09_VLM_Camera/`
- Notion 紀錄項目：相機設定、影像、模型輸出。

### Week10 VLM + ROS2 Topic

- 學習目標：將 VLM 語意輸出發布為 ROS2 Topic。
- 必懂概念：rclpy、String Message（字串訊息）、semantic_description（語意描述）。
- 實作任務：建立語意發布節點。
- 驗收標準：能在終端機訂閱並看到語意文字。
- GitHub 對應資料夾：`learning/Week10_VLM_ROS2/`
- Notion 紀錄項目：節點名稱、Topic 名稱、輸出範例。

### Week11 VLM + Navigation Concept

- 學習目標：理解語意輸出如何轉成導航任務。
- 必懂概念：Semantic Landmark（語意地標）、Goal（目標）、Navigation（導航）。
- 實作任務：設計文字指令到目標描述的轉換規則。
- 驗收標準：能處理簡單目標物導覽案例。
- GitHub 對應資料夾：`learning/Week11_VLM_Navigation/`
- Notion 紀錄項目：指令、解析結果、導航概念圖。

### Week12 VLM Robot System Prototype

- 學習目標：完成 VLM × ROS2 小型系統雛型。
- 必懂概念：節點、資料流、錯誤處理。
- 實作任務：整合文字輸入、VLM 推論與語意 Topic。
- 驗收標準：能完成可展示流程。
- GitHub 對應資料夾：`learning/Week12_Robot_Prototype/`
- Notion 紀錄項目：系統架構圖、執行截圖、問題。

### Week13 Isaac Sim Environment

- 學習目標：建立 Isaac Sim 室內模擬環境。
- 必懂概念：場景、目標物、障礙物、機器人模型。
- 實作任務：建立簡化教室、實驗室或走廊場景。
- 驗收標準：場景可載入並能放置目標物。
- GitHub 對應資料夾：`learning/Week13_IsaacSim_Environment/`
- Notion 紀錄項目：場景截圖、物件列表、設定。

### Week14 Isaac Sim Camera

- 學習目標：取得 Isaac Sim 中的 RGB Camera 影像。
- 必懂概念：Camera Sensor（相機感測器）、影像 Topic、畫面擷取。
- 實作任務：設定模擬相機並輸出影像。
- 驗收標準：能保存或訂閱相機畫面。
- GitHub 對應資料夾：`learning/Week14_IsaacSim_Camera/`
- Notion 紀錄項目：相機位置、影像結果、問題。

### Week15 Isaac Sim + VLM

- 學習目標：將 Isaac Sim 影像輸入 VLM。
- 必懂概念：模擬影像、模型輸入、語意輸出。
- 實作任務：讓 VLM 描述模擬場景內容。
- 驗收標準：語意輸出能反映場景中的主要物件。
- GitHub 對應資料夾：`learning/Week15_IsaacSim_VLM/`
- Notion 紀錄項目：場景、提示、回答、錯誤案例。

### Week16 Final Mini Project

- 學習目標：完成期末最小可行系統。
- 必懂概念：使用者指令、語意理解、導航概念、展示流程。
- 實作任務：展示「找出指定目標」或「前往指定位置」流程。
- 驗收標準：有完整 README、截圖、執行紀錄與回顧。
- GitHub 對應資料夾：`learning/Week16_FinalProject/`
- Notion 紀錄項目：成果展示、限制、下一步論文方向。

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
|---|---|---|---|
| CLIP | VLM | Week02 | 圖文對齊與語意標籤比對 |
| BLIP | VLM | Week06 | 影像描述與視覺問答基礎 |
| BLIP-2 | VLM | Week06 | 輕量連接視覺模型與語言模型 |
| LLaVA | VLM | Week04 | 影像問答與機器人場景理解 |
| MiniGPT-4 | VLM | Week06 | 多模態對話架構比較 |
| Qwen-VL | VLM | Week06 | 中文與多模態能力比較 |
| InternVL | VLM | Week06 | 高效能 VLM 架構比較 |
| RT-1 | VLA | Week12 | 機器人動作資料與策略學習 |
| RT-2 | VLA | Week12 | 視覺語言到動作的概念延伸 |
| OpenVLA | VLA | Week12 | 開源 VLA 實作參考 |
| SayCan | Robot Learning | Week11 | 語言模型結合機器人可行動作 |
| PaLM-E | Embodied AI | Week11 | 具身智慧與多模態機器人推理 |

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

