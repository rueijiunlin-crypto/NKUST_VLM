"""追蹤 Observe → Policy → Validate → Act → Observe。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--cycles",type=int,default=3);a=p.parse_args()
    if a.cycles<=0:p.error("--cycles 必須為正整數")
    for i in range(a.cycles):print(f"cycle={i}: observe -> policy -> validate -> controller -> new observation")
if __name__=="__main__":main()
