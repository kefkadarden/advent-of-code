import argparse
import pandas as pd

count = 0


def read_file(filename):
    # column widths
    col_widths = [5, 5, 5]
    df = pd.read_fwf(filename, widths=col_widths, header=None)

    # Clean up column spaces (optional but recommended)
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Access the first column (index 0), second column (index 1), etc.
    first_column = df[0]
    second_column = df[1]
    third_column = df[2]
    process_col(first_column)
    process_col(second_column)
    process_col(third_column)
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


def process_col(col):
    # Process rows by 3s
    for i in range(0, len(col), 3):
        num = [col[i], col[i + 1], col[i + 2]]
        check_sides(num)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)
    print("Count: " + str(count))


if __name__ == "__main__":
    main()
