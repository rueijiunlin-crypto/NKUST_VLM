"""用 seed 產生可重現的 domain randomization 參數。"""
import argparse,random
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--seed",type=int,default=7);a=p.parse_args()
    r=random.Random(a.seed)
    print({"light":round(r.uniform(.7,1.3),3),"camera_noise":round(r.uniform(0,.02),4),"object_x":round(r.uniform(-.1,.1),3)})
if __name__=="__main__":main()
