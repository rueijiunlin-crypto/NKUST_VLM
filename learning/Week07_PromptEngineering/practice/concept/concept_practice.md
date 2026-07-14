# Week07 Concept Practice

> 請先自行作答，再查看 `concept_answer_key.md`。

## 1. Prompt Anatomy

Role、Task、Evidence boundary、Output contract、Unknown policy 與 Safety boundary 各有何作用？

### 學生作答區



### 自我檢查

- [ ] 我沒有用「讓回答更準」概括所有段落。

## 2. Chat Template

Chat template 與 Prompt content 有何差異？為什麼不能把同一角色格式套到所有模型？

### 學生作答區



### 自我檢查

- [ ] 我有提到 checkpoint control tokens。

## 3. Structured Output

為室內語意目標設計至少四個 JSON 欄位、型別與允許值。

### 學生作答區



### 自我檢查

- [ ] 我包含未知狀態與 evidence。

## 4. Validation Layers

Syntax、schema、semantic、grounding、freshness 與 safety 各檢查什麼？

### 學生作答區



### 自我檢查

- [ ] 我能舉出 JSON 合法但 grounding 失敗的例子。

## 5. Retry Policy

哪些錯誤適合有限重試？哪些應要求新觀察或直接拒絕？

### 學生作答區



### 自我檢查

- [ ] 我沒有要求 unknown 強制改成 found。

## 6. Prompt Comparison

如何公平比較兩個 Prompt 版本？至少列出五個需要固定或記錄的條件。

### 學生作答區



### 自我檢查

- [ ] 我包含模型、資料、生成設定與評估規則。

## 7. Robot Safety

為什麼 VLM 輸出 `found exit` 不能直接轉成導航或速度命令？

### 學生作答區



### 自我檢查

- [ ] 我有列出語意、地圖、障礙與控制驗證。

## 8. Test Matrix

請設計正常、未知、錯誤前提、格式錯誤與安全違規案例的預期結果。

### 學生作答區



### 自我檢查

- [ ] 每個案例都有預期 status 與 failure layer。
