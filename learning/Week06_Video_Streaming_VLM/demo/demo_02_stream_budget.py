"""估算 Camera 與 VLM 速率不匹配時的取樣及 token budget。"""
import argparse

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--camera-fps", type=float, default=30)
    p.add_argument("--inference-fps", type=float, default=2)
    p.add_argument("--tokens-per-frame", type=int, default=576)
    p.add_argument("--seconds", type=float, default=1)
    a = p.parse_args()
    if min(a.camera_fps, a.inference_fps, a.tokens_per_frame, a.seconds) <= 0:
        p.error("所有參數必須大於 0")
    captured = int(a.camera_fps * a.seconds)
    processed = min(captured, int(a.inference_fps * a.seconds))
    print(f"captured={captured}, processed={processed}, skipped_or_replaced={captured-processed}")
    print(f"processed_visual_tokens={processed*a.tokens_per_frame}")
    print("Camera FPS != VLM Inference FPS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
