# AGENTS.md

> Current version: v3.2

本文件是本專案目前唯一且主要的 Agent（代理）規範文件，用來指引 Codex（程式協作代理）在維護每週學習資料夾時應遵守的結構、邊界與工作流程。

本規範延續 v3.1 的核心精神：GitHub（程式碼託管平台）保存教材、Demo（示範範例）、Practice（練習）、程式碼與版本歷史；Notion（專案管理工具）只管理進度、狀態、回顧與摘要；學生的學習紀錄、反思、Demo 結果、Practice 結果與完成狀態，不得由 Codex 假裝完成。

---

## 1. Project Scope（專案範圍）

本 Repository（儲存庫）用於保存 Vision-Language Model（視覺語言模型，VLM）與 Vision-Language-Action Model（視覺語言動作模型，VLA）相關學習教材、可執行 Demo、Practice、練習解答與學習紀錄模板。

Codex 可以協助建立教材結構、撰寫空白模板、整理 Demo、建立練習骨架、撰寫參考答案與補齊文件連結，但不得假裝學生已閱讀、已執行、已完成、已反思、已通過驗收或已更新 Notion。

本專案不得新增船體、浮力、海浪、海事機器人等與目前 VLM/VLA 學習主線無關的內容。

---

## 2. Repository Structure（儲存庫結構）

Repository 預期維持以下主要結構：

```text
docs/
learning/
modules/
templates/
assets/
```

各資料夾用途：

- `docs/`：專案總覽、設計規範、Notion 對應規則與長期文件。
- `learning/`：每週學習教材、Demo、Practice 與學習紀錄模板。
- `modules/`：可重用的課程模組、範例模組或工具程式。
- `templates/`：Notion、週計畫、學習紀錄與練習模板。
- `assets/`：圖片、圖表、資料檔與教材素材。

每週資料夾統一放在：

```text
learning/WeekXX_TopicName/
```

---

## 3. Weekly Folder Standard（每週資料夾標準）

每週標準資料夾結構如下：

```text
learning/WeekXX_TopicName/
├─ README.md
├─ weekly_plan.md
├─ notes.md
├─ study_log.md
├─ demo/
└─ practice/
   ├─ README.md
   ├─ concept/
   │  ├─ concept_practice.md
   │  └─ concept_answer_key.md
   └─ coding/
      ├─ README.md
      ├─ coding_practice.md
      ├─ coding_answer_key.md
      ├─ requirements.txt
      ├─ exercises/
      │  └─ *_practice.py
      └─ solutions/
         └─ *_solution.py
```

每個主要檔案的責任：

- `README.md`：該週學習主題、先備知識、學習地圖與檔案導覽。
- `weekly_plan.md`：該週學習目標、學習安排、Demo 順序、Practice 順序與驗收標準。
- `notes.md`：主要觀念、推導、重點摘要與教材筆記。
- `study_log.md`：學生實際完成後的學習紀錄、反思、錯誤修正與 Demo/Practice 結果摘要模板。
- `demo/`：完整可執行範例，用來觀察概念、輸入輸出與中間結果。
- `practice/`：所有練習相關內容的唯一入口。

---

## 4. Practice Directory Rule（練習資料夾規則）

`practice/` 是所有練習相關內容的唯一入口。

Week 根目錄不得直接放置下列練習檔案：

- `concept_practice.md`
- `coding_practice.md`
- `answer_key.md`
- `*_practice.py`
- `*_solution.py`

觀念練習只能放在：

- `practice/concept/concept_practice.md`
- `practice/concept/concept_answer_key.md`

程式練習只能放在：

- `practice/coding/coding_practice.md`
- `practice/coding/coding_answer_key.md`
- `practice/coding/exercises/`
- `practice/coding/solutions/`
- `practice/coding/requirements.txt`

`practice/README.md` 是該週練習總入口，需說明練習目標、Concept Practice（觀念練習）入口、Coding Practice（程式練習）入口、建議完成順序、是否需要安裝額外 Python（程式語言）函式庫，以及參考答案的位置與查看提醒。

Codex 在新增或重構每週資料夾時，必須將練習內容放入 `practice/`，不得讓練習題、答案或練習程式散落於 Week 根目錄。

