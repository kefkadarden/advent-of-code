import argparse
from enum import Enum
import numpy as np


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


STARTX = 1
STARTY = 1

cur_Loc = [1, 1]
cur_Num = 5
numbers = []  # np.array([])

GRID = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def read_file(filename):
    with open(filename, "r") as file:
        for row in file:
            if row.__len__() > 0:
                process_row(row)
                print("-----")
    # print(numbers)
    print("Numbers: ", *numbers, sep="")


def process_row(row):
    global numbers
    print(row)
    for cmd in list(row):
        cmd = cmd.strip()
        if len(cmd) > 0:
            # print(cmd)
            process_cmd(cmd)
    print("Rows Number: ", cur_Num)
    numbers = np.append(numbers, str(cur_Num))


def lookup_num(loc):
    x = loc[0]
    y = loc[1]
    return GRID[y][x]


def lookup_loc(num):
    return np.argwhere(GRID == num)


def process_cmd(cmd):
    global cur_Num
    match cmd:
        case "U":
            if cur_Loc[1] > 0:
                cur_Loc[1] = cur_Loc[1] - 1  # Move up on Y axis
        case "R":
            if cur_Loc[0] < 2:
                cur_Loc[0] = cur_Loc[0] + 1  # Move right on X axis
        case "D":
            if cur_Loc[1] < 2:
                cur_Loc[1] = cur_Loc[1] + 1  # Move down on Y axis
        case "L":
            if cur_Loc[0] > 0:
                cur_Loc[0] = cur_Loc[0] - 1  # Move left on X axis
        case _:
            print("ERROR: INVALID DIRECTION")
    cur_Num = lookup_num(cur_Loc)
    # print("Number: ", cur_Num)
    # print("(%s,%s) => %d", cur_Loc[0], cur_Loc[1], cur_Num)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
