# Week05 Concept Answer Key

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

## 1. Dual Encoder 與生成式 VLM

Dual Encoder 分別編碼圖片與文字，再比較向量，適合檢索或零樣本分類。生成式 VLM 讓視覺資訊進入語言模型上下文，逐 token 產生回答，適合描述與問答。前者通常容易預先索引，後者表達彈性較高但有生成成本與幻覺風險。

## 2. Vision Encoder

Patch 是固定像素區塊，不必然對應物件；經多層 attention 後才形成上下文化表示。寬高各加倍會使網格兩軸各加倍，總位置約四倍。

## 3. Projector

1 是 batch、576 是 image token positions、1024／4096 是前後 hidden size。線性或 MLP 轉換讓介面尺寸相容；真正語意對齊仍依賴訓練資料與目標，不能由 shape 單獨證明。

## 4. Query Connector

32 個 queries 可降低送入 LLM 的序列長度與計算，但固定壓縮可能遺失小物件、計數、邊界、相對姿態或操作接觸區等細節。對機器人操作而言，整體場景語意仍正確並不代表 manipulation-relevant features 已完整保留；優劣需由目標任務實驗驗證。

## 5. Cross-Attention

語言 states 通常作 Query，視覺 features 作 Key／Value，代表語言位置主動讀取視覺資訊。串接 self-attention 則把兩種 tokens 放在共同序列中依 attention mask 互動。

## 6. Token Budget

保留所有位置時為 `2 × 576 + 128 = 1280`。每張壓成 32 個 query positions 時為 `2 × 32 + 128 = 192`。兩者仍未計特殊 token 與輸出 token。

## 7. Camera-to-Answer 診斷

可能包含 Camera 白平衡或曝光、BGR／RGB 前處理錯誤、Vision Encoder domain shift、connector 資訊損失、LLM 幻覺或 validator 未檢查顏色。應保存各階段中間結果並定位第一個錯誤。

## 8. 架構選擇

大規模檢索可優先 Dual Encoder，因向量可預先建立索引；場景問答可優先生成式 VLM，因需依問題產生文字。仍需考慮資料、延遲、硬體、正確性與輸出驗證，不能只由模型類別決定。

## 9. Spatial Grounding 層級

Semantic Grounding 表示物體與關係，2D Grounding 對應影像像素中的 box／mask，3D Grounding 則需要深度與幾何形成某座標系中的三維位置。「左側」沒有公尺尺度、原點與軸定義，因此不等於三維座標。

## 10. Camera Coordinate 與 Robot Coordinate

Camera coordinate 以相機座標框架為參考；Robot Coordinate 以機器人基座或指定 frame 為參考。兩者轉換需相機外部標定、正確 transform、時間同步與一致的單位／軸定義。只讀到 depth 不會自動得到 Robot Coordinate。

## 11. Robot State

典型資料包括 Robot Pose、Joint Position、Joint Velocity、Gripper State、Camera Pose、Navigation State，也可能包含速度、力矩、電量與模式。相同影像在不同姿態、關節限制或導航狀態下，可行動作不同，因此 Image 不是完整決策狀態。

## 12. Structured Output

Schema 可指定必填欄位、型別、值域、缺失與不確定性，較容易驗證、記錄與串接模組。合法 JSON 只證明語法符合，仍可能包含幻覺物體、假深度或錯誤關係；必須再做 Grounding、來源與安全檢查。

## 13. Streaming Camera

Single-frame 沒有時間脈絡，multi-frame 可顯示變化，Streaming VLM 還需持續管理新影格、記憶與輸出延遲。逐幀送入 30 FPS 會快速增加 token、attention 成本、記憶體與延遲，因此通常要 Frame Sampling、事件觸發、壓縮或分層感知。

## 14. VLM Output 與 VLA Action Output

VLM 常輸出 embedding、score、文字或結構化語意；VLA action output 必須依明確 action space（動作空間）、Robot State、時間步與硬體介面解讀。文字中的 `grasp` 沒有自動定義姿態、軌跡、速度或控制頻率。

## 15. Safety Boundary

生成式 VLM 可能有幻覺、非確定性、延遲與分布外錯誤，通常也不具安全認證與硬即時保證。碰撞避免、安全連鎖、緊急停止與低階控制應由可驗證、具明確頻率與失效保護的專責模組處理；VLM 只能提供受約束的高階語意。
