# Tui Popenoe
# Challenge109E.py - Digits Check

import sys
import re

def checkDigits(string):
    if re.match('\D', string):
        return False
    else:
        return True

def main():
    if len(sys.argv) > 1:
        print(checkDigits(sys.argv[1]))
    else:
        print(checkDigits(raw_input()))

if __name__=='__main__':
    main()