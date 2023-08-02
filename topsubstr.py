# make top substring with given length based on wordlist
#
# examples:
#
# get top substrings with length 2 from top-228-passwords.txt
# $ python3 topsubstr.py top-228-passwords.txt -o result.txt -l 2

import argparse


ap = argparse.ArgumentParser(
    description="Make most popular substrings wordlist based on another wordlist",
    usage="python topsubstr.py <wordlist> -l <length> -o <output file>"
)

ap.add_argument("input", help="wordlist")
ap.add_argument("-c", "--count", help="with count", action="store_true")

ap.add_argument("-o", "--output", metavar="<FILE>", help="output file")
ap.add_argument("-l", "--length", metavar="<INT>", help="length of words", default=1, type=int, required=False)
ap.add_argument("--encoding", metavar="<ENCODING>", help="output encoding", default="utf-8", required=False)

args = ap.parse_args()

in_file = args.input
out_file = args.output
encoding = args.encoding
with_count = args.count
length = args.length

def iter_windowed(seq, window_size: int) -> list[str]:
    for i in range(len(seq) - window_size + 1):
        yield seq[i:i+window_size]

def get_substrings_with_count():
    substrings_count = dict()
    with open(in_file) as f:
        lines = f.readlines()
        for line in lines:
            for substring in iter_windowed(line.strip(), length):
                if substring not in substrings_count:
                    substrings_count[substring] = 0
                substrings_count[substring] += 1
    return substrings_count

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


substrings = get_substrings_with_count()
lines_to_write = get_formatted_lines(substrings)
write_result(lines_to_write)