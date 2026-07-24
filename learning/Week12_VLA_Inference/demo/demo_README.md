# Week12 Demo Guide

| Demo | 指令 | 目的 | 限制 |
| --- | --- | --- | --- |
| Basic VLA interface | `python demo/demo_01_basic_vla_inference.py --device cpu` | 觀察 observation/action chunk shape | deterministic mock，不是模型品質 |
| Runtime planner | `python demo/demo_02_runtime_planner.py` | 真實模型前置檢查 | 不下載權重 |
| Required Real SmolVLA | `python demo/demo_03_real_smolvla_inference.py --dataset-id lerobot/svla_so100_pickplace --device cuda` | 官方 preprocess → policy → postprocess | log-only；需模型、資料與相容 LeRobot |

真實 SmolVLA 是 Required Learning Track：需查官方來源、license、下載大小、套件版本與 VRAM；未執行時使用標準 runtime blocker，不得標為省略或完成。
