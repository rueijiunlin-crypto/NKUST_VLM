"""比較不同 prompt sets 如何影響 CLIP zero-shot 預測結果。"""
#這段程式碼定義了一個名為demo_03_prompt_comparison.py的Python腳本，用於比較不同提示集如何改變CLIP零樣本圖像分類的預測結果。
#腳本使用了argparse模塊來解析命令行參數，並使用了transformers庫中的CLIPModel和CLIPProcessor來處理圖像和文本輸入。
#腳本定義了三個不同的提示集，並將它們與同一張圖像進行比較，以觀察不同提示如何影響模型的預測結果。
from __future__ import annotations

import argparse
from pathlib import Path

#定義了模型名稱和三個不同的提示集，這些提示集將用於比較CLIP模型在不同文本描述下的預測結果。
MODEL_NAME = "openai/clip-vit-base-patch32"
PROMPT_SETS = {
    "object_only": [
        "cat",
        "dog",
        "sofa",
        "robot",
        "laboratory",
    ],
    "photo_template": [
        "a photo of a cat",
        "a photo of a dog",
        "a photo of a sofa",
        "a photo of a robot",
        "a photo of a laboratory",
    ],
    "scene_aware": [
        "a photo of two cats on a pink sofa",
        "a photo of a dog on a sofa",
        "a photo of a pink sofa without animals",
        "a photo of a robot in a laboratory",
        "a photo of a laboratory room",
    ],
}

#這段程式碼定義了一個名為parse_args的函數，用於解析命令行參數。該函數使用argparse模塊創建了一個ArgumentParser對象，並添加了兩個參數：
#--image：這是一個必需的參數，指定本地圖像文件的路徑。它使用Path類型來確保輸入是一個有效的文件路徑。
#--top-k：這是一個可選參數，指定要打印的每個提示集的最高得分標籤的數量。默認值為3。
#函數最後返回解析後的命令行參數作為argparse.Namespace對象。
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument("--top-k", type=int, default=3, help="每組 prompt set 要輸出的預測數量。")
    return parser.parse_args()

#這段程式碼定義了一個名為run_prompt_set的函數，用於運行CLIP模型對給定圖像和提示集進行推理。該函數接受處理器、模型、圖像、提示集名稱、提示列表和top_k作為參數。
#函數首先使用處理器將文本提示和圖像轉換為模型可接受的格式，然後使用torch.inference_mode()來禁用梯度計算，這樣可以節省內存並加快推理速度。
#接著，將處理器輸出的張量作為輸入傳遞給模型，獲取模型的輸出。
#模型的輸出包含每個提示對圖像的logits，然後使用softmax函數將logits轉換為概率。
#接著，使用topk()方法獲取概率最高的前k個標籤的索引，這裡k由命令行參數--top-k指定。最后，打印提示集名稱、logits的形狀以及每個提示對應的概率，並列出top-k的提示和它們的概率。
def run_prompt_set(processor, model, image, prompt_set_name: str, labels: list[str], top_k: int) -> None:
    import torch

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    safe_top_k = min(top_k, len(labels))
    top_indices = probabilities.topk(safe_top_k).indices.tolist()

    print(f"\nPrompt set（提示組）：{prompt_set_name}")
    print(f"logits_per_image shape: {tuple(logits.shape)}")
    for index, (label, probability) in enumerate(zip(labels, probabilities.tolist())):
        print(f"{index}: {label} -> {probability:.4f}")

    print(f"Top-{safe_top_k}：")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. label[{index}] {labels[index]} ({probabilities[index].item():.4f})")

#這段程式碼定義了一個名為main的函數，該函數首先嘗試導入PIL庫中的Image模塊和transformers庫中的CLIPModel和CLIPProcessor模塊。
#如果這些模塊未安裝，則會捕獲ImportError異常並打印錯誤信息，提示用戶安裝缺失的依賴項。
#接著，函數調用parse_args()來解析命令行參數，并檢查指定的圖像文件是否存在。
#如果圖像文件不存在，則打印錯誤信息並返回1。
def main() -> int:
    try:
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"缺少必要套件：{error.name}")
        print("請安裝：python -m pip install -r demo/requirements.txt")
        return 1
    
    #如果圖像文件存在，則使用PIL庫中的Image模塊打開圖像文件並將其轉換為RGB格式。
    #接著，從命令行參數中獲取文本標籤列表。
    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        print("請改用 Week02 demo 圖片，或用 --image 指定另一張本機圖片。")
        return 1
    #如果top-k的值小於1，則打印錯誤信息並返回1，因為top-k必須至少為1才能獲取至少一個最高得分的標籤。
    if args.top_k < 1:
        print("--top-k 必須至少為 1。")
        return 1
    #如果圖像文件存在，則使用PIL庫中的Image模塊打開圖像文件並將其轉換為RGB格式。
    image = Image.open(args.image).convert("RGB")
    #接著，從命令行參數中獲取文本標籤列表。
    #然後，使用CLIPProcessor從預訓練模型中加載處理器，並將文本標籤和圖像作為輸入傳遞給處理器。
    #處理器將返回一個包含處理後的張量的字典。
    #最後，打印模型名稱、圖像路徑、文本標籤列表以及處理器輸出的張量的形狀和數據類型。
    #還提供了如何解讀這些張量形狀的說明。
    print("正在載入 CLIPProcessor 與 CLIPModel...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()
    print(f"模型：{MODEL_NAME}")
    print(f"圖片：{args.image}")
    #然後，對於PROMPT_SETS字典中的每個提示集，調用run_prompt_set函數來運行CLIP模型並打印結果。
    #最後，打印一些關於提示集和概率分布的說明。
    for prompt_set_name, labels in PROMPT_SETS.items():
        run_prompt_set(processor, model, image, prompt_set_name, labels, args.top_k)

    print("\n觀察重點：")
    print("- 每一組 prompt set 都會建立不同的候選 label 空間。")
    print("- Softmax probabilities 是該 prompt set 內部的相對分布。")
    print("- 請比較 top-1 是否改變，以及分布是否更集中或更分散。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
