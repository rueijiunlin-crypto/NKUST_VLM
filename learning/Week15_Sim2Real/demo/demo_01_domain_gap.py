"""輸出 Sim-to-Real comparison matrix。"""
import argparse
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    for row in [("lighting","fixed","variable"),("camera_noise","none","present"),("latency","deterministic","jitter"),("calibration","exact","estimated")]:
        print(f"{row[0]:16} sim={row[1]:14} real={row[2]}")
if __name__=="__main__":main()
