"""追蹤文字如何變成 Token ID，再查表取得 Embedding。"""

import numpy as np


SENTENCE = "a small robot sees a cup"
EMBEDDING_DIM = 4

def main() -> None:
    # 先切成 Token。這裡使用空白切分，只為了看清楚資料流。
    tokens = SENTENCE.lower().split()

    # 依首次出現順序建立詞彙表，讓重複 Token 共用同一個 ID。
    vocabulary: dict[str, int] = {} #建立一個空字典來存儲詞彙表
    for token in tokens:
        if token not in vocabulary: #如果token不在詞彙表中，就將其加入詞彙表，並分配一個新的ID，ID的值為當前詞彙表的長度（即已經有多少個不同的token）
            vocabulary[token] = len(vocabulary) #len用來取得物件的長度或元素個數，這裡用來取得當前詞彙表的長度，作為新token的ID

    token_ids = np.array([vocabulary[token] for token in tokens])

    # 每一列對應一個 Token ID；真實模型會在訓練中學習這些數值。
    embedding_table = np.arange( #建立一個數組，用於存儲嵌入向量
        len(vocabulary) * EMBEDDING_DIM, dtype=float #數組的大小為詞彙表的長度乘以嵌入維度，數據類型為浮點數
    ).reshape(len(vocabulary), EMBEDDING_DIM) #將數組重塑為一個矩陣，行數為詞彙表的長度，列數為嵌入維度
    embedding_table /= 10.0 #將數組中的每個元素除以10.0，這樣做是為了讓嵌入向量的值更小，更適合後續的矩陣運算

    # NumPy 使用 Token ID 當列索引，一次取出整段序列的向量。
    embeddings = embedding_table[token_ids] #使用token_ids作為索引從embedding_table中取出對應的嵌入向量，這樣可以一次性獲取整段序列的嵌入向量

    print("輸入文字:", SENTENCE)
    print("Tokens:", tokens)
    print("Vocabulary:", vocabulary)
    print("Token IDs:", token_ids)
    print("token_ids shape:", token_ids.shape)
    print("\nEmbedding table:")
    print(embedding_table)
    print("embedding_table shape:", embedding_table.shape)
    print("\nLookup result:")
    print(embeddings)
    print("embeddings shape:", embeddings.shape)
    print("\n為什麼這樣寫：Token ID 只負責查表，Embedding 才是後續矩陣運算使用的向量。")


if __name__ == "__main__":
    main()
