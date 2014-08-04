# Tui Popenoe
# Challenge102E.py - Dice Roller

import random
import sys

def diceRoller(inp):
    numbers = list()
    output = list()
    mark = False
    for i in range(len(inp))
        if inp[i] == 'd':
            if i == 0:
                numbers.append(1)
                mark = True
            else:
                numbers.append(int(inp[:i]))
                mark = True
                if len(inp) > i +1:
                    number.append(int(inp[i+1:]))

    for i in range(1, numbers[0]):
        output.append(random.randint())

    return output
