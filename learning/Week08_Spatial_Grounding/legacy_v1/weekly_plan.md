# Week08 Weekly Plan

## 本週目標

- 建立影像描述與視覺問答的最小可執行流程。
- 使用共同 JSON Schema（JSON 結構規格）封裝成功、未知與錯誤結果。
- 分離輸入驗證、模型推論與輸出建構三個責任。
- 以至少三種情境檢查正常輸入、資訊不足與錯誤輸入。

## 必學概念

- Captioning 與 VQA 的輸入輸出差異。
- Processor（前處理器）、模型推論、解碼與結果封裝。
- 可驗證的資料契約、時間戳與追蹤識別碼。
- 失敗模式：檔案不存在、問題缺失、模型下載失敗與結果欄位錯誤。

## 建議學習順序

1. 閱讀 [README.md](./README.md) 與 [notes.md](./notes.md)。
2. 執行資料契約及驗證 Demo。
3. 安裝 Demo 依賴並準備本機影像。
4. 執行 Caption 與 VQA Demo，比較輸入與輸出。
5. 完成 [Practice Overview](./practice/README.md)，程式部分採 Implementation Practice Mode。
6. 在 [study_log.md](./study_log.md) 記錄三種測試情境與問題。

## Demo 執行順序

1. `python demo/demo_01_input_output_contract.py`
2. `python demo/demo_04_result_validation.py`
3. `python demo/demo_02_blip_caption.py --image <IMAGE_PATH>`
4. `python demo/demo_03_blip_visual_qa.py --image <IMAGE_PATH> --question "What is in the image?"`

完整安裝與觀察方式請見 [demo/demo_README.md](./demo/demo_README.md)。

## Practice 順序

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)（Implementation Practice Mode）

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)
- [Coding Answer Key](./practice/coding/coding_answer_key.md)
- [Coding Solutions](./practice/coding/solutions/)

## 任務清單

* [ ] 閱讀 README.md、weekly_plan.md 與 notes.md
* [ ] 執行必要 Demo 並保存輸出
* [ ] 以自己的影像完成 Caption 與 VQA 測試
* [ ] 完成 Concept Practice
* [ ] 完成 Coding Practice 中的 TODO
* [ ] 在 study_log.md 記錄觀察、錯誤與修正方式
* [ ] 更新 Notion 學習狀態
* [ ] 進行 ChatGPT 驗收

## 驗收條件

* [ ] 能解釋 Caption 與 VQA 的輸入差異
* [ ] 能說明共同結果資料契約各欄位用途
* [ ] 程式能阻擋不合法請求並輸出一致 JSON 結果
* [ ] 至少記錄正常、資訊不足與錯誤輸入三種情境
* [ ] Demo 與 Practice 的真實結果已寫入 study_log.md
* [ ] ChatGPT 驗收 Pass

