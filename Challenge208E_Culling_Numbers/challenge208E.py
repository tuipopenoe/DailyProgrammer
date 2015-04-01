#!/usr/bin/env python
# Tui Popenoe
# challenge208E.py Culling Numbers

import sys

def cull_numbers(numbers):
    return set(numbers)


def main():
    if len(sys.argv) > 1:
        print(' '.join(cull_numbers(sys.argv[1:])))
    else:
        print(' '.join(cull_numbers(sys.stdin.readline().split())))

if __name__ == '__main__':
    main()
