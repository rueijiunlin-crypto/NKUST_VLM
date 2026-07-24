# Curriculum Roadmap v2

> 本文件定義 Robot-oriented VLM / VLA research（機器人導向視覺語言模型／視覺語言動作模型研究）的目標課程路線與遷移計畫。它不是教材完成紀錄，不代表任何既有 Week 已重構或通過驗收。
>
> 現有 `learning/WeekXX_*` 資料夾名稱暫時保留。只有在逐週內容獲得明確批准、完成連結盤點後，才評估是否重新命名。

## 1. Why Refactor

原 Roadmap 大致沿著以下順序前進：

```text
VLM
→ Prompt
→ Mini Project
→ Camera
→ ROS2
→ Navigation
→ Isaac Sim
```

這條路線能建立 VLM 推論與機器人整合入門能力，但對 Robot VLM / VLA 碩士研究而言，後半段仍缺少完整的研究能力鏈：

- Video / Streaming VLM（影片／串流視覺語言模型）
- Spatial Grounding（空間語意定位）
- Robot State（機器人狀態）
- VLA Fundamentals（視覺語言動作模型基礎）
- Robot Dataset（機器人資料集）
- VLA Inference（視覺語言動作模型推論）
- Fine-tuning / Task Adaptation（微調／任務適應）
- Sim-to-Real（模擬到真實）
- Research Evaluation（研究評估）

新 Roadmap 將課程重新組成：

```text
Deep Learning Foundation
↓
Vision-Language Foundation
↓
Generative VLM
↓
Robot-oriented VLM
↓
Temporal Perception
↓
Realtime Perception
↓
Spatial Grounding
↓
Embodied Observation
↓
VLA
↓
Robot Dataset
↓
VLA Inference
↓
Fine-tuning
↓
Simulation
↓
Sim-to-Real
↓
Research Evaluation
```

## 2. New Six-Phase Curriculum

### Phase 1 — VLM Foundation

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week01 | Transformer Fundamentals | 建立 Token、Embedding、Attention、Transformer 與 Encoder／Decoder 基礎。 |
| Week02 | CLIP and Vision-Language Alignment | 建立 image／text representation 與跨模態對齊基礎。 |
| Week03 | Hugging Face Model Workflow | 建立模型載入、Processor、Tokenizer、裝置、dtype、checkpoint 與 configuration 工具能力。 |
| Week04 | LLaVA + Grounded Visual Reasoning | 從圖文對齊進入生成式 VLM，建立可觀察資訊與機器人實際狀態的能力邊界。 |
| Week05 | VLM Architecture for Robotics | 從一般 VLM 架構延伸到 Robot-oriented VLM system perspective（機器人導向系統觀點）。 |

### Phase 2 — Robot Perception

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week06 | Video and Streaming VLM | 從單張圖片進入多影格、影片、串流輸入、時間記憶與 latency／throughput。 |
| Week07 | ROS2 + Camera + Realtime VLM | 建立 Camera → ROS2 stream → sampling → inference → structured semantic interface。 |
| Week08 | Spatial Reasoning and Grounding | 建立語意物件、2D、深度、3D 相機座標與機器人座標的資料鏈。 |

現有 Paper Reading 教材不刪除。其 claim-to-evidence（主張到證據）方法未來將遷移為 Repository 共用的 Research Paper Reading Framework（研究論文閱讀框架），候選位置為 `docs/papers/` 或 `templates/`，但本次不搬動檔案。

### Phase 3 — Embodied AI / VLA

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week09 | Robot State + Multimodal Observation | 將 Vision、Language、proprioception（本體感覺）、關節、末端與時間同步組成 embodied observation（具身觀察）。 |
| Week10 | Embodied AI + VLA Fundamentals | 比較 VLM 語意輸出與 VLA action，建立 Policy、Action Space、Action Chunk 與 closed／open-loop 概念。 |

### Phase 4 — Robot Learning

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week11 | Robot Dataset and Demonstrations | 理解 episode、trajectory、teleoperation、observation-action alignment 與資料品質。 |
| Week12 | SmolVLA / OpenVLA Inference | 從較易部署的預訓練模型開始理解 Image + Robot State + Instruction → Predicted Action。 |
| Week13 | VLA Fine-tuning | 使用預訓練模型與機器人資料進行 task adaptation，不以從零訓練大型 VLA 為目標。 |

### Phase 5 — Simulation and Deployment

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week14 | Isaac Sim Robot Learning | 整合場景、機器人、Camera／Depth、Robot State、任務、Policy 與 evaluation。 |
| Week15 | Sim-to-Real / Real Robot Deployment | 分析 domain shift、感測與標定誤差、latency、action error、失敗恢復與部署安全。 |

若沒有實體機器人，可用 Sim-to-Real analysis（模擬到真實分析）或 hardware-ready pipeline（硬體就緒資料流）作替代驗收。

### Phase 6 — Research

| Week | Target Topic | Roadmap Role |
| --- | --- | --- |
| Week16 | Research Prototype and Evaluation | 建立 Research Question → Baseline → Method → Dataset → Experiment → Metric → Failure Analysis → Conclusion。 |

