import argparse

parser = argparse.ArgumentParser()
parser.add_argument("list2", type=str)
args = parser.parse_args()
list2 = [0, "hi", 2, 100, 300, 2] 
list2.count(2)
print ("list2 =", list2)
print("Number os 2s =", args.list2)