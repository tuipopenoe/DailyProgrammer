#!python2
# Tui Popenoe
# Challenge21E.py - Next Highest Num

from sys import argv

def next_highest(num):
    num = list(num)
    num = num[::-1]
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp
            num = num[::-1]
            return int(''.join(num))
    return int(''.join(num[::-1]))

def main():
    if len(argv) > 1:
        print(next_highest(argv[1]))
    else:
        print(next_highest(raw_input()))

if __name__ == '__main__':
    main()
