"""輸出一個最小 Robot Episode schema。"""
import argparse,json
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--steps",type=int,default=3);a=p.parse_args()
    if a.steps<=0:p.error("--steps 必須正整數")
    episode={"episode_id":"ep-001","instruction":"pick cup","steps":[
      {"t":i*.1,"image":f"frame_{i}.jpg","robot_state":[0,0],"action":[.01,0]} for i in range(a.steps)],
      "metadata":{"success":False,"source":"mock"}}
    print(json.dumps(episode,indent=2))
if __name__=="__main__":main()
