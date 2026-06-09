# AGENTS_v3.md

本文件定義本 Repository（程式碼與文件倉庫）的專案規則、工作流程、文件標準與 Codex 行為規範。

`AGENTS_v3.md` 只描述通用規則與每週文件格式，不得寫入具體 Week01、Week02 或任何特定週次的課程內容。每週課程規劃必須放在該週資料夾內的 `weekly_plan.md`。

---

## 1. Project Scope

### 專案目標

本 Repository 用於管理 Vision-Language Model（視覺語言模型，VLM）與 Vision-Language-Action Model（視覺語言動作模型，VLA）的碩士研究學習、實作、實驗紀錄、Notion（知識管理平台）同步與 GitHub（版本控制平台）工作流程。

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
* USV（無人船）
* 海浪
* PINNs（物理資訊神經網路）
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

* `docs/`：研究文件、Notion 規劃、論文、實驗與論文題目資料。
* `learning/`：每週教材、課程規劃、Demo 與學生學習紀錄。
* `modules/`：ROS2、Isaac Sim、VLM 模型等技術模組。
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
├─ weekly_plan.md
├─ notes.md
├─ study_log.md
└─ demo/
   ├─ demo_README.md
   └─ concept_name/
      ├─ README.md
      └─ demo_*.py
```

`concept_name/` 僅為占位範例。實際資料夾名稱必須依該週核心概念命名，使用英文或可維護命名。不得將某一週的概念資料夾固定套用到所有週次。

### 檔案職責分離

* `README.md`：本週學習入口，提供導覽、檔案說明與使用方式。
* `weekly_plan.md`：只存放該週課程規劃、任務與驗收條件。
* `notes.md`：只存放正式教材內容。
* `study_log.md`：只存放學生實際學習紀錄。
* `demo/`：只存放可執行 Demo 與 Demo 說明。

### 非必要檔案

以下檔案不再是每週必要檔案：

* `completion.md`
* `review.md`
* `tasks.md`

若需要任務、回顧或驗收條件，統一放入 `weekly_plan.md`。既有週次若已有上述檔案，可在後續遷移時逐步整併，不得在本規則文件中要求新週次必須建立。

---

## 3. Weekly Plan Rule

每週課程規劃必須放在該週資料夾內的：

```text
learning/WeekXX_TopicName/weekly_plan.md
```

不得將每週課程規劃放在 `AGENTS_v3.md`。`AGENTS_v3.md` 只能描述 `weekly_plan.md` 的格式與通用標準，不得寫入具體週次的課程內容。

### weekly_plan.md 必須包含

`weekly_plan.md` 只存放該週課程規劃，包括：

* 本週目標
* 必學概念
* 建議學習順序
* Demo 執行順序
* 任務清單
* 驗收條件

### weekly_plan.md 建議格式

```markdown
# WeekXX Weekly Plan

## 本週目標

-

## 必學概念

-

## 建議學習順序

1.
2.
3.

## Demo 執行順序

1. `python demo/concept_name/demo_example.py`

## 任務清單

* [ ] 閱讀 README.md
* [ ] 閱讀 notes.md
* [ ] 執行必要 Demo
* [ ] 在 study_log.md 記錄學習過程
* [ ] 更新 Notion 學習狀態
* [ ] 進行 ChatGPT 驗收

## 驗收條件

* [ ] weekly_plan.md 任務完成
* [ ] notes.md 已閱讀
* [ ] 必要 Demo 已執行
* [ ] study_log.md 已記錄
* [ ] Notion 狀態更新
* [ ] ChatGPT 驗收 Pass
```

---

## 4. Documentation Rules

### 語言規範

* 所有文件預設使用繁體中文撰寫。
* 英文專有名詞第一次出現時，必須附中文翻譯，例如 Vision-Language Model（視覺語言模型）。
* 程式檔名與技術資料夾可使用英文，但說明文件需使用繁體中文。
* 文件需清楚、可維護，並能作為 Notion 建置與同步依據。

### README 規範

`README.md` 是每週學習入口，應包含：

* 本週定位
* 文件導覽
* 建議使用方式
* 與 VLM/VLA 碩士研究的關聯
* 與 `weekly_plan.md`、`notes.md`、`study_log.md`、`demo/` 的關係

具體課程目標、任務清單與驗收條件應放在 `weekly_plan.md`。

### Notes 規範

`notes.md` 只存放正式教材內容，必須包含：

* 核心概念說明
* 初學者可理解的直覺解釋
* 必要的架構或資料流說明
* 與 Transformer、VLM、VLA 或機器人系統等適當應用脈絡的關聯
* 對應概念的 Demo 提示
* 本週尚未涵蓋內容

`notes.md` 不應存放學生個人學習紀錄、任務勾選狀態或 Notion 更新狀態。

### study_log.md 規範

`study_log.md` 用於紀錄學生實際學習過程，而不是教材內容。它應保存：

* 學習時間
* 閱讀進度
* Demo 執行結果
* 問題紀錄
* 修正方式
* 下一步

建議模板：

```markdown
# WeekXX Study Log

