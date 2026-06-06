# AGENTS_v2.md

## 1. Project Scope

### 專案目標

本 Repository（程式碼與文件倉庫）用於管理 Vision-Language Model（視覺語言模型）與 Vision-Language-Action Model（視覺語言動作模型）的碩士研究學習、實作、實驗紀錄、Notion（知識管理平台）同步與 GitHub（版本控制平台）工作流程。

所有教材、程式、Demo（示範程式）與研究文件應服務於 VLM/VLA 碩士研究，並能支援後續論文題目收斂、系統實作與實驗驗收。

### 學習範圍

本專案目前聚焦：

* Transformer（轉換器架構）
* CLIP（對比式圖文預訓練）
* LLaVA（大型語言與視覺助手）
* OpenVLA（開源視覺語言動作模型）
* ROS2（機器人作業系統第二版）
* Isaac Sim（NVIDIA 機器人模擬器）
* 室內語意導覽
* 災害巡檢
* 桌面操作機器人
* 碩士論文研究管理

### 排除項目

本階段不得新增以下內容作為研究主題、教材主題、Demo 主題或實驗主題：

* 船體
* 浮力
* USV
* 海浪
* PINNs
* 海事機器人

若因規範說明需要提及，只能出現在排除項目或限制條款中。

---

## 2. Repository Structure

Repository 頂層結構固定為：

```text
docs/
learning/
modules/
templates/
assets/
```

用途：

* `docs/`：研究文件、Notion（知識管理平台）規劃、論文、實驗與論文題目資料。
* `learning/`：WeekXX 每週教材、任務、Demo（示範程式）與學習紀錄。
* `modules/`：ROS2（機器人作業系統第二版）、Isaac Sim（NVIDIA 機器人模擬器）、VLM 模型等技術模組。
* `templates/`：Notion 與研究管理模板。
* `assets/`：文件附件、圖片、資料與其他素材。

每一週教材必須使用獨立資料夾，命名格式為：

```text
learning/WeekXX_TopicName/
```

每週資料夾統一結構如下：

```text
learning/WeekXX_TopicName/
├─ README.md
├─ notes.md
├─ tasks.md
├─ review.md
├─ completion.md
├─ study_log.md
└─ demo/
   ├─ demo_README.md
   └─ demo_*.py
```

### 必要檔案用途

* `README.md`：本週學習入口，說明目標、範圍、學習安排與驗收標準。
* `notes.md`：本週正式筆記，說明核心概念與 VLM/VLA 關聯。
* `tasks.md`：本週任務，包含觀念練習、程式練習與驗收要求。
* `review.md`：本週回顧模板，供學生整理理解與問題。
* `completion.md`：本週完成證明，由學生填寫，Codex 不得自動填寫學生理解內容。
* `study_log.md`：本週學習過程紀錄，保存閱讀、實作、Demo 執行與問題紀錄。
* `demo/`：保存本週所有 Demo 程式與 Demo 說明。

---

## 3. Documentation Rules

### 語言規範

* 所有文件預設使用繁體中文撰寫。
* 英文專有名詞第一次出現時，必須附中文翻譯，例如 Vision-Language Model（視覺語言模型）。
* 程式檔名與技術資料夾可使用英文，但說明文件需使用繁體中文。
* 文件需清楚、可維護，並能作為 Notion 建置與同步依據。

### README 規範

`README.md` 必須包含：

* 本週定位
* 學習目標
* 必懂概念
* 建議學習安排
* 實作任務摘要
* 驗收標準
* 與 VLM/VLA 碩士研究的關聯
* 與下一週主題的銜接

### Notes 規範

`notes.md` 必須包含：

* 核心概念說明
* 初學者可理解的直覺解釋
* 必要的架構或資料流說明
* 與 VLM/VLA 的關聯
* 不需要過深數學推導，除非使用者明確要求

### Tasks 規範

`tasks.md` 必須包含：

* 觀念練習
* 程式練習
* 每題驗收標準
* 建議輸出成果
* 可整理到 Notion 的項目

### Review 規範

`review.md` 必須包含：

* 本週完成項目
* 本週學到什麼
* 本週最重要的理解
* 本週遇到的問題
* 尚未解決的問題
* 下週目標
* 要詢問 ChatGPT 的問題
* 要交給 Codex 的任務

---

## 4. Demo Rules

### Demo 資料夾

每一週都必須建立 `demo/` 資料夾。若不存在，生成該週教材時必須自動建立。

所有 Demo 程式必須放在 `demo/` 中，不得散落於週資料夾根目錄或 Repository 根目錄。

### Demo 可執行性

Demo 必須符合：

* 可用明確指令執行
* 若需要外部套件，必須在 `demo_README.md` 說明安裝方式
* 若可能需要下載模型或資料，必須明確提示
* 程式輸出需能對應本週學習概念

### demo_README.md

每週 `demo/` 必須包含 `demo_README.md`，內容至少包含：

* Demo 檔案清單
* 如何執行
* 預期輸出
* 如何觀察結果
* 與本週主題的關係
* 與 VLM/VLA 研究的關係

---

## 5. GitHub Workflow

### 分支規範

