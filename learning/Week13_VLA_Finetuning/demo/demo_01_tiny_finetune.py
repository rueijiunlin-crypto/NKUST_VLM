"""用 tiny linear policy 展示 pretrained weight 的 task adaptation。"""
import argparse
import numpy as np
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--steps",type=int,default=20);p.add_argument("--lr",type=float,default=.1);a=p.parse_args()
    if a.steps<=0 or a.lr<=0:p.error("steps/lr 必須大於 0")
    x=np.array([[-1.],[0.],[1.]],dtype=float);y=2*x;w=np.array([[.5]])
    for step in range(a.steps):
        pred=x@w;grad=2*x.T@(pred-y)/len(x);w-=a.lr*grad
        if step in (0,a.steps-1):print(f"step={step} loss={np.mean((pred-y)**2):.6f} weight={w.item():.4f}")
if __name__=="__main__":main()
