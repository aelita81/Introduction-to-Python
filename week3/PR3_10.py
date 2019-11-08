import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val1", type=int)
args = parser.parse_args()
set3 = {0, 4, 10, 2, 1300, 2}
print(min (set3) < args.val1 <max (set3))