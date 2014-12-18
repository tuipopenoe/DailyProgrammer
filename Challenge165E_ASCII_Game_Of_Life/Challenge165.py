# Tui Popenoe
# Challenge 165 Game of Life

""" Implementation of a cellular replication simulation. Conway's game of life
    http://en.wikipedia.org/wiki/Conways_Game_of_Life"""

import sys

def life(filename=None):
    """ Open file and create a grid of cells. Iterate N times. """
    grid = list()
    if filename == None:
        filename = input.txt
    f = open(filename, 'r')
    [N, X, Y] = [int(i) for i in f.readline().split()]
    grid = f.read().split()

    for n in range(N):
        newGrid =''
        for x in range(X):
            for y in range(Y):
                # Get adjacent neighbors
                count = getAdjacent(grid, x, y, X, Y)

            if grid[x][y] == '.' and count == 3:
                newGrid += '#'
            elif grid[x][y] == '#' and count not in [2, 3]:
                newGrid += '.'
            else:
                newGrid += grid[x][y]
        newGrid += '\n'
    grid.append(newGrid.split())

    printGrid(grid)

def getAdjacent(grid, x, y, X, Y):
    """ Get the adjacent cells for a cell located at grid[x][y] in a grid of 
    size X by Y """
    count = 0
    # % X, % Y gets cells that are wrapped around the grid
    # Get x coordinates for adjacent cells 
    for i in [(x-1) % X, x, (x+1) % X]:
        # Get y coordinates for adjacent cells
        for j in [(y-1) % Y, y, (y+1) % Y]:
            # if the cell is on and not the center of the looped cells
            if (i, j) != (x, y) and grid[i][j] == '#':
                count += 1
    return count

def printGrid(grid):
    """Print the grid of cells"""
    print(grid)
    print('\n'.join(grid))

def main():
    if sys.argv[1]:
        life(sys.argv[1])

if __name__=='__main__':
    main()