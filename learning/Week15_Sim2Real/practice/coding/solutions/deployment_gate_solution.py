"""Deployment gate 參考解答。"""
import argparse
def deployment_ready(latency,max_latency,age,max_age,calibration):
    if min(latency,max_latency,age,max_age)<0:return False
    return latency<=max_latency and age<=max_age and calibration
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(deployment_ready(100,200,.1,.5,True))
if __name__=="__main__":main()
