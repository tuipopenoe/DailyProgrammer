# Tui Popenoe
# Challenge59E.py - .find()

import sys


def find_string(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    for i in range((l1 - l2) + 1):
        if string1[i:i+l2] == string2:
            return i
    return -1


def main():
    if len(sys.argv) > 1:
        print(find_string(sys.argv[1], sys.argv[2]))
    else:
        print(find_string(raw_input(), raw_input()))


if __name__ == '__main__':
    main()
