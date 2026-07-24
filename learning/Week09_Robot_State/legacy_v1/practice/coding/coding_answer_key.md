# Week09 Coding Answer Key

> 請先完成 `exercises/` 中的練習檔案，再查看本程式練習參考說明。

## TODO 1：來源

實體來源建立 `cv2.VideoCapture(camera_index)` 後立刻檢查 `isOpened()`；失敗時先釋放再丟出例外。合成來源可用簡單標記，讓 `read_frame` 決定如何產生固定影像。

## TODO 2：讀取

實體相機的 `read()` 同時回傳成功旗標與 frame，兩者都要檢查。標準彩色契約為三維、第三維為 3、dtype 為 `uint8`。合成影像也應遵守同一契約，使後續程式不需知道來源。

## TODO 3：保存

先建立父資料夾，再檢查 `cv2.imwrite()` 的布林回傳值。函式沒有拋錯不代表一定寫入成功。正式實驗也可在寫入後重新解碼或計算 checksum（校驗值）。

## TODO 4：handoff

從 `frame.shape` 取得 height、width、channels，明確標記 BGR，並加入 UUID、UTC 時間、輸出路徑、任務與問題。VQA 的空問題應在 handoff 階段拒絕。

## 常見錯誤

- 把 `(height, width)` 寫成 `(width, height)`。
- 未檢查 `frame is None` 就讀取 `.shape`。
- 在成功路徑呼叫 `release()`，但例外路徑未呼叫。
- 直接把 BGR 當 RGB 送入模型。
- 用合成影像通過取代相機驅動與權限驗收。

