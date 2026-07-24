"""建立 Isaac Sim Robot Learning 實驗設定摘要。"""
import argparse,json
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--seed",type=int,default=7);a=p.parse_args()
    config={"seed":a.seed,"scene":"tabletop.usd","robot":"mock_arm",
      "sensors":["rgb","depth"],"state":["joints","gripper"],"task":"pick",
      "policy":"baseline","metrics":["success_rate","latency"],"ground_truth":["object_pose"]}
    print(json.dumps(config,indent=2))
if __name__=="__main__":main()
