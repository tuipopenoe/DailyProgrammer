# Tui Popenoe
# Challenge 165 Game of Life

""" Implementation of a cellular replication simulation. """

import sys

def createGrid(x, y):
    grid = [['.' for i in xrange(x)] for j in xrange(y)]
    return grid

def createGrid(filename):
    f = open(filename, 'r')
    inputGrid = f.readlines()
    grid = list()
    for line in inputGrid:
        grid.append([])
        for char in line:
            grid[line].append(char)

def iterateCell(cellState='off', neighbors):
    for i in neighbors:
        if neighbors[i] == 'on':
            count += 1

    # cellState == off
    if cellState == '.' and count == 3:
        return '#'
    # cellState == on
    elif cellState == '#' and count <= 1:
        return '.'
    # cellState == on
    elif cellState == '#' and count >= 4:
        return '.'

    print('Error: Invalid state')
    return '.'

def printGrid(grid):
    for line in grid:
        print line

def lifeLoop(grid):
    count = 0

def main():
    