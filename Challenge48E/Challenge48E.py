#!python2
# Tui Popenoe
# Challenge48E.py - Even Sort

from ast import literal_eval
from sys import argv

def even_odd_sort(lst):
    i = 0
    j = len(lst) - 1
    temp = 0
    while i < j:
        while lst[i] % 2 == 0 and i < j:
            i += 1
        while lst[j] % 2 != 0 and i < j:
            j -= 1
        if i < j:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
    return lst

def main():
    if len(argv) > 1:
        print(even_odd_sort(literal_eval(argv[1])))
    else:
        print(even_odd_sort(literal_eval(raw_input("Enter a list to sort: "))))

if __name__ == '__main__':
    main()
