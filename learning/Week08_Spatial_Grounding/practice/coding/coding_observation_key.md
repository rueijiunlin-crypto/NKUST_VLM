# Week08 Coding Observation Key

> 請先執行 `guided_demos/guided_grounding_chain.py` 並記錄各階段的 frame、shape 與單位，再查看本說明。

## 觀察方向

- 2D detection 提供語意與 pixel location，但沒有 depth 時不能唯一決定 3D 位置。
- deprojection 後的點仍位於 camera frame，不能直接交給以 `base_link` 為基準的控制器。
- intrinsics（內部參數）負責 pixel-to-ray；extrinsics（外部參數）負責 frame-to-frame transform。
- 真實座標轉換需要 rotation 與 translation；範例只做平移是刻意簡化，不是完整機器人做法。

## 常見誤解

- bounding box center 不一定是物體可抓取點。
- 數值相同不代表 coordinate frame 相同。
- 忽略 meter／millimeter 單位會造成比模型辨識錯誤更危險的控制偏差。
