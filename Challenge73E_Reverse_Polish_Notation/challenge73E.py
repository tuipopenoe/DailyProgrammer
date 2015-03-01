#!/usr/bin/env python
# Tui Popenoe
# challenge73E.py Reverse Polish Notation

import sys
import operator

def rpn(string):
    stack = []
    ops = {
        "+" : operator.add,
        "-" : operator.sub,
        "/" : operator.divide,
        "*" : operator.multiply
    }
    for i in string:
        if is_int(i):
            stack.push(int(i))
        else:
            x = stack.pop()
            y = stack.pop()
            stack.push(ops[i](x, y))
        print(' '.join(stack))

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    if len(sys.argv) > 1:
        rpn(argv[1:])
    else:
        rpn(sys.stdin.readline())

if __name__ == '__main__':
    main()