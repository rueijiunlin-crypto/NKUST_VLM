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
   ├─ concept_a/
   │  ├─ README.md
   │  └─ demo_*.py
   ├─ concept_b/
   │  ├─ README.md
   │  └─ demo_*.py
   └─ concept_c/
      ├─ README.md
      └─ demo_*.py
```

`concept_a/`、`concept_b/`、`concept_c/` 僅為占位範例。實際資料夾名稱必須依該週核心概念命名，例如 Week01 可使用 `token/`、`embedding/`，Week02 則應依 CLIP（對比式圖文預訓練）或該週主題的核心概念另行命名。

### 必要檔案用途

* `README.md`：本週學習入口，說明目標、範圍、學習安排與驗收標準。
* `notes.md`：本週正式筆記，說明核心概念、資料流與適當的應用關聯。
* `tasks.md`：本週任務，包含觀念練習、程式練習與驗收要求。
* `review.md`：本週回顧模板，供學生整理理解與問題。
* `completion.md`：本週完成證明，由學生填寫，Codex 不得自動填寫學生理解內容。
* `study_log.md`：本週學習過程紀錄，保存閱讀、實作、Demo 執行與問題紀錄。
* `demo/`：保存本週所有 Demo 程式與 Demo 說明，並依核心概念建立子資料夾。

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
* 與 Transformer、VLM、VLA 或機器人系統等適當應用脈絡的關聯
* 避免不必要的深數學推導；若公式是理解核心機制所必需，必須依 Section 21：Mathematical Depth Rule（數學深度規則）清楚說明

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

`demo/` 底下必須依概念建立子資料夾，例如：

```text
demo/
├─ demo_README.md
├─ concept_a/
├─ concept_b/
└─ concept_c/
```

上述 `concept_*` 是通用占位名稱；實際資料夾必須使用該週核心概念的英文或可維護命名。不得要求所有 Week 都建立 Week01 Transformer（轉換器架構）專用的 `token/`、`embedding/`、`qkv/`、`attention/` 等資料夾。

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

notion網址:https://app.notion.com/p/VLM-VLA-377e28c1d7e081c3bd09c44d3368c921

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

### 核心概念 1

請用自己的話說明：

---

### 核心概念 2

請用自己的話說明：

---

### 核心概念 3

請用自己的話說明：

---

### 本週與 VLM/VLA 研究的關係

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

表示核心概念、Tasks、Demo 或應用關聯仍明顯不足。學生需重新閱讀與補做主要任務後再進入 Reviewing。

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

確保學生能理解、實作、驗證並連結到適當的應用脈絡。

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
* 必須同時遵守 Section 16：Concept Dependency Rule（概念依賴規則）
* 必須同時遵守 Section 17：Deep Learning Content Rule（深度學習內容規則）
* 若涉及公式，還必須遵守 Section 21：Mathematical Depth Rule（數學深度規則）

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

### Level 4：Application Relation（應用關聯）

必須回答：

「它與哪些後續應用或系統脈絡有關？」

要求：

* 可依概念內容選擇說明與 Transformer（轉換器架構）的關聯
* 可依概念內容選擇說明與 Vision-Language Model（視覺語言模型，VLM）的關聯
* 可依概念內容選擇說明與 Vision-Language-Action Model（視覺語言動作模型，VLA）的關聯
* 可依概念內容選擇說明與機器人系統的關聯
* 不要求每個概念都強制說明 VLM/VLA，但重要概念仍需說明其應用脈絡

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

當讀完 Concept A（核心概念 A）後：

執行：

```text
python demo/concept_a/demo_concept_a.py
```

觀察：

* Concept A 的輸入如何轉換
* Concept A 的輸出如何對應本週資料流

預期輸出：

```text
Concept A output: [...]
```

執行後請回答：

1. Concept A 的輸入與輸出是什麼？
2. Concept A 解決了本週資料流中的什麼問題？
3. Concept A 的下一步會接到哪個概念？

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

---

## 16. Concept Dependency Rule（概念依賴規則）

每個核心概念必須說明它在學習鏈中的位置，避免學生只背名詞而不知道資料如何往下一步流動。

每個核心概念必須包含：

1. 輸入是什麼
2. 輸出是什麼
3. 為什麼需要這個機制
4. 解決什麼問題
5. 下一步會進入哪個概念

### 範例：Embedding（嵌入向量）

輸入：

* Token ID（詞元編號）

輸出：

* Embedding Vector（嵌入向量）

目的：

* 將離散 Token（詞元）轉換為可運算的向量表示。

解決問題：

* 原始 Token ID 只是編號，無法直接表達語意相似度或上下文關係。

下一步：

* Query（查詢）、Key（鍵）、Value（值）

### 概念銜接要求

教材應清楚呈現概念之間的資料流，例如：

```text
Text（文字）
-> Token（詞元）
-> Token ID（詞元編號）
-> Embedding Vector（嵌入向量）
-> Query（查詢）/ Key（鍵）/ Value（值）
-> Attention Score（注意力分數）
-> Contextual Representation（上下文表示）
```

若某週教材只涵蓋其中一部分，也必須說明尚未涵蓋的後續概念會在何時補上。

---

## 17. Deep Learning Content Rule（深度學習內容規則）

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

### 範例：Attention（注意力機制）

不足寫法：

```text
Attention 是一種讓模型關注重要資訊的方法。
```

合格寫法應補足：

* 為什麼只靠 Embedding（嵌入向量）仍不足以理解上下文
* Query（查詢）與 Key（鍵）如何比對
* Q x K 如何產生 Attention Score（注意力分數）
* Attention Score 如何加權 Value（值）
* 為什麼加權後的表示比原本單一 Token 表示更有上下文資訊

---

## 18. Multi-Level Demo Rule（多層次 Demo 規則）

每個核心概念至少應具備以下其中兩種 Demo 類型。若概念是關鍵主題，建議三種都具備。

### Level A：Concept Demo（概念示範）

用途：

* 用於理解概念本身。
* 可以使用人工資料、簡化數字或生活化輸入。

### Level B：Mechanism Demo（機制示範）

用途：

* 用於理解內部運作。
* 應呈現中間步驟，例如分數、矩陣、向量、資料流或狀態變化。

### Level C：Real Model Demo（真實模型示範）

用途：

* 用於觀察真實模型行為。
* 可使用 Hugging Face Transformers（模型工具套件）、PyTorch（深度學習框架）或其他合適工具。
* 若需要下載模型、資料或大型套件，必須明確提示。

### 範例：Embedding（嵌入向量）

* Concept Demo（概念示範）：觀察 Token（詞元）如何轉成向量。
* Mechanism Demo（機制示範）：比較不同詞的向量相似度。
* Real Model Demo（真實模型示範）：使用 Hugging Face Transformers 取出真實模型 Embedding。

### 範例：Attention（注意力機制）

* Concept Demo（概念示範）：手動注意力分數。
* Mechanism Demo（機制示範）：QKV 計算流程。
* Mechanism Demo（機制示範）：Attention Matrix（注意力矩陣）。

### Demo 規模要求

Demo 應保持小而清楚：

* 一個 Demo 優先說明一個概念或一個機制。
* 不應用單一大型 Demo 同時混合 Token、Embedding、QKV、Attention Matrix、模型下載與視覺化。
* 若概念有多層理解，應拆成多個 Demo，並在概念子資料夾 `README.md` 說明建議順序。

---

## 19. Demo Unit Folder Rule（Demo 單元資料夾規則）

Demo 不得全部放於同一資料夾。

每週 `demo/` 底下必須依照概念建立子資料夾。

範例：

```text
demo/
├─ concept_a/
├─ concept_b/
└─ concept_c/
```

資料夾名稱應依該週主題決定，不得將 Week01 Transformer（轉換器架構）的概念資料夾固定套用到所有週次。

每個子資料夾至少包含：

```text
README.md
demo_*.py
```

每個概念子資料夾 `README.md` 必須包含：

* 對應概念
* 執行指令
* 預期輸出
* 觀察重點
* 執行後應回答的問題

教材中的 Demo 路徑必須指向對應子資料夾。

正確範例：

```text
python demo/concept_a/demo_concept_a.py
python demo/concept_b/demo_concept_b.py
```

錯誤範例：

```text
python demo/demo_xxx.py
```

若某週暫時沒有某概念的 Demo，該概念子資料夾可不建立；但一旦該概念有 Demo，就必須使用對應概念子資料夾。

---

## 20. Refactor Over Append Rule（重構優先於追加規則）

教材更新時，優先重構既有內容，而不是在文件最後追加補充內容。

不得出現以下結構：

```text
前面章節：
Token（簡易版）
Embedding（簡易版）
Attention（簡易版）

