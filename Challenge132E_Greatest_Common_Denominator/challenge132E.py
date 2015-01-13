#!python2
# Tui Popenoe
# challenge132E.py - Greatest Common Denominator

import sys

def gcd(a, b):
    # Euclid's Algorithm
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    if len(sys.argv) > 1:
        print(gcd(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print(gcd(int(raw_input()), int(raw_input())))

if __name__ == '__main__':
    main()