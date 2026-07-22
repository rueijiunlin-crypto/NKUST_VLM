# Week09 Demo Guide

## Demo 清單

| Demo | 概念 | 執行指令 | 預期輸出 |
|---|---|---|---|
| `demo_01_frame_contract.py` | shape、dtype、BGR/RGB | `python demo/demo_01_frame_contract.py` | 影格格式與像素順序 |
| `demo_02_camera_probe.py` | 相機開啟與讀取 | `python demo/demo_02_camera_probe.py --synthetic` | 來源及 frame shape |
| `demo_03_capture_snapshot.py` | 快照保存 | `python demo/demo_03_capture_snapshot.py --synthetic --output outputs/synthetic.jpg` | 檔案路徑及 shape |
| `demo_04_vlm_handoff.py` | VLM 請求交接 | `python demo/demo_04_vlm_handoff.py --image outputs/synthetic.jpg --task caption` | JSON payload |

## 安裝

```bash
python -m pip install -r demo/requirements.txt
```

- 不需要模型下載。
- 實體相機需作業系統權限、驅動與未被其他程式占用。
- `opencv-python` 適合一般桌面環境；無 GUI 伺服器可評估另建環境使用 headless 版本，不要在同一環境混裝兩者。

## 觀察重點與問題

### Demo 01

- 觀察：shape 是 HWC，顏色由 BGR 轉 RGB 後通道值交換。
- 問題：VLM processor 接收 RGB 時，應在哪一層轉換？

### Demo 02

- 觀察：合成來源固定為 480×640；實體來源另外列出 backend。
- 問題：`isOpened()` 成功後為何仍要檢查 `read()`？

實體相機指令：

```bash
python demo/demo_02_camera_probe.py --camera-index 0
```

### Demo 03

- 觀察：保存路徑、影格 shape，並確認檔案可重新開啟。
- 問題：合成影像成功能證明哪些層，又不能證明哪些層？

### Demo 04

- 觀察：`observation_id`、UTC 時間、來源與 frame metadata。
- 問題：哪些欄位會延續到 ROS2 語意結果 Topic？

VQA 範例：

```bash
python demo/demo_04_vlm_handoff.py --image outputs/synthetic.jpg --task vqa --question "What is visible?"
```

## Data Requirement（資料需求）

- Data：實體相機影格或程式產生的合成影像。
- Source：使用者控制的本機相機；合成影像由程式建立。
- Download size：無。
- Requires login：無；作業系統可能要求相機權限。
- License / Terms：自行拍攝資料仍須遵循研究倫理與隱私規範。
- CPU supported：支援。
- GPU recommended：不需要。
- Expected runtime：單張影格通常為秒內；依相機初始化而異。
- Common errors：錯誤索引、裝置被占用、權限拒絕、backend/驅動問題、輸出路徑不可寫。

## 與 VLM/VLA 研究的關係

本週把實體世界觀測轉成可追蹤的 VLM 輸入。保存原始快照與 metadata 能協助研究者判斷錯誤來自感測、前處理還是模型。

