# Week16 Notes：Research Prototype and Evaluation

## Why：從教材到可辯護研究

研究原型不是把 Week01–15 全部串起來，而是用最小系統回答一個明確問題。Research Question（研究問題）要指出自變因、依變因、情境與邊界；Hypothesis（假設）必須能被 evidence 支持或反駁。

## Integrated Pipeline

```text
image / video + timestamp
→ VLM perception / grounding
→ multimodal observation schema
→ VLA policy or baseline
→ action validator / safety gate
→ log-only, simulation, or approved controller
→ metric + failure recorder
→ reproducible artifact
```

每個箭頭都有 interface contract：input/output shape、dtype、unit、frame、timestamp、revision、validity。Prototype 可停在 log-only 或 simulation；研究價值來自問題與證據，不來自是否真的驅動硬體。

## Baseline、Proposed Method 與 Controls

Baseline 必須合理且可重現。比較時固定 dataset split、test cases、model/data revision、prompt、hardware、seed、action convention 與 safety threshold。Proposed method 只改研究變因；若一次改 model、data、prompt 與 latency pipeline，就無法歸因。

## Evaluation Design

- Perception：grounding accuracy、event recall、hallucination/unknown rate。
- System：latency p50/p95/p99、throughput、memory、drop/stale rate。
- Policy：offline action error、task success、replan count。
- Safety：rejection、limit violation、timeout、operator intervention。
- Robustness：lighting、occlusion、missing state、domain shift、seed variance。

Ground truth 的產生方式、標註者、版本與 uncertainty 必須公開。Success rate 需同時報樣本數與 confidence interval；不能只給百分比。

## Test Matrix 與 Failure Taxonomy

Test cases 至少涵蓋 nominal、boundary、missing/stale modality、domain shift 與 safety rejection。Failure 依 perception、grounding、synchronization、policy、validator、controller、simulation/real gap 分類，保存 raw input、raw output、timestamp 與 revision，避免只截成功畫面。

## Ablation 與 Evidence Chain

Ablation 一次移除或替換一個設計，回答它是否真的造成改善。論證鏈應為：

```text
paper claim
→ research gap
→ hypothesis
→ controlled implementation
→ metric evidence
→ failure / limitation
→ bounded conclusion
```

## Reproducibility Package

保存 Git revision、environment lock、model/dataset revision、license、config、seed、hardware、raw results、metric script、logs、failure cases 與 README。大型權重不直接加入 repository；記錄官方來源、checksum 或 immutable revision、cache 與取得條件。

## Limitation 與 Conclusion

Conclusion 只能涵蓋實際測試的 model、dataset、hardware 與情境。未執行的真實模型、Isaac 或硬體軌標為 `Not validated yet`；prototype completed 也不等於學生學習項目完成。

## Paper Mapping 與 Thesis Usage

- Core Paper：OpenVLA，作為開源 VLA 系統、資料與 evaluation 的深讀案例。
- 研究題目確定後，另選最接近的 baseline paper 與反例 paper。
- 完成 Evidence Table、Comparison Matrix、Reproducibility Check，轉寫成 proposal 的 Related Work 與 Method justification。

## 驗收邊界

驗收包含可執行性、schema、metric、failure evidence、reproducibility 與 safety boundary；不以單一成功 Demo 取代實驗。
