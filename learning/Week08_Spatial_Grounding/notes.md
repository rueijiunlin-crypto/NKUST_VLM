# Week08 Notes：Spatial Reasoning and Grounding

## Why 與 Problem

「杯子在桌上」是語意描述，不足以讓機器人導航或抓取。Spatial Grounding（空間定位）要把文字指稱連到 2D region，再結合 depth、camera calibration 與 rigid transform 得到帶座標系與不確定度的 3D observation。

## Input 與 Output

- Input：RGB `[H,W,3]`、depth `[H,W]`、box/mask、intrinsics `K [3,3]`、extrinsics `T_robot_camera [4,4]`。
- Output：camera-frame point `[Xc,Yc,Zc,1]`、robot-frame point `[Xr,Yr,Zr,1]`、timestamp、uncertainty、validity。

## 2D Grounding

Bounding box 適合快速指出範圍，但包含背景；segmentation mask 可從物體內取有效 depth 中位數，較能抵抗邊緣混合。文字、box、mask 必須共享同一張影像 revision 與 timestamp。

## Intrinsics：Pixel 到 Camera Frame

針孔模型：

```text
u = fx X/Z + cx
v = fy Y/Z + cy
X = (u-cx)Z/fx
Y = (v-cy)Z/fy
```

齊次形式為 `s [u,v,1]^T = K [X,Y,Z]^T`。例：`fx=fy=600`、`cx=320`、`cy=240`、pixel `(380,270)`、depth `Z=1.2 m`，則 `X=0.12 m`、`Y=0.06 m`，camera point 為 `[0.12,0.06,1.2,1]^T`。

## Extrinsics：Camera 到 Robot Frame

```text
T_robot_camera = [ R  t ]
                 [ 0  1 ]
p_robot = T_robot_camera p_camera
```

若 `R=I`、`t=[0.5,0,0.8]^T`，上述點轉換為 `[0.62,0.06,2.0,1]^T`。矩陣方向不可只靠名稱猜測；應以已知 calibration target 驗證，並檢查 `T_camera_robot = inverse(T_robot_camera)`。

## Data Flow 與 Shape

```text
phrase
→ 2D detector / segmenter
→ box [4] or mask [H,W]
→ robust depth Z
→ K^-1 [uZ,vZ,Z]
→ p_camera [4]
→ T_robot_camera @ p_camera
→ p_robot [4] + covariance [3,3]
→ workspace validator
```

Batch `N` 個點可用 `[N,4] @ T^T`。必須統一 column-vector 或 row-vector convention，不能混用。

## Error Propagation

近似而言，`X=(u-cx)Z/fx` 對 depth 的敏感度為 `∂X/∂Z=(u-cx)/fx`。Depth noise、pixel localization、intrinsic calibration 與 extrinsic drift 都會傳到 3D。至少保存 depth MAD/variance、重投影誤差與 transform age。

## Failure、Limitation 與 Safety

- 無效 depth、反光或透明物體。
- box 中心落在背景。
- depth 與 RGB 未對齊。
- 公尺／毫米單位混用。
- 左手／右手座標、軸方向或矩陣順序錯誤。
- 舊 extrinsics 與移動中的 camera pose。

Grounded point 仍不代表 reachable、collision-free 或 safe grasp。它只能進入 planner 前的候選 observation。

## Demo 與 Paper Mapping

- Numeric Demo：代入已知 `K`、depth、`T`，印出每一步矩陣與重投影誤差。
- Core Paper：3D-LLM，對應 3D-language alignment；本週聚焦可驗證的幾何介面，不複製其大規模訓練。

## 本週尚未涵蓋

不涵蓋完整 SLAM、trajectory planning 或 grasp synthesis。
