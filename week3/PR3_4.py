import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val1", type=int)
args = parser.parse_args()
list4 = [0, 4, 10, "a", 2, 1300, 2] 
print ("List before the change:", list4)
list4.remove(args.val1)
print("List after the change: =", list4)