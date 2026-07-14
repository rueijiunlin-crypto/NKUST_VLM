"""引導式程式閱讀：比較串接、查詢壓縮與 cross-attention 的資料流。"""

from __future__ import annotations

import numpy as np


def main() -> None:
    image_tokens = np.array([[1.0, 0.0], [0.8, 0.2], [0.1, 0.9], [0.0, 1.0]])
    text_tokens = np.array([[0.6, 0.4], [0.2, 0.8]])
    query_weights = np.array([[0.6, 0.3, 0.1, 0.0], [0.0, 0.1, 0.3, 0.6]])
    query_tokens = query_weights @ image_tokens
    attention_scores = text_tokens @ image_tokens.T
    attention_weights = np.exp(attention_scores)
    attention_weights /= attention_weights.sum(axis=1, keepdims=True)
    cross_attended = attention_weights @ image_tokens

    print(f"image tokens              : {image_tokens.shape}")
    print(f"text tokens               : {text_tokens.shape}")
    print(f"concat sequence            : {(6, 2)}")
    print(f"query-compressed tokens    : {query_tokens.shape}")
    print("query values:\n", np.round(query_tokens, 3))
    print(f"cross-attention weights    : {attention_weights.shape}")
    print(np.round(attention_weights, 3))
    print(f"cross-attended text output : {cross_attended.shape}")
    print("\n三種融合策略的介面與成本不同，不能只看最後 shape 判斷優劣。")


if __name__ == "__main__":
    main()
