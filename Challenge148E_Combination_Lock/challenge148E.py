#!python
# Tui Popenoe
# Challenge148E.py - Combination Lock

import sys

def combo_lock(n, digit_1, digit_2, digit_3):
    increments = (2*n) + (2* digit_1) + (2 * (n -digit_2)) + digit_3
    return increments

def main():
    if len(sys.argv) > 1:
        print(combo_lock(int(sys.argv[1]),
                         int(sys.argv[2]),
                         int(sys.argv[3]),
                         int(sys.argv[4])))
    else:
        print(combo_lock(int(raw_input('Enter number of digits on lock: ')),
                         int(raw_input('Enter the first opening digit: ')),
                         int(raw_input('Enter the second opening digit: ')),
                         int(raw_input('Enter the third opening digit: ')),
                         ))

if __name__ == '__main__':
    main()