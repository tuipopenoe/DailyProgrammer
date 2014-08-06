# Tui Popenoe
# Challenge82E.py - Substring List

import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def substring_list(n):
    output = ''
    for i in range(n):
        for j in range(i, n):
            output += alphabet[j]
            print(output)
        output = ''

def num_strings(n):
    return sum(range(n+1))

def main():
    if len(sys.argv) > 1:
        substring_list(int(sys.argv[1]))
    else:
        substring_list(int(raw_input()))

if __name__=='__main__':
    main()