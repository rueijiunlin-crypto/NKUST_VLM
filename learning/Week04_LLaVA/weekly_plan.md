# Week04 Weekly Plan：LLaVA + Grounded Visual Reasoning

## 本週目標

- 理解 Hugging Face LLaVA（大型語言與視覺助手）的完整推論流程。
- 能清楚區分 `AutoProcessor` 與 `LlavaForConditionalGeneration` 的分工。
- 能解讀圖片、文字、多模態序列與生成輸出的 tensor shape（張量形狀）。
- 能理解 Vision Encoder（視覺編碼器）、Projector（投影器）與 Large Language Model（大型語言模型，LLM）的資料流。
- 能設計問題比較實驗，分析回答是否具有影像依據。
- 能區分語意判斷、度量幾何、Robot State（機器人狀態）與 Action（動作）。
- 能說明單張 RGB 影像對機器人可達性與安全動作判斷的限制。

## 必學概念

- LLaVA 與 CLIP（對比式圖文預訓練）的任務差異。
- Processor（前處理器）、chat template（對話模板）與 `<image>` placeholder（影像占位符）。
- `input_ids`、`attention_mask`、`pixel_values` 與 batch dimension（批次維度）。
- Vision features（視覺特徵）、image tokens（影像詞元）與 hidden size（隱藏維度）。
- Autoregressive generation（自回歸生成）、`max_new_tokens` 與 decoding（解碼）。
- Prompt sensitivity（提示敏感性）、grounding（視覺依據）與 hallucination（幻覺）。
- Robot-Oriented Visual Reasoning（機器人導向視覺推理）與 capability boundary（能力邊界）。
- Supported／Uncertain／Contradicted／Requires Additional Sensor or Robot State。

## 建議學習順序

1. 閱讀 `README.md`，確認 Week04 主線與檔案用途。
2. 閱讀 `notes.md` 第 1–3 節，理解 Processor、模型分工與 tensor shape。
3. 執行 Demo 01，記錄 Processor 輸出的 keys、shape 與 dtype（資料型別）。
4. 執行 Demo 02，確認 Vision Encoder → Projector → LLM 的 shape 資料流。
5. 閱讀 `notes.md` 第 4–5 節，理解核心推論程式與文字生成。
6. 依序執行四個 Guided Demo，完成 shape tracing（張量形狀追蹤）與中間值觀察。
7. 閱讀 `notes.md` 第 6 節，完成一般與機器人導向問題比較。
8. 進入 Required Real Model Experiment：執行 Demo 03 與三個必要問題；受阻時完成環境檢查、指令與 blocker 紀錄。Demo 04 用於進階比較。
9. 完成 Concept Practice、Coding Practice 與 `study_log.md`。

## Demo 執行順序

請從 `learning/Week04_LLaVA` 執行：

```powershell
python -m pip install -r demo/requirements.txt
python demo/demo_01_llava_processor_inputs.py --image ../Week02_CLIP/demo/000000039769.jpg
python demo/demo_02_llava_architecture_flow.py
```

## Required Real Model Experiment

本軌是 Required Learning Track。若硬體、網路或模型存取不足，仍須完成環境檢查並在 `study_log.md` 記錄明確 blocker，不得略過。

```text
Image + Question
→ AutoProcessor
→ Real LLaVA Checkpoint
→ generate()
→ Generated Answer
→ Grounding Analysis
```

```powershell
python demo/demo_03_llava_visual_qa.py --revision <commit> --image ../Week02_CLIP/demo/000000039769.jpg --question "What objects are visible in this image?"
python demo/demo_03_llava_visual_qa.py --revision <commit> --image ../Week02_CLIP/demo/000000039769.jpg --question "Which visible objects could potentially be manipulated by a robot?"
python demo/demo_03_llava_visual_qa.py --revision <commit> --image ../Week02_CLIP/demo/000000039769.jpg --question "Can the exact 3D position be determined from this RGB image alone?"
python demo/demo_04_question_comparison.py --image ../Week02_CLIP/demo/000000039769.jpg
```

Demo03 是 Required；Demo04 用於三種問題的比較與 capability boundary 分析。記錄 model ID、revision、GPU、dtype、peak VRAM、load time、inference latency、generated token count、factual answer、hallucination、unsupported claim 與 uncertainty。

Demo 數量依本週必要概念設定，不受固定數量限制。每個 Demo 都必須對應 `notes.md` 中的概念與觀察問題。

## Practice 連結