研究 Prototype 成功執行不等於研究完成；必須逐步加入 baseline、metric、test cases、failure cases、reproducibility 與 limitation analysis。

## 3. Old → New Mapping

| Existing Week | Existing Topic | Target Topic | Migration Level |
| --- | --- | --- | --- |
| Week01 | Transformer | Transformer Fundamentals | Keep |
| Week02 | CLIP | CLIP and Vision-Language Alignment | Keep |
| Week03 | Hugging Face | Hugging Face Model Workflow | Keep |
| Week04 | LLaVA | LLaVA + Grounded Visual Reasoning | Minor Refactor |
| Week05 | VLM Architecture | VLM Architecture for Robotics | Moderate Refactor |
| Week06 | Paper Reading | Video and Streaming VLM | Major Refactor |
| Week07 | Prompt Engineering | ROS2 + Camera + Realtime VLM | Major Refactor |
| Week08 | Mini Project | Spatial Reasoning and Grounding | Major Refactor |
| Week09 | VLM + Camera | Robot State + Multimodal Observation | Major Refactor |
| Week10 | VLM + ROS2 | Embodied AI + VLA Fundamentals | Major Refactor |
| Week11 | VLM + Navigation | Robot Dataset and Demonstrations | Rebuild |
| Week12 | Robot Prototype | SmolVLA / OpenVLA Inference | Rebuild |
| Week13 | Isaac Sim Environment | VLA Fine-tuning | Rebuild |
| Week14 | Isaac Sim Camera | Isaac Sim Robot Learning | Rebuild |
| Week15 | Isaac Sim + VLM | Sim-to-Real / Real Robot Deployment | Rebuild |
| Week16 | Final Mini Project | Research Prototype and Evaluation | Rebuild |

Migration Level 定義：

- **Keep**：主題與能力位置一致，只需維護品質。
- **Minor Refactor**：保留主線，補強方向與能力邊界。
- **Moderate Refactor**：保留核心架構，重新整合部分系統觀點。
- **Major Refactor**：保留高價值內容，但需重新定位、拆分或跨週遷移。
- **Rebuild**：依新研究能力鏈重新設計；仍須先盤點並保存可重用內容。

此表只用於 migration planning（遷移規劃），不表示各週教材已修改或完成。

## 4. Content Preservation Plan

Roadmap 改變不得成為刪除高品質教材或學生紀錄的理由。以下內容必須保留並在後續逐週重構時安排適當位置：

| Existing Source | Preserved Content | Future Direction |
| --- | --- | --- |
| Week06 | claim-to-evidence paper reading framework | 遷移為跨週可重用的 Research Paper Reading Framework。 |
| Week07 | structured prompt、Prompt Contract、schema、validator、Unknown Policy、Retry Policy、Safety Gate | 規劃分配到新的 Week04、Week05、Week07 與 Week10；實際拆分需逐週批准。 |
| Week08 | observation contract、structured output、validator | 整合至新的 Robot Perception pipeline 與 Spatial Grounding 驗證。 |
| Week09 | camera lifecycle、timestamp | 整合至即時感知、Robot State 與多模態時間同步。 |
| Week10 | ROS2 semantic interface | 整合至 realtime VLM 與具身系統模組介面。 |

所有既有 `study_log.md`、學生答案、Practice 觀察、Demo 結果與 Notion 連結都必須保存。遷移前要先辨識內容擁有者與依賴路徑。

### Paper Reading Strategy

Paper Reading 不再單獨占用主要能力階段，但應貫穿所有主題：

```text
Transformer → Transformer paper
CLIP → CLIP paper
LLaVA → LLaVA paper
VLM Architecture → BLIP-2 / Flamingo
Video VLM → Video / Streaming VLM paper
VLA → RT-2 / OpenVLA / SmolVLA
Robot Dataset → dataset / imitation learning paper
Simulation → sim-to-real paper
```

未來可建立 `paper_reading_framework.md`，但其位置與實際遷移需另行批准。

### Prompt Engineering Migration Strategy

Prompt Engineering 不再作為獨立主階段。既有 Prompt Contract、Structured Output、Schema、Validator、Unknown Policy、Retry Policy 與 Safety Gate 應分散整合到最需要這些能力的主題中。本次不搬動或重寫原教材。

## 5. Refactor Order

```text
Step 1
Approve Curriculum Roadmap

Step 2
Update Week04 / Week05

Step 3
Refactor Week06–08

Step 4
Refactor Week09–10

Step 5
Rebuild Week11–13

Step 6
Rebuild Week14–16

Step 7
Rename directories only if necessary

Step 8
Final link / documentation audit
```

每一 Step 都需獨立批准。Roadmap approval 不授權修改多週教材，也不代表任何 Week 已 Generated 或 Completed。

## 6. Migration Guardrails

- 不因 Roadmap 改變而直接刪除、覆蓋或搬移 Week 教材。
- 不自動重新命名 `WeekXX_*` 資料夾。
- 不修改或代填學生 `study_log.md`。
- 不把 VLM output 默認為 motor command。
- 不把 Demo 成功執行當成研究驗收的全部條件。
- 每週重構前先檢查 Markdown、Notion、scripts 與 Git history 對舊路徑的依賴。
