"""Freshness policy 參考解答。"""
import argparse
def should_publish(age_seconds,max_age):
    if age_seconds<0 or max_age<0: raise ValueError("age 必須非負")
    return age_seconds<=max_age
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--age",type=float,default=.2);p.add_argument("--max-age",type=float,default=1);a=p.parse_args()
    print("publish" if should_publish(a.age,a.max_age) else "reject_stale")
if __name__=="__main__":main()
