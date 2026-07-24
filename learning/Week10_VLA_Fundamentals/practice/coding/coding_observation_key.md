# Week10 Coding Observation Key

> 請先執行 `guided_demos/guided_policy_loop.py` 並完成自己的觀察，再查看本說明。

## 觀察方向

- VLA policy（視覺語言動作策略）把 observation 與 instruction 映射為 action 或 action chunk。
- policy output 仍須通過 schema、range、freshness 與 safety gate，才能成為機器人命令。
- action chunk 能降低每一步推論成本，但 chunk 太長會降低對新觀測的反應速度。
- closed-loop（閉迴路）會重新取得 observation；open-loop（開迴路）則依賴先前預測持續執行。

## 常見誤解

- 模型輸出格式正確不代表動作安全。
- VLM 文字回答不能直接視為可執行 action。
- 單次推論成功不能代表長時間 rollout 穩定。
