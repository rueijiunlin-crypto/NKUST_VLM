# Week04 教材筆記：LLaVA 影像問答推論流程

本週沿用 Week03 的學習方式，從真實 Hugging Face（模型平台）推論介面出發，再拆解內部資料流：

```text
Image + Question
↓
AutoProcessor
↓
input_ids + attention_mask + pixel_values
↓
Vision Encoder → Projector → Image Tokens
↓
Large Language Model
↓
Generated Token IDs → Answer
```

## 1. 為什麼 Week04 要學 LLaVA

Week03 的 CLIP（對比式圖文預訓練）把圖片與候選文字轉成向量，輸出圖文相似度。它適合回答：「在這些候選描述中，哪一個最接近圖片？」

LLaVA（大型語言與視覺助手）則把圖片特徵與文字問題送進可生成文字的 Large Language Model（大型語言模型，LLM），適合回答：「根據圖片與問題，應該產生什麼文字？」

| 比較項目 | CLIP | LLaVA |
| --- | --- | --- |
| 主要任務 | 圖文對齊、檢索、零樣本分類 | 影像問答、多模態對話、文字生成 |
| 文字輸入 | 候選 labels／prompts | 問題、指令、對話歷史 |
| 常見輸出 | `[num_images, num_texts]` 相似度 | 一串 generated token IDs（生成詞元識別碼） |
| 是否依賴固定候選答案 | 通常是 | 不需要 |
| 主要風險 | 候選集合限制、相似度誤判 | 幻覺、提示敏感、生成不穩定 |

Week04 的核心不是把 CLIP 換成另一個模型名稱，而是理解分類式輸出如何轉變為生成式輸出。

## 2. `AutoProcessor` 與 `LlavaForConditionalGeneration` 的分工

### `AutoProcessor`

Processor（前處理器）同時負責圖片與文字：

- 開啟並正規化圖片。
- 將圖片整理成 `pixel_values`。
- 依 checkpoint（模型檢查點）格式建立 prompt（提示）。
- 將文字轉成 `input_ids` 與 `attention_mask`。
- 在輸入中保留 `<image>` placeholder（影像占位符）所需的多模態位置。

`<image>` 不是圖片本身，也不是單一 patch token（影像區塊詞元）。它是對話文字中的占位符；後續模型會依 processor 與模型設定對應多個 image embeddings（影像嵌入向量）。

### `LlavaForConditionalGeneration`

模型主要包含：

1. Vision Encoder（視覺編碼器）：把圖片切成 patches 並輸出視覺特徵。
2. Projector（投影器）：把視覺特徵轉成 LLM 可接收的 hidden size（隱藏維度）。
3. LLM：結合 image tokens（影像詞元）與 text tokens（文字詞元），逐 token 生成回答。

```text
pixel_values
↓
Vision Encoder
↓ [batch, image_tokens, vision_hidden]
Projector
↓ [batch, image_tokens, language_hidden]
LLM + text embeddings
↓
generated token IDs
```

Projector 不會直接產生自然語言；它輸出的是連續向量。自然語言由 LLM 自回歸生成。

### 對應 Demo

- Demo：`demo/demo_02_llava_architecture_flow.py`
- 執行：`python demo/demo_02_llava_architecture_flow.py`
- 觀察：Vision Encoder、Projector 與 LLM 前後的 shape。
- 預期輸出：圖片、patch grid、image tokens、文字 tokens 與總序列長度。
- 執行後應能回答：Projector 前後哪個維度改變？哪個維度可以保持不變？

## 3. LLaVA 推論中的 Tensor Shape 解讀

### `pixel_values`

常見概念 shape：

```text
[batch_size, channels, image_height, image_width]
```

例如 `[1, 3, 336, 336]` 代表一張 RGB 圖片。實際尺寸由 checkpoint 的 image processor 決定。

### `input_ids` 與 `attention_mask`

```text
input_ids:      [batch_size, sequence_length]
attention_mask: [batch_size, sequence_length]
```

`input_ids` 儲存文字與特殊 token 的識別碼；`attention_mask` 標記哪些位置有效。兩者 shape 相同，但內容與用途不同。

