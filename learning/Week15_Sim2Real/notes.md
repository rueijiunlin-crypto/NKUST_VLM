# Week15 Notes：Sim-to-Real / Real Robot Deployment

## Why 與 Problem

模擬成功只證明方法在模擬假設內成立。Reality Gap（現實落差）來自 rendering、camera response、lighting、background、sensor noise、calibration、object physics、robot dynamics 與 latency。Week15 的目標是用 paired evidence 找出 gap，而不是用一句「需要 domain randomization」帶過。

## Camera vs Simulation Comparison

對相同或可對齊場景，保存：

- Source metadata：camera model／Isaac version、resolution、color space、exposure。
- Image tensor：`[N,H,W,3] uint8`，轉模型前再形成 `[N,3,h,w]`。
- Geometry：intrinsics、extrinsics、depth scale、reprojection error。
- Timing：capture/render、transport、preprocess、inference latency。
- Semantic outcome：detection/grounding/VLM result 與 failure label。

## Data Flow

```text
real camera ─→ capture + calibration ─┐
                                     ├→ common preprocessing
sim camera ──→ render + metadata ─────┘
→ paired feature / image metrics
→ same model + prompt + revision
→ output difference
→ failure taxonomy
→ mitigation experiment
```

Common preprocessing 必須鎖定 resize、crop、color conversion 與 normalization，否則量到的是 pipeline 差異而非 domain gap。

## Metrics 與 Example

- Pixel：brightness mean/std、color histogram distance、noise estimate。
- Feature：cosine distance 或 Fréchet-style distribution distance。
- Geometry：depth MAE、reprojection error、pose error。
- System：latency p50/p95、drop/stale rate。
- Task：success rate、grounding accuracy、action error、安全拒絕率。

例：sim 與 real 都為 `[100,224,224,3]`，但 real brightness variance 更高且 VLM `unknown` rate 增加。這只建立相關性；需控制 lighting 或 exposure 做下一個實驗才能推論原因。

## Mitigation

Domain Randomization（領域隨機化）增加模擬變異；Domain Adaptation（領域適應）利用目標域資料調整表徵；Calibration 修正可量測的幾何／時間偏差；record/replay 與 fault injection 可在無硬體動作下測試恢復策略。

## Deployment Safety

```text
predicted action
→ finite / shape / unit / frame
→ joint + velocity + workspace limits
→ collision / freshness / watchdog
→ operator enable
→ low-level controller
```

需具備 E-stop、timeout、communication-loss fallback、bounded retry、operator takeover 與 rollback。模型 uncertainty 不能取代 deterministic safety checks。

## Failure 與 Limitation

- 比較場景不對齊或只挑成功案例。
- 使用不同模型 revision／prompt。
- 模擬 ground truth 洩漏到 model input。
- latency 只報平均值。
- calibration drift 被誤認為模型 domain shift。
- 硬體不可用時把 mock 結果當成 real validation。

## Demo 與 Paper Mapping

- Real Comparison Track：OpenCV camera 或錄影對 Isaac output，產生同一份 metrics JSON。
- Core Paper：Domain Randomization，對應「模擬變異成為真實樣本」的假設與限制。

## 本週尚未涵蓋

硬體不可用時只能完成 hardware-ready validation，不宣稱 real-robot pass。
