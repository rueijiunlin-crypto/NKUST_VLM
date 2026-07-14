# Week06 教材筆記：VLM Paper Reading

## 1. 論文閱讀的目標

論文閱讀不是把摘要翻譯成中文，也不是記住所有模型名稱。研究閱讀要建立一條可追溯鏈：

```text
Research Problem
↓
Proposed Method
↓
Experimental Design
↓
Observed Evidence
↓
Supported Claim + Scope + Limitation
```

若無法指出主張由哪一張表、哪一個圖、哪一段方法或附錄支持，就還沒有完成證據閱讀。

本週核心來源：

- [CLIP 原始論文](https://arxiv.org/abs/2103.00020)
- [LLaVA 原始論文](https://arxiv.org/abs/2304.08485)

## 2. 三階段閱讀流程

### Pass 1：Orientation（方向定位）

閱讀 title、abstract、主要 figure、introduction 結尾、conclusion 與 limitation。產出：

- 一句研究問題。
- 一句方法摘要。
- 一句核心主張。
- 一張輸入到輸出的資料流草圖。
- 三個尚未理解的名詞或問題。

Pass 1 不做逐句翻譯，也不急著相信所有結果。

### Pass 2：Evidence（證據閱讀）

閱讀 method、training data、experiments、baselines、metrics、ablations 與 error analysis。產出 claim-to-evidence table（主張到證據表）。

### Pass 3：Reproduction（重現評估）

閱讀 implementation details（實作細節）、appendix（附錄）、model card（模型說明頁）、code 與 license（授權）。判斷：

- 資料與權重能否取得。
- 環境、硬體與超參數是否充分揭露。
- 評估是否可重做。
- 哪些結果只能部分重現。

### 對應 Demo

- `python demo/demo_01_reading_passes.py`
- 觀察：每個 pass 的閱讀位置與產物。
- 執行後應能回答：為什麼 Pass 1 完成不能宣稱已驗證論文主張？

## 3. 從架構圖還原方法

看到 Figure 時依序找：

1. Input（輸入）：圖片、文字、影片、指令或動作。
2. Pretrained components（預訓練元件）。
3. Frozen／trainable modules（凍結／可訓練模組）。
4. Connector 或 fusion（融合）位置。
5. Training objectives（訓練目標）。
6. Output（輸出）：embedding、score、text token 或 action。

架構圖通常會省略 batch、資料清理、tokenization、loss weighting、evaluation decoding 等細節，因此仍需回到 Method 與 Appendix。

### CLIP 架構閱讀

```text
Image → Image Encoder → image embedding ┐
                                        ├→ contrastive similarity matrix
Text  → Text Encoder  → text embedding  ┘
```

研究問題聚焦：能否從大規模自然語言監督學到可轉移的視覺表示？證據重點是跨多個 downstream datasets（下游資料集）的 zero-shot transfer（零樣本遷移）。

### LLaVA 架構閱讀

```text
Image → Vision Encoder → Projection ┐
                                    ├→ LLM → generated response
Instruction → text tokens          ┘
```

研究問題聚焦：如何用 visual instruction tuning（視覺指令微調）建立通用圖文對話能力？證據包含 instruction-following evaluation（指令遵循評估）、任務 benchmark（基準測試）與質化案例。

## 4. Claim-to-Evidence Mapping

每筆紀錄至少包含：

| 欄位 | 問題 |
| --- | --- |
| Claim | 作者主張什麼？ |
| Source location | 位於哪一節、圖、表或附錄？ |
| Evidence | 實際觀察到什麼結果？ |
| Comparison | 與什麼 baseline 比較？ |
| Scope | 結論只適用哪些資料與設定？ |
| Limitation | 哪些替代解釋尚未排除？ |

### 常見過度解讀

- 「某資料集分數較高」被改寫成「所有任務都更好」。
- 「trainable parameters 較少」被改寫成「推論一定更快」。
- 「展示幾張成功案例」被改寫成「模型可靠理解圖片」。
- 「作者未報告」被自行補成模型事實。

### 對應 Demo

- `python demo/demo_02_claim_evidence_map.py`
- 執行後應能回答：效率主張至少還需要哪些資源與效能證據？

## 5. 實驗與 Metric Context

一個分數至少要與以下欄位一起讀：

```text
dataset + split + metric + evaluation setting + baseline + uncertainty
```

### Dataset 與 Split

Validation、test、test-dev 或私有資料可能不能直接比較。也要確認模型是否在訓練資料看過相同或高度相似樣本。

### Evaluation Setting

- Zero-shot（零樣本）。
- Few-shot（少樣本）。
- Fine-tuned（微調）。
- Prompt ensemble（提示集成）。
- External tools／data（外部工具／資料）。

設定不同時，即使 metric 名稱相同也不能直接判定模型優劣。

### Ablation

Ablation 移除或替換元件，嘗試回答「改善來自哪裡」。有效 ablation 仍需控制資料、訓練步數、模型規模與評估流程。

### 對應 Demo

- `python demo/demo_03_metric_context.py`
- 執行後應能回答：為什麼 87 不一定優於 85？

## 6. 比較 CLIP 與 LLaVA

使用相同欄位比較：

| 欄位 | CLIP | LLaVA |
| --- | --- | --- |
| 問題 | 從自然語言監督學可轉移視覺表示 | 建立多模態指令遵循能力 |
| 輸入 | 大規模 image-text pairs | image-instruction-response data |
| 架構 | Image Encoder + Text Encoder | Vision Encoder + Projection + LLM |
| 對齊／訓練 | Contrastive learning | Visual instruction tuning |
| 輸出 | Shared embeddings／similarity | Generated text |
| 證據焦點 | 多資料集 zero-shot transfer | 多模態對話與任務評估 |
| 風險 | Dataset bias、prompt sensitivity | Hallucination、judge bias、資料生成品質 |

這不是勝負表。兩篇論文解決不同研究問題，不能用單一分數直接排名。

### 對應 Demo

- `python demo/demo_04_clip_llava_comparison.py`
- 執行後應能回答：兩篇論文為什麼需要不同評估證據？

## 7. 引用、改寫與推論邊界

研究筆記需清楚標記：

- Direct fact（直接事實）：論文明確寫出，附來源位置。
- Paraphrase（改寫）：用自己的話保留原意，仍需引用。
- Inference（推論）：由多項證據推導，明確標示「我推論」。
- Unknown（未知）：論文未報告或目前找不到。

不要把推論偽裝成作者結論。直接引用應短且必要，避免大量複製原文；筆記重點是理解與證據位置。

## 8. 與碩士研究的連結

每篇論文最後回答：

1. 它能支援我的哪一個研究問題？
2. 哪個方法元件可成為 baseline 或比較對象？
3. 哪個資料集或 metric 可借用？
4. 哪個限制形成研究 gap（缺口）？
5. 我的 ROS2、Camera 或 NVIDIA Isaac Sim 6.0 系統需要新增什麼驗證？

Paper Database 不應只有標題、年份與「已讀」。至少保存研究問題、方法、資料、證據、限制、可重現性與研究關聯。

## 本週尚未涵蓋

- Systematic review（系統性回顧）與 PRISMA 流程。
- Meta-analysis（統合分析）。
- 引用網路與文獻計量分析。
- 完整重現 CLIP 或 LLaVA 訓練。
