# filter wordlist entries
#
# example: 
# all entries that start from R
# python3 filterwordlist.py top-trillion-usernames.txt -r "^[Rr].*$" -o result.txt

import argparse
import re


ap = argparse.ArgumentParser(
    description="filter file with regex",
    usage="python3 filterwordlist.py <FILE> -r <EXPR> -o <FILE>"
)

ap.add_argument("input", help="input file")
ap.add_argument("-o", "--output", metavar="<FILE>", help="output file", required=True)
ap.add_argument("-r", "--regex", metavar="<EXPR>", help="regex filter | option has no default anchors", required=True)

args = ap.parse_args()

in_file = args.input
out_file = args.output
regex_string = args.regex


with open(in_file, "r") as f, open(out_file, "w") as o:
    regex = re.compile(regex_string)
    for line in f:
        if regex.search(line):
            o.write(line.strip() + "\n")