文件最後：
Token（完整版）
Embedding（完整版）
Attention（完整版）
```

新增內容必須整合回原本對應章節。

例如：

* Token（詞元）的補強內容必須整合進 Token 章節。
* Embedding（嵌入向量）的補強內容必須整合進 Embedding 章節。
* QKV 內容必須整合進 Attention（注意力機制）或獨立 QKV 章節，而不是放在文件最後。
* Demo 提示必須出現在對應概念段落後方，而不是集中放在最後。

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

## 21. Mathematical Depth Rule（數學深度規則）

目的：

避免教材只給公式，不解釋公式。

若某概念的數學內容為理解核心機制所必需，教材不得只列出公式，必須同時說明公式背後的直覺、變數、用途與驗證方式。

常見需要數學深度說明的概念包含：

* Embedding（嵌入向量）
* Query-Key-Value（查詢-鍵-值，QKV）
* Attention（注意力機制）
* Softmax（柔性最大化函數）
* Position Encoding（位置編碼）
* Multi-Head Attention（多頭注意力）
* Transformer（轉換器架構）

### 必須包含

若教材使用公式，必須包含：

1. 公式
2. 各變數意義
3. 幾何或直覺解釋
4. 為什麼需要此公式
5. Demo 驗證方式

禁止只出現公式而沒有說明。

### 範例：Attention Score（注意力分數）

公式：

```text
score = Q x K^T
```

必須說明：

* Q 是 Query（查詢），代表目前位置想找的資訊。
* K 是 Key（鍵），代表每個位置可被比對的特徵。
* `K^T` 是 Key Matrix Transpose（鍵矩陣轉置），讓 Query 可以和多個 Key 做內積比對。
* 內積用來估計 Query 和 Key 的方向是否相近。
* score（分數）越高，代表目前 Query 越應該關注該 Key 對應的位置。
* Demo 可透過該週對應概念資料夾中的機制示範，例如 `demo/concept_a/demo_concept_a.py`，觀察公式中的輸入、輸出與中間數值變化。

### 數學說明深度

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

### 禁止寫法

不得只寫：

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

而沒有說明：

* Q、K、V 分別是什麼
* `d_k` 是什麼
* 為什麼要除以 `sqrt(d_k)`
* Softmax（柔性最大化函數）如何把分數轉成權重
* 權重如何加權 Value（值）
* Demo 中如何觀察上述步驟

---

## 22. Demo Completion Rule（Demo 完成規則）

目的：

避免學生只執行程式卻沒有學習。

Demo 不以成功執行為完成條件。

學生必須完成以下全部項目，才可視為 Demo 完成：

1. 成功執行 Demo。
2. 保存輸出結果。
3. 在 `study_log.md` 記錄觀察。
4. 回答 Demo `README.md` 中的問題。

### Demo README 必須提供

每個 Demo 的總覽或概念子資料夾 `README.md` 必須包含：

* 執行指令
* 預期輸出
* 觀察重點
* 驗收問題

### study_log.md 記錄要求

學生執行 Demo 後，`study_log.md` 應至少紀錄：

* Demo 名稱
* 執行日期
* 是否成功執行
* 重要輸出摘要
* 觀察到的概念
* 遇到的問題
* Demo README 驗收問題的回答位置

### Completion 判定

`completion.md` 中的 Demo 勾選必須代表學生已完成執行、保存、觀察與回答，不得只因程式沒有報錯就勾選完成。

Codex 不得代替學生勾選 Demo 完成，也不得代替學生撰寫個人理解。

---

## 23. Week01 Minimum Coverage Rule（Week01 專用最低涵蓋規則）

目的：

確保 Transformer（轉換器架構）基礎完整，避免 Week01 教材只涵蓋表層概念而直接進入 Generated（教材已生成）狀態。

本規則僅適用於 `learning/Week01_Transformer/`。其他 Week 不得直接套用 Week01 的必要概念與 Demo 資料夾清單，應依 Section 24：WeekXX Minimum Coverage Template（WeekXX 最低涵蓋模板）另行定義。

Week01 Transformer 必須至少涵蓋以下概念：

1. Token（詞元）
2. Token ID（詞元編號）
3. Embedding（嵌入向量）
4. Query（查詢）
5. Key（鍵）
6. Value（值）
7. Attention（注意力機制）
8. Self-Attention（自注意力）
9. Attention Matrix（注意力矩陣）
10. Position Encoding（位置編碼）
11. Multi-Head Attention（多頭注意力）
12. Encoder（編碼器）
13. Decoder（解碼器）

缺少以上任一項目，不得標記為 Generated（教材已生成）。

### Week01 Generated 最低條件

Week01 進入 Generated 前，除了 Section 6 的 Not Started → Generated 條件，也必須滿足：

* `notes.md` 已整合上述 13 個概念。
* 每個概念至少符合 Section 13 的五層學習架構。
* 每個概念至少說明輸入、輸出、目的、解決問題與下一步概念。
* 涉及公式的概念符合 Section 21：Mathematical Depth Rule（數學深度規則）。
* Demo 依 Section 19 建立概念子資料夾。
* Demo 完成定義依 Section 22 說明，不得只以成功執行作為完成。

### Week01 Demo 建議最低結構

Week01 `demo/` 建議至少包含：

```text
demo/
├─ demo_README.md
├─ token/
├─ embedding/
├─ qkv/
├─ attention/
├─ self_attention/
├─ position_encoding/
├─ multi_head_attention/
└─ encoder_decoder/
```

若某概念尚未有 Real Model Demo（真實模型示範），至少必須提供 Concept Demo（概念示範）或 Mechanism Demo（機制示範），並在 Knowledge Gap Check（知識缺口檢查）中說明後續補強方向。

---

## 24. WeekXX Minimum Coverage Template（WeekXX 最低涵蓋模板）

目的：

每一週都應依該週主題定義最低涵蓋概念，避免只有通用文件結構，卻沒有明確的主題驗收標準。

使用方式：

1. 建立或更新某週教材前，先依該週主題填寫本模板。
2. 將該週必要概念、必要 Demo、Generated（教材已生成）最低條件寫清楚。
3. 若某週已有專用 Minimum Coverage Rule（最低涵蓋規則），以該週專用規則為準。
4. 不得把 Week01 Transformer（轉換器架構）的必要概念清單直接套用到其他週。

### WeekXX 主題資訊

```text
Week：WeekXX
Topic：本週主題名稱
Folder：learning/WeekXX_TopicName/
```

### WeekXX 必要概念

請依本週主題列出必要概念。每個概念都必須符合 Section 13：Learning Content Standard（學習內容標準）、Section 16：Concept Dependency Rule（概念依賴規則）與 Section 17：Deep Learning Content Rule（深度學習內容規則）。

```text
1. Concept A（中文翻譯）
2. Concept B（中文翻譯）
3. Concept C（中文翻譯）
```

### WeekXX Demo 建議最低結構

`demo/` 子資料夾必須依本週核心概念建立，不得固定使用其他週次的資料夾名稱。

```text
demo/
├─ demo_README.md
├─ concept_a/
│  ├─ README.md
│  └─ demo_*.py
├─ concept_b/
│  ├─ README.md
│  └─ demo_*.py
└─ concept_c/
   ├─ README.md
   └─ demo_*.py
```

### WeekXX Generated 最低條件

WeekXX 進入 Generated（教材已生成）前，除了 Section 6 的 Not Started → Generated 條件，也必須滿足：

* `notes.md` 已整合本週必要概念。
* 每個必要概念至少符合五層學習架構。
* 每個必要概念至少說明輸入、輸出、目的、解決問題與下一步概念。
* 涉及公式的概念符合 Section 21：Mathematical Depth Rule（數學深度規則）。
* Demo 依 Section 19 建立概念子資料夾。
* Demo 完成定義依 Section 22 說明，不得只以成功執行作為完成。

### WeekXX Knowledge Gap Check（知識缺口檢查）

`notes.md` 最後必須列出：

* 已學會內容。
* 尚未深入內容。
* 下一週將銜接的方向。
