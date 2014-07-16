# Tui Popenoe
# Challenge118E.py - Date Localization

import datetime
import sys

def localizeDate(filename):
    dt = datetime.datetime.now()

    format = {
        '%l' : dt.microsecond * 1000,
        '%s' : dt.second,
        '%m' : dt.minute,
        '%h' : dt.hour,
        '%H' : dt.hour / 2,
        '%c' : 'AM' if dt.hour / 12 > 1 else 'PM',
        '%d' : dt.day,
        '%M' : dt.month,
        '%y' : dt.year
    }

    f = open(filename, 'r')
    inp = f.readlines()

    for i in inp:
        for k in range(len(i) - 1):
            if inp[i][k:k+1] in format:
                string.replace(inp[i][k:k+1], format[inp[i][k:k+1]])

    output = inp
    for i in output:
        print(i)

def main():
    if len(sys.argv) > 1:
        localizeDate(sys.argv[1])
    else:
        print("Enter a filename to localize: ")
        localizeDate(raw_input())

if __name__ == '__main__':
    main()