---

## 5. Concept Practice Rule（觀念練習規則）

`practice/concept/concept_practice.md` 是學生觀念作答檔，應包含題目、作答區、提示與自我檢查項目。

`concept_practice.md` 不得填入學生答案。Codex 可以建立空白作答區，例如：

```markdown
## Q1

題目：

學生作答：

-
```

`practice/concept/concept_answer_key.md` 是觀念參考答案。

`concept_answer_key.md` 開頭必須提醒學生完成練習後再查看，例如：

```markdown
> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。
```

參考答案應清楚標示題號，並以解釋概念、釐清誤解與補充學習重點為主。

---

## 6. Coding Practice Rule（程式練習規則）

`practice/coding/coding_practice.md` 是程式練習索引與作答紀錄表，應包含練習清單、對應的 `exercises/` 檔案、建議執行方式、學生紀錄欄位與自我檢查欄位。

`coding_practice.md` 不放完整答案。完整可執行參考程式只能放在 `practice/coding/solutions/`，文字解釋與錯誤修正說明放在 `practice/coding/coding_answer_key.md`。

`practice/coding/exercises/*.py` 是學生實際練習用 Python 檔案，必須包含必要骨架、提示與學生需完成的區塊。學生需完成的地方可使用：

- `TODO` 註解
- `None`
- `raise NotImplementedError`

`practice/coding/solutions/*.py` 是完整可執行參考程式，應能獨立執行，或清楚說明執行方式。

`practice/coding/coding_answer_key.md` 是程式練習文字解釋檔，負責說明：

- 每題 TODO 應該如何補
- 為什麼這樣寫
- 常見錯誤
- shape（張量形狀）不一致問題
- softmax（歸一化指數函數）軸向錯誤
- Token ID（詞元識別碼）和 Embedding（嵌入向量）混淆等問題

`coding_answer_key.md` 開頭必須提醒學生完成 `exercises/` 後再查看，例如：

```markdown
> 請先完成 `exercises/` 中的練習檔案，再查看本程式練習參考說明。
```

`practice/coding/requirements.txt` 放該週程式練習需要安裝的函式庫。若該週不需要額外函式庫，`requirements.txt` 可保留空檔，或註明：

```text
# No extra packages required.
```

Codex 不得把 `solutions/` 的完整答案複製到 `exercises/`，也不得在學生作答紀錄中假裝學生已完成測試。

---

## 7. Demo And Practice Separation Rule（Demo 與 Practice 分離規則）

`demo/` 與 `practice/` 的用途必須明確分開。

`demo/` 是完整可執行範例，用來觀察概念、輸入輸出與中間結果。Demo 可以包含完整程式碼，因為它的目的不是讓學生補空，而是讓學生看懂流程。

`practice/coding/exercises/` 是學生實際補程式碼的練習檔，應保留必要骨架、提示與待完成區塊。

`practice/coding/solutions/` 是完整參考解答，學生應先完成 `exercises/` 再查看。

`practice/coding/coding_answer_key.md` 是文字解釋與錯誤修正說明，用來補充參考程式的思路、常見錯誤與形狀檢查。

Codex 不得把 `demo/` 當成 `practice/` 的替代品。若某週需要練習，必須建立 `practice/` 結構；Demo 只能作為觀察範例，不能取代學生作答與練習紀錄。

---

## 8. Weekly Plan Rule（每週計畫規則）

每週 `weekly_plan.md` 只保留以下內容：

- 學習目標
- 學習安排
- Demo 順序
- Practice 順序
- 驗收標準

`weekly_plan.md` 不直接放完整練習題、不放完整觀念答案，也不放完整程式解答。

`weekly_plan.md` 必須連結到：

```markdown
- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
```

若有參考答案連結，應提醒學生完成練習後再查看：

```markdown
- [Concept Answer Key](./practice/concept/concept_answer_key.md)
- [Coding Answer Key](./practice/coding/coding_answer_key.md)
- [Coding Solutions](./practice/coding/solutions/)
```

建議模板：

