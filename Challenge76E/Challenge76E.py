# Tui Popenoe
# Challenge76E.py - Title Case

import sys

def title_case(string, exceptions):
    for i in string:
        i = i.lower()
        if i not in exceptions:
            i = i.title()
    string[0] = string[0].upper()
    return string

def main():
    if len(sys.argv) == 2:
        print(title_case(sys.argv[1], []))
    if len(sys.argv) == 3:
        print(title_case(sys.argv[1], sys.argv[2]))
    else:
        print("Invalid arguments")

if __name__ == '__main__':
    main()

