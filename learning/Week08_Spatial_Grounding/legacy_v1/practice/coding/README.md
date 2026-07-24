# Week08 Coding Practice

## 模式

本週採 Implementation Practice Mode（實作練習模式）。學習者在 `exercises/mini_vlm_pipeline_practice.py` 完成三個 TODO；參考解答位於 `solutions/`，不可先複製回練習檔。

## 環境與安裝

```bash
python -m pip install -r practice/coding/requirements.txt
```

- Python：建議 3.10 或 3.11。
- CPU：可執行但推論可能較慢。
- GPU：非必要；CUDA 環境必須與 Torch 版本相容。
- Model：Caption 與 VQA 使用公開 BLIP base 模型；來源、授權及下載限制見 [Demo Guide](../../demo/demo_README.md)。

## 執行

先測試不下載模型的路徑：

```bash
python practice/coding/exercises/mini_vlm_pipeline_practice.py --task caption --image placeholder.jpg --dry-run
```

完成 TODO 後，再用真實影像執行：

```bash
python practice/coding/exercises/mini_vlm_pipeline_practice.py --task vqa --image <IMAGE_PATH> --question "What is visible?"
```

完整任務與紀錄欄位見 [coding_practice.md](./coding_practice.md)。

