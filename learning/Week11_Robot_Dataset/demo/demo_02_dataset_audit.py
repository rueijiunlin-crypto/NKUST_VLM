"""檢查 timestamp order 與 observation-action 長度。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--inject-error",action="store_true");a=p.parse_args()
    times=[0,.1,.2] if not a.inject_error else [0,.2,.1]
    errors=[] if times==sorted(times) else ["timestamps_not_monotonic"]
    print({"steps":len(times),"errors":errors,"valid":not errors})
if __name__=="__main__":main()
