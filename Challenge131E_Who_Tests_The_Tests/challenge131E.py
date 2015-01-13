#!python2
# Tui Popenoe
# challenge131E.py - Who Tests the Tests

import sys

def test_test(line):
    line = line.split()
    num = int(line[0])
    if num == 0:
        if line[1] == reversed(line[2]):
            return True
        else:
            return False
    elif num == 1:
        if line[2] == line[1].upper():
            return True
        else:
            return False
    else:
        return False

def test_the_tests():
