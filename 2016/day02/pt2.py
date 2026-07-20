import argparse
from enum import Enum
from re import X
import numpy as np


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


STARTX = 1
STARTY = 1

cur_Loc = [0, 2]
cur_Num = 5
numbers = []  # np.array([])

GRID = np.array(
    [
        ["0", "0", "1", "0", "0"],
        ["0", "2", "3", "4", "0"],
        ["5", "6", "7", "8", "9"],
        ["0", "A", "B", "C", "0"],
        ["0", "0", "D", "0", "0"],
    ]
)
# GRID = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


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


def update_loc(loc, dir):
    x = loc[0]
    y = loc[1]
    match dir:
        case "U":
            if y > 0:
                y = y - 1
        case "R":
            if x < 4:
                x = x + 1
        case "D":
            if y < 4:
                y = y + 1
        case "L":
            if x > 0:
                x = x - 1
        case _:
            print("ERROR: INVALID DIRECTION")
    loc[0] = x
    loc[1] = y
    return loc


def process_cmd(cmd):
    global cur_Num
    tmp_Loc = update_loc(cur_Loc.copy(), cmd)
    if tmp_Loc[0] >= 0 and tmp_Loc[0] <= 4 and tmp_Loc[1] >= 0 and tmp_Loc[1] <= 4:
        tmp_num = lookup_num(tmp_Loc)
    else:
        tmp_num = "-1"
    match cmd:
        case "U":
            if cur_Loc[1] > 0 and tmp_num != "0":
                cur_Loc[1] = cur_Loc[1] - 1  # Move up on Y axis
        case "R":
            if cur_Loc[0] < 4 and tmp_num != "0":
                cur_Loc[0] = cur_Loc[0] + 1  # mainove right on X axis
        case "D":
            if cur_Loc[1] < 4 and tmp_num != "0":
                cur_Loc[1] = cur_Loc[1] + 1  # Move down on Y axis
        case "L":
            if cur_Loc[0] > 0 and tmp_num != "0":
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
