# Tui Popenoe
# Challenge57E.py - Max Sum Run

import ast
import sys


def max_sum_run(lst):
    max_sum = list()
    current_sum = list()
    for i in lst:
        if (sum(current_sum) + i) > sum(current_sum):
            current_sum.append(i)
            if(sum(current_sum) > sum(max_sum)):
                max_sum = list(current_sum)
        else:
            if(sum(current_sum) > sum(max_sum)):
                max_sum = list(current_sum)
            del current_sum[:]
    return max_sum


def main():
    if len(sys.argv) > 1:
        print(max_sum_run(ast.literal_eval(sys.argv[1])))
    else:
        print(max_sum_run(raw_input()))

if __name__ == '__main__':
    main()
