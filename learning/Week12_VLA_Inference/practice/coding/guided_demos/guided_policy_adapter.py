"""逐步追蹤 VLA Policy Adapter 資料流。"""
import argparse
import numpy as np
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--scale",type=float,default=2);a=p.parse_args()
    if a.scale<=0:p.error("--scale 必須大於 0")
    raw=np.array([1.,-1.]);normalized=raw/a.scale;predicted=-normalized;action=predicted*a.scale
    for name,value in [("raw_state",raw),("normalized",normalized),("policy_output",predicted),("unnormalized_action",action)]:print(name,value,value.shape)
if __name__=="__main__":main()
