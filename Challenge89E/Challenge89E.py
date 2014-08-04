# Tui Popenoe
# Challenge89E.py - Statistical Functions

import math
import sys

def mean(lst):
    return sum(lst) / len(lst)

def variance(lst):
    mean = mean(lst)
    sqd_diff = 0
    for i in lst:
        sqd_diff += math.pow(i - mean(i), 2)
    return mean(sqd_diff)

