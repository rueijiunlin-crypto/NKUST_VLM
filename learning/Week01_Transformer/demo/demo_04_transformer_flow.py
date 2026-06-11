"""快速展示 Transformer Encoder 與 Decoder 的角色。"""


def main() -> None:
    instruction = "go to the red door"
    encoder_context = {
        "intent": "navigation",
        "target": "door",
        "attribute": "red",
    }
    generated_tokens = ["move", "toward", "the", "red", "door"]

    print("Input:", instruction)
    print("Encoder context:", encoder_context)
    print("Decoder output:", " ".join(generated_tokens))
    print("\n觀察：Encoder 把輸入整理成上下文表示，Decoder 根據上下文逐步產生輸出。")
    print("在 VLM 中，類似流程可連接文字指令、影像資訊與文字回答。")


if __name__ == "__main__":
    main()
