import argparse
import re

sum = 0


def read_file(filename):
    with open(filename, "r") as file:
        for row in file:
            process_row(row)
            print("-----")


regex = r"([a-z,\-]*)-([0-9]*)\[([a-z]{5})\]"


def process_row(row):
    global sum
    letterDict = {}
    match = re.search(regex, row)
    if match:
        letters = match.group(1)
        sectorid = match.group(2)
        checksum = match.group(3)
        print(letters, sectorid, checksum)
        # Split letters into all a-z and count into dict.
        # sort dict by top letters get top 5 then sort alphabetically
        # Does top 5 match checksum? Then add sectorid to sum.
        for letter in list(letters):
            if letter.isalpha():
                if not letterDict.get(letter):
                    letterDict[letter] = 0

                letterDict[letter] += 1
        sorted_data = {
            k: v
            for k, v in sorted(letterDict.items(), key=lambda item: (-item[1], item[0]))
        }
        top_5 = dict(list(sorted_data.items())[0:5])
        keys = "".join(top_5.keys())
        if keys == checksum:
            sum += int(sectorid)
    print(row)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)
    print("Sum of Sector IDs: " + str(sum))


if __name__ == "__main__":
    main()
