"""Experiment config validator 參考解答。"""
import argparse
REQUIRED={"scene","robot","sensors","task","policy","metrics","seed"}
def validate(config):return not(REQUIRED-set(config)) and bool(config["sensors"]) and bool(config["metrics"])
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(validate({"scene":"s","robot":"r","sensors":["rgb"],"task":"t","policy":"p","metrics":["success"],"seed":1}))
if __name__=="__main__":main()
