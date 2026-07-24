# Week09 Multimodal Tensor Track

- Status：程式可離線建立實際 tensor；tokenizer 首次執行會下載。
- Entry：`python demo/demo_03_multimodal_tensors.py --image <path> --device cpu`
- Requirements：`torch>=2.2`、`transformers>=4.49`、`pillow>=10`。
- Model/Data：僅使用 `bert-base-uncased` tokenizer 示範 token IDs，授權以官方 model card 為準。
- 驗證：記錄 image/state/language/timestamp 的 shape、dtype、device、unit、joint order 與 freshness。
