# Tui Popenoe
# Challenge102E.py - Dice Roller

import random
import sys

def dice_roller(inp):
    """Input a string in the form <A>d<B>(+/-)<C>"""
    count = inp.split('d')[0]
    if '-' in inp:
        ch = '-'
    else:
        ch = '+'
    split = inp.split(ch)
    die_type = int(split[0][len(count)+1:])
    modifier = int(split[1])
    count = int(count)
    dice_sum = 0

    for i in range(count):
        dice_sum += random.randint(1, die_type)

    if ch == '-':
        dice_sum -= modifier
    else:
        dice_sum += modifier
    return dice_sum

def main():
    if len(sys.argv) > 1:
        print(dice_roller(sys.argv[1]))
    else:
        print(dice_roller(raw_input("Enter a die to simulate: ")))

if __name__ == '__main__':
    main()
