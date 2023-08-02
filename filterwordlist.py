# filter wordlist entries
#
# example: 
# all entries that start from R
# python3 filterwordlist.py top-trillion-usernames.txt -r "[Rr].*" -o result.txt

import argparse
import re


ap = argparse.ArgumentParser(description="filter file with regex")

ap.add_argument("input", help="input file")
ap.add_argument("-o", "--output", metavar="<FILE>", help="output file", required=True)
ap.add_argument("-r", "--regex", metavar="<EXPR>", help="regex filter", required=True)

args = ap.parse_args()

in_file = args.input
out_file = args.output
regex = args.regex


print(f"Opening file: {in_file}")

result = []
with open(in_file) as f:
    lines = f.readlines()
    result = filter(lambda x: re.match(regex, x), lines)

print(f"Writing file: {out_file}")
with open(out_file, 'w') as o:
    for line in result:
        o.write(line.strip() + "\n")
