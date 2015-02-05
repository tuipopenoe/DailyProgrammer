# Tui Popenoe
# Challenge85E

import numpy

def column_row_sorting(filename):
    f = open(filename, 'r')
    matrix = f.read.splitlines()

    row_totals = [sum(x) for x in matrix]
    col_totals = [sum(y) for y in zip(*matrix)]

