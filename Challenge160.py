# Tui Popenoe
# Challenge 160 Trigonometric Triangle Trouble

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
        

