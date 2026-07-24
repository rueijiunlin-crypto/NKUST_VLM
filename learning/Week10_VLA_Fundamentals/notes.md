# Week10 Notes：Embodied AI + VLA Fundamentals

## 1. VLM 與 VLA

VLM：`Vision + Language → Text / Semantic Output`。VLA：`Vision + Language + Robot State → Action`。Action 必須在明確 action space、單位、frame、時間步與安全限制下解讀。

## 2. Policy 與 Observation

Policy `π(a|o)` 將 observation `o` 映射成 action `a`。這不是說 action 一定安全；Policy output 還需 limits、collision、workspace 與 emergency stop 等獨立約束。

## 3. Action Representation

- Joint Action：關節 position／velocity／torque。
- Cartesian／End-Effector Action：末端 pose 或 delta。
- Gripper Action：open／close 或連續寬度。
- Action Chunk：一次預測多個時間步，降低推論頻率但增加 open-loop 風險。

## 4. Open-loop 與 Closed-loop

Open-loop 執行預測序列而不重新觀察；Closed-loop 反覆 Observe → Act → Observe，可修正誤差，但受 inference latency 與控制頻率限制。

## 5. Imitation Learning 與 Foundation Policy

Imitation Learning 從 demonstration 的 observation-action pairs 學習。Foundation Policy 以大規模、多任務資料預訓練，再做推論或 task adaptation。

## 6. 模型案例

RT-2、OpenVLA、SmolVLA、π0、GR00T 可用來比較輸入、action representation、資料、模型規模與部署條件；本週不宣稱它們介面相同。

## 7. Safety Boundary

Safety Gate 要檢查 action shape、finite values、limits、frame、freshness 與 state validity。VLA 是 action policy 也不等於可繞過 Controller 與 Safety。
