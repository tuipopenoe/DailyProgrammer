#!python2
# Tui Popenoe
# Challenge109E.py - Digits Check

import sys
import re

def check_digits(string):
    if re.match('\D', string):
        return False
    else:
        return True

def main():
    if len(sys.argv) > 1:
        print(check_digits(sys.argv[1]))
    else:
        print(check_digits(raw_input('Enter a string: ')))

if __name__=='__main__':
    main()