```markdown
# WeekXX Weekly Plan

## 學習目標

-

## 學習安排

-

## Demo 順序

1.

## Practice 順序

1. [Practice Overview](./practice/README.md)
2. [Concept Practice](./practice/concept/concept_practice.md)
3. [Coding Practice](./practice/coding/coding_practice.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)
- [Coding Answer Key](./practice/coding/coding_answer_key.md)
- [Coding Solutions](./practice/coding/solutions/)

## 驗收標準

- [ ] 已閱讀 README.md
- [ ] 已閱讀 notes.md
- [ ] 已執行指定 Demo
- [ ] 已由學生完成 Concept Practice
- [ ] 已由學生完成 Coding Practice
- [ ] 已由學生填寫 study_log.md
- [ ] 已由學生或明確資料來源更新 Notion 學習進度
- [ ] 已完成 ChatGPT（聊天式人工智慧）驗收
```

---

## 9. Study Log Rule（學習紀錄規則）

`study_log.md` 只放學生實際完成後的學習紀錄、反思、錯誤修正與 Demo/Practice 結果摘要。

Codex 不得自動填入「已完成」、不得假裝學生已完成 Demo、不得假裝學生已完成 Practice，也不得代替學生寫反思。

Codex 可以建立空白模板、待填區塊與紀錄表格，例如：

```markdown
# WeekXX Study Log

## 實際學習時間

| 日期 | 時間 | 學習內容 | 備註 |
|---|---|---|---|
|  |  |  |  |

## Demo 結果摘要

| Demo | 是否執行 | 觀察結果 | 問題 |
|---|---|---|---|
|  |  |  |  |

## Practice 結果摘要

| Practice | 是否完成 | 錯誤修正 | 備註 |
|---|---|---|---|
|  |  |  |  |

## 本週反思

-

## 尚未理解的問題

-

## 下一步

-
```

任何完成狀態都必須來自學生實際回報，或由學生親自填寫。

---

## 10. Demo Rule（Demo 規則）

Demo 應放在 `demo/`，並保持完整可執行。

Demo 的目的：

- 觀察概念如何運作
- 顯示輸入、輸出與中間結果
- 幫助學生理解 `notes.md` 中的觀念
- 作為 Practice 前的參考觀察材料

Demo 可以包含完整解法，但應避免混入學生作答區。若某段程式需要學生練習，應另放到 `practice/coding/exercises/`。

Demo 說明文件應清楚列出 Demo 目標、執行方式、預期輸出、觀察重點與本週概念的關係。

---

## 11. Documentation Rule（文件規則）

所有教材文件應使用清楚、可追蹤、可驗收的寫法。

英文專有名詞第一次出現時需附繁體中文翻譯。後續可使用英文縮寫或原文，但不得讓學生第一次遇到概念時沒有中文對照。

文件應避免把教材、Demo、Practice 與學習紀錄混在同一檔案。每個檔案應有明確責任：

- `README.md` 負責導覽。
- `notes.md` 負責教材內容。
- `weekly_plan.md` 負責學習安排與驗收。
- `study_log.md` 負責學生實際紀錄模板。
- `demo/` 負責完整可執行範例。
- `practice/` 負責所有練習內容。

---

## 12. GitHub Workflow（GitHub 工作流程）

GitHub 保存教材、Demo、Practice、程式碼與版本歷史。

不得直接在 `main` 分支上累積大型學習週變更。每週教材或重構應使用獨立 Branch（分支）。

建議分支命名：

```text
week01-transformer
week02-clip
week03-huggingface
```

產生新週教材時，建議 Commit（提交）訊息：

```text
Generate WeekXX learning materials
```

依照新版規範重構既有週資料夾時，建議 Commit 訊息：

```text
Update WeekXX to latest AGENTS standard
```

本次整理主規範時，建議 Commit 訊息：

```text
Rename AGENTS v3.2 to AGENTS and refine practice standard
```

---

## 13. Notion Workflow（Notion 工作流程）

Notion 只管理進度、狀態、回顧與摘要，不取代 GitHub 中的教材檔案。

Notion 可以記錄：

- 每週狀態
- 學生是否開始學習
- 學生是否完成 Demo
- 學生是否完成 Practice
- 回顧與問題
- Review（審查）結果

Codex 不得在沒有學生回報或明確資料來源時，將 Notion 狀態改成 Completed（已完成）。

