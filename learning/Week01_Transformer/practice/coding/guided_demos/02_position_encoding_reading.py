"""觀察 Token Embedding 如何加入位置資訊。"""

import numpy as np


SEQUENCE_LENGTH = 3 #為了簡化示範，這裡使用固定的序列長度，實際應用中通常會根據輸入文本的長度動態調整
EMBEDDING_DIM = 4 #嵌入維度，這裡設定為4，實際應用中通常會使用更高的維度（如512或1024），以捕捉更多的語義信息


def sinusoidal_position_encoding(sequence_length: int, embedding_dim: int) -> np.ndarray: #實現正弦位置編碼的函數，接受序列長度和嵌入維度作為參數，返回一個包含位置編碼的 NumPy 數組
    positions = np.arange(sequence_length)[:, np.newaxis] #創建一個包含位置索引的數組，使用 np.arange 生成從0到序列長度-1的數字，並使用[:, np.newaxis]將其轉換為列向量，以便後續計算
    dimensions = np.arange(embedding_dim)[np.newaxis, :] #創建一個包含維度索引的數組，使用 np.arange 生成從0到嵌入維度-1的數字，並使用[np.newaxis, :]將其轉換為行向量，以便後續計算
    angle_rates = 1.0 / np.power(10000.0, 2 * (dimensions // 2) / embedding_dim) #計算角度速率，根據論文中的公式，使用嵌入維度的一半來計算正弦和餘弦的頻率，這樣可以確保不同維度的編碼具有不同的頻率
    angles = positions * angle_rates #計算位置編碼的角度，將位置索引與角度速率相乘，得到每個位置和維度對應的角度值

    encoding = np.zeros((sequence_length, embedding_dim)) #創建一個全零的數組，用於存儲最終的位置編碼，形狀為(序列長度, 嵌入維度)
    encoding[:, 0::2] = np.sin(angles[:, 0::2]) #對於偶數維度，使用正弦函數計算位置編碼，將角度值傳入 np.sin 函數，並將結果存儲在對應的偶數維度位置
    encoding[:, 1::2] = np.cos(angles[:, 1::2]) #對於奇數維度，使用餘弦函數計算位置編碼，將角度值傳入 np.cos 函數，並將結果存儲在對應的奇數維度位置
    return encoding #返回計算得到的位置編碼數組，這個數組包含了每個位置在不同維度上的編碼值，可以用於後續的模型訓練和推理


def main() -> None: #主函數，演示如何將位置編碼與 Token Embedding 結合使用，並觀察它們的形狀和內容
    # 使用相同內容向量，刻意凸顯「位置」造成的差異。
    token_embeddings = np.tile( #使用 np.tile 函數創建一個重複的數組，這裡將一個包含相同值的行向量重複多次，以模擬不同位置的 Token Embedding，這樣做是為了突出位置編碼對於區分相同內容的影響
        np.array([[0.5, 0.5, 0.5, 0.5]]), (SEQUENCE_LENGTH, 1) #將行向量重複 SEQUENCE_LENGTH 次，形成一個形狀為 (SEQUENCE_LENGTH, EMBEDDING_DIM) 的數組，每一行都是相同的 Token Embedding
    )
    position_encoding = sinusoidal_position_encoding( #調用之前定義的 sinusoidal_position_encoding 函數，生成位置編碼數組，這個數組的形狀為 (SEQUENCE_LENGTH, EMBEDDING_DIM)，每一行對應一個位置的編碼
        SEQUENCE_LENGTH, EMBEDDING_DIM #傳入序列長度和嵌入維度作為參數，生成對應的正弦位置編碼數組
    )

    # 兩者 shape 相同，因此可以逐元素相加且不改變輸出 shape。
    position_aware_embeddings = token_embeddings + position_encoding

    print("Token embeddings:")
    print(token_embeddings)
    print("token_embeddings shape:", token_embeddings.shape)
    print("\nPosition encoding:")
    print(np.round(position_encoding, 4))
    print("position_encoding shape:", position_encoding.shape)
    print("\nPosition-aware embeddings:")
    print(np.round(position_aware_embeddings, 4))
    print("output shape:", position_aware_embeddings.shape)
    print("\n為什麼這樣寫：Self-Attention 沒有天然順序感，相加的位置訊號讓相同內容可被區分。")


if __name__ == "__main__":
    main()
