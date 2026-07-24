# Week08 Notes：Spatial Reasoning and Grounding

## 1. Grounding 層級

Semantic Location 描述「杯子在盒子左側」；2D Grounding 提供 pixel、box 或 mask；Depth 為光軸距離；3D Camera Coordinate 以相機為原點；Robot Coordinate 需外部標定與 transform。

## 2. Bounding Box 與 Mask

Box 是矩形範圍，便宜但含背景；segmentation mask 描述物體像素，適合邊界與接觸區，但仍不是三維幾何。

## 3. Camera Intrinsics

針孔模型反投影：

```text
X = (u - cx) Z / fx
Y = (v - cy) Z / fy
Z = depth
```

`u,v` 是像素，`fx,fy,cx,cy` 是內參，`X,Y,Z` 是 camera frame。公式需要有效 depth；沒有深度不能可靠產生公尺位置。

## 4. Extrinsics 與 Transform

齊次轉換 `p_robot = T_robot_camera · p_camera` 使用 rotation 與 translation。必須記錄 frame 名稱、時間、單位與 transform 來源；舊 transform 或錯誤方向會產生合理但錯誤的座標。

## 5. Spatial Observation Schema

至少包含 observation ID、source timestamp、object、2D region、depth validity、camera frame、robot frame、transform timestamp、3D position、uncertainty 與 validator status。

## 6. 系統邊界

Metric grounding 只提供幾何觀察，不自動證明 reachability、collision-free path 或 safe grasp。