不得直接修改 `main` 分支。每週教材必須使用對應週次 Branch（分支）。

命名格式：

```text
week01-transformer
week02-clip
week03-huggingface
```

### Generate WeekXX Commit

當 Codex 生成或補齊某週教材，使該週達到 Generated（教材已生成）條件時，使用：

```text
Generate WeekXX learning materials
```

或在更新既有教材到新規範時使用清楚描述，例如：

```text
Update WeekXX to latest AGENTS standard
```

### Complete WeekXX Commit

只有在學生完成學習、Tasks（任務）、Demo、Notion 更新，並通過 ChatGPT 驗收後，才可使用 Complete 類 Commit（提交）：

```text
Complete WeekXX learning cycle
```

### Push 規範

完成 Commit 後推送至 GitHub：

```text
git push -u origin <branch_name>
```

### 回報內容

每次 GitHub 操作後需回報：

* 新增檔案清單
* 修改檔案清單
* Branch 名稱
* Commit 訊息
* Push 結果

---

## 6. Notion Workflow

Notion 用於管理學習進度、文獻閱讀、實驗紀錄、論文規劃與每週回顧。教材與程式碼應保存在 GitHub Repository，不應以 Notion 作為主要教材存放區。

### Learning Roadmap 狀態

每個 Week 必須具有以下狀態之一：

* Not Started（尚未開始）
* Generated（教材已生成）
* Learning（學習中）
* Reviewing（驗收中）
* Completed（完成）

### 狀態轉換條件

#### Not Started → Generated

進入條件：

* `README.md` 已建立
* `notes.md` 已建立
* `tasks.md` 已建立
* `review.md` 已建立
* `completion.md` 已建立
* `study_log.md` 已建立
* `demo/` 已建立
* `demo/demo_README.md` 已建立
* 本週必要 Demo 已建立

#### Generated → Learning

進入條件：

* 學生開始閱讀 `README.md` 或 `notes.md`
* 或使用者明確表示開始學習該週內容

#### Learning → Reviewing

進入條件：

* 學生已閱讀 `README.md` 與 `notes.md`
* 學生已完成 `tasks.md`
* 學生已執行 `demo/` 中必要 Demo
* 學生已填寫 `completion.md`
* 學生已填寫 `study_log.md`

#### Reviewing → Completed

進入條件：

* ChatGPT 驗收結果為 Pass（通過）
* Learning Roadmap 已更新
* Experiment Log（實驗紀錄）已建立
* Weekly Review（每週回顧）已建立或更新

---

## 7. Study Log Rules

每個 Week 必須建立：

```text
study_log.md
```

### study_log.md 用途

`study_log.md` 用於紀錄學生實際學習過程，而不是教材內容。它應保存：

* 學習時間
* 閱讀進度
* Demo 執行結果
* 問題紀錄
* 修正方式
* 下一步

### study_log.md 建議模板

```markdown
# WeekXX Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 閱讀進度

* [ ] README.md
* [ ] notes.md
* [ ] tasks.md
* [ ] demo/demo_README.md

## Demo 執行結果

| Demo | 是否執行 | 結果 | 問題 |
|---|---|---|---|
|  |  |  |  |

## 問題紀錄

-

## 修正方式

-

## 下一步

-
```

---

## 8. Completion Rules

每個 Week 必須建立：

```text
completion.md
```

`completion.md` 作為該週學習完成證明，由學生填寫。Codex 不得自動修改學生的理解內容，也不得代替學生勾選已完成項目。

### completion.md 模板

```markdown
# WeekXX Completion

## 閱讀完成

* [ ] README.md
* [ ] notes.md

---

## Tasks 完成

* [ ] 觀念練習 1
* [ ] 觀念練習 2
* [ ] 觀念練習 3
* [ ] 程式練習 1
* [ ] 程式練習 2

---

## Demo 完成

* [ ] Demo 1
* [ ] Demo 2
* [ ] Demo 3

---

## 我的理解

### Token（詞元）

請用自己的話說明：

---

### Embedding（嵌入向量）

請用自己的話說明：

---

### Attention（注意力機制）

請用自己的話說明：

---

### 本週與 VLM（視覺語言模型）的關係

請用自己的話說明：

---

## Notion 更新

* [ ] Learning Roadmap
* [ ] Experiment Log
* [ ] Weekly Review

---

## ChatGPT 驗收

* [ ] 未驗收
* [ ] Pass
* [ ] Minor Revision
* [ ] Major Revision

---

## ChatGPT 評語

（由 ChatGPT 填寫）
```

---

## 9. ChatGPT Validation

ChatGPT 驗收分為三個等級：

### Pass

表示學生已能清楚說明本週核心概念、完成指定 Tasks 與 Demo，並能連結本週內容與 VLM/VLA 碩士研究。此狀態可進入 Completed。

### Minor Revision

表示大部分內容已理解，但有小範圍概念不清、紀錄不足或 Demo 觀察不完整。學生補強指定項目後可再次驗收。

### Major Revision

表示核心概念、Tasks、Demo 或 VLM/VLA 關聯仍明顯不足。學生需重新閱讀與補做主要任務後再進入 Reviewing。

