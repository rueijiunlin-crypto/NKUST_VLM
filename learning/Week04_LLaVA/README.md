# Week04 LLaVA + Grounded Visual Reasoning

## 本週定位

Week04 延續 Week03 Hugging Face（模型平台）與 CLIP（對比式圖文預訓練）推論流程，進一步學習 LLaVA（大型語言與視覺助手）如何根據圖片與問題生成文字回答，並加入 Grounded Visual Reasoning（具有視覺依據的多模態推理）。LLaVA 基礎推論仍是本週主線。

本週重點不是只把模型呼叫起來，而是要能說清楚：

- `AutoProcessor` 如何同時整理圖片、問題與對話模板。
- Vision Encoder（視覺編碼器）、Projector（投影器）與 Large Language Model（大型語言模型，LLM）的分工。
- `input_ids`、`attention_mask` 與 `pixel_values` 的 shape 代表什麼。
- `<image>` placeholder（影像占位符）如何對應多個 image tokens（影像詞元）。
- `generate()` 如何逐 token 產生回答。
- 問題與提示格式如何影響回答內容及 hallucination（幻覺）風險。
- 一般影像問答與 Robot-Oriented Visual Reasoning（機器人導向視覺推理）需要的證據有何不同。
- 為什麼「VLM 看得到」不等於「Robot 做得到」。

## 文件導覽

| 檔案或資料夾 | 用途 |
| --- | --- |
| `weekly_plan.md` | 本週學習順序、Demo 執行順序、Practice 任務與驗收條件。 |
| `notes.md` | LLaVA 推論流程、tensor shape（張量形狀）、核心程式與提示實驗教材。 |
| `study_log.md` | 學生實際執行 Demo、Practice、問題比較與疑問紀錄。 |
| `demo/` | 快速展示 Processor 輸入、架構資料流、真實視覺問答與問題比較。 |
| `practice/` | Concept Practice（觀念練習）與 Guided Code Reading Mode（引導式程式閱讀模式）。 |

## 建議使用方式

1. 閱讀 `weekly_plan.md`，確認本週任務與驗收條件。
2. 閱讀 `notes.md` 第 1–3 節，理解 Processor、模型元件與輸入 shape。
3. 執行 Demo 01 與 Demo 02，建立真實輸入與架構資料流的整體印象。
4. 執行 `practice/coding/guided_demos/`，追蹤 Processor、Projector、多模態序列與生成步驟。
5. 執行 Required Real Model Track 的 Demo 03；Demo 04 用於三個問題的比較。若環境受阻，仍須留下 blocker 與完整執行計畫。
6. 將回答拆成 Supported（影像支持）、Uncertain（無法確認）、Contradicted（影像不支持）或 Requires Additional Sensor / Robot State（需要額外感測或機器人狀態）。
7. 完成 Concept Practice 與 Coding Practice 的學生觀察欄位。
8. 將實際輸出、錯誤、幻覺案例與未解問題記錄到 `study_log.md`。

## Demo 主線

請從 `learning/Week04_LLaVA` 執行：

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_llava_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_02_llava_architecture_flow.py
python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg --question "What is shown in this image?"
python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg --question "Which visible objects could potentially be manipulated by a robot, and what information is still missing?"
python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

Demo 01 只下載 Processor（前處理器）相關檔案，不載入完整 7B 模型。Demo 03 是本週 Required Real Model Track；Demo 04 是必要比較活動。需要大型模型權重與較高硬體資源時，可將 runtime 記為 Hardware／Network／Environment blocked，但不得省略問題、revision、執行命令與預期證據。

## 真實模型執行契約

三個必要問題分別檢查場景描述、可操作物體與缺失的機器人／幾何資訊；詳見 `weekly_plan.md` 與 `demo/real_track_README.md`。每次執行需記錄 model、revision、GPU、dtype、VRAM、load/inference time、input/output token、完整回答與 hallucination evidence（幻覺證據）。回答必須區分 Supported、Uncertain、Contradicted 與 Requires Additional Sensor / Robot State。

## 與 VLM/VLA 碩士研究的關聯

LLaVA 可提供物體類別、場景與相對位置等 semantic information（語意資訊），但單張 RGB 圖片不能可靠提供精確 XYZ、Robot Base Coordinate（機器人基座座標）、Joint State（關節狀態）、Reachability（可達性）或安全動作。本週只建立能力邊界，不提前實作 ROS2、深度相機、模擬器或 VLA 訓練。

## 本週完成後應具備的能力

- 能解釋 `AutoProcessor` 與 `LlavaForConditionalGeneration` 的分工。
- 能畫出 Image → Vision Encoder → Projector → Image Tokens → LLM → Answer。
- 能解讀 `input_ids`、`attention_mask` 與 `pixel_values` 的 shape。
- 能解釋 `<image>` 為什麼不是單一 patch token（影像區塊詞元）。
- 能說明 LLaVA 與 CLIP 的輸出機制差異。
- 能比較不同問題的回答，辨識有影像依據與無法確認的主張。
- 能區分 semantic information 與 metric / geometric information（度量／幾何資訊）。
- 能說明 LLaVA 文字回答不能直接當成安全的 Robot Action（機器人動作）。
