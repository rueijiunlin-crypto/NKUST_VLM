# Week09 Weekly Plan

## 本週目標

- 理解 OpenCV 影格的 shape（張量形狀）、資料型別與 BGR 顏色順序。
- 正確管理 `VideoCapture` 的開啟、讀取與釋放。
- 保存可重現的相機快照及觀測 metadata（中繼資料）。
- 將相機輸出轉成 Week08 可接受的 VLM 請求。

## 必學概念

- `VideoCapture.isOpened()`、`read()` 與 `release()`。
- `[height, width, channels]`、`uint8`、BGR 與 RGB。
- 相機索引、backend（後端）、解析度與讀取失敗。
- 取樣頻率、舊影格、時間戳與模型延遲。

## 建議學習順序

1. 閱讀 README.md 與 notes.md。
2. 觀察影格契約，再以合成影像執行探測與保存 Demo。
3. 有相機時重跑探測與保存 Demo，記錄 backend 與解析度。
4. 產生 VLM handoff JSON，檢查與 Week08 的欄位相容性。
5. 完成 Implementation Practice Mode 練習並記錄真實結果。

## Demo 執行順序

1. `python demo/demo_01_frame_contract.py`
2. `python demo/demo_02_camera_probe.py --synthetic`
3. `python demo/demo_03_capture_snapshot.py --synthetic --output outputs/synthetic.jpg`
4. `python demo/demo_04_vlm_handoff.py --image outputs/synthetic.jpg --task caption`
5. `python demo/demo_02_camera_probe.py --camera-index 0`（需實體相機）

完整說明見 [demo/demo_README.md](./demo/demo_README.md)。

## Practice 順序

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)（Implementation Practice Mode）

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)
- [Coding Answer Key](./practice/coding/coding_answer_key.md)
- [Coding Solutions](./practice/coding/solutions/)

## 任務清單

* [ ] 閱讀本週文件
* [ ] 執行合成影像測試
* [ ] 執行實體相機探測與快照保存
* [ ] 產生並檢查 VLM handoff JSON
* [ ] 完成 Concept Practice
* [ ] 完成 Coding Practice 中的 TODO
* [ ] 在 study_log.md 記錄實際輸出與錯誤
* [ ] 更新 Notion 學習狀態並進行 ChatGPT 驗收

## 驗收條件

* [ ] 能解釋 OpenCV BGR 影格與 VLM RGB 輸入的差異
* [ ] 相機失敗時能區分開啟失敗與讀取失敗
* [ ] `release()` 在成功或例外時都會執行
* [ ] 實體相機快照可解碼，且 study_log.md 記有 backend、shape 與時間
* [ ] handoff JSON 包含追蹤欄位與影格 metadata
* [ ] ChatGPT 驗收 Pass

