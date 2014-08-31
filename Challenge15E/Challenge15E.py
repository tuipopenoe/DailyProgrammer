#!python2
# Tui Popenoe
# Challenge15E.py - Left/right justify

from ast import literal_eval
from sys import argv
import string

def justify(filename, right=False):
    with open(filename, 'r+') as f:
        text = f.readlines()
        f.seek(0)
        for i in text:
            if right == True:
                i = i.rjust(80, ' ')
            else:
                i = i.ljust(80, ' ')
            f.write(i)
            print(i)
        f.truncate()

def main():
    if len(argv) > 1:
        justify(argv[1], literal_eval(argv[2]))
    else:
        justify(raw_input("Filename: "),
            literal_eval(raw_input("Right Justify (True/False): ")))

if __name__ == '__main__':
    main()

