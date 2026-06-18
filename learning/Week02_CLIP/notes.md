# Week02 Notes: CLIP 基礎

## 學習主線

CLIP（Contrastive Language-Image Pre-training，對比式圖文預訓練）把影像與文字分別編碼成相同維度的向量，並在共同嵌入空間中比較方向是否接近。

```text
Image -> Image Encoder -> Image Embedding
Text -> Text Encoder -> Text Embedding
Normalize -> Similarity -> Matching / Retrieval / Zero-shot Classification
```

`demo/` 快速回答「CLIP 在做什麼」，`practice/coding/guided_demos/` 則逐步追蹤「如何做到」。

## Level 1：CLIP 是什麼

CLIP 的基本任務是圖文對齊。模型學習讓內容相符的圖片與文字向量靠近，內容不相符的配對遠離。它不是查詢既有圖片資料庫，也不是聊天模型或完整 VLM assistant（視覺語言助手）。

CLIP 的輸出通常是向量或相似度分數，因此適合 image-text retrieval（圖文檢索）、zero-shot classification（零樣本分類）與語意檢索。它不會像生成式語言模型一樣直接寫出長篇回答。

**對應 Demo**

```powershell
python demo/demo_04_clip_flow.py
```

觀察整體輸入、編碼、相似度矩陣與預測流程。執行後應能回答：CLIP 最後比較的是原始圖片與句子，還是兩者的向量？

## Level 2：為什麼需要圖文共同向量空間

影像像素與文字 Token 是不同型態，不能直接逐項比較。CLIP 讓 Image Encoder 與 Text Encoder 最後都輸出相同維度，例如 `(embedding_dim,)`，使兩種模態能用同一種相似度函數比較。

共同嵌入空間不是一張固定語意地圖，而是模型訓練出的表示空間。向量較接近表示模型認為語意較相關，不代表兩者在所有情境下都完全等價。

**對應 Demo**

```powershell
python demo/demo_01_text_image_embedding.py
```

觀察 image embedding 與所有 text embeddings 的最後一維是否相同。執行後應能回答：為什麼維度不同時不能直接做內積？

## Level 3：Image Encoder 與 Text Encoder

Image Encoder（影像編碼器）把影像轉成影像向量。真實 CLIP 可使用 Vision Transformer（視覺轉換器）或卷積神經網路處理影像，再經 projection（投影層）得到共同空間中的向量。

Text Encoder（文字編碼器）把提示詞切成 Token，建立文字表示，再經投影層得到同維度文字向量。兩個 Encoder 不共享原始輸入處理方式，但訓練目標會把輸出對齊。

常見 batch shape：

```text
image_embeddings: (image_count, embedding_dim)
text_embeddings:  (label_count, embedding_dim)
```

**對應 Demo**

```powershell
python demo/demo_01_text_image_embedding.py
```

觀察每個 label 對應一列文字向量。執行後應能回答：`label_count` 與 `embedding_dim` 分別代表什麼？

## Level 4：Cosine Similarity

Cosine Similarity（餘弦相似度）比較兩個向量的方向：

```text
cosine(a, b) = dot(a, b) / (norm(a) * norm(b))
```

方向越接近，相似度越接近 1；垂直時接近 0；方向相反時接近 -1。CLIP 常先做 L2 normalization，讓向量長度為 1，此時內積就等於餘弦相似度。

相似度高表示模型判斷語意較匹配，不等於客觀機率，也不能單獨證明模型理解了所有細節。

**對應 Demo**

```powershell
python demo/demo_02_cosine_similarity.py
```

觀察 dot product、兩個 norm 與排序。執行後應能回答：只看內積而不考慮向量長度可能產生什麼問題？

## Level 5：Zero-shot Classification

一般分類模型通常在固定類別上訓練分類頭。CLIP 的零樣本分類則把候選類別寫成文字提示詞，例如 `a photo of a robot`，再比較圖片向量與每個文字向量。

