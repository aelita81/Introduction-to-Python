import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="types the name after the input")
args = parser.parse_args()
print("Welcome, " + args.name + "!")
