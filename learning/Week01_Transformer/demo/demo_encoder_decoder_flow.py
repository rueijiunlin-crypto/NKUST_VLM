"""
demo_encoder_decoder_flow.py

用簡化流程比較 Encoder（編碼器）與 Decoder（解碼器）。
本範例不建立真實神經網路，而是展示兩者在 VLM/VLA 任務中的角色差異。
"""


def run_encoder_flow() -> None:
    instruction = "go to the red door"
    representation = {
        "intent": "navigation",
        "target": "door",
        "attribute": "red",
    }

    print("Encoder mode:")
    print("-" * 42)
    print(f"input instruction: {instruction}")
    print(f"contextual representation: {representation}")
    print("possible use: retrieval / classification / image-text matching")
    print()


def run_decoder_flow() -> None:
    context = "robot sees a hallway and a red door"
    generated_steps = ["move", "toward", "the"]
    next_token = "red"
    action_description = "move toward the red door"

    print("Decoder mode:")
    print("-" * 42)
    print(f"context: {context}")
    print(f"generated tokens so far: {generated_steps}")
    print(f"next token: {next_token}")
    print(f"action description: {action_description}")
    print("possible use: question answering / captioning / action planning text")
    print()


def main() -> None:
    run_encoder_flow()
    run_decoder_flow()

    print("說明：")
    print("Encoder（編碼器）偏向把完整輸入轉成可比較、可檢索的表示。")
    print("Decoder（解碼器）偏向根據上下文逐步產生文字、回答或動作描述。")
    print("在 VLM/VLA 中，兩者分別支援圖文理解與行動輸出。")


if __name__ == "__main__":
    main()
