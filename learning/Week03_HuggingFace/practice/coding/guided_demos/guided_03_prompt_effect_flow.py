"""引導式程式閱讀：比較 prompt wording 如何改變 CLIP predictions。"""

from __future__ import annotations

import argparse
from pathlib import Path


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="比較 prompt sets（提示詞集合），作為 Week03 CLIP guided practice（引導式練習）。"
    )
    parser.add_argument("--image", type=Path, required=True, help="本地圖片路徑。")
    return parser.parse_args()


def run_prompt_set(processor, model, image, prompt_set_name: str, labels: list[str]) -> None:
    import torch

    print(f"\n[Prompt set 提示詞集合] {prompt_set_name}")
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    with torch.inference_mode():
        outputs = model(**inputs)
        probabilities = outputs.logits_per_image.softmax(dim=1)[0]

    top_index = int(probabilities.argmax())
    for label, probability in zip(labels, probabilities.tolist()):
        print(f"- {label}: probability={probability:.4f}")
    print(f"Top-1（第一名預測）：{labels[top_index]} ({probabilities[top_index].item():.4f})")


def main() -> int:
    try:
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

    print("\n[Step 2] 將同一張圖片搭配不同 prompt sets 執行推論。")
    for prompt_set_name, labels in PROMPT_SETS.items():
        run_prompt_set(processor, model, image, prompt_set_name, labels)

    print("\n[Observation 觀察]")
    print("- CLIP 會比較圖片與你提供的確切 text prompts（文字提示詞）。")
    print("- 簡短 object labels（物件標籤）與完整句子 prompts 可能產生不同 text embeddings（文字嵌入向量）。")
    print("- Scene-aware prompts（場景感知提示詞）可能更適合描述有多物件或脈絡的圖片。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
