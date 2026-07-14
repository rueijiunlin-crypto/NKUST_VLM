# Week04 Demo README

`demo/` 只負責快速展示 LLaVA（大型語言與視覺助手）的主要現象，回答「這個流程在做什麼」。若要逐步閱讀 Projector（投影器）、shape tracing（張量形狀追蹤）、多模態序列與生成中間值，請搭配 `../practice/coding/guided_demos/`。

## 安裝方式

請從 `learning/Week04_LLaVA` 執行：

```powershell
python -m pip install -r demo/requirements.txt
```

Demo 01 只載入 Processor（前處理器），Demo 02 只使用 Python 標準函式庫。Demo 03、Demo 04 才會載入完整 7B 模型。

## Model / Data Requirement（模型與資料需求）

- Model / Dataset：`llava-hf/llava-1.5-7b-hf`
- Source：[Hugging Face LLaVA Model Card](https://huggingface.co/llava-hf/llava-1.5-7b-hf)
- Download size：完整 FP16 權重約為十多 GB 等級；Processor 檔案較小；實際快取大小可能隨版本變動
- Requires login：公開模型通常不需要；若存取狀態變動，以模型頁面為準
- License / Terms：模型頁目前標示 Llama 2 Community License，使用前須重新確認最新條款
- CPU supported：Demo 01、02 支援；完整 7B 模型技術上可嘗試，但速度慢且需要大量系統記憶體
- GPU recommended：Demo 03、04 建議 NVIDIA CUDA GPU，通常需要約 16 GB 以上可用 VRAM（顯示記憶體）；實際需求依環境而異
- Expected runtime：Demo 01、02 通常在數秒內完成（Demo 01 首次需下載 Processor）；完整模型首次下載與載入可能需數十分鐘以上
- Common errors：模型下載失敗、磁碟不足、CUDA 記憶體不足、套件版本不符、圖片路徑錯誤

## Demo 檔案清單

| Demo | 對應概念 | 執行指令 | 預期輸出 | 觀察重點 |
| --- | --- | --- | --- | --- |
| `demo_01_llava_processor_inputs.py` | `AutoProcessor` 多模態前處理 | `python demo/demo_01_llava_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg` | 輸入 keys、shape、dtype、token 數量 | 哪些 tensor 屬於文字，哪些屬於圖片。 |
| `demo_02_llava_architecture_flow.py` | Vision Encoder → Projector → LLM | `python demo/demo_02_llava_architecture_flow.py` | 架構各階段的示意 shape | Projector 改變哪個維度，image token 數量如何計算。 |
| `demo_03_llava_visual_qa.py` | 真實 LLaVA 視覺問答 | `python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg` | 輸入 shape、回答、token 數量、推論時間 | 回答中的主張是否由圖片支持。 |
| `demo_04_question_comparison.py` | Question／Prompt sensitivity | `python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg` | 同一圖片的多組問答 | 問題改寫如何影響細節、限制與幻覺。 |

Demo 數量依本週必要概念決定，不限制為固定三個，也不為增加數量而重複相同現象。

## Demo 01：LLaVA Processor Inputs

```powershell
python demo/demo_01_llava_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
```

應觀察：

- `input_ids` 與 `attention_mask` 的 shape。
- `pixel_values` 的 batch、channels、高度與寬度。
- Prompt 中的 `<image>` placeholder（影像占位符）。
- Processor 不等於完整生成模型。

執行後應能回答：

- 哪些輸入來自問題文字？哪些來自圖片？
- 為什麼 `<image>` 不能解釋成單一像素或單一 patch token（影像區塊詞元）？

## Demo 02：LLaVA Architecture Flow

```powershell
python demo/demo_02_llava_architecture_flow.py
python demo/demo_02_llava_architecture_flow.py --image-size 336 --patch-size 14 --text-tokens 20
```

應觀察：

- 圖片如何形成 patch grid（影像區塊網格）。
- Vision features（視覺特徵）與 projected image tokens（投影後影像詞元）的 shape。
- Projector 前後 image token 數量與 hidden size（隱藏維度）。
- 圖片與文字共同影響多模態序列長度。

執行後應能回答：

- Projector 為什麼必要？
- 影像寬高加倍、patch size 不變時，image token 數量可能如何變化？

## Demo 03：LLaVA Visual QA（選做／進階）

```powershell
python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg --question "What is shown in this image?"
```

應觀察：

- 模型 ID、硬體裝置與輸入 tensor shape。
- `max_new_tokens` 與實際生成 token 數量。
- 原始回答與推論時間。
- 回答是否包含圖片不存在或無法確認的細節。

執行後應能回答：

- 為什麼語句流暢不等於具有視覺依據？
- 為什麼真實模型成功載入不能取代 shape 與資料流理解？

## Demo 04：Question Comparison（選做／進階）

```powershell
python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

自訂問題：

```powershell
python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg --questions "What objects are visible?" "What cannot be confirmed?"
```

應觀察：

- 同一圖片、不同問題的回答差異。
- 全域描述、屬性問題與不確定性問題的回答方式。
- 回答中的 Supported（圖片支持）、Uncertain（無法確認）與 Contradicted（圖片不支持）主張。

執行後應能回答：

- 哪種問題最容易誘導模型補充不存在的細節？
- 如何設計問題讓模型明確說出無法確認的資訊？

## 常見問題

### Image path does not exist

確認 `--image` 指向本機存在的圖片。若 Week02 圖片不存在，改用自己的圖片：

```powershell
python demo/demo_01_llava_processor_inputs.py --image demo/my_image.jpg
```

### 首次執行較慢

Demo 01 首次會下載 Processor 檔案；Demo 03、04 會下載完整模型。兩者資源需求不同，不能因 Demo 01 成功就假設完整模型已下載。

### CUDA out of memory

關閉其他 GPU 程式並縮短 `--max-new-tokens`。若硬體仍不足，將 Demo 03、04 記錄為「未執行及原因」，完成 Basic Demo 與 Guided Code Reading 即可。

### SSL、網路或磁碟問題

確認 Hugging Face 連線、Python 憑證、代理設定與模型快取磁碟空間。請保存完整錯誤訊息到 `study_log.md`。

### 回答重複 Prompt

程式只解碼輸入長度之後的新 token。自行修改時若解碼整個 `output_ids`，可能把 prompt 一起印成回答。
