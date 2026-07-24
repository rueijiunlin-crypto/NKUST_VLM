"""比較語意、2D、3D 與 robot coordinate 資料層級。"""
import argparse,json
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--depth",type=float);a=p.parse_args()
    result={"semantic":"cup left_of box","pixel_center":[320,240],
            "camera_3d":"unknown" if a.depth is None else [0,0,a.depth],
            "robot_coordinate":"requires extrinsics"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
