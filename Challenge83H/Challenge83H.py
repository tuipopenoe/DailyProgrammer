# Tui Popenoe
# Challenge83H.py - Digits of the Square Root of 2

""" Calculate the first 100000 digits of the square root of 2. """

from decimal import *
import difflib


def calculate_digits():
    with open('digits.txt', 'a') as f:
        getcontext().prec = 100000
        x = str(Decimal(2).sqrt())
        f.write(x)


def compare_decimals():
    inp = ''
    dec = ''
    with open('input.txt', 'r') as f1:
        with open('digits.txt', 'r') as f2:
            inp = f1.read()
            dec = f2.read()

    for line in difflib.unified_diff(inp, dec, fromfile='input.txt',
                                     tofile='digits.txt'):
        print(line)


def main():
    calculate_digits()
    compare_decimals()

if __name__ == '__main__':
    main()
