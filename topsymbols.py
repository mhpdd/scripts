# make top symbols wordlist based on another wordlist
#
# examples:
#
# read from file and write to file 
# $ python3 topsymbols.py top-228-passwords.txt -o result.txt
#
# read from file and write to stdout with count
# $ python3 topsymbols.py top-228-passwords.txt -c 

import argparse


ap = argparse.ArgumentParser(description="Make most popular symbols wordlist based on another wordlist")

ap.add_argument("input", help="wordlist")
ap.add_argument("-c", "--count", help="with count", action="store_true")

ap.add_argument("-o", "--output", metavar="<FILE>", help="output file")
ap.add_argument("--encoding", metavar="<ENCODING>", help="output encoding", default="utf-8", required=False)

args = ap.parse_args()

in_file = args.input
out_file = args.output
with_count = args.count
encoding = args.encoding

print(encoding)

def get_symbols_with_count():
    symbols_count = dict()
    with open(in_file) as f:
        lines = f.readlines()
        for line in lines:
            for symbol in line.strip():
                if symbol not in symbols_count:
                    symbols_count[symbol] = 0
                symbols_count[symbol] += 1
    return symbols_count

def get_formatted_lines(symbols_count: dict):
    sorted_symbols = sorted(symbols_count.items(), key=lambda x: x[1], reverse=True)
    result_lines = []
    for symbol, count in sorted_symbols:
        line_to_write = symbol
        if with_count:
            line_to_write = f"{symbol},{count}"
        result_lines.append(line_to_write)
    return result_lines

def write_result(lines: list):
    if out_file is not None:
        with open(out_file, 'w', encoding=encoding) as o:
            for line in lines:
                o.write(line + "\n")
    else:
        for line in lines:
            print(line)


symbols = get_symbols_with_count()
lines_to_write = get_formatted_lines(symbols)
write_result(lines_to_write)