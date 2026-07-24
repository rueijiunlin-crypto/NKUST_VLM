"""展示 action chunk 與重新觀察頻率的取捨。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--chunk",type=int,default=4);p.add_argument("--steps",type=int,default=10);a=p.parse_args()
    if a.chunk<=0 or a.steps<=0:p.error("參數必須為正整數")
    for start in range(0,a.steps,a.chunk):
        print(f"observe -> predict actions {list(range(start,min(start+a.chunk,a.steps)))}")
    print("chunk 越長，推論次數越少，但 open-loop exposure 越長。")
if __name__=="__main__":main()
