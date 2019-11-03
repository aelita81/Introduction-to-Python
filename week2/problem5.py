import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="text to uppercase")
args = parser.parse_args()
print(args.text)
print(args.text.lower())
print(args.text.upper())

