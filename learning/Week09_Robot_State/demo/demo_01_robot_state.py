"""輸出典型 Robot State schema。"""
import argparse,json,time
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--joints",type=int,default=6);a=p.parse_args()
    if a.joints<=0:p.error("--joints 必須為正整數")
    state={"timestamp":time.time(),"joint_position":[0.0]*a.joints,"joint_velocity":[0.0]*a.joints,
           "end_effector_pose":[0,0,0,0,0,0,1],"gripper":"open","base_pose":[0,0,0]}
    print(json.dumps(state,indent=2))
if __name__=="__main__":main()
