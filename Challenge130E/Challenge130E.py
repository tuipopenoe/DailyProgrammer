# Tui Popenoe
# Challenge130E.py - Roll the Dies

import random

def main():
    random.seed()
    dice = ''
    while dice != 'q':
        dice = raw_input()
        if dice == 'q':
            break;
        n = int(dice[0])
        m = int(dice[2:])

        rolls = list()

        for i in range(n):
            roll = random.randint(1, m)
            rolls.append(roll)
            print(roll)

if __name__=='__main__':
    main()