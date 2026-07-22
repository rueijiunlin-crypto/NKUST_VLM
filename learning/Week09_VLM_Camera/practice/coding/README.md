# Week09 Coding Practice

## 模式與目標

本週採 Implementation Practice Mode。請完成 `exercises/camera_pipeline_practice.py` 的四個 TODO，建立可在合成來源與實體相機間切換的單張影格流程。

## 安裝

```bash
python -m pip install -r practice/coding/requirements.txt
```

環境限制與相機權限說明見 [Demo Guide](../../demo/demo_README.md)。本練習不下載模型，也不需 GPU。

## 執行

```bash
python practice/coding/exercises/camera_pipeline_practice.py --synthetic --output outputs/practice.jpg --task caption
python practice/coding/exercises/camera_pipeline_practice.py --camera-index 0 --output outputs/camera.jpg --task vqa --question "What is visible?"
```

`--synthetic` 只驗證軟體路徑；完成條件仍包含實體相機測試。詳細紀錄表見 [coding_practice.md](./coding_practice.md)。

