"""Dataset validator 參考解答。"""
import argparse
def validate_episode(e):
    for key in ("episode_id","instruction","steps"):
        if key not in e:return False
    times=[s.get("t") for s in e["steps"]]
    return bool(times) and None not in times and times==sorted(times)
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(validate_episode({"episode_id":"e","instruction":"pick","steps":[{"t":0},{"t":.1}]}))
if __name__=="__main__":main()
