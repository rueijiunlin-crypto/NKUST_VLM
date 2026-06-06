# NKUST VLM Master Project

本 Repository（程式碼與文件倉庫）用於管理 VLM/VLA 碩士研究、每週學習任務、論文閱讀、實驗紀錄與 Notion（筆記與資料庫管理工具）建置規劃。

## 專案目的

本專案聚焦 Vision-Language Model（視覺語言模型）與 Vision-Language-Action Model（視覺語言動作模型）在機器人研究中的應用，目標是建立可延伸到碩士論文的研究與實作流程。

主要方向包含：

- Transformer（轉換器架構）與 Attention（注意力機制）基礎
- CLIP（對比式圖文預訓練）與 LLaVA（大型語言與視覺助手）
- OpenVLA（開源視覺語言動作模型）
- ROS2（機器人作業系統第二版）整合
- Isaac Sim（NVIDIA 機器人模擬器）環境與相機感測器
- 室內語意導覽、災害巡檢、桌面操作機器人
- 碩士論文研究管理

## 16 週學習路線

| 週次 | 主題 | 對應資料夾 |
|---|---|---|
| Week01 | Transformer 基礎 | `Week01_Transformer/` |
| Week02 | CLIP | `Week02_CLIP/` |
| Week03 | Hugging Face（模型平台） | `Week03_HuggingFace/` |
| Week04 | LLaVA | `Week04_LLaVA/` |
| Week05 | VLM Architecture（視覺語言模型架構） | `Week05_VLM_Architecture/` |
| Week06 | VLM Paper Reading（論文閱讀） | `Week06_PaperReading/` |
| Week07 | Prompt Engineering（提示工程） | `Week07_PromptEngineering/` |
| Week08 | Mini Project：Image Caption（影像描述）與 Visual QA（視覺問答） | `Week08_MiniProject/` |
| Week09 | VLM + Camera（相機） | `Week09_VLM_Camera/` |
| Week10 | VLM + ROS2 Topic（主題） | `Week10_VLM_ROS2/` |
| Week11 | VLM + Navigation Concept（導航概念） | `Week11_VLM_Navigation/` |
| Week12 | VLM Robot System Prototype（機器人系統雛型） | `Week12_Robot_Prototype/` |
| Week13 | Isaac Sim Environment（模擬環境） | `Week13_IsaacSim_Environment/` |
| Week14 | Isaac Sim Camera（模擬相機） | `Week14_IsaacSim_Camera/` |
| Week15 | Isaac Sim + VLM | `Week15_IsaacSim_VLM/` |
| Week16 | Final Mini Project（期末小專案） | `Week16_FinalProject/` |

## GitHub 與 Notion 分工

GitHub（版本控制平台）負責保存程式碼、README、實驗腳本、執行紀錄與可重現設定。Notion 負責管理 Dashboard（儀表板）、每週進度、論文資料庫、實驗紀錄、題目評估與回顧。

## ChatGPT 與 Codex 分工

ChatGPT 適合用於理論討論、研究方向收斂、文獻摘要、口試問答準備與學習驗收。Codex 適合用於建立資料夾、撰寫程式、整理 README、建立實驗模板、檢查檔案與協助實作。

## 目前排除項目

本階段不將船體、浮力、USV、海浪、PINNs、海事機器人作為研究內容。所有新增文件需維持在 VLM/VLA、ROS2、Isaac Sim 與機器人語意理解範圍內。

## 如何使用本 Repository

1. 先閱讀 `docs/notion/VLM_Notion_System.md`，建立 Notion 管理系統。
2. 依照 16 週資料夾順序進行學習與實作。
3. 每週在對應資料夾撰寫筆記、任務、程式與回顧。
4. 每次實驗都在 `docs/experiments/` 或 Notion Experiment Log Database（實驗紀錄資料庫）留下紀錄。
5. 論文閱讀統一整理到 `docs/papers/` 與 Notion Paper Database（論文資料庫）。
6. 題目評估與研究架構整理到 `docs/thesis/` 與 Notion Thesis Research Database（論文研究資料庫）。

## 每週學習流程

1. 先與 ChatGPT 討論本週理論與目標
2. 將本週 Codex 任務貼給 Codex 執行
3. Codex 建立環境、程式、README 與練習
4. 學生自行執行與理解程式
5. 將結果回報 ChatGPT 驗收
6. 將實驗與心得整理到 Notion
