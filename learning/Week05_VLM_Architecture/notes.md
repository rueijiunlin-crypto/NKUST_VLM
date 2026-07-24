# Week05 教材筆記：VLM Architecture 架構與資料流

## 1. 從單一模型到架構家族

Vision-Language Model（視覺語言模型，VLM）不是單一固定架構。共同問題是：如何把不同型態的圖片與文字表示轉成可比較、可融合或可生成的資訊。

本週比較四種概念家族：

| 家族 | 主要元件 | 常見輸出 | 代表性例子 |
| --- | --- | --- | --- |
| Dual Encoder（雙編碼器） | Image Encoder + Text Encoder | 圖文相似度 | CLIP |
| Projector-based（投影器式） | Vision Encoder + Projector + LLM | 生成文字 | LLaVA |
| Query-based（查詢式） | Vision Encoder + Query Connector + LLM | 生成文字 | BLIP-2 |
| Cross-Attention（交叉注意力式） | Vision Encoder + Cross-Attention + LM | 生成文字 | Flamingo |

分類的目的是幫助閱讀資料流，不代表所有模型只能屬於一類。實際架構可能混合多種 connector（連接器）與訓練策略。

### 對應 Demo

- Demo：`demo/demo_01_architecture_families.py`
- 執行：`python demo/demo_01_architecture_families.py`
- 觀察：元件、輸出與例子。
- 執行後應能回答：為什麼 CLIP 與 LLaVA 都是 VLM，輸出卻不同？

## 2. Dual Encoder 與生成式 VLM

### Dual Encoder

Dual Encoder 分別產生 image embedding（影像嵌入向量）與 text embedding（文字嵌入向量）：

```text
Image → Image Encoder → image embedding ┐
                                        ├→ similarity
Text  → Text Encoder  → text embedding  ┘
```

它適合大規模檢索、圖文配對與零樣本分類，因為圖片與文字可以預先編碼。但單一相似度矩陣不會自然產生完整回答。

### 生成式 VLM

```text
Image → Vision Encoder → Connector → visual tokens ┐
                                                    ├→ Language Model → Answer
Question → tokenizer → text tokens                 ┘
```

生成式 VLM 可以回答開放問題，但需要處理序列長度、解碼、幻覺與輸出驗證。

### 研究選擇

- 若任務是從一萬張圖片找出與文字最相近者，Dual Encoder 通常更適合。
- 若任務是描述場景、回答問題或依指令產生語意結果，生成式 VLM 更合適。
- 「能生成較長文字」不是所有任務的優點；應先由研究問題決定輸出介面。

## 3. Vision Encoder 與視覺表示

Vision Encoder（視覺編碼器）常先將圖片切成 patches（影像區塊）：

```text
[batch, channels, height, width]
↓ patch embedding
[batch, patch_tokens, vision_hidden]
↓ transformer layers
[batch, contextualized_visual_tokens, vision_hidden]
```

Patch vector 只是局部像素的投影；經多層 self-attention（自注意力）後，位置才包含其他區域的上下文。

### 解析度與 token 數量

若圖片寬高皆加倍、patch size 不變，兩個方向的 patch 數量都加倍，因此總 patch 數量約增加四倍。這會影響注意力計算、記憶體與下游 connector 成本。

### 對應 Guided Demo

- 程式：`practice/coding/guided_demos/guided_01_vision_encoder_flow.py`
- 執行：`python practice/coding/guided_demos/guided_01_vision_encoder_flow.py`
- 觀察：RGB shape、patch grid、patch vector shape 與第一個 patch 數值。
- 執行後應能回答：Patch vector 與 contextualized vision feature 有何差異？

## 4. Connector 與 Modality Alignment

圖片與文字模型通常具有不同 hidden size（隱藏維度）與表示空間。Connector 的任務不是單純「改 shape」，還要在訓練中學會把有用視覺資訊轉到語言模型可使用的介面。

