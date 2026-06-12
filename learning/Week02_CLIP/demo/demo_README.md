# Week02 Demo Guide

本週採 Flat Integrated Demo（扁平整合式 Demo）。`demo_01` 至 `demo_04` 回答 CLIP「在做什麼（What）」；更完整的 shape 與中間值追蹤放在 `practice/coding/guided_demos/`。

## 安裝

只執行 NumPy Concept Demo：

```powershell
python -m pip install numpy
```

執行全部 Demo：

```powershell
python -m pip install -r demo/requirements.txt
```

## NumPy Concept Demo

### demo_01_text_image_embedding.py

- 對應概念：Image Embedding、Text Embedding、相同向量維度。
- 執行：`python demo/demo_01_text_image_embedding.py`
- 預期輸出：影像向量 shape、文字向量 shape、每個 label 的向量。
- 觀察重點：兩種模態需要相同 `embedding_dim` 才能比較。

### demo_02_cosine_similarity.py

- 對應概念：內積、向量長度、餘弦相似度。
- 執行：`python demo/demo_02_cosine_similarity.py`
- 預期輸出：每個標籤的 dot product、norm、cosine similarity 與排名。
- 觀察重點：餘弦相似度會排除向量長度的直接影響。

### demo_03_zero_shot_classification.py

- 對應概念：文字提示詞、相似度、Softmax、top-1。
- 執行：`python demo/demo_03_zero_shot_classification.py`
- 預期輸出：每個 label 的 score、probability 與預測。
- 觀察重點：機率是目前候選標籤之間的相對分布。

### demo_04_clip_flow.py

- 對應概念：完整 CLIP 資料流與相似度矩陣。
- 執行：`python demo/demo_04_clip_flow.py`
- 預期輸出：image/text embedding shape、similarity matrix 與每張圖片的預測。
- 觀察重點：`(image_count, embedding_dim)` 乘上轉置後文字矩陣，得到 `(image_count, label_count)`。

完成這四個 Demo 後，應能說明 CLIP 如何支援圖文檢索與零樣本分類，也能理解 VLM 為何需要視覺與文字表示。

## Real CLIP Demo（Optional / Advanced）

### demo_05_real_clip_zero_shot.py

- 模型：`openai/clip-vit-base-patch32`
- 來源：[Hugging Face model hub](https://huggingface.co/openai/clip-vit-base-patch32)
- 預設圖片：COCO validation 公開圖片 `000000039769.jpg`
- 圖片來源：`https://images.cocodataset.org/val2017/000000039769.jpg`
- 執行：

```powershell
python demo/demo_05_real_clip_zero_shot.py
python demo/demo_05_real_clip_zero_shot.py --image assets/sample_image.jpg
```

第一次執行會下載模型，需網路與數百 MB 磁碟空間。CPU 可執行但可能需數分鐘；GPU 非必要。模型與資料使用應遵守來源頁面的授權與條款，不需要登入即可嘗試公開模型。

若缺少套件，請執行 `python -m pip install -r demo/requirements.txt`。若網路、圖片或模型下載失敗，先完成四個 NumPy Demo，並在 `study_log.md` 記錄未執行原因；這不阻塞 Week02 基礎學習。

## 與 VLM / VLA 的關係

CLIP 展示了視覺與文字如何形成可比較的語意表示。後續 VLM 會加入回答與推理能力，VLA 則再結合機器人狀態與動作決策。相似度可作為候選排序訊號，但不能單獨取代空間感知、控制與安全驗證。
