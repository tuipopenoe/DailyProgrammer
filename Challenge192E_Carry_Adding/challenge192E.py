#!python2
# Tui Popenoe
# challenge192E.py - Carry Adding

import sys

def carry_adding(expression):
    print(expression)
    nums = expression.split('+')
    print(nums)
    nums = map(int, nums)
    print(nums)
    col_totals = [sum(x) for x in zip(*nums)]
    print(col_totals)
    # for row in nums[:-1]:
    #     print(row)
    # print('+' + str(nums[-1:]))
    # print('_' * len(nums[-1]))
    # print(sum(nums))

def main():
    if len(sys.argv) > 1:
        carry_adding(sys.argv[1])
    else:
        #carry_adding(raw_input("Enter an expression to carry add: "))
        carry_adding('23+456')
if __name__ == '__main__':
    main()