### Linear／MLP Projector

```text
[batch, N, vision_hidden]
↓ Linear or MLP
[batch, N, language_hidden]
```

優點是結構簡單、資料流清楚；若保留所有 N 個位置，序列成本可能較高。

### Query Connector

Query-based connector 使用固定數量的 learned queries（可學習查詢）從 N 個視覺位置擷取資訊：

```text
visual features: [batch, N, vision_hidden]
learned queries: [batch, Q, query_hidden]
↓ query-to-image attention
query output:    [batch, Q, language_hidden]
```

當 `Q << N` 時，可顯著壓縮送入語言模型的位置數量；代價是壓縮可能遺失小物件或精細空間資訊。

### 對應 Demo／Practice

- Demo：`demo/demo_03_connector_comparison.py`
- Guided Demo：`practice/coding/guided_demos/guided_02_projector_alignment.py`
- 觀察：token axes 與 hidden axes 哪些被保留或壓縮。
- 執行後應能回答：位置數量較少為何不必然代表效果更好？

## 5. Fusion Strategies

### Late Fusion（晚期融合）

Dual Encoder 各自編碼後才比較全域向量。計算與檢索效率高，但細粒度 token-to-token 互動較少。

### Token Concatenation（詞元串接）

將投影後 image tokens 與 text tokens 放進同一序列，讓 Language Model（語言模型）進行 self-attention。LLaVA 類模型可用這種觀念理解。

### Query Compression（查詢壓縮）

用少量 query tokens 吸收視覺資訊，再送入語言模型。BLIP-2 的 Q-Former（查詢轉換器）是代表性設計。

### Cross-Attention Fusion

語言 hidden states 作 Query，視覺 features 作 Key／Value：

```text
Q = language states
K, V = visual features
Attention(Q, K, V) → visually conditioned language states
```

Cross-attention 可以插在語言模型若干層之間，處理交錯圖片與文字；其介面、計算與訓練策略不同於單純串接。

### 對應 Guided Demo

- 程式：`practice/coding/guided_demos/guided_03_fusion_strategies.py`
- 觀察：串接後長度、query 壓縮結果與 cross-attention weights（交叉注意力權重）。
- 執行後應能回答：Cross-attention 中的 Query、Key、Value 分別來自哪一種模態？

## 6. Token + Latency Budget

多模態 context（上下文）概念長度可寫成：

```text
total_positions ≈ visual_positions + text_positions + special_positions
```

影響因素：

- 圖片數量。
- 圖片解析度與 patch size。
- Connector 是否壓縮位置。
- Prompt、對話歷史與輸出長度。
- Checkpoint 的最大 context length。
- frame count（影格數）、Frame Sampling（影格取樣）與 temporal context（時間上下文）。

### 估算例子

一張 `336 × 336` 圖片，patch size 14，產生 `24 × 24 = 576` 個 patch positions。若 connector 保留 576 個位置，再加 128 個文字位置，概念總數約 704；若 query connector 壓成 32 個位置，則約 160。

多影格未壓縮時：

```text
1 frame  × 576 =   576 visual tokens
4 frames × 576 = 2,304 visual tokens
16 frames × 576 = 9,216 visual tokens
32 frames × 576 = 18,432 visual tokens
```

在標準 full attention（全注意力）的簡化理解中，序列互動成本會隨位置數近似平方成長。真實 Latency（延遲）也受硬體、KV cache（鍵值快取）、實作與輸出長度影響，因此 Demo 只提供 relative cost indicator（相對成本指標），不冒充 GPU benchmark。

```text
Frames ↑ → Tokens ↑ → Memory pressure ↑ → Latency pressure ↑
```

機器人相機是 continuous stream（連續串流），不能假設把 30 FPS 每一幀完整送入大型 VLM 就能即時工作。常見架構選擇包含 Frame Sampling、事件觸發、視覺 token 壓縮、短期 temporal memory（時間記憶）或較小的前端感知模型；本週只理解取捨，不實作串流系統。

