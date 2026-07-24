# Week08 Weekly Plan：Spatial Reasoning and Grounding

## 本週目標

- 區分 semantic、2D pixel、depth、3D camera 與 robot frame。
- 建立可供機器人系統驗證的 Spatial Observation（空間觀測）。

## 必學概念

- 理解 Bounding Box、Segmentation、intrinsics、extrinsics、2D→3D 與 coordinate transform。
- 建立具 observation ID、timestamp、frame ID 與 uncertainty 的 Spatial Observation。

## 建議學習順序

1. 閱讀 `notes.md` 並畫出 grounding chain。
2. 執行 Demo，比較 semantic、2D 與 3D 層級。
3. 執行 Guided Demo，追蹤 pixel-to-robot-frame 資料流。
4. 完成座標轉換 Implementation Practice 並記錄錯誤。

## Demo 執行順序

```powershell
python demo/demo_01_grounding_levels.py
python demo/demo_02_pixel_to_3d.py
python practice/coding/guided_demos/guided_grounding_chain.py
python practice/coding/solutions/coordinate_transform_solution.py
```

## 任務清單

- [ ] 閱讀本週文件並標出每個 coordinate frame。
- [ ] 執行兩個 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `coordinate_transform_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 frame、unit 與 uncertainty。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

本週採 Guided + Implementation 混合模式。

## Paper Reading（論文閱讀）

### Core Reading

- Title: 3D-LLM: Injecting the 3D World into Large Language Models
- Authors: Yining Hong et al.
- Year / Venue: 2023 / NeurIPS
- DOI: N/A
- arXiv: 2307.12981
- Link: https://arxiv.org/abs/2307.12981
- Code / Project: https://github.com/UMass-Foundation-Model/3D-LLM
- Required Reading：Abstract、3D feature extraction、3D-language alignment、tasks、evaluation。
- Skim Reading：資料生成與完整附錄。
- Skip for Now：大規模 3D 預訓練重現。
- Optional Reading：Grounded-SAM；OpenScene。

### Reading Questions

1. 2D VLM 為何不足以處理機器人空間任務？
2. 3D scene 與 language 的輸入輸出是什麼？
3. 座標、特徵與文字如何對齊？
4. Camera、world、robot frame 的 transform shape 為何？
5. Grounding 如何由語詞連到 3D 區域？
6. 深度誤差如何傳播到世界座標？
7. 3D 表徵如何進入語言模型？
8. 主要任務與評估指標是什麼？
9. 哪項結果支持 3D-aware reasoning？
10. 遮擋、尺度與標定限制是什麼？
11. 空間語意如何安全交給導航或操作模組？
12. 哪個公式與證據必須寫進本週推導紀錄？

### Deep Reading

深讀座標系、幾何投影、3D-language alignment 與失敗案例，並將論文公式對應到本週數值 Demo。

## 驗收條件

- [ ] 能寫出 pinhole 反投影公式與變數。
- [ ] 能說明 camera intrinsics／extrinsics。
- [ ] 能區分 camera frame 與 robot frame。
- [ ] 不把語意關係誤當公尺座標。

## 銜接 Week09

Week09 將空間觀察與 Robot State、時間同步整合。