## 學習時間

| 日期 | 時間 | 內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 閱讀進度

* [ ] README.md
* [ ] weekly_plan.md
* [ ] notes.md
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

## 5. Demo Rules

### Demo 資料夾

每一週都必須建立 `demo/` 資料夾。若不存在，生成該週教材時必須自動建立。

所有 Demo 程式必須放在 `demo/` 中，不得散落於週資料夾根目錄或 Repository 根目錄。

`demo/` 底下必須依概念建立子資料夾：

```text
demo/
├─ demo_README.md
├─ concept_a/
├─ concept_b/
└─ concept_c/
```

上述 `concept_*` 是通用占位名稱；實際資料夾必須使用該週核心概念的英文或可維護命名。

每個概念子資料夾至少必須包含：

* `README.md`
* `demo_*.py`

Demo 應小而清楚，避免單一大型 Demo 混合太多概念。若一個概念需要多個層次的理解，應拆成多個小 Demo，而不是塞進同一個大型程式。

### Demo 可執行性

Demo 必須符合：

* 可用明確指令執行
* 若需要外部套件，必須在 `demo_README.md` 與對應概念子資料夾 `README.md` 說明安裝方式
* 若可能需要下載模型或資料，必須明確提示
* 程式輸出需能對應本週學習概念

### demo_README.md

每週 `demo/` 必須包含 `demo_README.md` 作為總覽文件，內容至少包含：

* Demo 檔案清單
* 如何執行
* 預期輸出
* 如何觀察結果
* 與本週主題的關係
* 與 VLM/VLA 研究的關係

### 概念子資料夾 README.md

各概念子資料夾的 `README.md` 作為局部說明文件，內容至少包含：

* 對應概念
* 執行指令
* 預期輸出
* 觀察重點
* 執行後應回答的問題

教材中的 Demo 路徑必須指向對應子資料夾，例如：

```text
python demo/concept_a/demo_concept_a.py
python demo/concept_b/demo_concept_b.py
```

不得只寫：

```text
python demo/demo_xxx.py
```

### Demo Integration Rule

教材不得將所有 Demo 集中於最後。

當某個概念有對應 Demo 時，必須於該概念段落後立即提示學生執行，並包含：

1. Demo 檔案名稱
2. 執行指令
3. 觀察重點
4. 預期輸出
5. 執行後應能回答的問題

### Multi-Level Demo Rule

每個核心概念至少應具備以下其中兩種 Demo 類型。若概念是關鍵主題，建議三種都具備。

* Level A：Concept Demo（概念示範）
* Level B：Mechanism Demo（機制示範）
* Level C：Real Model Demo（真實模型示範）

### Demo Completion Rule

Demo 不以成功執行為完成條件。

學生必須完成以下全部項目，才可視為 Demo 完成：

1. 成功執行 Demo。
2. 保存輸出結果。
3. 在 `study_log.md` 記錄觀察。
4. 回答 Demo `README.md` 中的問題。

Codex 不得代替學生勾選 Demo 完成，也不得代替學生撰寫個人理解。

---

## 6. GitHub Workflow

### 分支規範

不得直接修改 `main` 分支。每週教材必須使用對應週次 Branch（分支）。

命名格式：

```text
week01-transformer
week02-clip
week03-huggingface
```

非週次教材或規範更新應使用清楚描述目的的分支名稱。

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

只有在學生完成學習、`weekly_plan.md` 任務、Demo、Notion 更新，並通過 ChatGPT 驗收後，才可使用 Complete 類 Commit（提交）：

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

## 7. Notion Workflow

Notion 用於管理學習進度、每週回顧、實驗紀錄與學習狀態。教材與程式碼應保存在 GitHub Repository，不應以 Notion 作為主要教材存放區。

### Notion 管理

Notion 管理：

* Learning Roadmap
* Weekly Review
* Experiment Log
* 學習狀態

### GitHub 管理

GitHub 管理：

* 教材
* Demo
* notes
* weekly_plan
* study_log

### Learning Roadmap 狀態

