#!python2
# Tui Popenoe
# Challenge28E.py - Duplicates

def detect_duplicate(lst):
    hashtable = {}
    for i, v in enumerate(lst):
        if v in hashtable:
            print("Duplicate detected, array[%r] and array[%r] are both equal \
                to %r" % (hashtable[v], i, array[i]))
        hashtable[v] = i

def main():
    with open(argv[1], 'r') as f:
        l = f.read().split()
        l = map(int, l)
        detect_duplicate(l)

if __name__ == '__main__':
    main()