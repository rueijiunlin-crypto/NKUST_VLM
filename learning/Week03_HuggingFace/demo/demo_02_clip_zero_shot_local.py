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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    parser.add_argument(
        "--labels",
        nargs="+",
        default=DEFAULT_LABELS,
        help="候選文字 labels（標籤）或 prompts（提示詞）。請用引號提供一個或多個項目。",
    )
    parser.add_argument(
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

    image = Image.open(args.image).convert("RGB")

    print("正在載入 processor（前處理器）與 model（模型）。第一次執行可能會下載預訓練權重。")
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    model = CLIPModel.from_pretrained(MODEL_NAME)
    model.eval()

    labels = args.labels
    inputs = processor(
        text=labels,
        images=image,
        return_tensors="pt",
        padding=True,
    )

    with torch.inference_mode():
        outputs = model(**inputs)
        logits = outputs.logits_per_image
        probabilities = logits.softmax(dim=1)[0]

    top_k = min(args.top_k, len(labels))
    top_indices = probabilities.topk(top_k).indices.tolist()

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
