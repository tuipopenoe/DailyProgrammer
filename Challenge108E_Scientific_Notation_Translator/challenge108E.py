#!python2
# Tui Popenoe
# challenge108E.py

import sys

def notation_translator(decimal):
    decimal = float(decimal)
    exponent = 0
    if decimal > 10:
        while decimal > 10:
            exponent += 1
            decimal /= 10
    elif decimal < 1:
        while decimal < 1:
            exponent -= 1
            decimal *= 10
    else:
        exponent = 0
    return '%s x 10^%s' % (decimal, exponent)

def main():
    if len(sys.argv) > 1:
        print(notation_translator(sys.argv[1]))
    else:
        print(notation_translator(sys.stdin.readline()))

if __name__ == '__main__':
    main()