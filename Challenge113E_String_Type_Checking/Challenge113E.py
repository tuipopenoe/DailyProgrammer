# Tui Popenoe
# Challenge113E.py - String - Type Checking

import sys
import re

def checkType(string):
    #float
    if re.match(r"\d*\.\d*", string, re.I):
        return "float"
    #date
    if re.match(r"\d[2,2]-\d[2,2]-\d[4,4]", string, re.I):
        return "date"

    #int
    if re.match(r"\+?\-?\d*", string, re.I):
        return "int"

    #string
    if re.match(r"\D", string, re.I) or re.match(r"\s", string, re.I):
        return "string"

def main():
    if len(sys.argv) > 1:
        print(checkType(sys.argv[1]))
    else:
        print(checkType(raw_input()))

if __name__=='__main__':
    main()