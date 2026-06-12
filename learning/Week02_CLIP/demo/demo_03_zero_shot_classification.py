"""使用固定假向量展示零樣本分類的分數、機率與 top-1。"""

import numpy as np


LABELS = [
    "a photo of a robot",
    "a photo of a dog",
    "a photo of a red apple",
    "a photo of a laboratory",
    "a photo of a chair",
]


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.linalg.norm(vectors, axis=-1, keepdims=True)


def softmax(values: np.ndarray) -> np.ndarray: #np.ndarray是一種多維數組對象，提供了高效的數據存儲和操作功能。這裡的values參數是一個一維或多維的數組，表示需要進行softmax計算的輸入值。
    #softmax函數是一種常用的激活函數，將一組實數轉換為概率分布，使得輸出值在0和1之間，且總和為1。這裡的實現使用了數值穩定的技巧，即先將輸入值減去最大值，以避免指數運算中的溢出問題。
    shifted = values - np.max(values) #shifted是將輸入值values減去其最大值的結果，這樣做是為了提高數值穩定性，避免在計算指數時出現溢出問題。np.max(values)會返回values中的最大值，然後將其從每個元素中減去，得到shifted數組。這樣可以確保在計算指數時不會出現過大的數值，從而避免溢出。
    exponentials = np.exp(shifted) #exponentials是對shifted數組中的每個元素計算指數的結果。np.exp(shifted)會返回一個新的數組，其中每個元素都是shifted數組中對應元素的指數值。這是softmax函數的一部分，用於將輸入值轉換為概率分布。
    return exponentials / exponentials.sum()


def main() -> None:
    image_embedding = np.array([[0.90, 0.10, 0.30, 0.20]])
    text_embeddings = np.array(
        [
            [0.88, 0.12, 0.28, 0.22],
            [0.10, 0.90, 0.20, 0.10],
            [0.20, 0.15, 0.90, 0.10],
            [0.45, 0.20, 0.30, 0.80],
            [0.20, 0.30, 0.10, 0.85],
        ]
    )

    similarities = (normalize(image_embedding) @ normalize(text_embeddings).T)[0] 
    #normalize(image_embedding)是對image_embedding進行歸一化處理，將其轉換為單位向量。
    #normalize(text_embeddings)是對text_embeddings中的每個文本嵌入向量進行歸一化處理，將它們轉換為單位向量。然後，使用矩陣乘法（@）將歸一化的圖像嵌入與轉置的歸一化文本嵌入相乘，得到相似度分數矩陣。最後，[0]是從相似度分數矩陣中提取第一行，即圖像與每個文本的相似度分數。
    # similarities是圖像嵌入與每個文本嵌入之間的相似度分數，這些分數表示圖像與每個文本的相似程度，值越接近1表示越相似，值越接近-1表示越不相似，值為0表示兩者垂直。
    
    probabilities = softmax(similarities * 10.0) 
    #將相似度分數乘以10.0是為了放大分數的差異，使得softmax函數能夠更明顯地區分不同文本的相似度。這樣做可以使得最相似的文本獲得更高的概率，而不太相似的文本獲得更低的概率，從而提高分類的準確性。
    #probabilities是對相似度分數進行softmax轉換後得到的概率分布，表示圖像與每個文本的相似度在所有文本中的相對概率。這些概率值在0和1之間，且總和為1，表示圖像與每個文本的相似程度的概率分布。

    print("Zero-shot classification")
    for label, score, probability in zip(LABELS, similarities, probabilities):
        print(f"- {label}")
        print(f"  similarity score: {score:.4f}")
        print(f"  probability: {probability:.4f}")

    best_index = int(np.argmax(probabilities))
    print("\nTop-1 prediction:", LABELS[best_index])


if __name__ == "__main__":
    main()
