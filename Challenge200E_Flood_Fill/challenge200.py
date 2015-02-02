#!/usr/bin/env python
# Tui Popenoe
# challenge200.py - Flood Fill

def flood_fill():
    wh = sys.stdin.readline().split()
    width = int(wh[0])
    height = int(wh[1])
    grid = [['.' for i in range(width)] for j in range(height)]
    input_grid = []
    for i in height:
        input_grid.append(sys.stdin.readline())
    xyc = sys.stdin.readline().split()