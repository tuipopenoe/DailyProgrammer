#!/usr/bin/env python
# Tui Popenoe
# Challenge227E Square Spirals

from sys import argv

def create_spiral(n, point=None, num=None):
    """ """
    grid = create_grid(n)
    cur_x = 0
    cur_y = 0
    dx = 0
    dy = -1
    count = 1

    offset = n//2
    for i in range(n*n):
        if (-n/2 < cur_x <= n/2) and (-n/2 < cur_y <= n/2):
            grid[cur_x + offset][cur_y + offset] = count
            count += 1
        if cur_x == cur_y or (cur_x < 0 and cur_x == -cur_y) \
           or (cur_x > 0 and cur_x == 1 - cur_y):
            dx, dy = -dy, dx
        cur_x = cur_x + dx
        cur_y = cur_y + dy
    #print_grid(grid)
    grid = zip(*grid)[::-1]
    #print_grid(grid)
    if point:
        return grid[point.x-1][point.y-1]
    if num:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == num:
                    return [j+1, i+1]


def create_grid(n):
    """Create a grid of size n x n and return it."""
    return [[0 for x in range(n)] for y in range(n)]


def print_grid(grid):
    print('*' * len(grid))
    for x in grid:
        print '\t'.join([str(y) for y in x])
    print('*' * len(grid))

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def main():
    if len(argv) > 1:
        if len(argv) > 3:
            print(create_spiral(int(argv[1]),
                                point=Point(int(argv[2]),
                                int(argv[3]))))
        else:
            print(create_spiral(int(argv[1]), num=int(argv[2])))
    else:
        print(create_spiral(int(raw_input('Enter a size n: ')),
                            num=int(raw_input('Enter a number: '))))


if __name__ == '__main__':
    main()
