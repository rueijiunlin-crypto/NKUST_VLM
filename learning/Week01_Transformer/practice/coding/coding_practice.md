# Week01 Coding Practice（程式練習）

本檔案是程式練習索引與作答紀錄表，不放完整答案。請在完成每個 `exercises/` 檔案後記錄結果。

## 練習清單

| 順序 | 練習檔案 | 主題 | 是否完成 | 執行結果 | 備註 |
|---|---|---|---|---|---|
| 1 | `exercises/token_practice.py` | Token 與 Token ID |  |  |  |
| 2 | `exercises/embedding_practice.py` | Embedding 查表 |  |  |  |
| 3 | `exercises/qkv_practice.py` | Q、K、V 線性投影 |  |  |  |
| 4 | `exercises/attention_matrix_practice.py` | Attention Matrix |  |  |  |
| 5 | `exercises/self_attention_practice.py` | Self-Attention |  |  |  |
| 6 | `exercises/position_encoding_practice.py` | Position Encoding |  |  |  |
| 7 | `exercises/multi_head_attention_practice.py` | Multi-Head Attention |  |  |  |
| 8 | `exercises/encoder_decoder_practice.py` | Encoder / Decoder 流程 |  |  |  |

## 整合操作題

以下操作題由原 `weekly_plan.md` 移入，作為 Coding Practice 的補充索引。完整參考方向請完成練習後再查看 [`coding_answer_key.md`](./coding_answer_key.md)。

### 操作題 A：簡易 Token 與詞彙表

建立簡單 Python（程式語言）檔案，練習輸入英文句子 `take me to the laboratory`，用空白切分成 Token，建立 vocabulary（詞彙表），並印出 Token 列表與 ID 列表。

建議先完成：`exercises/token_practice.py`

### 操作題 B：簡易 Attention 權重直覺

建立簡單程式，模擬 `["go", "to", "red", "door", "laboratory"]` 中每個 Token 的注意力權重，找出分數最高的 Token，並用一句話說明它為什麼重要。

建議先完成：`exercises/attention_matrix_practice.py`

### 操作題 C：簡易 QKV 分數

建立簡單程式，手動設定一個 Query 向量與三個 Key 向量，計算 Q x K 分數，並說明分數最高的 Key 為什麼最接近 Query。

建議先完成：`exercises/qkv_practice.py`

## 建議執行方式

```bash
python exercises/token_practice.py
python exercises/embedding_practice.py
python exercises/qkv_practice.py
python exercises/attention_matrix_practice.py
python exercises/self_attention_practice.py
python exercises/position_encoding_practice.py
python exercises/multi_head_attention_practice.py
python exercises/encoder_decoder_practice.py
```

## 錯誤修正紀錄

| 檔案 | 錯誤訊息或問題 | 修正方式 | 是否理解 |
|---|---|---|---|
|  |  |  |  |

## 自我檢查

- [ ] 我沒有把完整答案貼回 `exercises/` 當作自己的練習。
- [ ] 我能說明每個 TODO 在做什麼。
- [ ] 我檢查過矩陣 shape（張量形狀）。
- [ ] 我確認 softmax 軸向符合每列注意力分布。
