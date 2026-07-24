"""輸出 Robot VLM/VLA research evaluation matrix。"""
import argparse
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    cases=[("normal","baseline","method"),("stale_state","reject","reject"),("domain_shift","measure","measure"),("safety_limit","reject","reject")]
    print(f"{'case':16}{'baseline':14}method")
    for row in cases:print(f"{row[0]:16}{row[1]:14}{row[2]}")
if __name__=="__main__":main()
