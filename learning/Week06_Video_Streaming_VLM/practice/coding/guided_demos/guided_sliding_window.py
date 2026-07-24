"""逐步追蹤串流影格如何進出 Sliding Window。"""
import argparse
from collections import deque

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--frames", type=int, default=8)
    p.add_argument("--window", type=int, default=3)
    a = p.parse_args()
    if a.frames <= 0 or a.window <= 0:
        p.error("參數必須為正整數")
    memory = deque(maxlen=a.window)
    for frame in range(a.frames):
        evicted = memory[0] if len(memory) == a.window else None
        memory.append(frame)
        print(f"new={frame}, evicted={evicted}, context={list(memory)}")
    print("觀察：成本有界，但較早影格不再位於原始 context。")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
