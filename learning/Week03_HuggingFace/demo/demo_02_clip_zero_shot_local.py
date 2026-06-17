"""使用 Hugging Face CLIP 對本地圖片執行 zero-shot classification。"""

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


def parse_args() -> argparse.Namespace: #parse_args 函式用來解析命令列參數，預期接收一個 --image 參數，指定本地圖片的路徑。
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="候選文字 labels（標籤）或 prompts（提示詞）。請用引號提供一個或多個項目。",
    )
    parser.add_argument( #--top-k 參數用來指定要印出的 top-k prediction（前 k 名預測）數量，預設值為 3。這個參數會影響最後輸出的預測結果的數量，讓使用者可以選擇只查看最有可能的幾個預測，而不是全部的候選標籤。
        "--top-k",
        type=int,
        default=3,
        help="要印出的 top-k prediction（前 k 名預測）數量。",
    )
    return parser.parse_args()


def main() -> int:
    try:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}")
        print("請安裝依賴：python -m pip install -r demo/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"圖片路徑不存在：{args.image}")
        print("若 Week02 範例圖片不存在，請改用自己的本地圖片路徑。")
        return 1

    image = Image.open(args.image).convert("RGB") #使用 PIL 庫打開指定路徑的圖片，並將其轉換為 RGB 模式。這是因為 CLIP 模型期望輸入的圖像是 RGB 格式的，如果圖片是其他格式（如 RGBA 或灰階），可能會導致處理錯誤或不正確的預測結果。

    print("正在載入 processor（前處理器）與 model（模型）。第一次執行可能會下載預訓練權重。")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    labels = args.labels
    inputs = processor(
        text=labels,
        images=image,
        return_tensors="pt", #return_tensors 參數指定輸出格式為 PyTorch 張量（"pt"）。這意味著 processor 會將處理後的圖像和文本數據轉換為 PyTorch 張量，方便直接輸入到 CLIPModel 中進行推理。
        padding=True,
    )

    with torch.inference_mode(): #torch.inference_mode()推論模式是 PyTorch 中的一個上下文管理器，用於在推理階段禁用梯度計算。這樣可以節省內存和計算資源，因為在推理過程中不需要進行反向傳播或更新模型權重。使用 torch.inference_mode() 可以提高推理效率，特別是在處理大型模型或批量輸入時。
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0] #softmax(dim=1)[0] 是把第 1 張圖片對所有 labels 的分數轉成相對機率。
        '''在不計算梯度的推論模式下，
           把圖片與文字輸入 CLIPModel，
           取得圖片對每個文字 label 的原始相似度分數，
           再把這些分數轉成相對機率，
           最後取出第 1 張圖片的分類結果。'''

    top_k = min(args.top_k, len(labels)) #確保 top_k 不超過候選標籤的數量，避免出現索引錯誤。
    top_indices = probabilities.topk(top_k).indices.tolist() #probabilities.topk(top_k).indices 會返回機率分布中前 top_k 大的索引，這些索引對應於 labels 中的候選標籤。tolist() 是把 PyTorch tensor（PyTorch 張量）轉成 Python list（Python 串列）。
    '''先確認要取的前 k 名數量不會超過 labels 數量。
       接著從 probabilities 裡找出機率最高的前 k 個位置。
       最後把這些位置轉成 Python list，方便後續印出 label 與機率。'''    
    print(f"模型：{MODEL_NAME}")
    print(f"圖片路徑：{args.image}")
    print(f"logits_per_image shape: {tuple(logits.shape)}")
    print("\nLabels（標籤）與 probabilities（機率分布）：")
    for label, probability in zip(labels, probabilities.tolist()):
        print(f"- {label}: {probability:.4f}")

    print(f"\nTop-{top_k} predictions（前 {top_k} 名預測）：")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {labels[index]} ({probabilities[index].item():.4f})")

    print("\n解讀：")
    print("- logits_per_image 是每個 image-label pair（圖片與標籤配對）的原始分數。")
    print("- softmax 會把分數轉成目前 labels 之間的相對分布。")
    print("- 結果會受到你提供的候選 labels 影響。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
