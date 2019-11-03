import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--age", help="shows the age")
args = parser.parse_args()
print(" “Happy Birthday, you are already " + str(args.age) + " years old" + "!")