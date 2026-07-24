"""依硬體條件產生真實 VLA 執行前檢查清單。"""
import argparse,json
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--vram-gb",type=float,default=0);p.add_argument("--model",choices=["smolvla","openvla"],default="smolvla");a=p.parse_args()
    if a.vram_gb<0:p.error("--vram-gb 必須非負")
    print(json.dumps({"model":a.model,"mode":"optional_real_model",
      "check":["official model card","license/access","processor compatibility","observation schema","action convention"],
      "hardware_note":"verify current requirement; do not infer from this toy planner"},indent=2))
if __name__=="__main__":main()
