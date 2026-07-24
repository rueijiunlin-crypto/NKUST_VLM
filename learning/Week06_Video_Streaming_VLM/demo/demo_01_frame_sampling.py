"""展示固定間隔影格取樣與時間戳。"""
import argparse

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--frames", type=int, default=12)
    p.add_argument("--stride", type=int, default=3)
    a = p.parse_args()
    if a.frames <= 0 or a.stride <= 0:
        p.error("--frames 與 --stride 必須為正整數")
    selected = list(range(0, a.frames, a.stride))
    print("all frames:", list(range(a.frames)))
    print("selected frames:", selected)
    print("觀察：取樣降低輸入量，但可能錯過取樣間隔中的短暫事件。")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
