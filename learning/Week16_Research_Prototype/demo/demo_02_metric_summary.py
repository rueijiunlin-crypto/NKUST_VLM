"""計算 success rate 與 latency summary。"""
import argparse,statistics
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--latencies",nargs="+",type=float,default=[100,120,90]);p.add_argument("--successes",nargs="+",type=int,default=[1,1,0]);a=p.parse_args()
    if not a.latencies or not a.successes or any(v<0 for v in a.latencies) or any(v not in (0,1) for v in a.successes):p.error("輸入無效")
    print({"success_rate":sum(a.successes)/len(a.successes),"latency_mean_ms":statistics.mean(a.latencies),"latency_max_ms":max(a.latencies)})
if __name__=="__main__":main()
