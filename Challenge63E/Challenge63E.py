# Tui Popenoe
# Challenge63E.py - Reverse(N, A)

""" Take an input list A and reverse the first N indices of the array in place
"""

import ast
import sys


def reverse_na(n, a):
    rev = a[:n]
    end = a[n:]
    output = rev[::-1] + end
    return output


def main():
    if len(sys.argv) == 3:
        print(reverse_na(sys.argv[1], sys.argv[2]))
    else:
        print(reverse_na(int(raw_input()), ast.literal_eval(raw_input())))

if __name__ == '__main__':
    main()
