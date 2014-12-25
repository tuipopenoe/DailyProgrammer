# Tui Popenoe
# Challenge128.py Sum-the-Digits II

import sys

def sumDigits(string):
    sum = 0
    if len(string) == 1:
        return int(string)
    for i in string:
        sum += int(i)

    print(sum)
    return sumDigits(str(sum))

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])
        sumDigits(sys.argv[1])
    else:
        sumDigits(raw_input())


if __name__=='__main__':
    main()