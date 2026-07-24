"""Embodied Observation 參考解答。"""
import argparse,json,time
def build_observation(image_id,instruction,robot_state):
    if not image_id or not instruction.strip():raise ValueError("image_id/instruction 不可空白")
    if "timestamp" not in robot_state:raise ValueError("robot_state 缺 timestamp")
    return {"image_id":image_id,"instruction":instruction,"robot_state":robot_state}
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(build_observation("cam0:42","pick cup",{"timestamp":time.time(),"gripper":"open"}),indent=2))
if __name__=="__main__":main()
