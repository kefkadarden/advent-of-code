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
        self.prevLocs = {}
        self.add_prevnode(self.node)

    def add_prevnode(self, node):
        nodename = str(node.x) + "_" + str(node.y)
        if nodename not in self.prevLocs:
            self.prevLocs[nodename] = 0

        self.prevLocs[nodename] = self.prevLocs[nodename] + 1


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
    #   print(cmd, cmdNode.x, cmdNode.y, cmdNode.currDir)

    twice_loc = find_loc_twice(cmdNode)
    distance = dist(0, 0, twice_loc.x, twice_loc.y)
    print("Distance:", distance)


def find_loc_twice(cmdNode):
    foundloc = Node(0, 0)
    for loc, value in cmdNode.prevLocs.items():
        if value >= 2:
            locsplit = loc.split("_")
            foundloc = Node(int(locsplit[0]), int(locsplit[1]))
            print("Found: ", foundloc.x, foundloc.y)
            break

    return foundloc


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

    for _ in range(int(stepCnt)):
        match cmdNode.currDir:
            case Direction.NORTH:
                cmdNode.node.y += 1
            case Direction.EAST:
                cmdNode.node.x += 1
            case Direction.SOUTH:
                cmdNode.node.y -= 1
            case Direction.WEST:
                cmdNode.node.x -= 1
            case _:
                print("ERROR: INVALID CMDNODE DIRECTION")

        # print_prevLocs(cmdNode)
        cmdNode.add_prevnode(cmdNode.node)
    return cmdNode


def print_prevLocs(cmdNode):
    for key in cmdNode.prevLocs:
        print("Previous Node: ", key)


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
