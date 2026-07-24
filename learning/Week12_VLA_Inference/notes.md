# Week12 Notes：SmolVLA / OpenVLA Inference

## 1. Pretrained VLA

Pretrained Policy 已從 robot demonstrations 學到 observation-action mapping。推論時必須使用相容的 processor、observation keys、normalization statistics 與 action convention。

## 2. Observation Input

輸入可能包含單／多相機、Robot State、language instruction 與 task metadata。缺欄位、順序、shape、unit 或 frame 不符都可能讓程式可執行但 action 無效。

## 3. Normalization

Image 與 state 前處理、action unnormalization 必須取自 checkpoint／dataset metadata。不能用任意 mean／scale 取代。

## 4. Action Output

記錄 action space、shape、chunk length、frequency、unit 與 frame。Predicted Action 只供評估或受限執行；真實 robot 前需 validator、controller 與 safety。

## 5. SmolVLA 與 OpenVLA

SmolVLA 適合作為較輕量的學習入口；OpenVLA 用於理解更大模型與部署成本。實際 API、license、權重與硬體可能更新，執行前以官方來源為準。

## 6. Hardware / Latency

必須記錄 CPU／GPU、VRAM、dtype、warm-up、同步方式、單次與穩態 latency。Basic Demo 的 mock latency 不能當真實模型 benchmark。

## 本週限制

不下載大型權重、不連接馬達、不假裝 mock action 是模型品質證據。
