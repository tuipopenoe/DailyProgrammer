#!/usr/bin/env python
# Tui Popenoe
# challenge203E.py - drawing a square

from graphics import *

def draw_square():
    win =  GraphWin()
    pt = Point(100,50)
    square = Rectangle(Point(20, 10), pt)
    square.draw(win)

def main():
    draw_square()

if __name__ == '__main__':
    main()