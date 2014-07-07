# Tui Popenoe
# Challenge142E.py - Falling Sand

import sys

def fallingSand(grid):
    n = len(grid)
    print(n)
    for i in range(n):
        for j in range(n-1):
            for k in range(n):
                if grid[j][k] == '.':
                    if grid[j+1][k] == ' ':
                        grid[j][k] = ' '
                        grid[j+1][k] = '.'
        print('\n')
        for i in grid:
            output =''
            for k in i:
                output += k
            print(output)
    return grid

def createGrid():
    n = int(raw_input())
    grid = list()
    line = ''
    for i in range(n):
        grid.append(list())
        line = raw_input()
        for j in line:
            grid[i].append(j)

    for i in grid:
        print(i)

    return grid

def main():
    fallingSand(createGrid())

if __name__=='__main__':
    main()