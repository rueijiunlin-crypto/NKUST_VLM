"""比較 VLM semantic output 與 VLA action output。"""
import argparse,json
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps({"vlm":{"output":"cup is left of box"},
      "vla":{"action_space":"end_effector_delta","action":[0.01,0,0,0,0,0,0]}},indent=2))
    print("Action 仍需 state、limits、controller 與 safety validation。")
if __name__=="__main__":main()
