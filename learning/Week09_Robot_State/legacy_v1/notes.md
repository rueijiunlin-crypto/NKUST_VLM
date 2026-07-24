# Week09 Notes：VLM + Camera

## 1. 相機不是單一函式呼叫

相機資料流包含裝置選擇、影格讀取、格式驗證、時間記錄、保存及交接。建議先把每一層驗證完成，再啟動成本較高的 VLM 推論：

```text
Camera / synthetic source
          ↓
Open and read frame
          ↓
Validate shape and dtype
          ↓
Save snapshot + metadata
          ↓
Week08 VLM request
```

對應 Demo：`demo/demo_02_camera_probe.py`。執行後應能回答：相機「打不開」與「打得開但讀不到影格」應如何區分？

## 2. OpenCV 影格契約

一般彩色 OpenCV 影格是 `numpy.ndarray`，shape 為 `[height, width, channels]`、型別為 `uint8`，顏色順序預設為 BGR。許多 VLM processor 接受 PIL RGB 影像，因此交接前需明確轉換：

```python
frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
```

這與深度學習模型常用的 `[batch, channels, height, width]` 不同。混淆兩者可能不會立即報錯，卻會造成顏色或維度語意錯誤。

對應 Demo：`demo/demo_01_frame_contract.py`。

- 觀察：BGR `[255, 0, 0]` 轉成 RGB 後變為 `[0, 0, 255]`。
- 問題：為何單看 shape 無法發現顏色空間錯誤？

## 3. `VideoCapture` 生命週期

官方 OpenCV `VideoCapture` 介面提供裝置開啟、`isOpened()`、`read()` 與 `release()`。即使程式發生例外，也應在 `finally` 釋放裝置，否則下一個程式可能無法取得相機。

參考：[OpenCV VideoCapture 官方文件](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html)

相機索引 `0` 只是常見預設，不代表所有電腦都相同。backend、作業系統權限、裝置是否被占用及驅動程式都會影響結果。

## 4. 保存快照與 metadata

`demo/demo_03_capture_snapshot.py` 同時支援合成與實體來源。`cv2.imwrite()` 會回傳布林值，因此不能只呼叫而不檢查；成功寫檔也應再保留：

- UTC 時間戳。
- 唯一 `observation_id`。
- 來源影像路徑。
- width、height、channels 與 color space。
- 相機索引、backend 與設定值（正式實驗建議）。

合成影像能驗證程式，但不能證明相機權限、驅動、曝光或實際畫質正常。

## 5. 即時不等於每一幀都推論

若相機為 30 FPS，而 VLM 一次推論需要數秒，逐幀推論會造成佇列越積越多，最後模型描述的是過時畫面。可採用：

- 固定時間間隔取樣。
- 只保留最新影格，丟棄舊影格。
- 事件觸發擷取。
- 將相機擷取與推論分成不同 process（程序）或 ROS2 Node。

研究紀錄必須包含「影格擷取時間」與「推論完成時間」，才能量測 end-to-end latency（端到端延遲）。

## 6. 交接至 VLM

`demo/demo_04_vlm_handoff.py` 不直接執行模型，而是產生 Week08 可接受的請求。這個分離讓相機與模型可單獨測試，也讓 Week10 能把結果透過 ROS2 Topic 發布。

執行後應能回答：若模型回答錯誤，哪些紀錄可先排除相機讀取與顏色空間問題？

## 7. 隱私與資料管理

相機可能擷取個人或敏感環境資訊。正式研究應事先定義告知、同意、保存期限、存取權限與去識別化方式，不應把未審核的影像直接提交至公開服務。

## 本週尚未涵蓋

- ROS2 Image message（影像訊息）與 `cv_bridge`。
- 多相機時間同步與硬體時間戳。
- 自動曝光、內外參校正與畸變校正。

