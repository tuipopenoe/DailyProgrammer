#!python2
# Tui Popenoe
# Challenge38E.py - Line and Word Count

from sys import argv

def counts(filename):
    with open(filename, 'r') as f:
        x = len(f.readlines())
        y = len(f.read().split())
        print("Number of lines: ", x)
        print("Number of words: ", y)

def main():
    if len(argv) > 1:
        counts(argv[1])
    else:
        counts(raw_input("Enter a filename: "))

if __name__ == '__main__':
    main()
