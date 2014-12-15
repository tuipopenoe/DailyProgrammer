# Tui Popenoe
# Challenge 160 Trigonometric Triangle Trouble

"""
    Implementation to solve for unknown values in a triangle given a variable
    number of known angles and sides.
    Accepts input as a file or a series of command line arguments.
"""

import math

a = 0.0
b = 0.0
c = 0.0

A = 0.0
B = 0.0
C = 0.0

sides = 0
angles = 0

def getInput():
    f = open('input.txt', 'r')
    n = f.readline()
    char = ''
    string = ''
    val = ''

    for i in range(n):
        string = f.readline()
        char = string[0]
        val = string[2:]

        assignValue(char, val)

def getInput(char, val):
    if char.islower():
        if char=='a':

        elif char=='b':

        elif char=='c':


def pythagoreas(s=None, r=None, h=None):
    if(s and h):

    if(r and h):


def calculateAttributes(sides, angles):
    if angles == 1 and sides == 2:

    if angles == 2 and sides == 1:
        