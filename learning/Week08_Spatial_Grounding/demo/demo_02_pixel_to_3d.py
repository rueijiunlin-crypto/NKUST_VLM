"""使用 pinhole intrinsics 將 pixel + depth 反投影到 camera frame。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n,d in [("u",320.),("v",240.),("depth",1.),("fx",600.),("fy",600.),("cx",320.),("cy",240.)]:p.add_argument("--"+n,type=float,default=d)
    a=p.parse_args()
    if a.depth<=0 or a.fx<=0 or a.fy<=0:p.error("depth、fx、fy 必須大於 0")
    x=(a.u-a.cx)*a.depth/a.fx;y=(a.v-a.cy)*a.depth/a.fy
    print(f"camera_coordinate_m=[{x:.4f}, {y:.4f}, {a.depth:.4f}]")
if __name__=="__main__":main()