這只是架構比較估算。實際模型可能使用特殊 token、動態解析度、patch merging（影像區塊合併）或其他 feature selection。

### 對應 Demo

- Demo：`demo/demo_04_token_budget.py`
- 執行：`python demo/demo_04_token_budget.py --frames 4 --query-tokens 32`
- 觀察：圖片數量、patch 與 query positions 如何改變總長度。
- 執行後應能回答：壓縮 visual positions 可能犧牲什麼資訊？

## 7. Camera-to-Structured-Perception

研究系統不應只畫模型內部方塊，還要包含輸入品質與輸出驗證：

```text
Camera Frame
↓ timestamp / color / blur checks
Preprocess
↓ shape / normalization checks
Vision Encoder
↓ feature and domain checks
Connector
↓ dimension / token budget checks
Language Model
↓ raw generated output
Validator
↓ grounding / schema / uncertainty checks
Structured Perception Result, Retry, or Reject
```

### 典型失敗位置

- Camera：影像過期、模糊、曝光錯誤。
- Preprocess：RGB／BGR 混淆、尺寸或正規化錯誤。
- Vision Encoder：domain shift（領域偏移）、小物件遺失。
- Connector：shape 相容但資訊壓縮不當。
- LLM：hallucination（幻覺）、錯誤前提、生成不穩定。
- Validator：只檢查 JSON 語法，未檢查視覺依據、欄位來源與不確定性。

### 對應 Demo／Practice

- Demo：`demo/demo_02_camera_to_answer_flow.py`
- Guided Demo：`practice/coding/guided_demos/guided_04_end_to_end_flow.py`
- 執行後應能回答：為什麼最後回答錯誤時，不能直接判定是 LLM 的問題？

## 8. Robot VLM System Boundary

機器人系統不是單一 VLM：

```text
Camera / Sensors
↓
Perception / VLM
↓
Semantic Representation
↓
Planner
↓
Controller
↓
Robot Action
```

VLM 通常適合提供 Scene Understanding（場景理解）、Object Semantics（物體語意）、Instruction Understanding（指令理解）、Spatial Semantic Relation（空間語意關係）與 High-Level Task Understanding（高階任務理解）。

它不應單獨負責 Low-Level Motor Control（低階馬達控制）、Collision Avoidance（碰撞避免）、Joint Torque（關節力矩）、Safety Interlock（安全連鎖）或 Emergency Stop（緊急停止）。這些功能需要確定性更高、更新頻率更快、可驗證且具失效保護的系統模組。

### 對應 Demo

- Demo：`demo/demo_05_robot_vlm_system_flow.py`
- 執行：`python demo/demo_05_robot_vlm_system_flow.py`
- 觀察：VLM 與其他模組各提供哪些資訊。
- 執行後應能回答：Why should a VLM not directly control the motor?

## 9. Robot State

一般 VLM 常被簡化為：

```text
Image + Language → VLM → Answer
```

機器人智能系統則至少要考慮：

```text
Image
+ Language Instruction
+ Robot State
↓
Robot Intelligence System
```

Robot State（機器人狀態）可包含 Robot Pose（機器人姿態）、Joint Position（關節位置）、Joint Velocity（關節速度）、Gripper State（夾爪狀態）、Camera Pose（相機姿態）與 Navigation State（導航狀態）。Image 不是機器人決策需要的全部資訊，而且不同狀態來源必須具有一致的時間與座標語意。

## 10. Spatial Grounding

Spatial Grounding（空間語意定位）可拆成不同資料層級：

```text
Semantic Object
↓
2D Grounding
↓
Bounding Box / Mask
↓
Depth Association
↓
3D Position
↓
Camera Coordinate
↓
Robot Coordinate
```

