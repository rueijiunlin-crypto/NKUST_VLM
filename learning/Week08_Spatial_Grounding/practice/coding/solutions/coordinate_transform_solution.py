"""Coordinate transform 簡化參考解答。"""
import argparse
def translate(point,offset):
    if len(point)!=3 or len(offset)!=3:raise ValueError("point/offset 必須為 3D")
    return [a+b for a,b in zip(point,offset)]
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--offset-x",type=float,default=.5);a=p.parse_args()
    print(translate([.1,.2,1.0],[a.offset_x,0,0]))
if __name__=="__main__":main()
