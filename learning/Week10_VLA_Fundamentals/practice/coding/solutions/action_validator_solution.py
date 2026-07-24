"""Action validator 參考解答。"""
import argparse,math
def validate_action(action,limit):
    if not action or limit<=0:return False
    return all(math.isfinite(v) and abs(v)<=limit for v in action)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--limit",type=float,default=.1);a=p.parse_args()
    print(validate_action([.01,0,-.02],a.limit))
if __name__=="__main__":main()
