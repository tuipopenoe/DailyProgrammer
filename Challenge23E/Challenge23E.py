#!python2
# Tui Popenoe
# Challenge23E.py - Split Lists

from ast import literal_eval
from sys import argv

def split_lists(lst):
    return lst[:(len(lst)/2], lst[len(lst)/2:]

def main():
    if len(argv) > 1:
        print(split_lists(literal_eval(argv[1])))
    else:
        print(split_lists(literal_eval(raw_input())))

if __name__ == '__main__':
    main()