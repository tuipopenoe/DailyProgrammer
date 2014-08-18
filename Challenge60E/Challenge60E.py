# Tui Popenoe
# Challenge60E.py - Polite Numbers 

import sys

def is_polite(n):
    for i in range(int(n/2)):
        if i + (i +1) == n:
            return True
    return False

def main():
    if len(sys.argv) > 1:
        print(is_polite(int(sys.argv[1])))
    else:
        print(is_polite(int(raw_input())))

if __name__ == '__main__':
    main()