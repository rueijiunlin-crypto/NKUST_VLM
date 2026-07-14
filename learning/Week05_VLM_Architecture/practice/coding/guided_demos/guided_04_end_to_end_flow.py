"""引導式程式閱讀：追蹤可驗證的 Camera-to-Answer 階段狀態。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Stage:
    name: str
    input_shape: str
    output_shape: str
    failure: str


STAGES = [
    Stage("camera", "scene", "[1,H,W,3]", "frame missing / blur"),
    Stage("preprocess", "[1,H,W,3]", "[1,3,S,S]", "wrong color / normalization"),
    Stage("vision_encoder", "[1,3,S,S]", "[1,N,Dv]", "detail loss / domain shift"),
    Stage("connector", "[1,N,Dv]", "[1,M,Dl]", "dimension or information mismatch"),
    Stage("language_model", "image + text tokens", "generated IDs", "hallucination"),
    Stage("validator", "raw answer", "accept/retry/reject", "schema or grounding failure"),
]


def main() -> None:
    for index, stage in enumerate(STAGES, start=1):
        print(f"[{index}] {stage.name}")
        print(f"    input : {stage.input_shape}")
        print(f"    output: {stage.output_shape}")
        print(f"    risk  : {stage.failure}")
    print("\n請從錯誤發生的第一個階段開始診斷，不要只看最後回答。")


if __name__ == "__main__":
    main()
