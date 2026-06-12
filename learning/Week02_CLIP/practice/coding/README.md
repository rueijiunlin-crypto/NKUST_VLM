# Week02 Coding Practice

## 模式

本週採 Guided Code Reading Mode（引導式程式閱讀模式）。重點是執行完整程式、閱讀 step-by-step comments（逐步註解）、追蹤 shape 與中間值，而不是從零實作 CLIP。

本週不需要補 TODO，也不使用 `exercises/`、`solutions/`。後續 ROS2、camera pipeline（相機流程）或系統整合週次，才會依學習目標採用 Implementation Practice Mode（實作練習模式）。

## 安裝

```powershell
python -m pip install -r practice/coding/requirements.txt
```

## 執行

```powershell
python practice/coding/guided_demos/01_vector_similarity_reading.py
python practice/coding/guided_demos/02_text_image_alignment_reading.py
python practice/coding/guided_demos/03_zero_shot_reading.py
python practice/coding/guided_demos/04_clip_pipeline_reading.py
```

## 觀察重點

- 向量正規化前後的 norm 與 shape。
- 圖片數、文字數、embedding 維度如何形成相似度矩陣。
- Softmax 軸向與每列機率總和。
- 對比式學習中矩陣對角線為何代表正配對。

請把執行結果寫入 `coding_practice.md` 與本週 `study_log.md`。完成自己的觀察後，再閱讀 `coding_observation_key.md`。
