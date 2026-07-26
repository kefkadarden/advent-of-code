import argparse
import numpy as np
from collections import Counter

lines = []


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = list(line)
            lines.append(line)

    lines = rotate_array(lines)
    decode_msg(lines)


def rotate_array(lines):
    arr = np.array(lines)
    trans = arr.T
    return trans


def decode_msg(lines):
    msg = ""
    for line in lines:
        freq = Counter(line)
        sort_freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        firstelement = next(iter(sort_freq))
        msg += firstelement
    print(msg)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 01")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
