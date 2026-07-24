"""建立並驗證簡化的 ROS2 semantic result payload。"""
import argparse,json,time

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--max-age",type=float,default=1.0)
    p.add_argument("--age",type=float,default=0.2)
    a=p.parse_args()
    if a.max_age<0 or a.age<0:p.error("age 必須非負")
    payload={"observation_id":"obs-001","source_timestamp":time.time()-a.age,
             "objects":["cup"],"unknown":["depth"],"valid":a.age<=a.max_age}
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    print("status:","publish" if payload["valid"] else "reject_stale")
    return 0
if __name__=="__main__":raise SystemExit(main())