- Semantic Location（語意位置）：`cup is left of box`。
- 2D Pixel Location（二維像素位置）：bounding box、mask 或像素座標。
- 3D Camera Coordinate（三維相機座標）：相對相機原點的公尺位置。
- Robot Coordinate：透過外部標定與座標轉換得到、相對機器人參考框架的位置。

`"The cup is left of the box."` 不等於 `cup = [0.42, 0.16, 0.81] m`。前者可能只描述影像中的相對語意；後者必須聲明座標系、單位、深度來源、標定與時間。本週只學架構鏈，不連接 RealSense 或 TF2。

## 11. Structured Output

機器人系統通常較適合處理 JSON、structured schema（結構化綱要）、symbolic representation（符號表示）或 task representation（任務表示），而不是直接解析自由文字：

```json
{
  "objects": [
    {
      "name": "cup",
      "relative_position": "left"
    }
  ],
  "uncertain": [
    "exact_depth",
    "robot_coordinate",
    "reachability"
  ]
}
```

Structured Output（結構化輸出）的優點是欄位可驗證、缺失值可表示、介面可版本化；但 JSON 語法正確不代表視覺內容、幾何或安全性正確。Validator 必須檢查 schema、值域、Grounding、來源與不確定性，且 Planner 仍須結合 Robot State 與安全約束。

## 12. Temporal / Multi-frame Input

```text
Single Image
↓
Multiple Images
↓
Sequential Frames
↓
Video VLM
↓
Streaming VLM
```

- frame（影格）：某一時間點的單張影像。
- multiple images（多張圖片）：不一定具連續時間關係。
- sequential frames（連續影格）：具有順序與時間間隔。
- Temporal Context（時間上下文）：用多個時間點理解變化、持續性與事件。
- multi-frame tokens（多影格詞元）：多個影格各自或壓縮後送入模型的位置。
- Streaming VLM（串流視覺語言模型）：持續接收輸入並管理更新、記憶與延遲。

本週不實作真正 Streaming VLM；重點是理解機器人 Camera 不是單張圖片，架構必須處理 Frame Sampling、Temporal Context、temporal memory 與 token explosion（詞元爆增）。

## 13. VLM Output 與 VLA Action Output

VLM output 常是 embedding、score、自然語言或 Structured Perception；Vision-Language-Action Model（視覺語言動作模型，VLA）的 action output 則需映射到明確的 action representation（動作表示），並以 Robot State、控制頻率、硬體介面與安全約束解讀。即使未來使用 VLA，也不代表可以移除 Planner、Controller 或 safety layer（安全層）。

本週只建立輸出介面差異，不進行 OpenVLA／SmolVLA 訓練、資料收集或真實控制。

## 14. 架構比較與研究閱讀

閱讀架構圖時固定問：

1. 圖片與文字輸入在哪裡？
2. 哪些模組是 pretrained（預訓練）、frozen（凍結）或 trainable（可訓練）？
3. Connector 的輸入、輸出 shape 是什麼？
4. 圖文在哪一層互動？
5. 模型輸出是 embedding、score、token、structured representation 還是 action？
6. 訓練目標與推論任務是否一致？
7. 論文用什麼實驗支持架構選擇？

參考原始來源：

- [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [LLaVA: Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)
- [BLIP-2](https://arxiv.org/abs/2301.12597)
- [Flamingo](https://arxiv.org/abs/2204.14198)

## 本週尚未涵蓋

- 各模型完整訓練 loss（損失函數）與資料配方。
- 動態解析度、多圖片、影片與 Streaming VLM 的實作細節。
- 量化、KV cache（鍵值快取）與部署最佳化。
- ROS2 Node／Topic、RealSense SDK、TF2、MoveIt、Navigation2、Isaac Sim／Isaac Lab 的實際整合。
- OpenVLA／SmolVLA 訓練、Robot Dataset Collection、LoRA／QLoRA 與 VLA fine-tuning。