### Vision features 與 image tokens

以 `336 × 336` 圖片與 `14 × 14` patch 為示意：

```text
patch grid:       24 × 24
patch count:      576
vision features:  [1, 576, vision_hidden]
projected tokens: [1, 576, language_hidden]
```

576 不是所有 LLaVA 模型的固定常數。解析度、patch size、特殊 token、feature selection（特徵選擇）與模型版本都可能改變實際數量。

### Generated token IDs

`generate()` 對 decoder-only（僅解碼器）模型常回傳包含輸入 prompt 與新增回答的 token 序列。因此程式會用輸入長度切出新生成部分：

```python
prompt_length = inputs["input_ids"].shape[1]
new_token_ids = output_ids[:, prompt_length:]
```

### 對應 Demo

- Demo：`demo/demo_01_llava_processor_inputs.py`
- 執行：`python demo/demo_01_llava_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg`
- 觀察：Processor 輸出的 keys、shape 與 dtype（資料型別）。
- 預期輸出：`input_ids`、`attention_mask`、`pixel_values` 等實際輸入摘要。
- 執行後應能回答：哪些 tensor 屬於文字？哪些 tensor 屬於圖片？

## 4. 核心程式碼逐行解釋

### 4.1 載入 Processor 與模型

```python
processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=dtype,
    low_cpu_mem_usage=True,
    device_map="auto",
)
```

`from_pretrained()` 會讀取 checkpoint 的設定與檔案。Processor 與模型必須使用相容的 Model ID（模型識別名稱），不能任意混用。

### 4.2 建立單輪輸入

LLaVA 1.5 常見示意格式：

```python
prompt = f"USER: <image>\n{question} ASSISTANT:"
inputs = processor(images=image, text=prompt, return_tensors="pt")
```

`ASSISTANT:` 是生成起點，不是模型已經產生的答案。不同 LLaVA 系列可能採用不同角色與特殊 token，真實研究應優先使用 checkpoint 提供的 chat template（對話模板）。

### 4.3 將 tensor 放到模型裝置

```python
input_device = next(model.parameters()).device
inputs = {name: tensor.to(input_device) for name, tensor in inputs.items()}
```

若模型與輸入位於不同裝置，會出現 device mismatch（裝置不一致）錯誤。

### 4.4 生成與解碼

```python
with torch.inference_mode():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=False,
    )

answer = processor.batch_decode(
    output_ids[:, inputs["input_ids"].shape[1]:],
    skip_special_tokens=True,
)[0]
```

`torch.inference_mode()` 關閉梯度紀錄，降低推論額外成本。`do_sample=False` 常搭配 greedy decoding（貪婪解碼），提高可重現性，但不代表回答一定正確。

### 對應 Demo

- Demo：`demo/demo_03_llava_visual_qa.py`
- 執行：`python demo/demo_03_llava_visual_qa.py --image ../Week02_CLIP/demo/000000039769.jpg --question "What is shown in this image?"`
- 觀察：模型、裝置、輸入 shape、生成 token 數量、回答與推論時間。
- 預期輸出：一段由圖片與問題條件生成的文字。
- 執行後應能回答：回答中的哪些主張能由圖片直接支持？

## 5. Image Tokens 與文字生成

### 多模態序列

概念上，Processor 與模型會把一個人類可讀的提示：

```text
USER: <image> What is visible? ASSISTANT:
```

轉成類似：

```text
[USER] [IMG_1] [IMG_2] ... [IMG_N] [What] [is] [visible] [ASSISTANT]
```

Prompt 中雖然只有一個 `<image>`，模型序列中可能有數百個 image positions（影像位置）。圖片解析度、圖片數量與文字長度都會增加序列成本。

### 自回歸生成

LLM 每一步根據目前上下文計算 next-token logits（下一詞元分數），選出下一個 token，再把它接回序列：

```text
multimodal context → next-token logits → select token
                                      ↓
updated context    ← append token  ←───┘
```

常見參數：

