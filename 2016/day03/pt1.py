import argparse
import csv

count = 0


def read_file(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter=" ")
        for row in reader:
            filtered_list = [item for item in row if item]
            process_row(filtered_list)
            print("-----")


def check_sides(num):
    global count
    first = int(num[0])
    second = int(num[1])
    third = int(num[2])

    # Check these sides
    # 1+2 > 3
    # 2+3 > 1
    # 3+1 > 2
    if first + second > third and second + third > first and third + first > second:
        count += 1
        print(*num, " ", "Yes")
    else:
        print(*num, " ", "No")


def process_row(row):
    global numbers
    if len(row) == 3:
        check_sides(row)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)
    print("Count: " + str(count))


if __name__ == "__main__":
    main()
