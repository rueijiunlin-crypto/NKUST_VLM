# Week10 Notes：Embodied AI + VLA Fundamentals

## Why：從理解到動作

VLM 輸出文字或語意；Vision-Language-Action Model（視覺語言動作模型，VLA）接收影像、語言與 robot state，輸出連續或離散 action。這個轉換把模型錯誤從「回答錯」提升為可能造成物理風險，因此 action convention、rate、normalization 與 safety boundary 必須成為模型介面的一部分。

## Input、Output 與 Policy

Policy 可寫成 `π(a_t | o_≤t, l)`。Observation 包含 image `[B,Ncam,C,H,W]`、state `[B,S]`、language tokens `[B,L]`；output 可為單步 `[B,A]` 或 action chunk `[B,H,A]`。`H` 是未來步數，`A` 是 action dimension。

## Architecture Data Flow

```text
images → processor → visual tokens ┐
language → tokenizer → text tokens ├→ multimodal backbone
state → projector → state tokens ──┘
                                  → action expert / decoder
                                  → normalized action chunk
                                  → unnormalize
                                  → action validator
                                  → controller (outside model)
```

Config 描述模型維度、camera keys、state/action features 與 chunk size；Processor 負責 resize、tokenize、normalization 與 batch；Policy 負責 forward／select_action。三者版本必須配套。

## Action Representation

- Joint position/velocity/torque：與 robot joint order 強耦合。
- Cartesian pose/delta pose：需 frame、rotation convention 與 controller。
- Gripper：binary、continuous 或力控制。
- Discrete action token：可沿用 language decoder，但有 quantization error。
- Continuous action／flow matching：直接建模連續軌跡，但需 noise schedule 與多步去噪。

Action chunk 降低反覆推論成本，但 open-loop horizon 太長會累積誤差。Closed-loop 需定期重新觀測、重排或裁切 chunk。

## Real VLA Architecture Inspection

真實模型檢查不先執行機器人：讀取 config、processor 與 model card，列印 model ID、revision、parameter count、dtype、device、camera/state/action feature、chunk size、normalization mode與 license。再以符合 schema 的 dummy observation dry-run；若權重未下載，狀態標記 `Not validated yet`。

## Model Comparison

| Model | Action form | 特點 | 主要限制 |
|---|---|---|---|
| RT-2 | action tokens | web knowledge co-fine-tuning | closed model |
| OpenVLA | discrete actions | 7B open implementation | 計算與 Llama 2 license |
| SmolVLA | continuous action chunk | 約 450M、flow matching | dataset schema 強耦合 |
| π0 | flow-based action | heterogeneous embodiment | 完整訓練成本高 |
| GR00T N1 | dual-system / continuous | humanoid foundation model | 硬體與生態系門檻 |

## Failure、Limitation 與 Safety

Shape 相同但 joint order 不同、錯誤 normalization、action frame 不一致、NaN、超出 joint limit、stale observation 與 latency spike 都可能造成危險。Validator 至少檢查 finite、shape、range、frame、freshness、rate limit；E-stop、collision checking 與 low-level controller 永遠在模型外。

## Demo 與 Paper Mapping

- Basic Demo：比較 single-step、chunk 與 closed-loop。
- Real Track：檢查 SmolVLA/OpenVLA config 與 processor，不動硬體。
- Core Paper：RT-2；Deep Reading 比較 OpenVLA、SmolVLA、π0、GR00T N1。

## 本週尚未涵蓋

資料載入、真實 inference 與 fine-tuning 分別在 Week11–13。
