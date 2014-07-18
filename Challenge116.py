# Tui Popenoe
# Challenge116.py - Permutation of a string

import sys

def permutation(string, prefix):
    n = len(string)
    if n == 1:
        return prefix
    else:
        for i in range(n):
            return permutation(prefix + string[i], string[0:i] + string[i+1:n])

def main():
    if len(sys.argv) > 1:
        print(permutation("", sys.argv[1]))
    else:
        print(permutation("", raw_input()))

if __name__=='__main__':
    main()