"""引導式程式閱讀：追蹤 logits、softmax probability 與 top-k prediction。"""

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="追蹤 CLIP logits 與 top-k prediction，作為 Week03 guided practice（引導式練習）。"
    )
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="候選文字 labels（標籤）或 prompts（提示詞）。請用引號提供一個或多個項目。",
    )
    parser.add_argument("--top-k", type=int, default=3, help="要印出的 top-k prediction（前 k 名預測）數量。")
    return parser.parse_args()


def main() -> int:
    try:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"缺少套件：{error.name}")
        print("請安裝依賴：python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"圖片路徑不存在：{args.image}")
        print("請使用本地圖片路徑，例如：--image demo/my_image.jpg")
        return 1

    print("[Step 1] 載入圖片、processor（前處理器）與 CLIPModel。")
    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    print("\n[Step 2] 使用一張圖片與候選 labels 建立模型輸入。")
    labels = args.labels
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    print("圖片數量：1")
    print(f"labels 數量：{len(labels)}")

    print("\n[Step 3] 執行 inference（推論），並觀察 logits_per_image。")
    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    print(f"logits_per_image shape: {tuple(logits.shape)}")
    print("預期 shape：(圖片數量, labels 數量)")

    print("\n[Step 4] 比較 logits（未正規化分數）與 softmax probability（softmax 機率分布）。")
    for label, logit, probability in zip(labels, logits[0].tolist(), probabilities.tolist()):
        print(f"- {label}: logit={logit:.4f}, probability={probability:.4f}")

    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()
    print(f"\n[Step 5] 從排序後的 probability 取得 Top-{top_k} prediction。")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. {labels[index]} ({probabilities[index].item():.4f})")

    print("\n[Observation 觀察]")
    print("- 改變 labels 數量會改變 logits_per_image 的第二個維度。")
    print("- Softmax probability 是相對於你提供的 labels 集合。")
    print("- Top-k 來自 probability 排序，不是另一個獨立的 model head（模型分類頭）。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
