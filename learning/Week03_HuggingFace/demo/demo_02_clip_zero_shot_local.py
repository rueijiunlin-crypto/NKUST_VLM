"""Run Hugging Face CLIP zero-shot image classification on a local image."""
#本程式碼定義了一個名為demo_02_clip_zero_shot_local.py的Python腳本，用於在本地圖像上運行Hugging Face CLIP零樣本圖像分類。
#腳本使用了argparse模塊來解析命令行參數，並使用了transformers庫中的CLIPModel和CLIPProcessor來處理圖像和文本輸入。
from __future__ import annotations

import argparse
from pathlib import Path


MODEL_NAME = "openai/clip-vit-base-patch32"
DEFAULT_LABELS = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a pink sofa",
    "a photo of a robot",
    "a photo of a laboratory",
]

#這段程式碼定義了一個名為parse_args的函數，用於解析命令行參數。
#該函數使用argparse模塊創建了一個ArgumentParser對象，並添加了三個參數：
#--image：這是一個必需的參數，指定本地圖像文件的路徑。它使用Path類型來確保輸入是一個有效的文件路徑。
#--labels：這是一個可選參數，允許用戶提供一個或多個文本標籤或提示，這些文本將與圖像進行比較。默認值是一個包含四個描述性文本的列表。
#--top-k：這是一個可選參數，指定要打印的最高得分標籤的數量。默認值為3。
#函數最後返回解析後的命令行參數作為argparse.Namespace對象。
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="Path to the local image file.")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="Candidate labels or prompts. CLIP compares the image against these texts.",
    )
    parser.add_argument("--top-k", type=int, default=3, help="Number of highest-scoring labels to print.")
    return parser.parse_args()


def main() -> int:
    try:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"Missing dependency: {error.name}")
        print("Install with: python -m pip install -r demo/requirements.txt")
        return 1
    #這段程式碼定義了一個名為main的函數，該函數首先嘗試導入torch庫、PIL庫中的Image模塊和transformers庫中的CLIPModel和CLIPProcessor模塊。
    #如果這些模塊未安裝，則會捕獲ImportError異常並打印錯誤信息，提示用戶安裝缺失的依賴項。
    #接著，函數調用parse_args()來解析命令行參數，并檢查指定的圖像文件是否存在。
    #如果圖像文件不存在，則打印錯誤信息並返回1。
    args = parse_args()
    if not args.image.is_file():
        print(f"Image file not found: {args.image}")
        print("Try the Week02 demo image or pass another local image with --image.")
        return 1
    if args.top_k < 1:
        print("--top-k must be at least 1.")
        return 1
    #如果圖像文件存在，則使用PIL庫中的Image模塊打開圖像文件並將其轉換為RGB格式。
    #接著，從命令行參數中獲取文本標籤列表。
    image = Image.open(args.image).convert("RGB")
    labels = args.labels
    
    #然後，使用CLIPProcessor從預訓練模型中加載處理器，並將文本標籤和圖像作為輸入傳遞給處理器。
    #處理器將返回一個包含處理後的張量的字典
    print("Loading CLIPProcessor and CLIPModel...")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()
    
    #最後，打印模型名稱、圖像路徑、文本標籤列表以及處理器輸出的張量的形狀和數據類型。
    #還提供了如何解讀這些張量形狀的說明。
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    
    #使用torch.inference_mode()來禁用梯度計算，這樣可以節省內存並加快推理速度。接著，將處理器輸出的張量作為輸入傳遞給模型，獲取模型的輸出。
    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    #使用topk()方法獲取概率最高的前k個標籤的索引，這裡k由命令行參數--top-k指定。然后，打印模型名稱、圖像路徑、文本標籤列表以及處理器輸出的張量的形狀和數據類型。
    #還提供了如何解讀這些張量形狀的說明。
    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()

    print(f"Model: {MODEL_NAME}")
    print(f"Image: {args.image}")
    print("\nTensor shapes:")
    print(f"- input_ids: {tuple(inputs['input_ids'].shape)}")
    print(f"- attention_mask: {tuple(inputs['attention_mask'].shape)}")
    print(f"- pixel_values: {tuple(inputs['pixel_values'].shape)}")
    print(f"- logits_per_image: {tuple(logits.shape)}")
    print(f"- probabilities for image 0: {tuple(probabilities.shape)}")

    print("\nLabels and probabilities:")
    for index, (label, probability) in enumerate(zip(labels, probabilities.tolist())):
        print(f"{index}: {label} -> {probability:.4f}")

    print(f"\nTop-{top_k} predictions:")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. label[{index}] {labels[index]} ({probabilities[index].item():.4f})")

    print("\nNotes:")
    print("- logits_per_image has shape [num_images, num_texts].")
    print("- softmax(dim=1) normalizes across the candidate text labels for each image.")
    print("- topk().indices returns label indices, so we use labels[index] for the text.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
