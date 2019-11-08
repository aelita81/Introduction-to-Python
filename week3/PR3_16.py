import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", type=str)
parser.add_argument("value", type=str)
args = parser.parse_args()
dict1 = {'a':3,'b':4,'c':5,'d':6}
print ("Before the change:", dict1)
dict1.update({'key': 'value'})
print ("After the change:", args.dict1)