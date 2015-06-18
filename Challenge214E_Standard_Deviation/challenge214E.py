#!/usr/bin/env python
# Tui Popenoe
# Challenge214E.py - Calculating the Standard Deviation

from math import pow, sqrt
from sys import argv

def calculate_standard_deviation(lst):
    lst = map(float, lst)
    mean = sum(lst) / len(lst)
    r_squared = [pow(r - mean, 2) for r in lst]
    variance = sum(r_squared) / len(lst)
    return round(sqrt(variance), 4)

def test_calculate_standard_deviation():
    assert calculate_standard_deviation([5, 6, 11, 13, 19, 20, 25, 26, 28, 37]) == 9.7775

def main():
    test_calculate_standard_deviation()
    if len(argv) > 1:
        print(calculate_standard_deviation(argv[1:]))
    else:
        print(calculate_standard_deviation(raw_input('Enter a list: ').split()))


if __name__ == '__main__':
    main()