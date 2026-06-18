# Week01 Guided Code Reading（引導式程式閱讀）

Week01 採用 Guided Code Reading Mode（引導式程式閱讀模式）。這裡提供完整可執行的小型程式，重點是追蹤 Transformer（轉換器架構）的資料流，而不是從零實作模型。

## 學習方式

1. 安裝需求：

   ```bash
   pip install -r requirements.txt
   ```

2. 依序執行 [`guided_demos/`](./guided_demos/) 中的程式。
3. 對照程式內中文註解，觀察 shape（張量形狀）與中間結果。
4. 依 [`coding_practice.md`](./coding_practice.md) 修改小參數並記錄變化。
5. 使用 [`coding_observation_key.md`](./coding_observation_key.md) 檢查觀察方向與常見誤解。

## 建議順序

```text
Token / Token ID / Embedding
-> Position Encoding
-> QKV
-> Self-Attention
-> Multi-Head Attention
-> Encoder / Decoder
```

## 核心原則

- `demo/` 快速回答「這個概念在做什麼」。
- 此資料夾逐步回答「這個流程如何做到」。
- 修改句子長度、向量維度、head 數量或遮罩等小參數，觀察資料流如何改變。
- 不需要補寫缺漏程式碼，也不要求從零實作 Transformer。
