"""檢查 camera 與 robot state timestamp 是否同步。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--camera-time",type=float,default=10);p.add_argument("--state-time",type=float,default=9.94);p.add_argument("--max-delta",type=float,default=.1);a=p.parse_args()
    if a.max_delta<0:p.error("--max-delta 必須非負")
    delta=abs(a.camera_time-a.state_time)
    print(f"delta={delta:.3f}s status={'aligned' if delta<=a.max_delta else 'stale_or_misaligned'}")
if __name__=="__main__":main()
