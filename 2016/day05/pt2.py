import argparse
import hashlib


def read_file(filename):
    with open(filename, "r") as file:
        doorid = file.readline()
        doorid = doorid.strip()
    process_door(doorid)


def process_door(doorid):
    i = 0
    password = ["", "", "", "", "", "", "", ""]
    while "" in password:
        strhash = hashlib.md5((doorid + str(i)).encode("utf-8")).hexdigest()
        # print(doorid + str(i))
        if strhash.find("00000", 0, 5) == 0:
            if try_parse_int(strhash[5]) is None:
                i += 1
                continue
            position = int(strhash[5])
            if position > 7:
                i += 1
                continue  # outside of the bounds of the password
            if password[position] == "":
                password[position] = strhash[6]  # Only set position if empty
                print(strhash[6] + " Added to position " + str(position))
        i += 1
    print("Password is: " + "".join(password))


def try_parse_int(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def main():
    parser = argparse.ArgumentParser(description="A script to process aoc day 02")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    read_file(args.filename)


if __name__ == "__main__":
    main()
