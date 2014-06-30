# Tui Popenoe
# Challenge 162 Novel Compression, pt. 1

""" Implementation of a compression algorithm. Accepts input as a file or 
    arguments from the command line. 

    Rules:
    1.) If the chunk is just a number (eg. 37), word number 37 from 
    the dictionary (zero-indexed, so 0 is the 1st word) is printed lower-case.
    2.) If the chunk is a number followed by a caret (eg. 37^), then word 37 
    from  the dictionary will be printed lower-case, with the first letter 
    capitalised.
    3.) If the chunk is a number followed by an exclamation point (eg. 37!), 
    then word 37 from the dictionary will be printed upper-case.
    4.) If it's a hyphen (-), then instead of putting a space in-between the 
    previous and next words, put a hyphen instead.
    5.) If it's any of the following symbols: . , ? ! ; :, then put that 
    symbol at the end of the previous outputted word.
    6.) If it's a letter R (upper or lower), print a new line.
    7.) If it's a letter E (upper or lower), the end of input has been reached.
"""

import sys

def decompress(n, list):



def main():
    f = open('input.txt', 'r')

    count = int(f.readline())

    l = []

    for i in range(0, count):
        l.append(f.readline())

    