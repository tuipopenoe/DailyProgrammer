#!/usr/bin/env python
# Tui Popenoe
# Challenge91E.py - Sleep Sort

import sys
from threading import Thread
import time

def f(n, *args):
    time.sleep(int(n))
    print(n)

def sleepSort(lst):
    for i in lst:
        try:
            Thread(target=f, args=(i, 1)).start()
        except Exception, err:
            print(err)

def main():
    if len(sys.argv) > 1:
        lst = sys.argv[1:]
        sleepSort(lst)
    else:
        lst = raw_input().split()
        sleepSort(lst)

if __name__=='__main__':
    main()