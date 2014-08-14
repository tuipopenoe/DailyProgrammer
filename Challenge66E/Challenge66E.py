# Tui Popenoe
# Challenge66E.py - Roman Numerals

import sys


def roman_numerals_comparison(x, y):
    """ Compare two roman numerals. Return true iff x < y """
    x_val = 0
    y_val = 0
    for i in x:
        x_val += convert_numeral(i)
    for j in y:
        y_val += convert_numeral(j)
    if x_val < y_val:
        return True
    else:
        return False


def convert_numeral(n):
    if n == 'I':
        return 1
    elif n == 'V':
        return 5
    elif n == 'X':
        return 10
    elif n == 'L':
        return 50
    elif n == 'C':
        return 100
    elif n == 'D':
        return 500
    elif n == 'M':
        return 1000
    else:
        return 0


def main():
    if len(sys.argv) == 3:
        print(roman_numerals_comparison(sys.argv[1], sys.argv[2]))
    else:
        print(roman_numerals_comparison(raw_input(), raw_input()))

if __name__ == '__main__':
    main()
