import argparse
import os


ap = argparse.ArgumentParser(
    description="Combine words from wordlist. Complexity O(n^length)",
    usage="python genwords.py <wordlist> -l <length> -o <output file>"
)

ap.add_argument("input", help="wordlist")

ap.add_argument("-l", "--length", metavar="<INT>", help="combine length", type=int, required=True)
ap.add_argument("-o", "--output", metavar="<FILE>", help="output file", type=str)
ap.add_argument("--encoding", metavar="<ENCODING>", help="output encoding", default="utf-8", type=str)

args = ap.parse_args()


in_file = args.input
out_file = args.output
encoding = args.encoding
length = args.length


top_substrings = []
with open(in_file) as f:
    lines = f.readlines()
    for line in lines:
        line_strip = line.strip()
        if len(line.strip()) > 0:
            top_substrings.append(line_strip)

def generate_words(length: int):
    if length == 0:
        return
    
    generated_files = dict()
    tmp_file_prefix = "genwords_tmp_"

    for i in range(length):
        current_combination = i + 1
        prev_tmp = tmp_file_prefix + str(current_combination - 1)
        curr_tmp = tmp_file_prefix + str(current_combination)

        with open(curr_tmp, 'w', encoding=encoding) as curr:
            generated_files[curr_tmp] = current_combination
            print(f"Created tmp file: {curr_tmp}")

            if current_combination == 1:
                for substring in top_substrings:
                    curr.write(substring + "\n")
            else:
                with open(prev_tmp, "r", encoding=encoding) as prev:
                    for line in prev:
                        for substring in top_substrings:
                            curr.write(line.strip() + substring + "\n")

    for filename, words_length in generated_files.items():
        if words_length == length:
            os.replace(filename, out_file)
            print(f"Result file: {out_file}")
        else:
            os.remove(filename)
            print(f"Removed tmp file: {filename}")

generate_words(length)
