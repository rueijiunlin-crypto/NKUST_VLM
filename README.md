# NKUST VLM Master Project

本 Repository（程式碼與文件倉庫）用於管理 Vision-Language Model（視覺語言模型）與 Vision-Language-Action Model（視覺語言動作模型）的碩士研究、每週學習任務、論文閱讀、實驗紀錄、Demo（示範程式）與 Notion（知識管理平台）建置規劃。

## 專案目的

本專案聚焦 VLM/VLA 在機器人研究中的應用，目標是建立可延伸到碩士論文的研究與實作流程。

主要方向包含：

- Transformer（轉換器架構）與 Attention（注意力機制）基礎
- CLIP（對比式圖文預訓練）與 LLaVA（大型語言與視覺助手）
- OpenVLA（開源視覺語言動作模型）
- ROS2（機器人作業系統第二版）整合
- Isaac Sim（NVIDIA 機器人模擬器）環境與相機感測器
- 室內語意導覽、災害巡檢、桌面操作機器人
- 碩士論文研究管理

## Repository 結構

```text
docs/       研究文件、Notion 規劃、論文、實驗與論文題目資料
learning/   Week01 到 Week16 每週教材、任務、Demo 與學習紀錄
modules/    ROS2、Isaac Sim、VLM 模型等技術模組
templates/  Notion 與研究管理模板
assets/     文件附件、圖片、資料與其他素材
```

## 16 週學習路線

> Curriculum 狀態：Active Curriculum（正式課程）。教材已依新版研究能力鏈遷移；這只表示教材結構啟用，不代表學生已完成任何 Week。

### Phase 1 — VLM Foundation（視覺語言模型基礎）

Week01–05：建立深度學習、視覺語言對齊、真實模型操作、生成式 VLM 與機器人導向架構基礎。

### Phase 2 — Robot Perception（機器人感知）

Week06–08：建立時間感知、即時相機資料流與空間定位能力。

### Phase 3 — Embodied AI / VLA（具身人工智慧／視覺語言動作模型）

Week09–10：將視覺、語言與 Robot State（機器人狀態）整合為具身觀察，銜接 VLA 與 Policy（策略）。

### Phase 4 — Robot Learning（機器人學習）

Week11–13：學習示範資料、預訓練 VLA 推論與任務適應。

### Phase 5 — Simulation and Deployment（模擬與部署）

Week14–15：建立機器人學習模擬、Sim-to-Real（模擬到真實）分析與部署能力。

### Phase 6 — Research（研究）

Week16：完成具有 baseline（基準方法）、metric（評估指標）、失敗分析與可重現性的研究 Prototype（原型）。

| Week | Topic | Directory |
| --- | --- | --- |
| Week01 | Transformer Fundamentals | `learning/Week01_Transformer/` |
| Week02 | CLIP and Vision-Language Alignment | `learning/Week02_CLIP/` |
| Week03 | Hugging Face Model Workflow | `learning/Week03_HuggingFace/` |
| Week04 | LLaVA + Grounded Visual Reasoning | `learning/Week04_LLaVA/` |
| Week05 | VLM Architecture for Robotics | `learning/Week05_VLM_Architecture/` |
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

完整的舊課程對照、內容保存與遷移執行紀錄請見 [Curriculum Roadmap v2](./docs/learning/curriculum_roadmap_v2.md)。

## GitHub 與 Notion 分工

GitHub（版本控制平台）負責保存教材、程式碼、Demo、README、實驗腳本、執行紀錄與可重現設定。Notion 負責管理 Dashboard（儀表板）、每週進度、論文資料庫、實驗紀錄、題目評估與回顧。

## ChatGPT 與 Codex 分工

ChatGPT 適合用於理論討論、研究方向收斂、文獻摘要、口試問答準備與學習驗收。Codex 適合用於建立資料夾、撰寫程式、整理 README、建立實驗模板、檢查檔案與協助實作。

## 目前排除項目

本階段不將船體、浮力、USV、海浪、PINNs、海事機器人作為研究內容。所有新增文件需維持在 VLM/VLA、ROS2、Isaac Sim 與機器人語意理解範圍內。

## 如何使用本 Repository

1. 先閱讀目前正式的 `AGENTS.md`，確認代理與週次流程規範。
2. 先閱讀 `docs/notion/VLM_Notion_System.md`，建立 Notion 管理系統。
3. 依照 `learning/` 中的 16 週資料夾順序進行學習與實作。
4. 每週在對應資料夾撰寫筆記、任務、程式、Demo 執行結果與回顧。
5. 每次實驗都在 `docs/experiments/` 或 Notion Experiment Log Database（實驗紀錄資料庫）留下紀錄。
6. 論文閱讀統一整理到 `docs/papers/` 與 Notion Paper Database（論文資料庫）。
7. 題目評估與研究架構整理到 `docs/thesis/` 與 Notion Thesis Research Database（論文研究資料庫）。

## 每週學習流程

1. 先與 ChatGPT 討論本週理論與目標
2. 將本週 Codex 任務貼給 Codex 執行
3. Codex 建立環境、程式、README 與練習
4. 學生自行執行與理解程式
5. 將結果回報 ChatGPT 驗收
6. 將實驗與心得整理到 Notion