- `max_new_tokens`：最多新增多少 token，不是回答字數。
- `do_sample=False`：不抽樣，通常較容易重現。
- `temperature`：抽樣時調整分布平坦程度。
- `top_p`：限制抽樣候選集合。

研究比較時必須固定並記錄生成參數，否則回答差異可能來自抽樣設定。

## 6. Question／Prompt 設計與回答差異

同一張圖片可使用不同問題觀察模型能力：

| 問題類型 | 範例 | 主要觀察 |
| --- | --- | --- |
| 全域描述 | What is shown in this image? | 主要場景與物件 |
| 物件問題 | What objects are visible? | 物件遺漏或新增 |
| 屬性問題 | What colors can be verified? | 顏色是否有影像依據 |
| 空間關係 | Where is the object located? | 左右、前後、上下關係 |
| 安全限制 | What cannot be confirmed? | 模型是否承認不確定性 |

### Prompt sensitivity

更詳細的問題不一定更準確。若問題包含不存在的前提，例如「紅色箱子旁邊有什麼？」，模型可能順著語言前提產生內容，而不是先否定圖片中沒有紅色箱子。

### 最小 Grounding 分析

將回答拆成獨立主張，逐項標記：

- Supported（圖片支持）。
- Uncertain（圖片無法確認）。
- Contradicted（圖片明顯不支持）。

語法流暢不等於事實正確。LLaVA 回答也不能直接當成 ROS2 或 VLA（視覺語言動作模型）的控制命令。

### 對應 Demo

- Demo：`demo/demo_04_question_comparison.py`
- 執行：`python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg`
- 觀察：不同問題的回答長度、細節、共同主張與可能幻覺。
- 預期輸出：同一圖片對多個問題的回答與推論時間。
- 執行後應能回答：哪一個問題最容易引導模型產生無法確認的細節？

## 7. 常見執行問題與模型限制

### 圖片路徑

若出現 `FileNotFoundError`，確認命令是從 `learning/Week04_LLaVA` 執行，或改用自己的絕對圖片路徑。

### 模型下載

Demo 01 只需下載 Processor 相關設定；Demo 03、Demo 04 使用 `llava-hf/llava-1.5-7b-hf`，FP16 權重約為十多 GB 等級，另需足夠磁碟快取。下載量與模型頁內容可能更新，執行前應查看官方 Model Card（模型說明頁）。

### CPU／GPU

- Processor Demo 可使用 CPU。
- 完整 7B 模型技術上可在高記憶體 CPU 環境嘗試，但速度很慢。
- 建議使用具有約 16 GB 以上可用 VRAM（顯示記憶體）的 NVIDIA GPU；實際需求依 dtype、裝置映射與環境而異。
- CUDA out of memory（CUDA 記憶體不足）時，先關閉其他 GPU 程式並縮短生成長度；量化屬進階內容，不列為本週必要依賴。

### 授權與登入

模型頁目前標示 Llama 2 Community License。下載、研究使用與再散布前都應重新確認最新模型頁面及條款，不應把權重直接放進 Repository。

### 模型限制

- 可能描述不存在的物件或屬性。
- 可能受問題中的錯誤前提誘導。
- 小物件、文字辨識、遮擋與精確計數可能不可靠。
- 回答長度與自信語氣不是可信度指標。
- 研究紀錄需保存失敗案例，不能只選成功輸出。

## 8. 與 Week05 VLM Architecture 的銜接

Week04 用具體 LLaVA 推論建立以下主線：

```text
Processor
↓
Vision Encoder
↓
Projector
↓
Large Language Model
↓
Generated Answer
```

Week05 將把這條流程抽象成一般 VLM Architecture（視覺語言模型架構），比較不同模型如何完成視覺編碼、跨模態對齊、token 組合與文字生成。

本週尚未涵蓋：

- LLaVA 的完整訓練與 visual instruction tuning（視覺指令微調）。
- LoRA／QLoRA（低秩適應微調）實作。
- 多圖片、影片與 LLaVA-NeXT／OneVision 的架構細節。
- ROS2、Camera 與 NVIDIA Isaac Sim 6.0 的實際整合。
- VLM 回答到機器人動作的安全控制器。
