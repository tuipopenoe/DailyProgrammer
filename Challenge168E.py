# Tui Popenoe
# Challenge 168 (E) String Index

import re
import sys

def indexString(string):
    lst = re.findall(r"[a-zA-Z0-9]+", string)
    for i in lst:
        print(i)

def main():
    indexString(sys.argv[1])

if __name__=='__main__':
    main()