每個 Week 必須具有以下狀態之一：

* Not Started（尚未開始）
* Generated（教材已生成）
* Learning（學習中）
* Reviewing（驗收中）
* Completed（完成）

### 狀態轉換條件

#### Not Started -> Generated

進入條件：

* `README.md` 已建立
* `weekly_plan.md` 已建立
* `notes.md` 已建立
* `study_log.md` 已建立
* `demo/` 已建立
* `demo/demo_README.md` 已建立
* 本週必要 Demo 已建立

#### Generated -> Learning

進入條件：

* 學生開始閱讀 `README.md`、`weekly_plan.md` 或 `notes.md`
* 或使用者明確表示開始學習該週內容

#### Learning -> Reviewing

進入條件：

* 學生已閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`
* 學生已完成 `weekly_plan.md` 任務
* 學生已執行 `demo/` 中必要 Demo
* 學生已填寫 `study_log.md`

#### Reviewing -> Completed

進入條件：

* ChatGPT 驗收結果為 Pass（通過）
* Learning Roadmap 已更新
* Experiment Log（實驗紀錄）已建立或更新
* Weekly Review（每週回顧）已建立或更新
* 學習狀態已更新

### Notion 自動化限制

若 Codex 具有 Notion 存取權限，且使用者提供對應 Page（頁面）或 Database（資料庫）URL/ID，Codex 可自動同步：

* Learning Roadmap
* Experiment Log
* Weekly Review
* 學習狀態

同步時必須遵守狀態轉換條件，不得自行將教材生成完成的 Week 標記為 Completed。

若 Codex 沒有 Notion 權限，或使用者未提供目標 Notion URL/ID，Codex 不得宣稱已更新 Notion。此時 Codex 應輸出建議更新內容、建議狀態、建議 Experiment Log 與建議 Weekly Review。

---

## 8. Week Lifecycle

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

* 該週必要教材、`weekly_plan.md`、`study_log.md` 與 Demo 已建立。
* Generated 不代表學生已完成學習。

### Learning

進入條件：

* 學生開始閱讀教材或執行 Demo。

### Reviewing

進入條件：

* 學生完成閱讀、`weekly_plan.md` 任務、Demo 與 `study_log.md`，等待 ChatGPT 驗收。

### Completed

Week 是否 Completed 不再依賴 `completion.md`。

Week 必須同時滿足以下條件，才可標記為 Completed：

* `weekly_plan.md` 任務完成
* `notes.md` 已閱讀
* 必要 Demo 已執行
* `study_log.md` 已記錄
* Notion 狀態更新
* ChatGPT 驗收 Pass

不得因教材生成完成而直接標記 Completed。

---

## 9. Week Generation Rules

禁止一次生成多週教材。

只有符合以下任一條件時，才能生成下一週教材：

1. 前一週狀態為 Completed。
2. ChatGPT 明確批准生成下一週教材。

若使用者要求生成多週內容，Codex 應提醒此規範，並只處理已被批准的週次。

每一週的最低涵蓋概念、必要 Demo、任務清單與驗收條件，應寫在該週的 `weekly_plan.md`，不得寫入 `AGENTS_v3.md`。

---

## 10. ChatGPT Validation

ChatGPT 驗收分為三個等級：

### Pass

表示學生已能清楚說明本週核心概念、完成指定任務與 Demo，並能連結本週內容與 VLM/VLA 碩士研究。此狀態可進入 Completed。

### Minor Revision

表示大部分內容已理解，但有小範圍概念不清、紀錄不足或 Demo 觀察不完整。學生補強指定項目後可再次驗收。

### Major Revision

表示核心概念、任務、Demo 或應用關聯仍明顯不足。學生需重新閱讀與補做主要任務後再進入 Reviewing。

---

## 11. Learning Content Standard

所有 Week 教材必須符合以下五層學習架構。

目的：

* 避免教材只停留在概念介紹。
* 確保學生能理解、實作、驗證並連結到適當的應用脈絡。

### Level 1：直覺理解

必須回答：

```text
這個東西是什麼？
```

要求：

* 初學者可理解
* 避免數學公式
* 使用生活化例子

### Level 2：技術原理

必須回答：

```text
它實際上怎麼運作？
```

要求：

* 說明內部機制
* 引入必要技術名詞
* 可以使用簡化架構圖
* 必須同時遵守 Concept Dependency Rule（概念依賴規則）
* 必須同時遵守 Deep Learning Content Rule（深度學習內容規則）
* 若涉及公式，還必須遵守 Mathematical Depth Rule（數學深度規則）

### Level 3：實作驗證

必須回答：

```text
我可以怎麼觀察它？
```

要求：

* 至少一個可執行 Demo
* 提供執行方式
* 提供觀察重點
* 提供預期輸出

### Level 4：Application Relation（應用關聯）

必須回答：

```text
它與哪些後續應用或系統脈絡有關？
```

要求：

* 可依概念內容選擇說明與 Transformer 的關聯
* 可依概念內容選擇說明與 VLM 的關聯
* 可依概念內容選擇說明與 VLA 的關聯
* 可依概念內容選擇說明與機器人系統的關聯
* 不要求每個概念都強制說明 VLM/VLA，但重要概念仍需說明其應用脈絡

### Level 5：驗收問題

必須回答：

```text
我是否真的理解？
```

要求：

* 至少三個觀念問題
* 至少一個應用問題
* 必須能用自己的話回答

每個核心概念都必須符合五層架構。

---

## 12. Concept Dependency Rule（概念依賴規則）

每個核心概念必須說明它在學習鏈中的位置，避免學生只背名詞而不知道資料如何往下一步流動。

每個核心概念必須包含：

1. 輸入是什麼
2. 輸出是什麼
3. 為什麼需要這個機制
4. 解決什麼問題
5. 下一步會進入哪個概念

教材應清楚呈現概念之間的資料流。若某週教材只涵蓋其中一部分，也必須說明尚未涵蓋的後續概念會在何時補上。

---

## 13. Deep Learning Content Rule（深度學習內容規則）

技術原理不得只描述定義。

每個核心概念必須回答：

1. 為什麼需要它
2. 沒有它會發生什麼問題
3. 它如何解決問題
4. 它與前一個概念的關係
5. 它與下一個概念的關係

禁止只出現：

```text
XXX 是一種...
```

而沒有進一步說明原因、輸入、輸出、機制與限制。

### 深度說明最低要求

每個核心概念的技術原理至少應包含：

* 輸入與輸出
* 核心運作流程
* 解決的限制或問題
* 與前後概念的銜接
* 初學者容易誤解的地方

---

## 14. Mathematical Depth Rule（數學深度規則）

目的：

避免教材只給公式，不解釋公式。

若某概念的數學內容為理解核心機制所必需，教材不得只列出公式，必須同時說明公式背後的直覺、變數、用途與驗證方式。

### 必須包含

若教材使用公式，必須包含：

1. 公式
2. 各變數意義
3. 幾何或直覺解釋
4. 為什麼需要此公式
5. Demo 驗證方式

數學內容應先提供直覺，再提供公式，最後提供 Demo 驗證。

建議順序：

```text
問題直覺
-> 為什麼需要公式
-> 公式
-> 變數意義
-> 幾何或計算直覺
-> Demo 驗證
-> 驗收問題
```

不得只放公式而沒有說明變數、用途、直覺與 Demo 觀察方式。

---

## 15. Refactor Over Append Rule（重構優先於追加規則）

教材更新時，優先重構既有內容，而不是在文件最後追加補充內容。

不得出現以下結構：

```text
前面章節：概念簡易版
文件最後：概念完整版
```

新增內容必須整合回原本對應章節。

### 重構要求

更新教材時應優先：

1. 找到既有概念章節。
2. 將新增直覺、技術原理、Demo、觀察重點與驗收問題整合進該章節。
3. 移除或避免重複的尾端補充章節。
4. 保留必要的 Knowledge Gap Check（知識缺口檢查），但不得把完整概念教學塞進該區。

### 允許放在文件最後的內容

文件最後可以保留：

* 本週已掌握內容
* 本週尚未涵蓋內容
* 下一週預告
* 學習反思或回顧指引

文件最後不應放置核心概念的完整版教學內容。

---

## 16. Codex 行為規範

Codex 在本 Repository 工作時必須遵守：

* 執行任務前先閱讀並遵守目前最高版本的 `AGENTS_v*.md`。
* 不得直接修改 `main` 分支。
* 不得在未經要求時修改既有 Week 內容。
* 建立或更新每週教材時，必須維持 `weekly_plan.md`、`notes.md`、`study_log.md`、`demo/` 的職責分離。
* 不得把具體週次課程內容寫入 `AGENTS_v3.md`。
* 不得代替學生撰寫個人理解、學習反思或 Demo 驗收回答。
* 不得宣稱已更新 Notion，除非確實具有 Notion 權限並完成同步。
* 更新教材時應重構既有內容，避免在文件尾端堆疊重複補充。

