# Week06 Concept Answer Key

> 請先完成 `concept_practice.md` 再查看。

1. Camera FPS 是產生影格速率；inference FPS 是模型完成結果速率，兩者不匹配時需取樣或丟棄舊影格。
2. Multi-frame 可一次處理有限影格；Streaming 必須在線更新、限制記憶並處理未知未來。
3. Sliding Window 限制 context 成本，但可能遺忘早期事件。
4. KV Cache 仍占記憶體，長串流需淘汰、壓縮或摘要。
5. 語意結果缺少完整 Robot State、規劃、控制頻率與安全驗證。
