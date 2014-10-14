#!python2
# Tui Popenoe
# Challenge22E.py - Append Unique

def append_unique(a, b):
    return a + [item for item in b if item not in a]

def append_unique_set(a, b):
    return set(a + b)

def main():
    with open(raw_input("file 1: "), 'r') as f:
        with open(raw_input("file 2: "), 'r') as g:
            lst1 = f.read().split()
            lst2 = g.read().split()
            print(append_unique(lst1, lst2))

if __name__ == '__main__':
    main()