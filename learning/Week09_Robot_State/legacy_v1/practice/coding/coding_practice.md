# Week09 Coding Practice Record

## 練習清單

| 練習 | 模式 | 對應檔案 | 目標 |
|---|---|---|---|
| Camera Pipeline | Implementation Practice Mode | `exercises/camera_pipeline_practice.py` | 完成來源、讀取、保存與交接 |

## TODO

1. `open_source`：合成模式回傳標記；相機模式建立並檢查 `VideoCapture`。
2. `read_frame`：產生或讀取一張 BGR 影格，檢查回傳值、shape 與 dtype。
3. `save_snapshot`：建立父資料夾並檢查 `cv2.imwrite()`。
4. `build_handoff`：加入 trace fields（追蹤欄位）、影格 metadata 及任務規則。

## 學生觀察

| 測試 | 是否執行 | frame shape/backend | 觀察 |
|---|---|---|---|
| synthetic caption |  |  |  |
| synthetic VQA |  |  |  |
| physical camera caption |  |  |  |
| invalid VQA |  |  |  |

## 錯誤紀錄

| 錯誤 | 所屬層 | 修正方式 |
|---|---|---|
|  |  |  |

## 自我檢查

* [ ] 例外發生時仍會釋放實體相機
* [ ] 我有檢查 `read()` 與 `imwrite()` 回傳值
* [ ] metadata 與實際 frame shape 一致
* [ ] VQA 問題為空時會被拒絕
* [ ] 我沒有把合成測試記成實體相機驗收
* [ ] 結果已記錄至 study_log.md

