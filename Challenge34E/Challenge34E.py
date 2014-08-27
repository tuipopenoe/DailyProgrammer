#!python2
# Tui Popenoe
# Challenge34E.py - Max Squares

from sys import argv

def max_squares(lst):
    lst = map(int, lst)
    lst.sort(reverse=True)
    return (lst[0] ** 2 + lst[1] ** 2)

def main():
    if len(argv) > 1:
        print(max_squares(argv[1:]))
    else:
        print(max_squares(list(raw_input())))

if __name__ == '__main__':
    main()
