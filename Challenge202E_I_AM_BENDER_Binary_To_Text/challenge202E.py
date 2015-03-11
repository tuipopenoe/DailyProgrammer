#!/usr/bin/env python
# Tui Popenoe
# challenge202E.py - Binary to String

import sys
import binascii

def i_am_bender(binary):
    return binascii.unhexlify('%x' % int(binary, 2))

def main():
    if len(sys.argv) > 1:
        print(i_am_bender(sys.argv[1]))
    else:
        print(i_am_bender(sys.stdin.read()))

if __name__ == '__main__':
    main()