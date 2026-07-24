"""展示 Robot VLM 系統邊界：語意感知、機器人狀態、規劃與控制。"""

from __future__ import annotations

import argparse
import json
import math


def positive_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed) or parsed < 0:
        raise argparse.ArgumentTypeError("distance 必須是大於或等於 0 的有限數值")
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", default="cup", help="示意語意物件名稱。")
    parser.add_argument("--relation", default="left_of_box", help="示意相對關係。")
    parser.add_argument(
        "--depth-m",
        type=positive_float,
        help="選填的深度感測值；省略時不得宣稱精確幾何資訊。",
    )
    parser.add_argument("--robot-pose-known", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.object.strip() or not args.relation.strip():
        print("--object 與 --relation 不可為空白。")
        return 1

    print("Robot VLM system flow")
    print("RGB Camera ─┐")
    print("Depth ──────┼──> Perception / Grounding")
    print("Instruction ┘              │")
    print("Robot State ────────────────┘")
    print("                              ↓")
    print("Semantic / Task Representation")
    print("              ↓")
    print("Planner（任務規劃器）")
    print("              ↓")
    print("Controller（控制器）")

    representation = {
        "vlm_can_provide": {
            "semantic_object": args.object.strip(),
            "relation": args.relation.strip(),
            "task_understanding": "identify a possible manipulation target",
        },
        "other_modules_provide": {
            "metric_geometry": (
                {"depth_m": args.depth_m}
                if args.depth_m is not None
                else "missing: depth sensor / geometry pipeline"
            ),
            "robot_state": (
                "available to downstream system"
                if args.robot_pose_known
                else "missing: pose / joints / gripper state"
            ),
            "safety_constraint": "planner and safety layer",
            "low_level_control": "controller",
        },
    }
    print("\nModule responsibilities:")
    print(json.dumps(representation, ensure_ascii=False, indent=2))
    print("\nWhy should a VLM not directly control the motor?")
    print(
        "因為文字生成只提供具不確定性的語意資訊；它沒有單獨驗證精確幾何、"
        "完整 Robot State、碰撞限制、安全連鎖與即時控制條件。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
