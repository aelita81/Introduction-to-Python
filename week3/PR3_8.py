import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val1", type=int)
args = parser.parse_args()
set2 = {0, 4, 10, "a", 2, 1300, 2}
print ('set2 before the change: ', set2)
set2.remove(args.val1)
print ('set2 after the change: ', set2)