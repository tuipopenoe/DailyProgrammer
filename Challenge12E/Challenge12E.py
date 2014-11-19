#!python2
# Tui Popenoe
# Challenge12E.py - Permutations

from sys import argv
import itertools

def pers(string):
    return '\n'.join(str(i) for i in itertools.permutations(string))

def main():
    if len(argv) > 1:
        print(pers(argv[1]))
    else:
        print(pers(raw_input("Enter a string: ")))

if __name__ == '__main__':
    main()