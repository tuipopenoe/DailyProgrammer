# Tui Popenoe
# Challenge 153 Pascal's Pyramid

""" Calculates and displays the Nth layer of Pascal's Pyramid.
    Number of terms in the nth layer is (n+1) x (n+2)/2
    Sum of layer is 3^n"""

import math

def createPyramid(n):
    num = n-1

    # initialize the pyramid slice
    pyramid = list()

    # create rows = n
    for i in range(n):