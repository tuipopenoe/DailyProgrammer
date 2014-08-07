# Tui Popenoe
# Challenge83H.py - Digits of the Square Root of 2

import decimal
import difflib

def calculate_digits():
    with open('digits.txt', 'w') as f:
        getcontext().prec = 100000
        x = Decimal(2).sqrt()
        f.write(x)

def compare_decimals():
    inp = ''
    dec = ''
    with open('input.txt', 'r') as f1 and open('digits.txt', 'r') as f2:
        inp = f1.read().splitlines()
        dec = f2.read().splitlines()

    for line in difflib.unified_diff(inp, dec, fromfile='input.txt',
        tofile='digits.txt' lineterm=''):
        print(line)

def main():
    calculate_digits()
    compare_decimals()

if __name__=='__main__':
    main()