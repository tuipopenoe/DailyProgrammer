#!python2
# Tui Popenoe
# challenge111E.py - Star Delete

import sys

def star_delete(string):
    return string.replace('*', '')
    

def main():
    if len(sys.argv) > 1:
        print(star_delete(sys.argv[1]))
    else:
        print(star_delete(sys.stdin.readline()))

if __name__ == '__main__':
    main()