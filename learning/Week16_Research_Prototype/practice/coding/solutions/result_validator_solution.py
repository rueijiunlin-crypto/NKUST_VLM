"""Research result validator 參考解答。"""
import argparse
REQUIRED={"case_id","method","metrics","failures","environment","revision"}
def validate_result(r):return not(REQUIRED-set(r)) and isinstance(r["metrics"],dict)
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(validate_result({"case_id":"c1","method":"baseline","metrics":{"success":1},"failures":[],"environment":"cpu","revision":"abc"}))
if __name__=="__main__":main()
