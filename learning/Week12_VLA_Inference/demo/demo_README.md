# Week12 Demo Guide

| Demo | 指令 | 目的 | 限制 |
| --- | --- | --- | --- |
| Basic VLA interface | `python demo/demo_01_basic_vla_inference.py --device cpu` | 觀察 observation/action chunk shape | deterministic mock，不是模型品質 |
| Runtime planner | `python demo/demo_02_runtime_planner.py` | 真實模型前置檢查 | 不下載權重 |

真實 SmolVLA／OpenVLA 為 optional／advanced：需查官方來源、license、下載大小、套件版本與 VRAM；未執行時標記 `Skipped - hardware/model requirement`。
