import argparse

from enum import Enum


class Status(Enum):
    VALID = 1
    INVALID = 2
    INVALID_VALIDINSIDE = 3


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            lines.append(line)

    for line in lines:
        # print(line)
        check_ipv7(line)


# Function to check for reversal of contiguious 4 characters
# Function to check if reversal is within [] brackets


def check_ipv7(line):
    inside_brackets = False
    ABBA = Status.INVALID
    # grab first 4 characters
    first_chars = line[0:4]
    # is first character a "[]", if so then mark as inside brackets and continue.
    if first_chars[0] == "[" or first_chars[0] == "]":
        inside_brackets = True
        first_chars = line[1:5]

    line_iterator = iter(enumerate(line))

    for idx, char in line_iterator:
        # print("Index: " + str(idx) + " Char: " + char)
        if char == "[":
            inside_brackets = True
            print("inside bracket")
            continue

        if char == "]":
            inside_brackets = False
            print("outside bracket")
            continue

        remaining_elements = ""
        found = None
        # if "[" or "]" exists in string skip to that character, mark inside/outside bracket and continue
        # print("4 char: " + line[idx : idx + 4])
        if "[" in line[idx : idx + 4]:
            # print("Skip to next [")
            found = next(((i, c) for i, c in line_iterator if c == "["), None)
            inside_brackets = True
            # continue

        if "]" in line[idx : idx + 4]:
            # print("Skip to next ]")
            next(((i, c) for i, c in line_iterator if c == "]"), None)
            inside_brackets = False
            # continue

        # print("Current 4: " + line[idx : idx + 4] + " ABBA: " + str(ABBA))
        # Once Valid it can only become invalid if inside bracket
        Next_ABBA = check_abba(line[idx : idx + 4], inside_brackets)
        # print("Next_ABBA" + str(Next_ABBA))
        if ABBA == Status.INVALID_VALIDINSIDE:
            ABBA = Status.INVALID_VALIDINSIDE
        elif ABBA == Status.VALID and Next_ABBA == Status.INVALID:
            ABBA = Status.VALID
        else:
            ABBA = Next_ABBA

    print(line + " - " + str(ABBA))
    # if not, is the last character a "[]", if so then shift outside brackets, mark as outside, and continue.
    # check if the 4 characters are ABBA
    # shift 1 character over each iteration.
    # if ABBA found, you can skip checking any other characters outside bracket. go to next bracket sets to
    # verify no abba found.


def check_abba(chars, inside_brackets):
    # if4 length < 4 then false
    if len(chars) < 4:
        return Status.INVALID

    # are the characters the same 4 characters? If so then not ABBA
    if chars[0] + chars[1] == chars[2] + chars[3]:
        return Status.INVALID

    # grab first 2 characters, reverse, compare to last 2 characters. If same then true, else false
    if chars[1] + chars[0] == chars[2] + chars[3]:
        if inside_brackets:
            return Status.INVALID_VALIDINSIDE
        else:
            return Status.VALID

    return Status.INVALID


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 01")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)
    # python pt1.py input.txt | grep "Status.VALID" | wc -l


if __name__ == "__main__":
    main()
