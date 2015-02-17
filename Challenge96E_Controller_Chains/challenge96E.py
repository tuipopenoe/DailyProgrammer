#!/usr/bin/env python
# Tui Popenoe
# challenge96E.py - Controller Chains

import sys

def controller_chains(d):
    ports = 2
    while ports < (d / 20 +1):
        ports += 3
        d -= 12
    return d / 20 + 1;

def main():
    if len(sys.argv) > 1:
        print(controller_chains(int(sys.argv[1])))
    else:
        print(controller_chains(int(sys.stdin.readline())))

if __name__ == '__main__':
    main()