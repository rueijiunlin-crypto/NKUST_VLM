"""引導式程式閱讀：追蹤 Robot VLM 的語意、幾何、狀態與系統邊界。"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json


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
    Stage("validator", "raw answer", "structured perception", "schema / grounding failure"),
    Stage("planner", "task representation + robot state", "candidate plan", "infeasible plan"),
    Stage("controller", "validated plan", "low-level control", "timing / safety violation"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frames", type=int, default=1)
    parser.add_argument("--robot-state-known", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.frames <= 0:
        print("--frames 必須為正整數。")
        return 1
    for index, stage in enumerate(STAGES, start=1):
        print(f"[{index}] {stage.name}")
        print(f"    input : {stage.input_shape}")
        print(f"    output: {stage.output_shape}")
        print(f"    risk  : {stage.failure}")
    result = {
        "frames": args.frames,
        "semantic": {"object": "cup", "relation": "left_of_box"},
        "metric_geometry": "missing: depth and calibration",
        "robot_state": (
            "available to planner"
            if args.robot_state_known
            else "missing: pose, joints, gripper"
        ),
        "decision": "request additional information",
    }
    print("\nStructured trace:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("\n請從錯誤發生的第一個階段開始診斷，不要只看最後回答。")
    print("VLM 提供語意候選；幾何、Robot State、規劃、安全與低階控制各有來源。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
