"""計算感知到控制的 end-to-end latency budget。"""
import argparse
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--capture",type=float,default=10);p.add_argument("--inference",type=float,default=120);p.add_argument("--planning",type=float,default=20);p.add_argument("--control",type=float,default=5);p.add_argument("--limit",type=float,default=200);a=p.parse_args()
    values=[a.capture,a.inference,a.planning,a.control,a.limit]
    if min(values)<0:p.error("latency 必須非負")
    total=sum(values[:-1]);print(f"total_ms={total:.1f} status={'pass' if total<=a.limit else 'timeout'}")
if __name__=="__main__":main()
