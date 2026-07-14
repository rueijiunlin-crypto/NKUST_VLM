# Week04 Coding Observation Key

> 請先完成 `coding_practice.md` 的執行與觀察，再查看本文件。以下是理解方向，不是學生的實際執行紀錄。

## 1. Multimodal Processor Tensor Shape

`input_ids` 與 `attention_mask` 通常同為 `[batch, sequence_length]`，但前者保存 Token ID（詞元識別碼），後者標記有效位置。問題變長時，`sequence_length` 可能增加。

`pixel_values` 常為 `[batch, channels, height, width]`。只改問題文字時，圖片前處理設定沒有改變，因此圖片 tensor shape 通常不變。

Processor 只建立模型輸入，不執行完整 LLM 生成。常見誤解是看到 tensor 已產生，就以為模型已經理解圖片或產生回答。

## 2. Projector Flow

範例保留 batch 與 image-token axes（影像詞元軸），將最後一維由 vision hidden size 轉成 language hidden size。Seed（隨機種子）改變會改變權重與中間數值，但結構參數不變時 shape 不變。

因此 shape 正確只能證明介面尺寸可連接，不代表權重、數值或語意一定正確。Projector 也不直接輸出文字。

## 3. Multimodal Sequence

Prompt 只有一個 `<image>` placeholder（影像占位符），但處理後會插入多個 image positions。把 image tokens 從 4 改成 8，總序列長度增加 4；文字 token 本身沒有因此改變。

實際 checkpoint 的特殊 token、image token 數量與插入規則可能不同，應由 Processor 與模型設定決定。

## 4. Generation Flow

預設 toy policy（玩具策略）逐步選出預設回答，遇到 `<eos>` 停止；`max_new_tokens=2` 時則因長度上限提前停止，可能只得到不完整片段。

Toy logits 是人工設計的下一 token 分數，沒有讀取圖片。因此即使輸出句子合理，也完全不能證明有 visual grounding（視覺依據）。

## 5. Question／Prompt 實驗

好的問題比較不是只看哪個回答比較長，而是先定義要驗證的影像資訊，再把回答拆成獨立主張：

- Supported：圖片直接支持。
- Uncertain：受解析度、遮擋或視角限制，無法確認。
- Contradicted：圖片明顯不支持。

帶有錯誤前提的問題容易誘導模型順著語言生成。研究紀錄應保存這類失敗案例，而不是只留下看似合理的回答。

## 常見誤解修正

- Token ID 不等於 embedding vector（嵌入向量）。
- Patch token 不等於物件 token。
- Projector 不直接輸出文字。
- `<image>` 不等於只有一個影像向量位置。
- `max_new_tokens` 不等於回答字數。
- Greedy generation（貪婪生成）可重現，不代表事實正確。
