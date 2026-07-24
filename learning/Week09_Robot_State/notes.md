# Week09 Notes：Robot State + Multimodal Observation

## Why 與 Problem

相同影像在不同 robot state 下可能需要完全不同的動作。Embodied model 必須知道 joint position、end-effector pose、gripper state、camera pose 與資料時間；只用畫面容易把「看得到」誤認為「現在可執行」。

## Observation Schema

```text
observation = {
  images: {camera_name: Tensor[B,C,H,W]},
  state: Tensor[B,S],
  language_tokens: Tensor[B,L],
  timestamps: {image, state, instruction},
  validity: {per modality},
  provenance: {sensor, calibration, revision}
}
```

典型輸入為兩台 camera `[B,2,3,H,W]`、state `[B,S]`、attention mask `[B,L]`。加入時間窗後可成為 `[B,T,2,3,H,W]` 與 `[B,T,S]`。所有維度都要由 schema 命名，不能只憑 position 猜語意。

## Mechanism 與 Data Flow

```text
camera frames ─→ image processor ─→ image tensors
joint / pose ──→ unit + frame check ─→ state tensor
instruction ───→ tokenizer ─────────→ token IDs / mask
timestamps ────→ synchronizer ──────→ aligned observation
                                     ↓
                              validity / freshness gate
```

State 需先依 training metadata normalization；角度 radian、位置 meter、quaternion order 與 base frame 都必須明示。Token ID 是 embedding table 的索引，不是 language embedding。

## Timestamp 與 Synchronization

Exact synchronization 要求時間戳一致，真實 sensor 常需 Approximate Synchronization（近似同步）。可定義 `Δt = |t_image - t_state|`，超過容許值就拒絕或標記 invalid。Last-known state 必須附 age，不能把補值當成新量測。

## Missing Modality Policy

- Reject：安全需求高且缺少必要狀態。
- Mask：模型在訓練時明確支援 missing modality。
- Last-known：只在短時窗內使用並保存 age。
- Safe fallback：停止或要求重新觀測。

以 0 填補很危險，因為 0 可能是合法 joint position。

## Actual Tensor Example

一筆 RGB 影像由 `uint8 [480,640,3]` 轉為 `float32 [1,3,224,224]`；7 軸 joint 加 gripper 得到 `state [1,8]`；tokenizer 產生 `input_ids [1,L]` 與 `attention_mask [1,L]`；timestamp 以 `float64 [1,3]` 保存 image/state/instruction 時間。Demo 應印出 dtype、device、min/max 與 freshness。

## Failure、Limitation 與 Safety

- camera 與 state 時序錯位。
- normalization statistics 不屬於目前 dataset。
- joint order 不同但 shape 相同，造成靜默錯誤。
- quaternion convention 或 coordinate frame 錯誤。
- 多相機 identity 對調。

Observation 通過 schema 不代表安全；policy output 還需 Week10 的 action validator。

## Demo 與 Paper Mapping

- Demo：建立真實 image/state/language/timestamp tensors 並驗證 shape。
- Core Paper：PaLM-E，對應 sensor embedding 與 multimodal sentence。
- Robot research：這個 schema 是 dataset、inference、fine-tuning 與 evaluation 的共同契約。

## 本週尚未涵蓋

不產生控制 action，也不處理 VLA training。
