#!python2
# Tui Popenoe
# Challenge121E.py - Bytelandian Exchange I

import sys

c = {0 : 1}
def bytelandian_exchange(n):
    if n not in c:
        c[n] = (bytelandian_exchange(n/2) + 
                   bytelandian_exchange(n/3) + 
                   bytelandian_exchange(n/4))
    return c[n]

def main():
    #sys.setrecursionlimit(10000)
    if len(sys.argv) > 1:
        print(bytelandian_exchange(int(sys.argv[1])))
    else:
        print(bytelandian_exchange(int(sys.stdin.readline())))


if __name__ == '__main__':
    main()