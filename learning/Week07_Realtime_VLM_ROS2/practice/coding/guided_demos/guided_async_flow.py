"""逐步展示 capture、replace、infer、validate、publish。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--age",type=float,default=.3);a=p.parse_args()
    if a.age<0:p.error("--age 必須非負")
    for step in ["capture(timestamp)","replace pending frame","infer semantic","validate schema","check freshness","publish"]:
        print("->",step)
    print("decision:", "publish" if a.age<=1 else "reject_stale")
if __name__=="__main__":main()
