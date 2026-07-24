"""展示 train loss 下降但 validation loss 回升的 overfitting 訊號。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--epochs",type=int,default=8);a=p.parse_args()
    if a.epochs<=0:p.error("--epochs 必須正整數")
    for e in range(a.epochs):
        train=1/(e+1);val=.35+abs(e-3)*.06
        print(f"epoch={e} train={train:.3f} validation={val:.3f}")
if __name__=="__main__":main()
