"""快速比較四種常見 Vision-Language Model 架構家族。"""

from __future__ import annotations


ARCHITECTURES = [
    ("Dual Encoder", "Image Encoder + Text Encoder", "similarity", "CLIP"),
    ("Projector-based", "Vision Encoder + Projector + LLM", "generated text", "LLaVA"),
    ("Query-based", "Vision Encoder + Query Connector + LLM", "generated text", "BLIP-2"),
    ("Cross-Attention", "Vision Encoder + Cross-Attention + LM", "generated text", "Flamingo"),
]


def main() -> None:
    print(f"{'Family':18} {'Core components':42} {'Output':16} Example")
    print("-" * 95)
    for family, components, output, example in ARCHITECTURES:
        print(f"{family:18} {components:42} {output:16} {example}")
    print("\n觀察：不是所有 VLM 都把圖片 token 直接串到 LLM 前面。")
    print("架構選擇會改變輸出型態、訓練方式、序列成本與可用任務。")


if __name__ == "__main__":
    main()
