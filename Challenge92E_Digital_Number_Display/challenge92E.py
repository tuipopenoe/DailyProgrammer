#!/usr/bin/env python
# Tui Popenoe
# challenge92E.py - Digital Number Display

import sys

digital_numbers = {
    '1': [  ['    + '],
            ['    | '],
            ['    | '],
            ['    + '],
            ['    | '],
            ['    | '],
            ['    + ']],
    '2': [  [' +--+ '],
            ['    | '],
            ['    | '],
            [' +--+ '],
            [' |    '],
            [' |    '],
            [' +--+ ']],
    '3': [  [' +--+ '],
            ['    | '],
            ['    | '],
            [' +--+ '],
            ['    | '],
            ['    | '],
            [' +--+ ']],
    '4': [  [' +  + '],
            [' |  | '],
            [' |  | '],
            [' +--+ '],
            ['    | '],
            ['    | '],
            ['    + ']],
    '5': [  [' +--+ '],
            [' |    '],
            [' |    '],
            [' +--+ '],
            ['    | '],
            ['    | '],
            [' +--+ ']],
    '6': [  [' +--+ '],
            [' |    '],
            [' |    '],
            [' +--+ '],
            [' |  | '],
            [' |  | '],
            [' +--+ ']],
    '7': [  [' +--+ '],
            ['    | '],
            ['    | '],
            ['    + '],
            ['    | '],
            ['    | '],
            ['    + ']],
    '8': [  [' +--+ '],
            [' |  | '],
            [' |  | '],
            [' +--+ '],
            [' |  | '],
            [' |  | '],
            [' +--+ ']],
    '9': [  [' +--+ '],
            [' |  | '],
            [' |  | '],
            [' +--+ '],
            ['    | '],
            ['    | '],
            [' +--+ ']],
    '0': [  [' +--+ '],
            [' |  | '],
            [' |  | '],
            [' +  + '],
            [' |  | '],
            [' |  | '],
            [' +--+ ']]
}

def digital_display(number):
    numbers = []
    for i in number:
        numbers.append(digital_numbers[i])
    lines = []
    for j in range(7):
        line_out = []
        for i in numbers:
            line_out.append(i[j])
        lines.append(line_out)
    for i in lines:
        print(i)

def main():
    if len(sys.argv) > 1:
        print(digital_display(sys.argv[1]))
    else:
        print(digital_display(sys.stdin.readline()))

if __name__ == '__main__':
    main()