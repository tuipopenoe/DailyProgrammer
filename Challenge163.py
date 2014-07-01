# Tui Popenoe
# Challenge 163 Probability Distribution of six sided die

import sys
import random
import math

def printGrid(grid):
    print(grid)

def createGrid():
    grid = list()
    for i in range(8):
        grid.append(list())
        rolls = simulateRolls(10**i)
        for j in range(7):
            if i == 0:
                grid[i].append(10**i)
            else:
                grid[i].append(rolls[j-1])

    return grid


def simulateRolls(n):
    rolls = [0, 0, 0, 0, 0, 0]
    for k in range(n):
        r = random.randint(0,5)
        rolls[r] += 1
    for k in range(len(rolls)):
        rolls[k] /= float(n)
    print(rolls)
    return rolls



def main():
    random.seed()
    grid = createGrid()
    print(grid)

if __name__=='__main__':
    main()