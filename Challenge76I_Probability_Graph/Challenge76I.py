# Tui Popenoe
# Challenge76I.py - Probability Graph

import random
import sys


def graph(f, low, high, tests):
    results = list()
    for i in range(tests):
        results.append(f)
    results.sort()
    scale = int(tests / 100)
    
    for i in range(low, high+1):
        lst = [i]
        bar = [results[x] for x in lst]
        print(bar)


def two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    graph(two_dice, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()