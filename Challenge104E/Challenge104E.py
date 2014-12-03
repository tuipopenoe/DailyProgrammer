#!python2
# Tui Popenoe
# Challenge104E.py - Powerplant Simulation

import sys

def power_plant(n):
    l = []
    for i in range(1, n+1):
        if i % 3 == 0:
            pass
        elif i % 14 == 0:
            pass
        elif i % 100 == 0:
            pass
        else:
            l.append(i)

    return len(l)

def main():
    if len(sys.argv) > 1:
        print(power_plant(int(sys.argv[1])))
    else:
        print("Enter the number of days to simulate: ")
        print(power_plant(int(raw_input())))

if __name__=='__main__':
    main()
