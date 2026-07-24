# Week09 Notes：Robot State + Multimodal Observation

## 1. Robot State

Robot State 包含 joint position、joint velocity、end-effector pose、gripper state、robot base pose、camera pose 等。Vision 提供外部場景，proprioception 提供機器人自身狀態；兩者缺一都可能讓動作判斷失真。

## 2. Observation Space

Observation 是 Policy 可讀的結構化輸入，不等於所有感測器原始資料。Schema 應定義 shape、unit、frame、timestamp、validity、normalization 與 missing policy。

## 3. Multi-camera

不同相機有不同 intrinsics、extrinsics、視角與 capture time。不能只把圖片 list 串接而忽略 camera ID 與 pose。

## 4. Timestamp Synchronization

若影像與 joint state 相差太久，模型看到的物體與機器人姿態可能不屬於同一時刻。可採 exact／approximate sync、最大 age 與拒絕 stale state。

## 5. Missing State

缺值策略應明確：reject、mask、last-known state（附 age）或 safe fallback。不得悄悄填 0，因為 0 可能是合法狀態。

## 6. 系統邊界

Embodied Observation 是 Policy 的輸入契約；它本身不產生或驗證安全動作。
