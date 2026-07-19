import csv
import argparse
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


ROOTX = ROOTY = 0
ROOTDIR = Direction.NORTH


class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class CmdNode:
    def __init__(self, x, y, dir) -> None:
        self.node = Node(x, y)
        self.currDir = dir


def read_file(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row.__len__() > 0:
                process_row(row)


def process_row(row):
    # print(row)
    cmdNode = CmdNode(ROOTX, ROOTY, Direction.NORTH)
    for cmd in row:
        cmd = cmd.strip()
        cmdNode = parse_cmd(cmd, cmdNode)
        # print(cmd, cmdNode.x, cmdNode.y, cmdNode.currDir)

    distance = dist(ROOTX, ROOTY, cmdNode.node.x, cmdNode.node.y)
    print("Distance:", distance)


def parse_cmd(cmd, cmdNode):
    match cmd[0]:
        case "R" if cmdNode.currDir.value < 3:
            cmdNode.currDir = Direction(cmdNode.currDir.value + 1)
        case "R":
            cmdNode.currDir = Direction.NORTH
        case "L" if cmdNode.currDir.value > 0:
            cmdNode.currDir = Direction(cmdNode.currDir.value - 1)
        case "L":
            cmdNode.currDir = Direction.WEST
        case _:
            print("ERROR: INVALID CMD DIRECTION")

    stepCnt = cmd[1:]

    match cmdNode.currDir:
        case Direction.NORTH:
            cmdNode.node.y += int(stepCnt)
        case Direction.EAST:
            cmdNode.node.x += int(stepCnt)
        case Direction.SOUTH:
            cmdNode.node.y -= int(stepCnt)
        case Direction.WEST:
            cmdNode.node.x -= int(stepCnt)
        case _:
            print("ERROR: INVALID CMDNODE DIRECTION")

    return cmdNode


def dist(x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 01")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
