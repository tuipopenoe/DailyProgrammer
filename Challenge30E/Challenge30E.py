#!python2
# Tui Popenoe
# Challenge30E.py - Target num. 

from ast import literal_eval
from sys import argv

def target_num(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
    return ("No such integers exist")

def main():
    if len(argv) > 1:
        print(target_num(literal_eval(argv[1]), int(argv[2])))
    else:
        print(target_num(literal_eval(raw_input()), int(raw_input())))

if __name__ == '__main__':
    main()