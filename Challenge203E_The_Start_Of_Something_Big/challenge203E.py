#!/usr/bin/env python
# Tui Popenoe
# challenge203E.py - drawing a square

from graphics import *

def draw_square():
    win =  GraphWin("New Square", 100, 100)
    pt = Point(100, 100)
    square = Rectangle(Point(20, 20), pt)
    square.draw(win)
    win.getMouse()
    win.close()

def main():
    draw_square()

if __name__ == '__main__':
    main()