```text
Image -> Image Embedding
Labels -> Prompt Texts -> Text Embeddings
Similarity Scores -> Softmax -> Top-1 Label
```

Softmax 把同一組候選標籤的分數轉成相對分布。若改變標籤集合或提示詞，機率也可能改變；它不是對世界中所有可能類別的絕對信心。

**對應 Demo**

```powershell
python demo/demo_03_zero_shot_classification.py
```

觀察 similarity score、probability 與 top-1。執行後應能回答：為什麼新增一個候選標籤可能改變其他標籤的機率？

## Level 6：Contrastive Learning 的直覺

Contrastive Learning（對比式學習）使用一個 batch（批次）中的正負配對學習：

- Positive Pair（正樣本配對）：真正相符的圖片與文字。
- Negative Pair（負樣本配對）：batch 中不相符的圖片與文字。

模型建立 image-to-text 與 text-to-image 的相似度矩陣，讓對角線正配對分數提高，其他錯誤配對分數降低。這不是要求模型背誦資料庫位置，而是調整兩個 Encoder，使語意相符的表示更容易匹配。

**對應 Demo**

```powershell
python demo/demo_04_clip_flow.py
```

觀察相似度矩陣對角線。執行後應能回答：若第 2 張圖片和第 2 段文字是正配對，理想上矩陣哪個位置應較高？

## Level 7：CLIP 與 VLM 的關係

CLIP 擅長把圖文映射到可比較表示，但不負責長篇生成。後續 VLM 會加入更完整的視覺特徵、跨模態連接模組與語言模型，使系統能根據影像回答、描述與推理。

可以把 CLIP 視為重要的圖文對齊基礎，而不是完整 VLM assistant。不同 VLM 不一定直接使用 CLIP，但常需要相似的視覺表示與跨模態對齊能力。

## Level 8：CLIP 在機器人語意理解中的用途

在室內語意導覽、災害巡檢或桌面操作研究中，CLIP 類模型可協助：

- 比較相機影像與文字目標的語意相似度。
- 用開放詞彙標籤做場景或物件候選排序。
- 建立可供後續 VLM 推理的檢索或篩選模組。

CLIP 分數不能直接等同安全決策。VLA 仍需結合感知可靠度、空間資訊、控制限制與任務驗證，才能產生動作。

## Level 9：本週常見誤解

1. **CLIP 是查資料庫。** 不正確；CLIP 先編碼，再計算向量相似度。檢索系統可以使用 CLIP 向量，但資料庫不是 CLIP 本身。
2. **CLIP 是聊天模型。** 不正確；標準 CLIP 不會逐字生成回答。
3. **CLIP 是完整 VLM assistant。** 不正確；它缺少完整語言生成與多步推理流程。
4. **相似度最高就一定正確。** 不正確；top-1 只是在目前候選標籤中最高。
5. **Softmax 機率是絕對真實機率。** 不正確；它依賴候選集合、提示詞與溫度尺度。
6. **共同空間表示圖文完全相同。** 不正確；兩種模態仍由不同 Encoder 處理，只是輸出被訓練成可比較。

## Level 10：Week02 驗收問題

1. CLIP 的輸入、Encoder、向量與輸出分別是什麼？
2. 為什麼 image embedding 與 text embedding 需要相同維度？
3. 餘弦相似度比較的是向量方向還是原始資料？
4. 零樣本分類如何把文字標籤轉成分類候選？
5. 對比式學習如何使用正配對與負配對？
6. 為什麼 CLIP 不是聊天模型？
7. CLIP 能如何支援後續 VLM 與 VLA？
8. Week03 使用 Hugging Face 載入模型時，你預期 processor 與 model 各自負責什麼？

## 本週尚未涵蓋

- CLIP 論文損失函數的完整數學推導。
- 大規模資料蒐集、訓練與分散式運算。
- Prompt ensembling（提示詞集成）與校準技術。
- 真實機器人控制與安全驗證。
