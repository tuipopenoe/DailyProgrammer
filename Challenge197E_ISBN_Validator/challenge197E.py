#!/usr/bin/env python
# Tui Popenoe
# challenge197E.py - ISBN Validator

import re
import sys

def validate_isbn(isbn_number):
    isbn_number = re.sub('-', '', isbn_number)
    digits = [n for n in isbn_number[::-1]]
    digits = map(int, digits)
    digit_sum = 0
    for i, digit in enumerate(digits):
        digit_sum += (i+1)*int(digit)
    if digit_sum % 11 == 0:
        return True
    else:
        return falsefo

def main():
    if len(sys.argv) > 1:
        isbn = ''.join(sys.argv[1:])
    else:
        isbn = sys.stdin
    print(validate_isbn(isbn))

if __name__ == '__main__':
    main()