import argparse
import hashlib


def read_file(filename):
    with open(filename, "r") as file:
        doorid = file.readline()
        doorid = doorid.strip()
    process_door(doorid)


def process_door(doorid):
    i = 0
    cnt = 0
    strhash = ""
    code = ""
    while cnt < 8:
        strhash = hashlib.md5((doorid + str(i)).encode("utf-8")).hexdigest()
        # print(doorid + str(i))
        if strhash.find("00000", 0, 5) == 0:
            code += strhash[5]
            cnt += 1
        i += 1
    print("Password is: " + code)


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 01")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
