import argparse

parser = argparse.ArgumentParser()
args = parser.parse_args()
list5 = [0, 4, 10, "a", 2, 1300, 2] 
print ("List before the change:", list5)
list5.pop [5,4,0]
print("List after the change: =", list5)