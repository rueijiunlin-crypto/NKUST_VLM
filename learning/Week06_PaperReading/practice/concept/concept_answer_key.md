# Week06 Concept Answer Key

> 請先完成 `concept_practice.md`，再查看本參考答案。

## 1. 三階段閱讀

Pass 1 定位問題、方法與主張；Pass 2 對照方法、資料、實驗與證據；Pass 3 檢查實作、附錄、資源、授權與重現條件。三者產物分別是方向摘要、claim-evidence 表與重現／風險清單。

## 2. Research Problem 與 Topic

Topic 沒有比較條件與可觀察結果。例如：「不同提示格式如何影響室內語意目標 grounding accuracy，且錯誤是否隨視角改變？」才較接近可驗證問題。

## 3. Claim-to-Evidence

至少記錄 claim、source location、evidence、comparison、scope 與 limitation。Scope 防止過度推廣，limitation 保留尚未排除的替代解釋。

## 4. Metric Context

不能直接比較，因 test／validation split 與 zero-shot／fine-tuned setting 不同。必須在相同資料、split、metric 與設定下才有合理直接比較基礎。

## 5. Ablation

Ablation 嘗試隔離元件貢獻。若同時改變資料量，就有 confounder（混淆因素），結果不能單獨歸因於 connector。

## 6. CLIP 與 LLaVA

CLIP 聚焦自然語言監督下的可轉移視覺表示，以雙編碼器與 contrastive objective 產生相似度；LLaVA 聚焦多模態指令遵循，以 vision encoder、projection 與 LLM 生成回答。兩者任務不同，因此證據設計也不同。

## 7. 引用與推論

Direct fact 是來源明示內容；Paraphrase 是保留原意的改寫；Inference 是讀者由證據推導的判斷；Unknown 是未報告或尚未查明。分開標記可避免把自己的推論誤寫成作者結論。

## 8. 可重現性

可檢查資料來源與 split、模型與 revision、程式與套件環境、硬體、超參數、random seed、訓練／推論流程、解碼設定與完整評估方法。重點是他人能否重建相同條件。
