# lowercase wordlist entries and deduplicate them
#
# example:
# python3 lowercasewordlist.py top-trillion-usernames.txt -o result.txt

import argparse
import sys

ap = argparse.ArgumentParser(description="filter file with regex")

ap.add_argument("input", help="input file")
ap.add_argument("-o", "--output", metavar="<FILE>", help="output file", required=True)

args = ap.parse_args()

in_file = args.input
out_file = args.output

print(f"Opening file: {in_file}")

result = []
with open(in_file) as f:
    lines = f.readlines()
    lines_lower = map(lambda x: x.strip().lower(), lines)
    lines_lower_undup = list(set(lines_lower))
    result = lines_lower_undup

print(f"Writing file: {out_file}")
with open(out_file, 'w') as o:
    for line in result:
        o.write(line + "\n")
