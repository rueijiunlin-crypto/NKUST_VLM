# Week10 Weekly Plan：Embodied AI + VLA Fundamentals

## 本週目標

- 區分 VLM 的語意輸出與 VLA 的動作輸出。
- 建立 Observation → Policy → Action → Robot → Observation 閉迴路。

## 必學概念

Embodied AI、Policy、Observation、Action Space／Representation、Joint／Cartesian／End-Effector／Gripper Action、Action Chunk、open-loop、closed-loop、Imitation Learning、Foundation Policy 與 Safety Boundary。

## 建議學習順序

1. 閱讀 `notes.md` 並比較 VLM 與 VLA。
2. 執行快速 Demo，觀察 action representation 與 action chunk。
3. 執行 Guided policy loop。
4. 完成小型 action validator Implementation Practice。

## Demo 執行順序

```powershell
python demo/demo_01_vlm_vs_vla.py
python demo/demo_02_action_chunk.py
python practice/coding/guided_demos/guided_policy_loop.py
python practice/coding/solutions/action_validator_solution.py
```

## 任務清單

- [ ] 閱讀本週文件並畫出 VLA closed-loop。
- [ ] 執行兩個 Demo 與 Guided Demo。
- [ ] 完成 Concept Practice。
- [ ] 完成 `action_validator_practice.py` 後再比較 solution。
- [ ] 在 `study_log.md` 記錄 safety boundary 與 failure case。

## Practice

- [Overview](./practice/README.md)
- [Concept](./practice/concept/concept_practice.md)
- [Coding](./practice/coding/coding_practice.md)
- [Guided Demos](./practice/coding/guided_demos/)
- [Coding Observation Key](./practice/coding/coding_observation_key.md)

模式：Guided 為主、少量 Implementation。

## Paper Reading（論文閱讀）

### Core Reading

- Title: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- Authors: Brianna Zitkovich et al.
- Year / Venue: 2023 / CoRL
- DOI: N/A
- arXiv: 2307.15818
- Link: https://proceedings.mlr.press/v229/zitkovich23a.html
- Code / Project: https://robotics-transformer2.github.io/
- Required Reading：Abstract、VLA co-fine-tuning、action tokenization、evaluation、limitations。
- Skim Reading：完整資料混合比例與附錄案例。
- Skip for Now：封閉模型的訓練重現。
- Optional Reading：OpenVLA；π0；GR00T N1。

### Reading Questions

1. RT-2 將哪個 VLM 問題改寫成 VLA 問題？
2. Observation、instruction、action 的輸入輸出為何？
3. Action 如何表示成 token？
4. Image tokens、language tokens、action tokens 的 shape 關係為何？
5. Co-fine-tuning 如何保留 web knowledge？
6. Action chunk 與單步 action 的差異是什麼？
7. Config、processor、policy 各負責什麼？
8. 使用哪些 seen／unseen 任務評估？
9. 哪項結果支持 emergent semantic reasoning？
10. Tokenization、latency 與 safety 的限制是什麼？
11. 真實 VLA 架構檢查要驗證哪些欄位？
12. 哪個比較維度適合放入 VLA 論文矩陣？

### Deep Reading

比較 RT-2、OpenVLA、SmolVLA、π0 與 GR00T N1 的 action representation、資料、模型規模、開放性與部署限制。

### Paper Reading Acceptance Criteria

- [ ] 能說明 Core Paper 的 Research Problem。
- [ ] 能用自己的話解釋 Architecture、Experiment 與主要資料流。
- [ ] 能指出至少一項 Claim、Evidence 與 Ablation。
- [ ] 能說明 Limitation、Boundary 與 Reproducibility 條件。
- [ ] 能完成 VLA 模型比較矩陣。

## 驗收條件

- [ ] 能區分 VLM output 與 VLA action。
- [ ] 能比較 joint／Cartesian action。
- [ ] 能解釋 action chunk、open／closed-loop。
- [ ] 能畫出 Observation → Policy → Action → Robot → Observation。
- [ ] 能說明 Safety Gate 不能只靠生成模型。

## 銜接 Week11

Week11 將說明 imitation policy 所需的 demonstrations 與 dataset schema。
