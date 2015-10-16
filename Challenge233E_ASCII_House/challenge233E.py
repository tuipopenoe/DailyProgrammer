#!/usr/bin/env python
# Tui Popenoe
# Challenge 233 E - The House That ASCII Built

import sys

def create_house():
    blueprint = [line.strip('\n') for line in sys.stdin.readlines()]
    base = [''.join(['+---' for x in usr_inp[-1] if x == '*']) + '+']
    frame = [''.join(['+---' for x in y if x == '*']) + '+' for y in usr_inp[:-1]]
