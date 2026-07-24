# Week10 Concept Answer Key

> 請先完成 `concept_practice.md` 的作答，再查看本參考答案。

## 題目 1

Topic 名稱讓端點在同一資料通道相遇；message type 規定 ROS 序列化型別；JSON schema 規定 `String.data` 內的業務欄位。名稱與型別正確只能證明字串可傳輸，不能保證它包含 VLM 結果或必要追蹤資訊。

## 題目 2

若模型延遲高，舊影像的結果可能在機器人已移動後才抵達。下游若依序執行所有舊語意，可能對過去場景做現在的動作。應比較時間戳、觀測 ID 或序號，並依任務選擇保留最新值、丟棄過期值或可靠保存全部結果。

## 題目 3

可依序確認 ROS_DISTRO 與 source、Domain ID、node list、topic list、topic info 的型別和端點、topic echo、topic hz，最後才檢查 JSON 解析與 schema。這能分別排除環境、discovery、連線、發布頻率與應用內容錯誤。

