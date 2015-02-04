#!/usr/bin/env python
# Tui Popenoe
# challenge200.py - Flood Fill

import sys

def flood_fill(input_file):
    with open(input_file, 'r') as f:
        wh = f.readline().split()
        width = int(wh[0])
        height = int(wh[1])
        grid = [['.' for i in range(width)] for j in range(height)]
        input_grid = []
        for i in height:
            input_grid.append(f.readline())
        xyc = f.readline().split()
        x = int(xyc[0])
        y = int(xyc[1])
        c = xyc[2]

        for i in range(y):
            for j in range(x):
                if grid[j][i] == '.':
                    grid[j][i] == c
                else:
                    break
        return grid

def main():
    if len(sys.argv) > 1:
        flood_fill(sys.argv[1])
    else:
        flood_fill(sys.stdin.readline())


if __name__ == '__main__':
    main()