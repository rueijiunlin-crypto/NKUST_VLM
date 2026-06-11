"""用最小 Cross-Attention 追蹤 Encoder memory 如何被 Decoder 取用。"""

import numpy as np


def softmax(values: np.ndarray, axis: int = -1) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def main() -> None:
    source_tokens = ["red", "door", "ahead"]
    target_tokens = ["move", "toward"]

    # 將 Encoder 輸出視為 memory，每一列保存一個來源 Token 的上下文。
    encoder_memory = np.array(
        [
            [1.0, 0.0, 0.5],
            [0.8, 0.2, 0.5],
            [0.0, 1.0, 0.5],
        ]
    )

    # Decoder 目前有兩個位置，因此 Query 序列長度是 2。
    decoder_queries = np.array(
        [
            [0.2, 0.8, 0.5],
            [0.9, 0.1, 0.5],
        ]
    )

    # Cross-Attention：Q 來自 Decoder，K/V 來自 Encoder memory。
    scores = decoder_queries @ encoder_memory.T
    weights = softmax(scores / np.sqrt(encoder_memory.shape[-1]), axis=-1)
    decoder_context = weights @ encoder_memory

    print("Source tokens:", source_tokens)
    print("Target tokens:", target_tokens)
    print("\nEncoder memory:")
    print(encoder_memory)
    print("encoder_memory shape:", encoder_memory.shape)
    print("\nDecoder queries:")
    print(decoder_queries)
    print("decoder_queries shape:", decoder_queries.shape)
    print("\nCross-Attention scores:")
    print(np.round(scores, 4))
    print("scores shape:", scores.shape)
    print("\nCross-Attention weights:")
    print(np.round(weights, 4))
    print("weights shape:", weights.shape)
    print("row sums:", np.round(weights.sum(axis=-1), 4))
    print("\nDecoder context:")
    print(np.round(decoder_context, 4))
    print("decoder_context shape:", decoder_context.shape)

    for index, target in enumerate(target_tokens):
        source_index = int(np.argmax(weights[index]))
        print(f"Decoder '{target}' 最關注 Encoder '{source_tokens[source_index]}'")

    print("\n為什麼這樣寫：Decoder 用自己的 Query 選擇 Encoder memory 中與目前生成位置最相關的資訊。")


if __name__ == "__main__":
    main()
