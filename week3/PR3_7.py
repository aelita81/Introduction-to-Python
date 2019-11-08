import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val1", type=int)
args = parser.parse_args()
set1 = {0, 4, 10, "a", 2, 1300, 2} 
set2 = set1.copy()
print ('Set1 before the change: ',set1)
print ('Set2 before the change:', set2)
set2.add(args.val1)
print("Set1 after the change: =", set1)
print ('Set2 after the change: ', set2)