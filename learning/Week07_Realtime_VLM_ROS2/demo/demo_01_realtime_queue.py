"""模擬相機快於推論時的 latest-frame queue。"""
import argparse

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--frames",type=int,default=10)
    p.add_argument("--process-every",type=int,default=3)
    a=p.parse_args()
    if a.frames<=0 or a.process_every<=0:p.error("參數必須為正整數")
    pending=None
    for i in range(a.frames):
        replaced=pending
        pending=i
        if i%a.process_every==0:
            print(f"process frame={pending}; replaced={replaced}")
            pending=None
    print(f"remaining_latest={pending}")
    return 0
if __name__=="__main__":raise SystemExit(main())
