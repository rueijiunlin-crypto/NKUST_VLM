# Week08 Notes：Mini VLM Project

## 1. 從模型呼叫走向小型系統

單次模型推論只回答「模型能不能產生文字」；小型系統還必須回答輸入是否合理、結果如何追蹤、失敗時如何表達，以及下游程式是否能穩定讀取。這也是本週把流程拆成三層的原因：

```text
Request validation
        ↓
Model inference
        ↓
Result envelope
```

對應 Demo：`demo/demo_01_input_output_contract.py`

- 觀察重點：Caption 請求不需要問題，VQA 請求必須含問題。
- 預期輸出：請求與結果均為可讀取的 JSON。
- 執行後應能回答：為什麼不能只回傳一段文字？

## 2. Caption 與 VQA

Image Captioning（影像描述）通常只接受影像，輸出整體描述；VQA 同時接受影像與自然語言問題，輸出針對問題的回答。兩者可以共用結果欄位，但不能共用完全相同的請求驗證規則。

| 任務 | 必要輸入 | 主要輸出 | 適合用途 |
|---|---|---|---|
| Caption | 影像 | 整體描述 | 場景摘要、巡檢紀錄 |
| VQA | 影像、問題 | 問題導向答案 | 目標確認、屬性查詢 |

對應 Demo：

- `demo/demo_02_blip_caption.py`
- `demo/demo_03_blip_visual_qa.py`

執行後應能回答：同一張圖在兩種任務中，輸出的資訊範圍為何不同？

## 3. BLIP 推論資料流

本週以 Salesforce BLIP 模型作為可重現範例。Caption 使用 `BlipForConditionalGeneration`，VQA 使用 `BlipForQuestionAnswering`；兩者都透過 `BlipProcessor` 將影像與文字轉成模型需要的 tensor（張量），再將產生的 Token ID（詞元識別碼）解碼為文字。

```text
PIL image + optional question
            ↓ BlipProcessor
pixel_values + optional input_ids
            ↓ BLIP model.generate()
generated token ids
            ↓ processor.decode()
answer text
```

模型卡與使用條件：

- [BLIP image captioning base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [BLIP VQA base](https://huggingface.co/Salesforce/blip-vqa-base)

本專案固定 `transformers>=4.49,<5`，避免 Transformers 5 移除舊版 image-to-text pipeline 所造成的介面差異；程式則直接使用 BLIP 類別，不依賴 pipeline 捷徑。

## 4. 共同結果資料契約

每次結果都包含：

| 欄位 | 用途 |
|---|---|
| `schema_version` | 區分未來欄位變更 |
| `observation_id` | 串接影像、推論與 ROS2 訊息 |
| `timestamp_utc` | 記錄結果產生時間 |
| `task` | `caption` 或 `vqa` |
| `status` | `ok`、`unknown` 或 `error` |
| `source_image` | 輸入來源 |
| `question` | VQA 問題；Caption 為 `null` |
| `answer` | 模型結果或錯誤說明 |
| `model_id` | 模型來源與版本識別 |

`unknown` 表示輸入合理但資訊不足；`error` 表示系統無法完成推論。兩者不可混用，否則研究紀錄會把模型不確定性與系統故障混為一談。

## 5. 驗證與失敗模式

`demo/demo_04_result_validation.py` 展示跨欄位規則，例如 VQA 必須有問題、`ok` 必須有答案。執行時應觀察合法案例通過、缺少問題的案例被拒絕。

常見失敗包含：

- 影像路徑不存在或格式無法解碼。
- 第一次執行無法下載模型，或快取空間不足。
- CPU 推論時間過長。
- Caption 與 VQA 使用錯誤的模型類別。
- `pixel_values` 所在裝置與模型所在裝置不同。

## 6. 三種驗收情境

至少保留以下三類測試紀錄：

1. 正常且目標清楚的影像。
2. 遮擋、模糊或無法回答問題的影像。
3. 不存在的路徑、缺少 VQA 問題或不合法任務。

這些情境會在 Week09 換成相機影像，並在 Week10 將同一份結果發布至 ROS2 Topic。

## 本週尚未涵蓋

- 即時相機擷取與取樣策略。
- ROS2 Node（節點）、Topic（主題）與 QoS（服務品質）。
- 模型微調、量化與正式效能基準。