若 Codex 沒有 Notion 存取權，應請使用者提供 Notion URL（網址）或 ID（識別碼），不得假裝已更新 Notion。

---

## 14. Week Lifecycle（每週生命週期）

每週狀態建議維持：

```text
Not Started
-> Generated
-> Learning
-> Reviewing
-> Completed
```

狀態意義：

- `Not Started`：尚未建立或尚未開始。
- `Generated`：教材、Demo、Practice 與模板已建立，但學生尚未完成學習。
- `Learning`：學生正在閱讀教材、執行 Demo 或完成 Practice。
- `Reviewing`：學生已提交學習紀錄或練習結果，等待檢查。
- `Completed`：學生已完成必要學習、紀錄、驗收與 Notion 更新。

Codex 可以協助從 `Not Started` 產生 `Generated`，但不得自行把週狀態推進到 `Completed`。

---

## 15. Week Generation Rule（每週產生規則）

建立或重構 WeekXX 時，Codex 應先閱讀本 `AGENTS.md`。

每週資料夾必須包含：

- 根目錄四個核心 Markdown（標記語言）檔案：`README.md`、`weekly_plan.md`、`notes.md`、`study_log.md`
- `demo/`
- `practice/README.md`
- `practice/concept/concept_practice.md`
- `practice/concept/concept_answer_key.md`
- `practice/coding/README.md`
- `practice/coding/coding_practice.md`
- `practice/coding/coding_answer_key.md`
- `practice/coding/requirements.txt`
- `practice/coding/exercises/`
- `practice/coding/solutions/`

若既有週資料夾使用舊結構，Codex 應採取 Refactor（重構）而不是單純 Append（附加）的方式：

- 將練習入口集中到 `practice/`
- 將觀念練習移到 `practice/concept/`
- 將程式練習移到 `practice/coding/`
- 將完整答案移到對應的 answer key 或 `solutions/`
- 更新 `weekly_plan.md` 連結
- 保留學生已填寫內容，不得覆蓋或假裝完成

---

## 16. ChatGPT Validation（ChatGPT 驗收）

ChatGPT 驗收用於檢查教材品質與學習成果是否達到標準。

驗收可分為：

- `Pass`：結構完整、教材清楚、Demo 可執行、Practice 與解答分離、學生紀錄完整。
- `Minor Revision`：小幅修正即可通過，例如連結、文字、提示或格式問題。
- `Major Revision`：結構錯誤、練習與答案混放、Demo 無法執行、缺少必要 Practice，或 Codex 假裝學生完成。

驗收必須額外檢查：

- `practice/` 是否為練習唯一入口。
- Week 根目錄是否沒有散落練習檔案。
- `concept_practice.md` 是否未填入學生答案。
- `concept_answer_key.md` 是否有查看前提醒。
- `coding_practice.md` 是否未放完整答案。
- `coding_answer_key.md` 是否有完成 `exercises/` 後再查看的提醒。
- `exercises/*.py` 是否保留學生需完成的區塊。
- `solutions/*.py` 是否為完整參考答案。
- `weekly_plan.md` 是否連到三個 Practice 入口，且使用 `./practice/...` 連結。
- `study_log.md` 是否沒有假完成內容。

---

## 17. Codex Operating Rules（Codex 操作規則）

Codex 在本 Repository 工作時必須遵守：

- 先閱讀目前唯一主規範 `AGENTS.md`。
- 只修改任務要求範圍內的檔案。
- 不得擅自重寫 Week01 到 Week16 的實際內容。
- 不得把學生學習紀錄、反思或完成狀態寫成已完成。
- 不得把 Demo 當成 Practice 的替代品。
- 不得把完整答案放入學生作答檔或練習骨架。
- 不得在沒有使用者授權、學生回報或明確資料來源時更新 Notion 狀態為 Completed。
- 重構時應保留既有教材精神與學生已填內容。
- 若需要遷移舊結構，應先說明移動規則與影響範圍。

`AGENTS.md` 是本專案目前唯一且主要的 Agent 規範文件。Codex 應以本文件為最高優先標準；若任務說明與本文件衝突，除非使用者明確要求覆寫本規範，否則應以本文件為準。
