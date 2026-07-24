"""Scalar training step 參考解答。"""
import argparse
def update(weight,x,target,learning_rate):
    if learning_rate<=0:raise ValueError("learning_rate 必須大於 0")
    prediction=weight*x;gradient=2*(prediction-target)*x
    return weight-learning_rate*gradient
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--lr",type=float,default=.1);a=p.parse_args()
    print(update(.5,1,2,a.lr))
if __name__=="__main__":main()
