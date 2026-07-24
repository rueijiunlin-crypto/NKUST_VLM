# Week06 Notes：Video and Streaming VLM

## Why：為什麼單張圖片不夠

機器人面對的是持續變動的世界。單張 Vision-Language Model（視覺語言模型，VLM）只能回答「現在看見什麼」，無法可靠判斷物體剛才是否移動、門是否正在關閉，或操作是否已完成。Video VLM（影片視覺語言模型）要把多個時間點壓縮成可查詢的語意記憶；Streaming VLM（串流視覺語言模型）還必須在有限延遲與記憶體下持續更新。

## Problem、Input 與 Output

- Input：影片或 frame stream `[B, T, C, H, W]`、文字問題 `[B, L]`、frame timestamp。
- Output：文字 token、結構化事件、時間區間或置信資訊。
- 核心限制：`T` 增加會同步增加視覺 token、attention 成本與 latency。

若每張 frame 產生 `V` 個 visual tokens，未壓縮的序列長度約為 `T × V + L`。Self-Attention 的記憶與計算成本近似序列長度平方，因此不能把無限串流直接串接。

## Mechanism 與 Data Flow

```text
Camera / Video
→ decode + timestamp
→ frame sampling / scene-change trigger
→ resize + normalize
→ vision encoder
→ per-frame tokens [B,T,V,D]
→ temporal pooling / memory compression
→ memory tokens [B,M,D]
→ language-conditioned decoder
→ structured semantic event
→ freshness / schema validator
```

Frame Sampling（影格取樣）可固定每秒取樣、均勻取樣、依場景變化觸發，或依任務事件自適應。Sliding Window（滑動視窗）只保留最近 `W` 張；hierarchical memory 先在 clip 內聚合，再將摘要送入長期記憶。KV Cache（鍵值快取）可避免重算既有 token，但不等於保存了所有視覺細節。

## Shape Example

輸入 8 張 `224×224` RGB frame：`[1,8,3,224,224]`。若每張得到 256 tokens、hidden size 為 1024，原始視覺表示為 `[1,8,256,1024]`；將每張壓成 4 個 memory tokens 後為 `[1,32,1024]`。壓縮率高不代表語意一定保留，必須用事件召回率與時間定位誤差驗證。

## Online 與 Offline

Offline 理解可讀完整影片，適合摘要與回溯。Online streaming 只能看到過去與現在，還要分別量測 capture、decode、preprocess、inference、validation 的延遲。機器人應優先處理 freshness；準確但過期的結果可能比 `unknown` 更危險。

## Failure、Limitation 與 Safety

- 過度取樣：token 爆炸、OOM、延遲上升。
- 取樣過疏：短暫事件被漏掉。
- 時序混淆：模型把前一時刻的物件狀態當成現在。
- Memory overwrite：長期事件被新 frame 覆蓋。
- Hallucination：模型補出畫面沒有發生的動作。

輸出必須含 `source_timestamp`、`result_timestamp`、`model_id`、`valid` 與 `unknown`，且只能作為 semantic observation，不能直接當 Motor Command（馬達命令）。

## Demo、Real Model 與 Paper Mapping

- Basic Demo：觀察 sampling、window 與 token budget，回答 What。
- Guided Code Reading：追蹤 `[B,T,V,D] → [B,M,D]`，回答 How。
- Real Model Track：Qwen2.5-VL 影片推論；需記錄 model revision、device、dtype、輸入 shape、生成時間與 peak memory。
- Core Paper：MovieChat，對應 sparse memory、long-video context 與失敗分析。

## 本週尚未涵蓋

本週不實作 ROS2 callback、硬體控制或 VLA action；即時 ROS2 系統邊界留到 Week07。
