"""觀察表示如何拆成多個 head，再合併回 d_model。"""

import numpy as np


NUM_HEADS = 2


def softmax(values: np.ndarray, axis: int = -1) -> np.ndarray:
    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def split_heads(values: np.ndarray, num_heads: int) -> np.ndarray:
    sequence_length, d_model = values.shape
    if d_model % num_heads != 0:
        raise ValueError("d_model 必須可被 num_heads 整除")
    head_dim = d_model // num_heads
    return values.reshape(sequence_length, num_heads, head_dim).transpose(1, 0, 2)


def combine_heads(values: np.ndarray) -> np.ndarray:
    num_heads, sequence_length, head_dim = values.shape
    return values.transpose(1, 0, 2).reshape(sequence_length, num_heads * head_dim)


def main() -> None:
    x = np.array(
        [
            [1.0, 0.0, 0.5, 0.5],
            [0.8, 0.2, 0.4, 0.6],
            [0.0, 1.0, 0.7, 0.3],
        ]
    )

    heads = split_heads(x, NUM_HEADS)

    # 每個 head 都在自己的子空間做 Self-Attention。
    head_dim = heads.shape[-1]
    head_scores = heads @ heads.transpose(0, 2, 1) / np.sqrt(head_dim)
    head_weights = softmax(head_scores, axis=-1)
    head_outputs = head_weights @ heads
    combined = combine_heads(head_outputs)

    print("Input X:")
    print(x)
    print("X shape:", x.shape)
    print("NUM_HEADS:", NUM_HEADS)
    print("head_dim:", x.shape[-1] // NUM_HEADS)
    print("\nSplit heads:")
    print(heads)
    print("heads shape:", heads.shape)

    for head_index, head in enumerate(heads):
        print(f"\nHead {head_index} shape:", head.shape)
        print(head)
        print(f"Head {head_index} attention weights:")
        print(np.round(head_weights[head_index], 4))
        print("row sums:", np.round(head_weights[head_index].sum(axis=-1), 4))
        print(f"Head {head_index} output:")
        print(np.round(head_outputs[head_index], 4))

    print("\nCombined output:")
    print(np.round(combined, 4))
    print("combined shape:", combined.shape)
    print("\n為什麼這樣寫：每個 head 在較小子空間獨立計算關係，再把多個觀察結果合併回共同表示空間。")


if __name__ == "__main__":
    main()
