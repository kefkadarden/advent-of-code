import argparse
import re

# USAGE: prints out all the rotated room names with sectorid. Used "grep" to find the
# room with "north".


def read_file(filename):
    global rooms_to_check
    with open(filename, "r") as file:
        for row in file:
            process_row(row)
    for room in rooms_to_check:
        process_room(room)


regex = r"([a-z,\-]*)-([0-9]*)\[([a-z]{5})\]"
rooms_to_check = []


def process_room(room):
    arr = room.split("_")
    letters = arr[0]
    sectorid = int(arr[1])
    roomword = ""
    for letter in list(letters):
        roomword += rotate_letter(letter, sectorid)
    print(str(sectorid) + ": " + roomword)


def process_row(row):
    global sum
    global rooms_to_check
    match = re.search(regex, row)
    if match:
        letters = match.group(1)
        sectorid = match.group(2)
        # Save room to be processed later
        rooms_to_check.append(letters + "_" + str(sectorid))


def rotate_letter(letter, sectorid):
    i = 1
    while i <= sectorid:
        if letter == "z":
            letter = "a"
        elif letter == "-":
            letter = " "
            break
        else:
            letter = chr(ord(letter) + 1)
        i += 1
    return letter


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
