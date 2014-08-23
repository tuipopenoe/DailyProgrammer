#!python2
# Tui Popenoe
# Challenge53 - Sorted Lists

from ast import literal_eval

def merge_lists(lst1, lst2):
    lst1.append(lst2)
    return sorted(lst1)

def main():
    print(merge_lists(literal_eval(raw_input()), literal_eval(raw_input())))

if __name__ == '__main__':
    main()