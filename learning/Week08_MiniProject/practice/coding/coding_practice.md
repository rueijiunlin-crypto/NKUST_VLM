# Week08 Coding Practice Record

## 練習清單

| 練習 | 模式 | 檔案 | 學習目標 |
|---|---|---|---|
| Mini VLM Pipeline | Implementation Practice Mode | `exercises/mini_vlm_pipeline_practice.py` | 完成驗證、推論與結果封裝 |

## TODO

1. `validate_request`：檢查任務、問題與影像路徑；`--dry-run` 時允許占位路徑。
2. `run_model`：依任務選擇正確 BLIP 模型，將輸入移到同一裝置並解碼結果。
3. `build_result`：建立含 UUID、UTC 時間與共同欄位的 JSON-compatible dictionary（可轉 JSON 的字典）。

## 執行方式

```bash
python practice/coding/exercises/mini_vlm_pipeline_practice.py --task caption --image placeholder.jpg --dry-run
python practice/coding/exercises/mini_vlm_pipeline_practice.py --task caption --image <IMAGE_PATH>
python practice/coding/exercises/mini_vlm_pipeline_practice.py --task vqa --image <IMAGE_PATH> --question "What is visible?"
```

## 學生觀察

| 測試 | 是否執行 | 輸出／觀察 |
|---|---|---|
| dry-run |  |  |
| caption |  |  |
| vqa |  |  |
| 不合法請求 |  |  |

## 錯誤紀錄

| 錯誤訊息 | 發生條件 | 修正方式 |
|---|---|---|
|  |  |  |

## 自我檢查

* [ ] 我沒有修改 Demo 作為練習答案
* [ ] VQA 問題為空時會在模型載入前失敗
* [ ] Caption 與 VQA 使用正確模型類別
* [ ] 所有模型輸入與模型位於相同裝置
* [ ] 輸出可由 `json.dumps` 序列化
* [ ] 我已將真實觀察記錄到 study_log.md