---

## 10. Week Lifecycle

每週生命週期如下：

```text
Not Started
↓
Generated
↓
Learning
↓
Reviewing
↓
Completed
```

### Not Started

進入條件：

* 該週尚未建立教材，或尚未達到 Generated 條件。

### Generated

進入條件：

* 該週必要教材、Demo、`completion.md` 與 `study_log.md` 已建立。
* Generated 不代表學生已完成學習。

### Learning

進入條件：

* 學生開始閱讀教材或執行 Demo。

### Reviewing

進入條件：

* 學生完成閱讀、Tasks、Demo、`completion.md` 與 `study_log.md`，等待 ChatGPT 驗收。

### Completed

進入條件：

* ChatGPT 驗收為 Pass。
* Notion 已同步 Learning Roadmap、Experiment Log 與 Weekly Review。
* 不得因教材生成完成而直接標記 Completed。

---

## 11. Week Generation Rules

禁止一次生成多週教材。

只有符合以下任一條件時，才能生成下一週教材：

1. 前一週狀態為 Completed。
2. ChatGPT 明確批准生成下一週教材。

若使用者要求生成多週內容，Codex 應提醒此規範，並只處理已被批准的週次。

---

## 12. Codex Automation Rules

### 具有 Notion 權限時

若 Codex 具有 Notion 存取權限，且使用者提供對應 Page（頁面）或 Database（資料庫）URL/ID，Codex 可自動同步：

* Learning Roadmap
* Experiment Log
* Weekly Review

同步時必須遵守狀態轉換條件，不得自行將教材生成完成的 Week 標記為 Completed。

### 無 Notion 權限時

若 Codex 沒有 Notion 權限，或使用者未提供目標 Notion URL/ID，Codex 不得宣稱已更新 Notion。

此時 Codex 應輸出：

* 建議更新內容
* 建議狀態
* 建議 Experiment Log
* 建議 Weekly Review

### Completed 自動化限制

只有在使用者明確提供「ChatGPT 已驗收通過 WeekXX」或等價訊息時，Codex 才能協助將該週推進到 Completed 相關流程。

## 13. Learning Content Standard

所有 Week 教材必須符合以下五層學習架構。

目的：

避免教材只停留在概念介紹。

確保學生能理解、實作、驗證並連結到 VLM/VLA 研究。

---

### Level 1：直覺理解

必須回答：

「這個東西是什麼？」

要求：

* 初學者可理解
* 避免數學公式
* 使用生活化例子

範例：

Attention（注意力機制）是模型決定要關注哪些資訊的方法。

---

### Level 2：技術原理

必須回答：

「它實際上怎麼運作？」

要求：

* 說明內部機制
* 引入必要技術名詞
* 可以使用簡化架構圖

範例：

Attention 的 Query（查詢）、Key（鍵）、Value（值）機制。

---

### Level 3：實作驗證

必須回答：

「我可以怎麼觀察它？」

要求：

* 至少一個可執行 Demo
* 提供執行方式
* 提供觀察重點
* 提供預期輸出

---

### Level 4：VLM/VLA 關聯

必須回答：

「它與 VLM/VLA 有什麼關係？」

要求：

* 說明在 CLIP、LLaVA、OpenVLA 中的用途
* 說明在機器人應用中的角色

---

### Level 5：驗收問題

必須回答：

「我是否真的理解？」

要求：

* 至少三個觀念問題
* 至少一個應用問題
* 必須能用自己的話回答

---

### 每個核心概念都必須符合五層架構

例如：

Token（詞元）

Embedding（嵌入向量）

Attention（注意力機制）

Self-Attention（自注意力）

Encoder（編碼器）

Decoder（解碼器）

皆需具備：

Level 1~Level 5

## 14. Demo Integration Rule

教材不得將所有 Demo 集中於最後。

當某個概念有對應 Demo 時，

必須於該概念段落後立即提示學生執行。

---

### 必須包含

1. Demo 檔案名稱

2. 執行指令

3. 觀察重點

4. 預期輸出

5. 執行後應能回答的問題

---

### 範例

#### 建議執行 Demo

當讀完 Token（詞元）後：

執行：

python demo/demo_tokenizer.py

觀察：

* Token 如何切分
* Token ID 如何產生

預期輸出：

Tokens: [...]

Token IDs: [...]

執行後請回答：

1. Token 和原始文字有什麼差異？
2. Token ID 的用途是什麼？
3. 為什麼需要 Embedding（嵌入向量）？

---

每個 Demo 必須有明確的執行時機。

不得只在 demo_README.md 中列出。

## 15. Knowledge Gap Check

每個 Week 的 notes.md 最後必須包含：

### 本週尚未涵蓋內容

列出：

* 已學會內容
* 尚未學習內容
* 下一週將補充內容

---

範例

Week01 Transformer（轉換器）

已學會：

* Token
* Embedding
* Attention
* Self-Attention

尚未涵蓋：

* Position Encoding（位置編碼）
* Multi-Head Attention（多頭注意力）
* Layer Normalization（層正規化）

下一週：

* CLIP（對比式圖文預訓練）
* Vision Transformer（視覺轉換器）
