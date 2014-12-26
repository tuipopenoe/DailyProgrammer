# Tui Popenoe
# Challenge123E.py - Sum Them Digits

import sys

def sumDigits(inp):
    if len(inp) == 1:
        print(int(inp))
        return int(inp)
    n = 0

    for i in inp:
        n += int(i)

    return sumDigits(str(n))

def main():
    if len(sys.argv) > 1:
        sumDigits(sys.argv[1])

    else:
        sumDigits(raw_input())

if __name__=='__main__':
    main()