- [Practice Overview](./practice/README.md)
- [Concept Practice](./practice/concept/concept_practice.md)
- [Coding Practice](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

參考答案請完成練習後再查看：

- [Concept Answer Key](./practice/concept/concept_answer_key.md)

本週 Coding Practice 採 Guided Code Reading Mode。程式提供完整可執行流程，學習者應閱讀逐步註解、追蹤 shape 與中間值，再修改小參數觀察變化。本週不使用 `exercises/`、`solutions/` 或 TODO 補空題。

## 任務清單

- [ ] 閱讀 `README.md`、`weekly_plan.md` 與 `notes.md`。
- [ ] 執行 Demo 01，記錄 Processor 輸出 shape。
- [ ] 執行 Demo 02，記錄架構資料流與 image token 數量。
- [ ] 完成四個 Guided Demo 的閱讀與觀察。
- [ ] 完成 Concept Practice。
- [ ] 完成 Coding Practice 的問題／提示實驗設計。
- [ ] 完成 Demo 03 Required Real Track；若無法執行，記錄標準 runtime blocker、環境與重現命令。
- [ ] 執行 Demo 04 進階比較，或完成比較設計與 blocker 紀錄。
- [ ] 記錄至少一個可能的 hallucination 或無法由圖片確認的主張。
- [ ] 比較 semantic relation（語意關係）與 metric coordinate（度量座標）。
- [ ] 對 robot reachability 主張標記其所需的額外感測與 Robot State。
- [ ] 在 `study_log.md` 記錄實際結果與未解問題。
- [ ] 更新 Notion 學習狀態。
- [ ] 進行 ChatGPT 驗收。

## Paper Reading（論文閱讀）

### Core Reading

- Title: Visual Instruction Tuning
- Authors: Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
- Year / Venue: 2023 / NeurIPS
- DOI: N/A
- arXiv: 2304.08485
- Link: https://papers.nips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html
- Code / Project: https://github.com/haotian-liu/LLaVA / https://llava-vl.github.io/
- Required Reading：Abstract、Figure 1、visual instruction data、architecture、evaluation。
- Skim Reading：完整 prompt 與附錄案例。
- Skip for Now：大規模訓練基礎設施細節。
- Optional Reading：LLaVA-1.5；LLaVA-NeXT。

### Reading Questions

1. Visual Instruction Tuning（視覺指令調校）解決什麼問題？
2. Vision Encoder、Projector、LLM 的輸入輸出為何？
3. Image tokens 如何進入語言模型？
4. Projector 前後的 shape 如何對齊？
5. 兩階段訓練各自更新哪些參數？
6. 指令資料如何產生，可能帶來什麼偏差？
7. Grounded reasoning 與一般 caption 有何不同？
8. 使用哪些基準與評審方式？
9. 哪項結果支持 instruction tuning 有效？
10. Hallucination（幻覺）與定位限制是什麼？
11. LLaVA 輸出如何安全轉成機器人語意事件？
12. 真實模型執行時要保存哪些重現資訊？

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Core Method 與主要資料流。
- [ ] 能指出至少一項 Claim 與對應 Evidence。
- [ ] 能說明至少一項 Limitation／Boundary。
- [ ] 能說明本論文與本週及後續研究的關聯。

## 驗收條件

- [ ] 能解釋 `AutoProcessor` 與模型的分工。
- [ ] 能看懂 `input_ids`、`attention_mask` 與 `pixel_values` 的 shape。
- [ ] 能說明 Vision Encoder、Projector、image tokens 與 LLM 的資料流。
- [ ] 能解釋 `<image>` placeholder 與多個 image embeddings（影像嵌入向量）的關係。
- [ ] 能比較 CLIP 相似度輸出與 LLaVA 生成式輸出。
- [ ] 能提出至少三種問題，說明各自要驗證的影像資訊。
- [ ] 能把回答拆成可由圖片支持、無法確認與明顯錯誤的主張。
- [ ] 能解釋為什麼單張 RGB VLM 不能直接提供 robot coordinate。
- [ ] 能解釋為什麼自然語言回答不能直接送給 motor controller（馬達控制器）。
- [ ] `study_log.md` 已由學生記錄實際觀察與尚未解決問題。

## 銜接 Week05 VLM Architecture

Week04 先用 LLaVA 建立一條可執行的 VLM（視覺語言模型）推論主線與能力邊界；Week05 將抽象成 VLM Architecture for Robotics（機器人視覺語言模型架構），加入 Robot State、Spatial Grounding（空間語意定位）、Structured Output（結構化輸出）與系統責任分界。
