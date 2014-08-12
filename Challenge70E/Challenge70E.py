# Tui Popenoe
# Challenge70E.py - Word Count

import sys
from collections import Counter

def sort_by_count(filename, n):
    with open(filename, 'r') as f:
        words = f.read().split()
        count = Counter()
        for word in words:
            count[word] += 1
        return count.most_common(n)

def main():
    if len(sys.argv) == 3:
        print(sort_by_count(sys.argv[1], int(sys.argv[2])))
    else:
        print(sort_by_count(raw_input(), raw_input()))

if __name__ == '__main__':
    main()