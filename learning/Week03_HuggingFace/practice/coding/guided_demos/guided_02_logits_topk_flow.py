"""引導式程式閱讀：追蹤 CLIP logits、softmax probabilities 與 top-k 索引。"""

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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本機圖片檔案路徑。")
    parser.add_argument("--labels", nargs="+", default=DEFAULT_LABELS, help="候選 labels 或 prompts。")
    parser.add_argument("--top-k", type=int, default=3, help="要觀察的最高分預測數量。")
    return parser.parse_args()


def main() -> int:
    try:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
    except ImportError as error:
        print(f"缺少必要套件：{error.name}")
        print("請安裝：python -m pip install -r practice/coding/requirements.txt")
        return 1

    args = parse_args()
    if not args.image.is_file():
        print(f"找不到圖片檔案：{args.image}")
        return 1
    if args.top_k < 1:
        print("--top-k 必須至少為 1。")
        return 1

    print("[步驟 1] 載入圖片、processor 與 model")
    image = Image.open(args.image).convert("RGB")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    print("\n[步驟 2] 建立模型輸入")
    labels = args.labels
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    print(f"labels 數量：{len(labels)}")
    print(f"input_ids shape: {tuple(inputs['input_ids'].shape)}")
    print(f"attention_mask shape: {tuple(inputs['attention_mask'].shape)}")
    print(f"pixel_values shape: {tuple(inputs['pixel_values'].shape)}")

    print("\n[步驟 3] 在不記錄梯度的情況下執行推論")
    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    print(f"logits_per_image shape: {tuple(logits.shape)}")
    print(f"使用 [0] 取出第 0 張圖片後的 probabilities shape: {tuple(probabilities.shape)}")

    print("\n[步驟 4] 比較 logits 與 probabilities")
    for index, (label, logit, probability) in enumerate(zip(labels, logits[0].tolist(), probabilities.tolist())):
        print(f"{index}: {label} | logit={logit:.4f} | probability={probability:.4f}")

    print("\n[步驟 5] 觀察 top-k indices")
    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()
    print(f"使用者要求 top_k={args.top_k}，實際安全 top_k={top_k}")
    print(f"top indices（前 k 名索引）: {top_indices}")
    for rank, index in enumerate(top_indices, start=1):
        print(f"{rank}. labels[{index}] = {labels[index]} ({probabilities[index].item():.4f})")

    print("\n觀察問題：")
    print("- 為什麼 logits_per_image 使用 [num_images, num_texts]？")
    print("- 為什麼 softmax 要使用 dim=1？")
    print("- 為什麼 top-k 結果需要透過索引找回 label 文字？")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
