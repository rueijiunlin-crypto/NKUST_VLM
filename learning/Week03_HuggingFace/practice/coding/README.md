# Week03 Coding Practice README

本資料夾是 Week03 的 Coding Practice（程式練習）入口。本週採 Guided Code Reading Mode（引導式程式閱讀模式），重點是閱讀完整可執行程式、追蹤資料流、觀察 shape（形狀）與中間值，而不是從零補 TODO。

## 模式說明

本週區分兩種程式材料：

- `../../demo/`：Demo（示範程式），快速展示 Hugging Face（模型平台）CLIP（對比式圖文預訓練）推論在做什麼。
- `guided_demos/`：Guided Code Reading（引導式程式閱讀），拆解 processor（前處理器）、tensor（張量）、logits（未正規化分數）、probability（機率分布）與 top-k（前 k 名）流程如何運作。

## 安裝方式

請從 `learning/Week03_HuggingFace` 目錄執行：

```powershell
python -m pip install -r practice/coding/requirements.txt
```

也可以使用 Demo 共用依賴：

```powershell
python -m pip install -r demo/requirements.txt
```

## Model / Data Requirement（模型與資料需求）

- Model / Dataset（模型 / 資料集）：`openai/clip-vit-base-patch32`
- Source（來源）：Hugging Face Model Hub（模型中心）上的 OpenAI CLIP 模型頁面
- Download size（下載大小）：約數百 MB，依 Hugging Face 快取與版本而定。
- Requires login（是否需要登入）：通常不需要。
- License / Terms（授權 / 條款）：請以 Hugging Face 模型頁面與 OpenAI CLIP 原始授權說明為準。
- CPU supported（是否支援 CPU）：支援。
- GPU recommended（是否建議 GPU）：非必要；若有 CUDA GPU（NVIDIA 平行運算 GPU）可加速。
- Expected runtime（預期執行時間）：第一次執行需下載權重，之後通常數秒到數十秒內完成。
- Common errors（常見錯誤）：模型下載失敗、SSL（安全通訊憑證）錯誤、圖片路徑錯誤、套件未安裝。

## 執行順序

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_02_logits_topk_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
python practice/coding/guided_demos/guided_03_prompt_effect_flow.py --image ../Week02_CLIP/demo/000000039769.jpg
```

若 Week02 範例圖片不存在，請改用自己的本地圖片路徑，例如：

```powershell
python practice/coding/guided_demos/guided_01_processor_flow.py --image demo/my_image.jpg
```

## 觀察任務

- 記錄 processor 輸出的 keys（欄位）與 shape。
- 說明 `input_ids`、`attention_mask`、`pixel_values` 分別來自文字或圖片。
- 改變 labels（候選標籤）數量，觀察 `logits_per_image` 的 shape 變化。
- 說明 top-k prediction（前 k 名預測）如何從 softmax probability 排序取得。
- 比較不同 prompt set（提示詞集合）如何改變 CLIP zero-shot classification（零樣本分類）結果。

請將觀察填入 `coding_practice.md`，完成後再查看 `coding_observation_key.md`。
